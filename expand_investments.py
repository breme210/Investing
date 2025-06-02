import asyncio
import sys
import os
from datetime import datetime, timedelta
import random

# Add the backend directory to the path
sys.path.append('/app/backend')

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import uuid

# Load environment variables
load_dotenv('/app/backend/.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

async def create_comprehensive_investment_recommendations():
    """Create a comprehensive set of investment recommendations across all sectors"""
    
    recommendations = [
        # === TECHNOLOGY STOCKS ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "META",
            "name": "Meta Platforms, Inc.",
            "asset_type": "stock",
            "current_price": 298.75,
            "target_price": 350.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 84,
            "timeframe": "12M",
            "analyst": "Sarah Chen",
            "analysis": "Meta's AI investments and metaverse pivot are showing promising results. Strong user engagement across platforms and improving ad efficiency through AI targeting.",
            "key_factors": [
                "Reality Labs showing progress in VR/AR development",
                "AI-driven ad targeting improving ROAS for advertisers",
                "Instagram and WhatsApp monetization expanding",
                "Cost discipline initiatives improving margins",
                "Strong user growth in emerging markets"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=1),
            "price_change_24h": 4.25,
            "price_change_percent": 1.44,
            "market_cap": "$760B",
            "sector": "Technology",
            "technical_indicators": {
                "rsi": 61.2,
                "moving_avg_50": 285.40,
                "moving_avg_200": 260.15,
                "pe_ratio": 23.1,
                "volatility": 0.28
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "NFLX",
            "name": "Netflix, Inc.",
            "asset_type": "stock",
            "current_price": 456.30,
            "target_price": 500.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 78,
            "timeframe": "18M",
            "analyst": "David Rodriguez",
            "analysis": "Netflix's content strategy and global expansion continue to drive subscriber growth. Ad-supported tier gaining traction and improving revenue per user.",
            "key_factors": [
                "Ad-supported tier exceeding subscriber expectations",
                "Strong content pipeline including original productions",
                "International markets showing robust growth",
                "Gaming initiative adding new revenue streams",
                "Password sharing crackdown driving conversions"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=3),
            "price_change_24h": -2.85,
            "price_change_percent": -0.62,
            "market_cap": "$200B",
            "sector": "Technology",
            "technical_indicators": {
                "rsi": 54.8,
                "moving_avg_50": 445.20,
                "moving_avg_200": 420.75,
                "pe_ratio": 34.2,
                "volatility": 0.32
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "CRM",
            "name": "Salesforce, Inc.",
            "asset_type": "stock",
            "current_price": 224.80,
            "target_price": 260.00,
            "recommendation": "BUY",
            "risk_level": "LOW",
            "confidence_score": 81,
            "timeframe": "12M",
            "analyst": "Emily Zhang",
            "analysis": "Salesforce's AI integration across its platform is driving customer adoption and retention. Strong enterprise demand for CRM solutions continues.",
            "key_factors": [
                "Einstein AI platform gaining enterprise traction",
                "Subscription model providing predictable revenue",
                "Strong customer retention rates above 90%",
                "Data Cloud and analytics offerings expanding",
                "Strategic acquisitions enhancing platform capabilities"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=2),
            "price_change_24h": 3.15,
            "price_change_percent": 1.42,
            "market_cap": "$220B",
            "sector": "Technology",
            "technical_indicators": {
                "rsi": 58.7,
                "moving_avg_50": 218.30,
                "moving_avg_200": 205.40,
                "pe_ratio": 41.3,
                "volatility": 0.25
            }
        },
        
        # === HEALTHCARE STOCKS ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "JNJ",
            "name": "Johnson & Johnson",
            "asset_type": "stock",
            "current_price": 162.45,
            "target_price": 180.00,
            "recommendation": "BUY",
            "risk_level": "LOW",
            "confidence_score": 89,
            "timeframe": "12M",
            "analyst": "Dr. Michael Thompson",
            "analysis": "J&J's diversified healthcare portfolio and strong pharmaceutical pipeline provide stability and growth potential. Dividend aristocrat with consistent returns.",
            "key_factors": [
                "Strong pharmaceutical pipeline with multiple late-stage trials",
                "Medical device division showing recovery post-COVID",
                "Consistent dividend payments for 60+ years",
                "Global healthcare infrastructure well-positioned",
                "Recent spin-off creating focused pure-play healthcare company"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=4),
            "price_change_24h": 1.25,
            "price_change_percent": 0.77,
            "market_cap": "$435B",
            "sector": "Healthcare",
            "technical_indicators": {
                "rsi": 52.3,
                "moving_avg_50": 159.80,
                "moving_avg_200": 155.20,
                "pe_ratio": 15.8,
                "volatility": 0.18
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "PFE",
            "name": "Pfizer Inc.",
            "asset_type": "stock",
            "current_price": 28.95,
            "target_price": 35.00,
            "recommendation": "HOLD",
            "risk_level": "MEDIUM",
            "confidence_score": 65,
            "timeframe": "12M",
            "analyst": "Dr. Jennifer Liu",
            "analysis": "Pfizer faces post-COVID revenue normalization but maintains strong pipeline. Oncology and vaccine platforms provide long-term growth opportunities.",
            "key_factors": [
                "COVID vaccine revenues normalizing to baseline",
                "Strong oncology pipeline with multiple approvals expected",
                "RSV vaccine showing commercial promise",
                "Cost reduction initiatives improving efficiency",
                "Attractive dividend yield above 5%"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=6),
            "price_change_24h": -0.45,
            "price_change_percent": -1.53,
            "market_cap": "$165B",
            "sector": "Healthcare",
            "technical_indicators": {
                "rsi": 42.1,
                "moving_avg_50": 29.80,
                "moving_avg_200": 32.15,
                "pe_ratio": 12.4,
                "volatility": 0.24
            }
        },
        
        # === FINANCIAL STOCKS ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "JPM",
            "name": "JPMorgan Chase & Co.",
            "asset_type": "stock",
            "current_price": 184.70,
            "target_price": 205.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 86,
            "timeframe": "12M",
            "analyst": "Robert Kim",
            "analysis": "JPMorgan's diversified revenue streams and strong balance sheet position it well for economic uncertainty. Rising rates benefit net interest margins.",
            "key_factors": [
                "Net interest margin expansion from higher rates",
                "Strong credit quality with low loss provisions",
                "Investment banking recovery expected",
                "Robust capital ratios exceed regulatory requirements",
                "Consistent dividend growth track record"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=5),
            "price_change_24h": 2.85,
            "price_change_percent": 1.57,
            "market_cap": "$540B",
            "sector": "Financial Services",
            "technical_indicators": {
                "rsi": 64.2,
                "moving_avg_50": 178.90,
                "moving_avg_200": 165.45,
                "pe_ratio": 11.8,
                "volatility": 0.22
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "BAC",
            "name": "Bank of America Corporation",
            "asset_type": "stock",
            "current_price": 33.45,
            "target_price": 40.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 79,
            "timeframe": "15M",
            "analyst": "Kevin Park",
            "analysis": "Bank of America benefits significantly from rising interest rates given its large deposit base. Strong consumer banking franchise provides stability.",
            "key_factors": [
                "Large deposit base benefits from rate increases",
                "Consumer banking showing resilient performance",
                "Credit card spending remaining strong",
                "Wealth management division growing assets",
                "Efficiency initiatives reducing operational costs"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=7),
            "price_change_24h": 0.75,
            "price_change_percent": 2.29,
            "market_cap": "$270B",
            "sector": "Financial Services",
            "technical_indicators": {
                "rsi": 59.8,
                "moving_avg_50": 32.10,
                "moving_avg_200": 29.85,
                "pe_ratio": 12.3,
                "volatility": 0.25
            }
        },
        
        # === ENERGY STOCKS ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "XOM",
            "name": "Exxon Mobil Corporation",
            "asset_type": "stock",
            "current_price": 108.25,
            "target_price": 125.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 74,
            "timeframe": "12M",
            "analyst": "Alex Morgan",
            "analysis": "Exxon's disciplined capital allocation and focus on high-return projects in Permian Basin drive strong cash generation. Dividend sustainability improved.",
            "key_factors": [
                "Permian Basin production ramping significantly",
                "Strong free cash flow generation at current oil prices",
                "Capital discipline maintaining returns focus",
                "Dividend coverage substantially improved",
                "Refining margins providing additional upside"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=8),
            "price_change_24h": 1.95,
            "price_change_percent": 1.83,
            "market_cap": "$475B",
            "sector": "Energy",
            "technical_indicators": {
                "rsi": 56.4,
                "moving_avg_50": 105.80,
                "moving_avg_200": 98.30,
                "pe_ratio": 14.2,
                "volatility": 0.29
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "CVX",
            "name": "Chevron Corporation",
            "asset_type": "stock",
            "current_price": 154.80,
            "target_price": 170.00,
            "recommendation": "BUY",
            "risk_level": "LOW",
            "confidence_score": 82,
            "timeframe": "12M",
            "analyst": "Maria Santos",
            "analysis": "Chevron's conservative financial management and consistent dividend policy make it a defensive energy play. Strong downstream operations provide stability.",
            "key_factors": [
                "Consistent dividend payments for decades",
                "Strong balance sheet with low debt levels",
                "Diversified operations including refining",
                "Permian and international projects delivering",
                "Share buyback program returning cash to shareholders"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=9),
            "price_change_24h": 0.85,
            "price_change_percent": 0.55,
            "market_cap": "$290B",
            "sector": "Energy",
            "technical_indicators": {
                "rsi": 51.7,
                "moving_avg_50": 152.40,
                "moving_avg_200": 148.90,
                "pe_ratio": 13.8,
                "volatility": 0.21
            }
        },
        
        # === CONSUMER GOODS ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "PG",
            "name": "Procter & Gamble Company",
            "asset_type": "stock",
            "current_price": 158.30,
            "target_price": 170.00,
            "recommendation": "BUY",
            "risk_level": "LOW",
            "confidence_score": 85,
            "timeframe": "12M",
            "analyst": "Lisa Wong",
            "analysis": "P&G's strong brand portfolio and pricing power provide resilience during economic uncertainty. Consistent dividend growth makes it a defensive staple.",
            "key_factors": [
                "Strong brand portfolio with pricing power",
                "Consistent market share in key categories",
                "Innovation pipeline driving premium positioning",
                "Emerging markets growth acceleration",
                "Dividend aristocrat with 67 years of increases"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=10),
            "price_change_24h": 1.45,
            "price_change_percent": 0.92,
            "market_cap": "$375B",
            "sector": "Consumer Staples",
            "technical_indicators": {
                "rsi": 54.2,
                "moving_avg_50": 156.70,
                "moving_avg_200": 152.30,
                "pe_ratio": 24.1,
                "volatility": 0.16
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "KO",
            "name": "The Coca-Cola Company",
            "asset_type": "stock",
            "current_price": 62.15,
            "target_price": 68.00,
            "recommendation": "HOLD",
            "risk_level": "LOW",
            "confidence_score": 71,
            "timeframe": "12M",
            "analyst": "James Miller",
            "analysis": "Coca-Cola's global brand strength and diversified beverage portfolio provide stability. Health consciousness trends present long-term challenges.",
            "key_factors": [
                "Global brand recognition and distribution network",
                "Diversification into healthier beverage options",
                "Strong emerging markets presence",
                "Reliable dividend payments for 60+ years",
                "Bottling partner relationships providing operational leverage"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=11),
            "price_change_24h": 0.25,
            "price_change_percent": 0.40,
            "market_cap": "$270B",
            "sector": "Consumer Staples",
            "technical_indicators": {
                "rsi": 48.9,
                "moving_avg_50": 61.80,
                "moving_avg_200": 59.45,
                "pe_ratio": 26.3,
                "volatility": 0.14
            }
        },
        
        # === ETFs AND INDICES ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "QQQ",
            "name": "Invesco QQQ Trust ETF",
            "asset_type": "index",
            "current_price": 428.75,
            "target_price": 465.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 83,
            "timeframe": "12M",
            "analyst": "Robert Kim",
            "analysis": "Technology-focused ETF provides exposure to innovation leaders. AI and cloud computing trends support continued outperformance of tech sector.",
            "key_factors": [
                "Exposure to leading technology companies",
                "AI revolution benefiting major holdings",
                "Strong historical performance track record",
                "Liquid trading with tight spreads",
                "Growing influence of technology in economy"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=2),
            "price_change_24h": 3.25,
            "price_change_percent": 0.76,
            "market_cap": "$240B AUM",
            "sector": "Technology",
            "technical_indicators": {
                "rsi": 62.8,
                "moving_avg_50": 418.30,
                "moving_avg_200": 385.60,
                "volatility": 0.22
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "VTI",
            "name": "Vanguard Total Stock Market ETF",
            "asset_type": "index",
            "current_price": 243.85,
            "target_price": 260.00,
            "recommendation": "BUY",
            "risk_level": "LOW",
            "confidence_score": 88,
            "timeframe": "12M",
            "analyst": "Sarah Chen",
            "analysis": "Broad market exposure with low fees provides excellent diversification. Long-term secular growth of US economy supports continued appreciation.",
            "key_factors": [
                "Complete US stock market exposure",
                "Ultra-low expense ratio of 0.03%",
                "Strong long-term historical returns",
                "Automatic rebalancing and diversification",
                "Backed by Vanguard's reputation and scale"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=1),
            "price_change_24h": 1.85,
            "price_change_percent": 0.76,
            "market_cap": "$1.8T AUM",
            "sector": "Diversified",
            "technical_indicators": {
                "rsi": 57.2,
                "moving_avg_50": 239.40,
                "moving_avg_200": 225.80,
                "volatility": 0.16
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "IWM",
            "name": "iShares Russell 2000 ETF",
            "asset_type": "index",
            "current_price": 198.45,
            "target_price": 220.00,
            "recommendation": "BUY",
            "risk_level": "HIGH",
            "confidence_score": 76,
            "timeframe": "18M",
            "analyst": "David Rodriguez",
            "analysis": "Small-cap stocks positioned to benefit from economic recovery and domestic growth. Higher volatility but greater upside potential than large caps.",
            "key_factors": [
                "Small-cap valuations attractive relative to large caps",
                "Domestic focus benefits from US economic strength",
                "Higher beta provides leverage to market upside",
                "M&A activity supporting small-cap premiums",
                "Fed policy normalization benefiting smaller companies"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=3),
            "price_change_24h": -1.25,
            "price_change_percent": -0.63,
            "market_cap": "$72B AUM",
            "sector": "Small Cap",
            "technical_indicators": {
                "rsi": 44.3,
                "moving_avg_50": 202.10,
                "moving_avg_200": 185.75,
                "volatility": 0.28
            }
        },
        
        # === COMMODITIES ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "GLD",
            "name": "SPDR Gold Trust ETF",
            "asset_type": "commodity",
            "current_price": 184.25,
            "target_price": 210.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 79,
            "timeframe": "18M",
            "analyst": "Alex Morgan",
            "analysis": "Gold provides portfolio diversification and inflation hedge. Central bank buying and geopolitical tensions support higher prices.",
            "key_factors": [
                "Central banks increasing gold reserves globally",
                "Inflation hedge during monetary uncertainty",
                "Geopolitical tensions driving safe-haven demand",
                "Dollar weakness supporting gold prices",
                "Portfolio diversification benefits during volatility"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=4),
            "price_change_24h": 2.15,
            "price_change_percent": 1.18,
            "market_cap": "$68B AUM",
            "sector": "Precious Metals",
            "technical_indicators": {
                "rsi": 61.7,
                "moving_avg_50": 178.90,
                "moving_avg_200": 172.40,
                "volatility": 0.19
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "USO",
            "name": "United States Oil Fund ETF",
            "asset_type": "commodity",
            "current_price": 72.80,
            "target_price": 85.00,
            "recommendation": "HOLD",
            "risk_level": "HIGH",
            "confidence_score": 68,
            "timeframe": "12M",
            "analyst": "Emily Zhang",
            "analysis": "Oil prices supported by supply constraints but face headwinds from economic uncertainty and renewable energy transition.",
            "key_factors": [
                "OPEC+ production cuts supporting prices",
                "Strategic petroleum reserve releases ending",
                "Refining capacity constraints",
                "Economic growth uncertainty affecting demand",
                "Long-term transition to renewable energy"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=5),
            "price_change_24h": -1.45,
            "price_change_percent": -1.95,
            "market_cap": "$2.1B AUM",
            "sector": "Energy",
            "technical_indicators": {
                "rsi": 46.2,
                "moving_avg_50": 75.30,
                "moving_avg_200": 68.15,
                "volatility": 0.35
            }
        },
        
        # === INTERNATIONAL EXPOSURE ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "EFA",
            "name": "iShares MSCI EAFE ETF",
            "asset_type": "index",
            "current_price": 78.45,
            "target_price": 85.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 74,
            "timeframe": "15M",
            "analyst": "Maria Santos",
            "analysis": "European and Asian developed markets offer geographic diversification and attractive valuations relative to US markets.",
            "key_factors": [
                "Attractive valuations vs US markets",
                "European economic recovery gaining momentum",
                "Currency diversification benefits",
                "Strong dividend yields from international stocks",
                "Japan showing signs of sustained growth"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=6),
            "price_change_24h": 0.95,
            "price_change_percent": 1.22,
            "market_cap": "$98B AUM",
            "sector": "International",
            "technical_indicators": {
                "rsi": 53.8,
                "moving_avg_50": 77.20,
                "moving_avg_200": 74.85,
                "volatility": 0.21
            }
        },
        
        # === EMERGING MARKETS ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "EEM",
            "name": "iShares MSCI Emerging Markets ETF",
            "asset_type": "index",
            "current_price": 42.30,
            "target_price": 50.00,
            "recommendation": "BUY",
            "risk_level": "HIGH",
            "confidence_score": 71,
            "timeframe": "24M",
            "analyst": "Kevin Park",
            "analysis": "Emerging markets offer long-term growth potential as demographics and infrastructure development drive economic expansion.",
            "key_factors": [
                "Favorable demographics in key markets",
                "Infrastructure investment driving growth",
                "Commodity exporters benefiting from supply constraints",
                "Technology adoption accelerating",
                "Valuations attractive relative to developed markets"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=7),
            "price_change_24h": 0.65,
            "price_change_percent": 1.56,
            "market_cap": "$25B AUM",
            "sector": "Emerging Markets",
            "technical_indicators": {
                "rsi": 49.7,
                "moving_avg_50": 41.85,
                "moving_avg_200": 39.20,
                "volatility": 0.26
            }
        },
        
        # === REAL ESTATE ===
        {
            "id": str(uuid.uuid4()),
            "symbol": "VNQ",
            "name": "Vanguard Real Estate ETF",
            "asset_type": "index",
            "current_price": 89.75,
            "target_price": 98.00,
            "recommendation": "HOLD",
            "risk_level": "MEDIUM",
            "confidence_score": 69,
            "timeframe": "12M",
            "analyst": "Jennifer Liu",
            "analysis": "REITs face pressure from higher interest rates but offer attractive dividend yields and inflation protection over long term.",
            "key_factors": [
                "Attractive dividend yields above 3.5%",
                "Inflation protection through rent escalations",
                "Commercial real estate fundamentals mixed",
                "Interest rate sensitivity creating headwinds",
                "Data centers and logistics showing strength"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=8),
            "price_change_24h": -0.75,
            "price_change_percent": -0.83,
            "market_cap": "$28B AUM",
            "sector": "Real Estate",
            "technical_indicators": {
                "rsi": 45.1,
                "moving_avg_50": 91.30,
                "moving_avg_200": 85.60,
                "volatility": 0.24
            }
        }
    ]
    
    # Add the existing recommendations to preserve them
    existing_recs = await db.investment_recommendations.find().to_list(1000)
    all_recommendations = existing_recs + recommendations
    
    # Clear and replace all recommendations
    await db.investment_recommendations.delete_many({})
    await db.investment_recommendations.insert_many(all_recommendations)
    
    print(f"✅ Created comprehensive database with {len(all_recommendations)} investment recommendations")
    print(f"   • {len([r for r in all_recommendations if r['asset_type'] == 'stock'])} Individual Stocks")
    print(f"   • {len([r for r in all_recommendations if r['asset_type'] == 'index'])} ETFs/Indices") 
    print(f"   • {len([r for r in all_recommendations if r['asset_type'] == 'commodity'])} Commodities")
    print(f"   • {len([r for r in all_recommendations if r['recommendation'] == 'BUY'])} BUY recommendations")
    print(f"   • {len([r for r in all_recommendations if r['recommendation'] == 'HOLD'])} HOLD recommendations")
    print(f"   • {len([r for r in all_recommendations if r['recommendation'] == 'SELL'])} SELL recommendations")

async def main():
    """Main function to expand investment database"""
    print("🚀 Expanding investment recommendation database...")
    
    try:
        await create_comprehensive_investment_recommendations()
        print("\n🎉 Investment database successfully expanded!")
        
    except Exception as e:
        print(f"❌ Error expanding database: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())