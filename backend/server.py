from fastapi import FastAPI, APIRouter, HTTPException, Query
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class StatusCheck(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class StatusCheckCreate(BaseModel):
    client_name: str

# News Models
class NewsArticle(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    summary: str
    content: str
    author: str
    category: str
    publish_date: datetime = Field(default_factory=datetime.utcnow)
    image_url: Optional[str] = None
    tags: List[str] = []
    read_time: int = 5  # estimated read time in minutes

class NewsArticleResponse(BaseModel):
    id: str
    title: str
    summary: str
    content: str
    author: str
    category: str
    publish_date: datetime
    image_url: Optional[str] = None
    tags: List[str] = []
    read_time: int

# Investment Models
class TechnicalIndicators(BaseModel):
    rsi: Optional[float] = None
    moving_avg_50: Optional[float] = None
    moving_avg_200: Optional[float] = None
    pe_ratio: Optional[float] = None
    volatility: Optional[float] = None

class InvestmentRecommendation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    symbol: str
    name: str
    asset_type: str  # "stock", "index", "commodity"
    current_price: float
    target_price: float
    recommendation: str  # "BUY", "SELL", "HOLD"
    risk_level: str  # "LOW", "MEDIUM", "HIGH"
    confidence_score: int  # 1-100
    timeframe: str  # "1M", "3M", "6M", "1Y"
    analyst: str
    analysis: str
    key_factors: List[str] = []
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    price_change_24h: float = 0.0
    price_change_percent: float = 0.0
    market_cap: Optional[str] = None
    sector: Optional[str] = None
    technical_indicators: Optional[TechnicalIndicators] = None

class InvestmentRecommendationResponse(BaseModel):
    id: str
    symbol: str
    name: str
    asset_type: str
    current_price: float
    target_price: float
    recommendation: str
    risk_level: str
    confidence_score: int
    timeframe: str
    analyst: str
    analysis: str
    key_factors: List[str]
    last_updated: datetime
    price_change_24h: float
    price_change_percent: float
    market_cap: Optional[str]
    sector: Optional[str]
    technical_indicators: Optional[TechnicalIndicators]

# Q&A Models
class InvestmentQuestion(BaseModel):
    question: str
    user_id: Optional[str] = "anonymous"

class InvestmentAnswer(BaseModel):
    question: str
    answer: str
    relevant_symbols: List[str] = []
    confidence: float
    response_time: datetime = Field(default_factory=datetime.utcnow)
    sources: List[str] = []

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.dict()
    status_obj = StatusCheck(**status_dict)
    _ = await db.status_checks.insert_one(status_obj.dict())
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    status_checks = await db.status_checks.find().to_list(1000)
    return [StatusCheck(**status_check) for status_check in status_checks]

# News API Endpoints
@api_router.get("/news", response_model=List[NewsArticleResponse])
async def get_news_articles(category: Optional[str] = Query(None)):
    query = {}
    if category:
        query["category"] = category
    
    articles = await db.news_articles.find(query).sort("publish_date", -1).to_list(100)
    return [NewsArticleResponse(**article) for article in articles]

@api_router.get("/news/{article_id}", response_model=NewsArticleResponse)
async def get_news_article(article_id: str):
    article = await db.news_articles.find_one({"id": article_id})
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return NewsArticleResponse(**article)

@api_router.get("/news/categories/list")
async def get_news_categories():
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    categories = await db.news_articles.aggregate(pipeline).to_list(100)
    return [{"category": cat["_id"], "count": cat["count"]} for cat in categories]

# Investment API Endpoints
@api_router.get("/investments/summary")
async def get_investment_summary():
    total_count = await db.investment_recommendations.count_documents({})
    
    # Count by recommendation type
    buy_count = await db.investment_recommendations.count_documents({"recommendation": "BUY"})
    hold_count = await db.investment_recommendations.count_documents({"recommendation": "HOLD"})
    sell_count = await db.investment_recommendations.count_documents({"recommendation": "SELL"})
    
    # Count by asset type
    stocks_count = await db.investment_recommendations.count_documents({"asset_type": "stock"})
    indices_count = await db.investment_recommendations.count_documents({"asset_type": "index"})
    commodities_count = await db.investment_recommendations.count_documents({"asset_type": "commodity"})
    
    return {
        "total_recommendations": total_count,
        "recommendations_by_type": {
            "BUY": buy_count,
            "HOLD": hold_count,
            "SELL": sell_count
        },
        "assets_by_type": {
            "stocks": stocks_count,
            "indices": indices_count,
            "commodities": commodities_count
        }
    }

# Q&A API Endpoints
@api_router.post("/investments/ask", response_model=InvestmentAnswer)
async def ask_investment_question(question: InvestmentQuestion):
    """AI-powered investment Q&A system"""
    try:
        # Get all investment data for context
        all_investments = await db.investment_recommendations.find().to_list(100)
        
        # Process the question and generate intelligent response
        answer_data = await process_investment_question(question.question, all_investments)
        
        return InvestmentAnswer(
            question=question.question,
            answer=answer_data["answer"],
            relevant_symbols=answer_data["relevant_symbols"],
            confidence=answer_data["confidence"],
            sources=answer_data["sources"]
        )
        
    except Exception as e:
        # Fallback response for any errors
        return InvestmentAnswer(
            question=question.question,
            answer="I apologize, but I'm unable to process your question at the moment. Please try asking about specific stocks, sectors, or investment strategies.",
            relevant_symbols=[],
            confidence=0.5,
            sources=[]
        )

async def process_investment_question(question: str, investments: List[dict]) -> dict:
    """Process investment questions and provide intelligent responses"""
    question_lower = question.lower()
    relevant_symbols = []
    sources = []
    confidence = 0.8
    
    # Check if question mentions specific symbols
    symbols_mentioned = []
    for inv in investments:
        if inv["symbol"].lower() in question_lower or inv["name"].lower() in question_lower:
            symbols_mentioned.append(inv)
            relevant_symbols.append(inv["symbol"])
    
    # Question pattern matching and response generation
    if any(word in question_lower for word in ["should i buy", "recommend", "good investment"]):
        return await handle_recommendation_question(question_lower, investments, symbols_mentioned)
    
    elif any(word in question_lower for word in ["price target", "target price", "price prediction"]):
        return await handle_price_question(question_lower, investments, symbols_mentioned)
    
    elif any(word in question_lower for word in ["risk", "risky", "safe", "volatile"]):
        return await handle_risk_question(question_lower, investments, symbols_mentioned)
    
    elif any(word in question_lower for word in ["sector", "industry", "technology", "healthcare", "financial"]):
        return await handle_sector_question(question_lower, investments)
    
    elif any(word in question_lower for word in ["portfolio", "diversification", "allocation"]):
        return await handle_portfolio_question(question_lower, investments)
    
    elif any(word in question_lower for word in ["market", "economy", "outlook", "trend"]):
        return await handle_market_question(question_lower, investments)
    
    else:
        return await handle_general_question(question_lower, investments, symbols_mentioned)

async def handle_recommendation_question(question: str, investments: List[dict], symbols_mentioned: List[dict]) -> dict:
    """Handle recommendation-related questions"""
    
    if symbols_mentioned:
        # Question about specific symbol
        inv = symbols_mentioned[0]
        rec = inv["recommendation"]
        confidence_score = inv["confidence_score"]
        analyst = inv["analyst"]
        
        answer = f"Based on our analysis, {inv['symbol']} ({inv['name']}) currently has a **{rec}** recommendation with {confidence_score}% confidence from analyst {analyst}. "
        
        if rec == "BUY":
            answer += f"The target price is ${inv['target_price']:.2f} compared to the current price of ${inv['current_price']:.2f}, representing a potential upside of {((inv['target_price'] - inv['current_price']) / inv['current_price'] * 100):.1f}%. "
        elif rec == "HOLD":
            answer += f"The stock is fairly valued at current levels around ${inv['current_price']:.2f}. "
        else:  # SELL
            answer += f"We see downside risk with a target of ${inv['target_price']:.2f} vs current ${inv['current_price']:.2f}. "
            
        answer += f"Key factors include: {', '.join(inv['key_factors'][:3])}. Risk level is {inv['risk_level']}."
        
        return {
            "answer": answer,
            "relevant_symbols": [inv["symbol"]],
            "confidence": 0.9,
            "sources": [f"Analysis by {analyst}", f"{inv['symbol']} recommendation report"]
        }
    
    else:
        # General recommendation question
        buy_recs = [inv for inv in investments if inv["recommendation"] == "BUY"]
        top_buys = sorted(buy_recs, key=lambda x: x["confidence_score"], reverse=True)[:3]
        
        answer = f"Based on our current analysis, here are our top 3 BUY recommendations:\n\n"
        for i, inv in enumerate(top_buys, 1):
            upside = ((inv['target_price'] - inv['current_price']) / inv['current_price'] * 100)
            answer += f"{i}. **{inv['symbol']}** ({inv['name']}) - {upside:.1f}% upside potential, {inv['confidence_score']}% confidence, {inv['risk_level']} risk\n"
        
        answer += "\nThese recommendations are based on fundamental analysis, technical indicators, and market conditions."
        
        return {
            "answer": answer,
            "relevant_symbols": [inv["symbol"] for inv in top_buys],
            "confidence": 0.85,
            "sources": ["Current investment recommendations", "Analyst reports"]
        }

async def handle_price_question(question: str, investments: List[dict], symbols_mentioned: List[dict]) -> dict:
    """Handle price target and prediction questions"""
    
    if symbols_mentioned:
        inv = symbols_mentioned[0]
        current_price = inv["current_price"]
        target_price = inv["target_price"]
        timeframe = inv["timeframe"]
        
        if inv["symbol"] == "BTC-USD":
            answer = f"{inv['symbol']} is currently trading at ${current_price:,.0f}. Our {timeframe} price target is ${target_price:,.0f}, "
        else:
            answer = f"{inv['symbol']} is currently trading at ${current_price:.2f}. Our {timeframe} price target is ${target_price:.2f}, "
            
        change_percent = ((target_price - current_price) / current_price) * 100
        if change_percent > 0:
            answer += f"representing a potential upside of {change_percent:.1f}%. "
        else:
            answer += f"representing a potential downside of {abs(change_percent):.1f}%. "
            
        answer += f"This target is based on {inv['analysis'][:150]}..."
        
        if inv.get("technical_indicators"):
            ti = inv["technical_indicators"]
            if ti.get("rsi"):
                answer += f" Technical indicators show RSI at {ti['rsi']:.1f}"
                if ti["rsi"] > 70:
                    answer += " (overbought territory)."
                elif ti["rsi"] < 30:
                    answer += " (oversold territory)."
                else:
                    answer += " (neutral territory)."
        
        return {
            "answer": answer,
            "relevant_symbols": [inv["symbol"]],
            "confidence": 0.85,
            "sources": [f"{inv['symbol']} price analysis", f"Technical analysis by {inv['analyst']}"]
        }
    
    else:
        answer = "Our price targets are based on comprehensive fundamental and technical analysis. Here are some key targets:\n\n"
        
        high_conviction = [inv for inv in investments if inv["confidence_score"] >= 80][:4]
        for inv in high_conviction:
            change = ((inv['target_price'] - inv['current_price']) / inv['current_price']) * 100
            answer += f"• **{inv['symbol']}**: ${inv['current_price']:.2f} → ${inv['target_price']:.2f} ({change:+.1f}%) in {inv['timeframe']}\n"
        
        answer += "\nAll targets are based on fundamental analysis, technical indicators, and market conditions."
        
        return {
            "answer": answer,
            "relevant_symbols": [inv["symbol"] for inv in high_conviction],
            "confidence": 0.8,
            "sources": ["Price target analysis", "Technical analysis reports"]
        }

async def handle_risk_question(question: str, investments: List[dict], symbols_mentioned: List[dict]) -> dict:
    """Handle risk-related questions"""
    
    if symbols_mentioned:
        inv = symbols_mentioned[0]
        risk_level = inv["risk_level"]
        volatility = inv.get("technical_indicators", {}).get("volatility", 0) if inv.get("technical_indicators") else 0
        
        answer = f"{inv['symbol']} has a **{risk_level}** risk rating. "
        
        if risk_level == "LOW":
            answer += "This is considered a conservative investment with stable fundamentals and lower volatility. "
        elif risk_level == "MEDIUM":
            answer += "This represents a balanced risk-reward profile with moderate volatility. "
        else:  # HIGH
            answer += "This is a higher-risk investment with significant volatility and growth potential. "
            
        if volatility > 0:
            answer += f"The stock has a volatility of {volatility:.2f}, "
            if volatility > 0.4:
                answer += "indicating high price swings."
            elif volatility > 0.25:
                answer += "showing moderate price movements."
            else:
                answer += "suggesting relatively stable price action."
        
        answer += f" Key risk factors include: {', '.join(inv['key_factors'][-3:])}."
        
        return {
            "answer": answer,
            "relevant_symbols": [inv["symbol"]],
            "confidence": 0.9,
            "sources": [f"{inv['symbol']} risk analysis", "Risk assessment methodology"]
        }
    
    else:
        low_risk = [inv for inv in investments if inv["risk_level"] == "LOW"]
        high_risk = [inv for inv in investments if inv["risk_level"] == "HIGH"]
        
        answer = f"**Risk Analysis Overview:**\n\n"
        answer += f"**Low Risk Options ({len(low_risk)} available):** "
        answer += ", ".join([inv["symbol"] for inv in low_risk[:5]])
        answer += f"\n\n**High Risk/High Reward ({len(high_risk)} available):** "
        answer += ", ".join([inv["symbol"] for inv in high_risk[:5]])
        answer += "\n\nRisk levels are determined by volatility, sector stability, and fundamental strength."
        
        return {
            "answer": answer,
            "relevant_symbols": [],
            "confidence": 0.85,
            "sources": ["Risk assessment framework", "Portfolio risk analysis"]
        }

async def handle_sector_question(question: str, investments: List[dict]) -> dict:
    """Handle sector-related questions"""
    
    sectors = {}
    for inv in investments:
        if inv.get("sector"):
            if inv["sector"] not in sectors:
                sectors[inv["sector"]] = []
            sectors[inv["sector"]].append(inv)
    
    if "technology" in question or "tech" in question:
        tech_stocks = sectors.get("Technology", [])
        answer = f"**Technology Sector Analysis:**\n\n"
        answer += f"We cover {len(tech_stocks)} technology stocks with strong growth potential:\n"
        
        for inv in tech_stocks[:5]:
            answer += f"• **{inv['symbol']}** ({inv['recommendation']}) - {inv['confidence_score']}% confidence\n"
        
        answer += "\nTechnology sector benefits from AI innovation, cloud adoption, and digital transformation trends."
        
        return {
            "answer": answer,
            "relevant_symbols": [inv["symbol"] for inv in tech_stocks],
            "confidence": 0.9,
            "sources": ["Technology sector analysis", "Industry research reports"]
        }
    
    else:
        answer = "**Sector Breakdown:**\n\n"
        for sector, stocks in sectors.items():
            buy_count = len([s for s in stocks if s["recommendation"] == "BUY"])
            answer += f"• **{sector}**: {len(stocks)} stocks, {buy_count} BUY recommendations\n"
        
        answer += "\nEach sector is analyzed based on specific industry dynamics and economic factors."
        
        return {
            "answer": answer,
            "relevant_symbols": [],
            "confidence": 0.8,
            "sources": ["Sector analysis", "Industry research"]
        }

async def handle_portfolio_question(question: str, investments: List[dict]) -> dict:
    """Handle portfolio and diversification questions"""
    
    buy_recs = [inv for inv in investments if inv["recommendation"] == "BUY"]
    sectors = {}
    
    for inv in buy_recs:
        if inv.get("sector"):
            if inv["sector"] not in sectors:
                sectors[inv["sector"]] = []
            sectors[inv["sector"]].append(inv)
    
    answer = "**Diversified Portfolio Recommendations:**\n\n"
    answer += "For a balanced portfolio, consider allocation across multiple sectors:\n\n"
    
    for sector, stocks in list(sectors.items())[:5]:
        top_pick = max(stocks, key=lambda x: x["confidence_score"])
        answer += f"• **{sector}**: {top_pick['symbol']} ({top_pick['confidence_score']}% confidence)\n"
    
    answer += f"\n**Risk Distribution:**\n"
    risk_levels = {"LOW": 0, "MEDIUM": 0, "HIGH": 0}
    for inv in buy_recs:
        risk_levels[inv["risk_level"]] += 1
    
    total = sum(risk_levels.values())
    for risk, count in risk_levels.items():
        percentage = (count / total) * 100
        answer += f"• {risk} Risk: {count} positions ({percentage:.0f}%)\n"
    
    answer += "\nDiversification reduces risk while maintaining growth potential."
    
    return {
        "answer": answer,
        "relevant_symbols": [max(stocks, key=lambda x: x["confidence_score"])["symbol"] for stocks in sectors.values()],
        "confidence": 0.85,
        "sources": ["Portfolio optimization analysis", "Risk management framework"]
    }

async def handle_market_question(question: str, investments: List[dict]) -> dict:
    """Handle market outlook and trend questions"""
    
    total_recs = len(investments)
    buy_count = len([inv for inv in investments if inv["recommendation"] == "BUY"])
    hold_count = len([inv for inv in investments if inv["recommendation"] == "HOLD"])
    sell_count = len([inv for inv in investments if inv["recommendation"] == "SELL"])
    
    buy_percentage = (buy_count / total_recs) * 100
    
    answer = f"**Current Market Outlook:**\n\n"
    answer += f"Our analyst consensus shows {buy_percentage:.0f}% BUY recommendations ({buy_count}/{total_recs}), "
    answer += f"indicating a **{'bullish' if buy_percentage > 60 else 'neutral' if buy_percentage > 40 else 'bearish'}** market sentiment.\n\n"
    
    answer += f"**Recommendation Distribution:**\n"
    answer += f"• BUY: {buy_count} positions ({buy_percentage:.0f}%)\n"
    answer += f"• HOLD: {hold_count} positions ({(hold_count/total_recs)*100:.0f}%)\n"
    answer += f"• SELL: {sell_count} positions ({(sell_count/total_recs)*100:.0f}%)\n\n"
    
    # Get sectors with most BUY recommendations
    sector_buys = {}
    for inv in investments:
        if inv["recommendation"] == "BUY" and inv.get("sector"):
            sector_buys[inv["sector"]] = sector_buys.get(inv["sector"], 0) + 1
    
    top_sectors = sorted(sector_buys.items(), key=lambda x: x[1], reverse=True)[:3]
    answer += f"**Strongest Sectors:** {', '.join([sector for sector, count in top_sectors])}\n\n"
    
    answer += "Market outlook is based on economic indicators, earnings growth, and technical analysis."
    
    return {
        "answer": answer,
        "relevant_symbols": [],
        "confidence": 0.8,
        "sources": ["Market analysis", "Analyst consensus", "Economic indicators"]
    }

async def handle_general_question(question: str, investments: List[dict], symbols_mentioned: List[dict]) -> dict:
    """Handle general investment questions"""
    
    if symbols_mentioned:
        inv = symbols_mentioned[0]
        answer = f"**{inv['symbol']} ({inv['name']}) Overview:**\n\n"
        answer += f"• **Current Price:** ${inv['current_price']:.2f}\n"
        answer += f"• **Recommendation:** {inv['recommendation']} ({inv['confidence_score']}% confidence)\n"
        answer += f"• **Target Price:** ${inv['target_price']:.2f} ({inv['timeframe']})\n"
        answer += f"• **Risk Level:** {inv['risk_level']}\n"
        answer += f"• **Sector:** {inv.get('sector', 'N/A')}\n\n"
        answer += f"**Analysis Summary:** {inv['analysis'][:200]}...\n\n"
        answer += f"**Key Factors:** {', '.join(inv['key_factors'][:3])}"
        
        return {
            "answer": answer,
            "relevant_symbols": [inv["symbol"]],
            "confidence": 0.9,
            "sources": [f"{inv['symbol']} investment report", f"Analysis by {inv['analyst']}"]
        }
    
    else:
        answer = "I'm here to help with investment questions! You can ask me about:\n\n"
        answer += "• **Specific stocks** (e.g., 'Should I buy AAPL?')\n"
        answer += "• **Price targets** (e.g., 'What's the target for Tesla?')\n"
        answer += "• **Risk analysis** (e.g., 'How risky is Bitcoin?')\n"
        answer += "• **Sector insights** (e.g., 'How's the tech sector?')\n"
        answer += "• **Portfolio advice** (e.g., 'How should I diversify?')\n"
        answer += "• **Market outlook** (e.g., 'What's the market trend?')\n\n"
        answer += f"I have analysis on {len(investments)} investments across {len(set(inv.get('sector') for inv in investments if inv.get('sector')))} sectors."
        
        return {
            "answer": answer,
            "relevant_symbols": [],
            "confidence": 0.7,
            "sources": ["Investment knowledge base", "Q&A system guide"]
        }

@api_router.get("/investments/types/list")
async def get_investment_asset_types():
    pipeline = [
        {"$group": {"_id": "$asset_type", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    types = await db.investment_recommendations.aggregate(pipeline).to_list(100)
    return [{"asset_type": type_data["_id"], "count": type_data["count"]} for type_data in types]

@api_router.get("/investments", response_model=List[InvestmentRecommendationResponse])
async def get_investment_recommendations(asset_type: Optional[str] = Query(None)):
    query = {}
    if asset_type:
        query["asset_type"] = asset_type
    
    recommendations = await db.investment_recommendations.find(query).sort("last_updated", -1).to_list(100)
    return [InvestmentRecommendationResponse(**rec) for rec in recommendations]

@api_router.get("/investments/{recommendation_id}", response_model=InvestmentRecommendationResponse)
async def get_investment_recommendation(recommendation_id: str):
    recommendation = await db.investment_recommendations.find_one({"id": recommendation_id})
    if not recommendation:
        raise HTTPException(status_code=404, detail="Investment recommendation not found")
    return InvestmentRecommendationResponse(**recommendation)

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
