import asyncio
import uuid
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path
import random

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Sample investment recommendations covering stocks, indices, and commodities
sample_recommendations = [
    # STOCKS
    {
        "id": str(uuid.uuid4()),
        "symbol": "AAPL",
        "name": "Apple Inc.",
        "asset_type": "stock",
        "current_price": 195.89,
        "target_price": 220.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 87,
        "timeframe": "6M",
        "analyst": "Sarah Chen, CFA",
        "analysis": "Apple continues to demonstrate strong fundamentals with robust iPhone sales and expanding services revenue. The company's focus on AI integration across its ecosystem and potential Vision Pro adoption creates multiple growth catalysts. Strong balance sheet and consistent dividend payments make it an attractive long-term investment.",
        "key_factors": [
            "Strong Q4 earnings beat expectations",
            "AI integration driving product innovation",
            "Services revenue growing 16% YoY",
            "Vision Pro market potential",
            "Solid cash flow and dividend yield"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 3.45,
        "price_change_percent": 1.79,
        "market_cap": "$3.01T",
        "pe_ratio": None,
        "sector": "Technology"
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "TSLA",
        "name": "Tesla, Inc.",
        "asset_type": "stock",
        "current_price": 248.42,
        "target_price": 280.00,
        "recommendation": "BUY",
        "risk_level": "HIGH",
        "confidence_score": 72,
        "timeframe": "1Y",
        "analyst": "Michael Rodriguez",
        "analysis": "Tesla's position in the EV market remains strong despite increased competition. The company's energy business and Full Self-Driving technology represent significant upside potential. However, high volatility and execution risks on new projects require careful consideration.",
        "key_factors": [
            "EV market leadership position",
            "Energy storage business growth",
            "FSD technology advancement",
            "Cybertruck production ramp",
            "Supercharger network expansion"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": -5.67,
        "price_change_percent": -2.23,
        "market_cap": "$792.3B",
        "pe_ratio": None,
        "sector": "Automotive"
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "NVDA",
        "name": "NVIDIA Corporation",
        "asset_type": "stock",
        "current_price": 875.30,
        "target_price": 950.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 91,
        "timeframe": "3M",
        "analyst": "Dr. Jennifer Park",
        "analysis": "NVIDIA's dominance in AI chip market continues with strong datacenter revenue growth. The company benefits from the AI boom across industries. Gaming recovery and automotive segment growth provide additional revenue streams.",
        "key_factors": [
            "AI datacenter demand surge",
            "H100 and upcoming H200 chip leadership",
            "Strong partnership ecosystem",
            "Gaming market recovery",
            "Automotive AI solutions"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=1),
        "price_change_24h": 12.45,
        "price_change_percent": 1.44,
        "market_cap": "$2.15T",
        "pe_ratio": None,
        "sector": "Technology"
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "MSFT",
        "name": "Microsoft Corporation",
        "asset_type": "stock",
        "current_price": 420.55,
        "target_price": 450.00,
        "recommendation": "HOLD",
        "risk_level": "LOW",
        "confidence_score": 78,
        "timeframe": "3M",
        "analyst": "Robert Kim, CFA",
        "analysis": "Microsoft shows steady growth across cloud services and productivity software. Azure continues gaining market share, while AI integration in Office suite drives subscription growth. Current valuation appears fairly priced with limited near-term upside.",
        "key_factors": [
            "Azure cloud growth momentum",
            "AI integration in productivity suite",
            "Strong enterprise relationships",
            "Steady dividend increases",
            "Fair current valuation"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 1.23,
        "price_change_percent": 0.29,
        "market_cap": "$3.12T",
        "pe_ratio": None,
        "sector": "Technology"
    },
    
    # INDICES
    {
        "id": str(uuid.uuid4()),
        "symbol": "SPY",
        "name": "SPDR S&P 500 ETF Trust",
        "asset_type": "index",
        "current_price": 515.67,
        "target_price": 545.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 82,
        "timeframe": "6M",
        "analyst": "Maria Gonzalez, CFA",
        "analysis": "The S&P 500 index shows resilience with strong corporate earnings and economic fundamentals. Technology sector leadership and defensive sector stability provide balanced exposure. Fed policy normalization creates favorable environment for equity markets.",
        "key_factors": [
            "Strong corporate earnings growth",
            "Technology sector outperformance",
            "Economic resilience indicators",
            "Fed policy stabilization",
            "Low unemployment rates"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 2.34,
        "price_change_percent": 0.46,
        "market_cap": "$460.8B",
        "sector": "Diversified"
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "QQQ",
        "name": "Invesco QQQ Trust ETF",
        "asset_type": "index",
        "current_price": 445.23,
        "target_price": 420.00,
        "recommendation": "HOLD",
        "risk_level": "MEDIUM",
        "confidence_score": 68,
        "timeframe": "3M",
        "analyst": "David Thompson",
        "analysis": "NASDAQ-100 faces headwinds from high valuations in technology sector. While AI theme continues driving growth, rising interest rates and increased competition may pressure multiples. Selective approach recommended over broad exposure.",
        "key_factors": [
            "High technology sector valuations",
            "AI theme driving innovation",
            "Interest rate sensitivity",
            "Competitive landscape changes",
            "Earnings growth sustainability"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": -1.89,
        "price_change_percent": -0.42,
        "market_cap": "$205.3B",
        "sector": "Technology"
    },
    
    # COMMODITIES
    {
        "id": str(uuid.uuid4()),
        "symbol": "GLD",
        "name": "SPDR Gold Shares ETF",
        "asset_type": "commodity",
        "current_price": 185.45,
        "target_price": 205.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 75,
        "timeframe": "6M",
        "analyst": "Amanda Foster, CFA",
        "analysis": "Gold serves as effective hedge against inflation and currency debasement. Central bank purchases and geopolitical tensions support demand. Technical indicators suggest breakout potential above $2000/oz level.",
        "key_factors": [
            "Inflation hedging properties",
            "Central bank accumulation",
            "Geopolitical uncertainty",
            "Dollar weakness potential",
            "Technical breakout setup"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=1),
        "price_change_24h": 2.67,
        "price_change_percent": 1.46,
        "market_cap": "$68.2B",
        "sector": "Precious Metals"
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "USO",
        "name": "United States Oil Fund",
        "asset_type": "commodity",
        "current_price": 78.90,
        "target_price": 75.00,
        "recommendation": "SELL",
        "risk_level": "HIGH",
        "confidence_score": 73,
        "timeframe": "3M",
        "analyst": "James Wilson",
        "analysis": "Oil prices face pressure from increased US production and global economic slowdown concerns. OPEC+ production decisions remain key variable, but demand growth appears limited in near term. Technical support levels weakening.",
        "key_factors": [
            "US production increases",
            "Global demand concerns",
            "OPEC+ policy uncertainty",
            "Strategic reserve releases",
            "Technical support breakdown"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": -2.45,
        "price_change_percent": -3.01,
        "market_cap": "$4.1B",
        "sector": "Energy"
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "BTC-USD",
        "name": "Bitcoin",
        "asset_type": "commodity",
        "current_price": 67845.32,
        "target_price": 75000.00,
        "recommendation": "BUY",
        "risk_level": "HIGH",
        "confidence_score": 69,
        "timeframe": "6M",
        "analyst": "Alex Carter, CFA",
        "analysis": "Bitcoin shows institutional adoption momentum with ETF approvals and corporate treasury allocation. Regulatory clarity improvements and halving event create positive technical backdrop. High volatility requires appropriate position sizing.",
        "key_factors": [
            "Institutional adoption growth",
            "Bitcoin ETF approvals",
            "Regulatory clarity improvements",
            "Upcoming halving event",
            "Corporate treasury adoption"
        ],
        "last_updated": datetime.utcnow() - timedelta(minutes=30),
        "price_change_24h": 1234.56,
        "price_change_percent": 1.85,
        "market_cap": "$1.33T",
        "sector": "Cryptocurrency"
    }
]

async def populate_investment_recommendations():
    """Populate the database with sample investment recommendations"""
    try:
        # Clear existing recommendations
        await db.investment_recommendations.delete_many({})
        print("Cleared existing investment recommendations")
        
        # Insert sample recommendations
        result = await db.investment_recommendations.insert_many(sample_recommendations)
        print(f"Inserted {len(result.inserted_ids)} investment recommendations")
        
        # Verify insertion
        count = await db.investment_recommendations.count_documents({})
        print(f"Total recommendations in database: {count}")
        
        # Show asset types
        asset_types = await db.investment_recommendations.distinct("asset_type")
        print(f"Asset types available: {', '.join(asset_types)}")
        
        # Show recommendations breakdown
        for asset_type in asset_types:
            count = await db.investment_recommendations.count_documents({"asset_type": asset_type})
            print(f"- {asset_type}: {count} recommendations")
        
    except Exception as e:
        print(f"Error populating database: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(populate_investment_recommendations())