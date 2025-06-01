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
