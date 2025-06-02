import asyncio
import uuid
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Comprehensive commodities and indices expansion
additional_commodities_and_indices = [
    # ADDITIONAL COMMODITIES (12 new ones)
    
    # Energy Commodities
    {
        "id": str(uuid.uuid4()),
        "symbol": "UNG",
        "name": "United States Natural Gas Fund",
        "asset_type": "commodity",
        "current_price": 18.45,
        "target_price": 22.00,
        "recommendation": "BUY",
        "risk_level": "HIGH",
        "confidence_score": 71,
        "timeframe": "6M",
        "analyst": "Energy Commodities Team",
        "analysis": "Natural gas benefits from increased LNG exports and winter heating demand. Supply constraints in major producing regions supporting prices. However, renewable energy transition poses long-term headwinds.",
        "key_factors": [
            "LNG export capacity expanding 25% in 2024",
            "Winter heating demand supporting seasonal rally",
            "US production growth slowing in key basins",
            "European energy security driving demand",
            "Storage levels below 5-year averages",
            "Industrial demand recovering post-recession"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 0.85,
        "price_change_percent": 4.83,
        "market_cap": "$1.2B",
        "sector": "Energy",
        "technical_indicators": {
            "rsi": 62.1,
            "moving_avg_50": 17.80,
            "moving_avg_200": 16.20,
            "pe_ratio": None,
            "volatility": 0.58
        }
    },
    
    # Agricultural Commodities
    {
        "id": str(uuid.uuid4()),
        "symbol": "CORN",
        "name": "Teucrium Corn Fund",
        "asset_type": "commodity",
        "current_price": 22.85,
        "target_price": 26.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 68,
        "timeframe": "9M",
        "analyst": "Agricultural Specialist",
        "analysis": "Corn prices supported by strong ethanol demand and export growth to key markets. Weather concerns in major growing regions could provide upside catalysts. Biofuel mandates supporting demand floor.",
        "key_factors": [
            "Ethanol demand growing 8% annually",
            "Export demand from Asia strengthening",
            "Weather concerns in Midwest growing regions",
            "Biofuel mandates supporting price floor",
            "Livestock feed demand remaining stable",
            "Inventory levels declining year-over-year"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": 0.45,
        "price_change_percent": 2.01,
        "market_cap": "$0.8B",
        "sector": "Agriculture",
        "technical_indicators": {
            "rsi": 58.3,
            "moving_avg_50": 22.40,
            "moving_avg_200": 21.15,
            "pe_ratio": None,
            "volatility": 0.42
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "WEAT",
        "name": "Teucrium Wheat Fund",
        "asset_type": "commodity",
        "current_price": 8.95,
        "target_price": 10.50,
        "recommendation": "BUY",
        "risk_level": "HIGH",
        "confidence_score": 73,
        "timeframe": "6M",
        "analyst": "Grain Markets Analyst",
        "analysis": "Wheat prices supported by geopolitical tensions affecting major exporters and weather-related production concerns. Global food security issues driving strategic stockpiling by importing nations.",
        "key_factors": [
            "Geopolitical tensions affecting Black Sea exports",
            "Weather concerns in major producing regions",
            "Strategic stockpiling by importing nations",
            "Global food security driving demand",
            "Currency weakness in exporting countries",
            "Quality premiums for high-grade wheat"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 0.28,
        "price_change_percent": 3.23,
        "market_cap": "$0.3B",
        "sector": "Agriculture",
        "technical_indicators": {
            "rsi": 64.7,
            "moving_avg_50": 8.70,
            "moving_avg_200": 8.20,
            "pe_ratio": None,
            "volatility": 0.51
        }
    },
    
    # Industrial Metals
    {
        "id": str(uuid.uuid4()),
        "symbol": "CPER",
        "name": "United States Copper Index Fund",
        "asset_type": "commodity",
        "current_price": 25.40,
        "target_price": 29.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 76,
        "timeframe": "9M",
        "analyst": "Industrial Metals Team",
        "analysis": "Copper benefits from electric vehicle adoption and renewable energy infrastructure development. Supply constraints from major mines and China's infrastructure spending supporting demand.",
        "key_factors": [
            "EV adoption driving wire and cable demand",
            "Renewable energy infrastructure requiring copper",
            "China infrastructure spending remaining elevated",
            "Mine supply growth limited by permitting",
            "Inventory levels at multi-year lows",
            "Industrial automation increasing usage"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 0.75,
        "price_change_percent": 3.05,
        "market_cap": "$0.9B",
        "sector": "Industrial Metals",
        "technical_indicators": {
            "rsi": 61.2,
            "moving_avg_50": 24.80,
            "moving_avg_200": 23.15,
            "pe_ratio": None,
            "volatility": 0.38
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "PPLT",
        "name": "Aberdeen Standard Physical Platinum Shares ETF",
        "asset_type": "commodity",
        "current_price": 85.20,
        "target_price": 95.00,
        "recommendation": "HOLD",
        "risk_level": "HIGH",
        "confidence_score": 69,
        "timeframe": "12M",
        "analyst": "Precious Metals Specialist",
        "analysis": "Platinum faces mixed fundamentals with automotive demand declining due to EV adoption, offset by industrial and hydrogen fuel cell applications. South African supply risks provide support.",
        "key_factors": [
            "Automotive demand declining with EV adoption",
            "Hydrogen fuel cell applications expanding",
            "Industrial demand for chemical processing stable",
            "South African mining supply risks elevated",
            "Investment demand remaining subdued",
            "Jewelry demand recovering in key markets"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": -1.25,
        "price_change_percent": -1.45,
        "market_cap": "$1.8B",
        "sector": "Precious Metals",
        "technical_indicators": {
            "rsi": 47.8,
            "moving_avg_50": 87.40,
            "moving_avg_200": 89.60,
            "pe_ratio": None,
            "volatility": 0.34
        }
    },
    
    # Currency/Dollar
    {
        "id": str(uuid.uuid4()),
        "symbol": "UUP",
        "name": "Invesco DB US Dollar Index Bullish Fund",
        "asset_type": "commodity",
        "current_price": 28.75,
        "target_price": 30.50,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 74,
        "timeframe": "6M",
        "analyst": "Currency Strategist",
        "analysis": "US Dollar strength supported by relative economic outperformance and Fed policy divergence. Safe haven demand and energy independence supporting dollar dominance in global trade.",
        "key_factors": [
            "US economic outperformance vs global peers",
            "Fed policy supporting dollar strength",
            "Safe haven demand during geopolitical tensions",
            "Energy independence reducing trade deficit",
            "Reserve currency status maintaining demand",
            "Real interest rate differentials favoring dollar"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=1),
        "price_change_24h": 0.15,
        "price_change_percent": 0.53,
        "market_cap": "$1.5B",
        "sector": "Currency",
        "technical_indicators": {
            "rsi": 57.3,
            "moving_avg_50": 28.45,
            "moving_avg_200": 27.80,
            "pe_ratio": None,
            "volatility": 0.16
        }
    },
    
    # ADDITIONAL INDICES (12 new ones)
    
    # Broad Market Indices
    {
        "id": str(uuid.uuid4()),
        "symbol": "VTI",
        "name": "Vanguard Total Stock Market ETF",
        "asset_type": "index",
        "current_price": 245.80,
        "target_price": 265.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 85,
        "timeframe": "9M",
        "analyst": "Broad Market Strategist",
        "analysis": "Total stock market exposure provides comprehensive US equity diversification with low fees. Economic resilience and corporate earnings growth supporting broad market performance across all capitalizations.",
        "key_factors": [
            "Comprehensive US equity market exposure",
            "Ultra-low expense ratio of 0.03%",
            "Small, mid, and large-cap diversification",
            "Economic fundamentals supporting equities",
            "Corporate earnings growth acceleration",
            "Long-term demographic trends positive"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=1),
        "price_change_24h": 1.85,
        "price_change_percent": 0.76,
        "market_cap": "$330.5B",
        "sector": "Diversified",
        "technical_indicators": {
            "rsi": 59.4,
            "moving_avg_50": 242.60,
            "moving_avg_200": 230.15,
            "pe_ratio": 22.1,
            "volatility": 0.17
        }
    },
    
    # International Indices
    {
        "id": str(uuid.uuid4()),
        "symbol": "EFA",
        "name": "iShares MSCI EAFE ETF",
        "asset_type": "index",
        "current_price": 78.90,
        "target_price": 85.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 72,
        "timeframe": "12M",
        "analyst": "International Equity Strategist",
        "analysis": "European and Asian developed markets trading at attractive valuations relative to US markets. Economic recovery in Europe and dividend yields providing income opportunity.",
        "key_factors": [
            "Valuation discount to US markets attractive",
            "European economic recovery gaining momentum",
            "Dividend yields higher than US equivalents",
            "Currency hedging opportunities available",
            "Diversification benefits vs US concentration",
            "Emerging market exposure through multinationals"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 0.95,
        "price_change_percent": 1.22,
        "market_cap": "$89.2B",
        "sector": "International",
        "technical_indicators": {
            "rsi": 54.8,
            "moving_avg_50": 77.90,
            "moving_avg_200": 75.40,
            "pe_ratio": 14.2,
            "volatility": 0.21
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "EEM",
        "name": "iShares MSCI Emerging Markets ETF",
        "asset_type": "index",
        "current_price": 42.15,
        "target_price": 48.00,
        "recommendation": "BUY",
        "risk_level": "HIGH",
        "confidence_score": 70,
        "timeframe": "18M",
        "analyst": "Emerging Markets Specialist",
        "analysis": "Emerging markets offer compelling long-term growth potential with demographic advantages and infrastructure development. China reopening and commodity cycles supporting near-term performance.",
        "key_factors": [
            "Demographic dividend in key markets",
            "Infrastructure development accelerating",
            "China economic reopening supporting region",
            "Commodity cycle benefiting resource exporters",
            "Valuation discount vs developed markets",
            "Technology adoption leapfrogging developed markets"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": 1.25,
        "price_change_percent": 3.06,
        "market_cap": "$29.8B",
        "sector": "Emerging Markets",
        "technical_indicators": {
            "rsi": 61.7,
            "moving_avg_50": 41.30,
            "moving_avg_200": 38.90,
            "pe_ratio": 12.8,
            "volatility": 0.28
        }
    },
    
    # Sector Indices
    {
        "id": str(uuid.uuid4()),
        "symbol": "XLK",
        "name": "Technology Select Sector SPDR Fund",
        "asset_type": "index",
        "current_price": 185.40,
        "target_price": 200.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 81,
        "timeframe": "6M",
        "analyst": "Technology Sector Strategist",
        "analysis": "Technology sector benefits from AI revolution, cloud adoption, and digital transformation trends. Strong fundamentals and innovation pipeline supporting continued outperformance.",
        "key_factors": [
            "AI revolution driving technology demand",
            "Cloud adoption accelerating across industries",
            "Digital transformation investments continuing",
            "Strong balance sheets and cash generation",
            "Innovation pipeline robust across subsectors",
            "Regulatory environment stabilizing"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 2.85,
        "price_change_percent": 1.56,
        "market_cap": "$58.9B",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 63.2,
            "moving_avg_50": 182.70,
            "moving_avg_200": 172.80,
            "pe_ratio": 29.4,
            "volatility": 0.24
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "XLF",
        "name": "Financial Select Sector SPDR Fund",
        "asset_type": "index",
        "current_price": 38.75,
        "target_price": 42.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 78,
        "timeframe": "9M",
        "analyst": "Financial Sector Strategist",
        "analysis": "Financial sector benefits from rising interest rates and improving credit quality. Bank earnings recovering while insurance companies benefit from higher investment yields.",
        "key_factors": [
            "Rising interest rates expanding net interest margins",
            "Credit quality metrics improving across sector",
            "Bank earnings recovering from pandemic lows",
            "Insurance companies benefiting from higher yields",
            "Regulatory environment becoming more favorable",
            "Capital return programs resuming"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 0.65,
        "price_change_percent": 1.70,
        "market_cap": "$42.1B",
        "sector": "Financial Services",
        "technical_indicators": {
            "rsi": 59.6,
            "moving_avg_50": 38.20,
            "moving_avg_200": 36.40,
            "pe_ratio": 13.8,
            "volatility": 0.26
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "XLE",
        "name": "Energy Select Sector SPDR Fund",
        "asset_type": "index",
        "current_price": 88.30,
        "target_price": 95.00,
        "recommendation": "HOLD",
        "risk_level": "HIGH",
        "confidence_score": 67,
        "timeframe": "6M",
        "analyst": "Energy Sector Strategist",
        "analysis": "Energy sector faces mixed outlook with oil price volatility and energy transition headwinds offset by strong cash flows and shareholder returns. Geopolitical factors providing support.",
        "key_factors": [
            "Strong cash flow generation at current prices",
            "Shareholder return programs well-funded",
            "Geopolitical factors supporting oil prices",
            "Capital discipline maintaining returns",
            "Energy transition creating long-term headwinds",
            "Refining margins remaining elevated"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": -1.45,
        "price_change_percent": -1.62,
        "market_cap": "$27.5B",
        "sector": "Energy",
        "technical_indicators": {
            "rsi": 52.1,
            "moving_avg_50": 89.80,
            "moving_avg_200": 85.60,
            "pe_ratio": 11.9,
            "volatility": 0.31
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "XLV",
        "name": "Health Care Select Sector SPDR Fund",
        "asset_type": "index",
        "current_price": 135.60,
        "target_price": 145.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 83,
        "timeframe": "9M",
        "analyst": "Healthcare Sector Strategist",
        "analysis": "Healthcare sector benefits from aging demographics and innovative drug pipelines. Defensive characteristics attractive during market volatility while growth opportunities remain robust.",
        "key_factors": [
            "Aging demographics driving healthcare demand",
            "Innovative drug pipelines showing promise",
            "Defensive characteristics during volatility",
            "Medical device innovation accelerating",
            "Biotech sector showing signs of recovery",
            "Healthcare services expanding access"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 1.85,
        "price_change_percent": 1.38,
        "market_cap": "$32.8B",
        "sector": "Healthcare",
        "technical_indicators": {
            "rsi": 60.4,
            "moving_avg_50": 134.20,
            "moving_avg_200": 128.90,
            "pe_ratio": 16.7,
            "volatility": 0.18
        }
    },
    
    # Bond Indices
    {
        "id": str(uuid.uuid4()),
        "symbol": "TLT",
        "name": "iShares 20+ Year Treasury Bond ETF",
        "asset_type": "index",
        "current_price": 95.40,
        "target_price": 105.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 71,
        "timeframe": "12M",
        "analyst": "Fixed Income Strategist",
        "analysis": "Long-term Treasury bonds positioned for potential rate cuts and economic slowdown scenarios. Duration risk elevated but yields attractive for income-focused investors seeking safety.",
        "key_factors": [
            "Potential Fed rate cuts supporting long bonds",
            "Economic slowdown scenarios favoring Treasuries",
            "Duration risk elevated with high sensitivity",
            "Yields attractive for income investors",
            "Safe haven demand during market stress",
            "Inflation expectations moderating"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 1.85,
        "price_change_percent": 1.98,
        "market_cap": "$18.9B",
        "sector": "Fixed Income",
        "technical_indicators": {
            "rsi": 55.8,
            "moving_avg_50": 94.20,
            "moving_avg_200": 91.80,
            "pe_ratio": None,
            "volatility": 0.22
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "HYG",
        "name": "iShares iBoxx High Yield Corporate Bond ETF",
        "asset_type": "index",
        "current_price": 78.25,
        "target_price": 82.00,
        "recommendation": "HOLD",
        "risk_level": "MEDIUM",
        "confidence_score": 69,
        "timeframe": "9M",
        "analyst": "Credit Strategist",
        "analysis": "High yield corporate bonds offer attractive income but face credit cycle headwinds. Spread levels reasonable but economic slowdown could pressure lower-quality issuers.",
        "key_factors": [
            "Attractive yield income for bond investors",
            "Credit spreads at reasonable levels",
            "Economic slowdown pressuring credit quality",
            "Corporate earnings supporting fundamentals",
            "Default rates remaining below historical averages",
            "Federal Reserve policy impact on credit markets"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": -0.25,
        "price_change_percent": -0.32,
        "market_cap": "$12.4B",
        "sector": "Fixed Income",
        "technical_indicators": {
            "rsi": 48.7,
            "moving_avg_50": 78.80,
            "moving_avg_200": 79.40,
            "pe_ratio": None,
            "volatility": 0.14
        }
    }
]

async def add_comprehensive_commodities_and_indices():
    """Add comprehensive commodities and indices coverage"""
    try:
        # Get current count
        current_count = await db.investment_recommendations.count_documents({})
        print(f"Current recommendations in database: {current_count}")
        
        # Insert additional commodities and indices
        result = await db.investment_recommendations.insert_many(additional_commodities_and_indices)
        print(f"Added {len(result.inserted_ids)} additional commodities and indices")
        
        # Verify new total
        new_count = await db.investment_recommendations.count_documents({})
        print(f"Total recommendations now: {new_count}")
        
        # Show comprehensive breakdown
        asset_types = await db.investment_recommendations.distinct("asset_type")
        sectors = await db.investment_recommendations.distinct("sector")
        
        print(f"\nAsset types: {', '.join(asset_types)}")
        print(f"Sectors covered: {', '.join(filter(None, sectors))}")
        
        for asset_type in asset_types:
            count = await db.investment_recommendations.count_documents({"asset_type": asset_type})
            print(f"- {asset_type}: {count} recommendations")
            
        # Show commodities breakdown
        commodities = await db.investment_recommendations.find({"asset_type": "commodity"}).to_list(1000)
        commodity_sectors = {}
        for commodity in commodities:
            sector = commodity.get("sector", "Unknown")
            commodity_sectors[sector] = commodity_sectors.get(sector, 0) + 1
            
        print(f"\nCommodities breakdown by sector:")
        for sector, count in sorted(commodity_sectors.items()):
            print(f"- {sector}: {count} commodities")
            
        # Show indices breakdown
        indices = await db.investment_recommendations.find({"asset_type": "index"}).to_list(1000)
        index_sectors = {}
        for index in indices:
            sector = index.get("sector", "Unknown")
            index_sectors[sector] = index_sectors.get(sector, 0) + 1
            
        print(f"\nIndices breakdown by sector:")
        for sector, count in sorted(index_sectors.items()):
            print(f"- {sector}: {count} indices")
            
        # List all symbols by type
        commodity_symbols = sorted([c["symbol"] for c in commodities])
        index_symbols = sorted([i["symbol"] for i in indices])
        
        print(f"\nAll commodity symbols ({len(commodity_symbols)}):")
        print(", ".join(commodity_symbols))
        
        print(f"\nAll index symbols ({len(index_symbols)}):")
        print(", ".join(index_symbols))
        
        # Recommendation distribution
        buy_count = await db.investment_recommendations.count_documents({"recommendation": "BUY"})
        hold_count = await db.investment_recommendations.count_documents({"recommendation": "HOLD"})
        sell_count = await db.investment_recommendations.count_documents({"recommendation": "SELL"})
        print(f"\nOverall recommendations: {buy_count} BUY, {hold_count} HOLD, {sell_count} SELL")
        
    except Exception as e:
        print(f"Error adding commodities and indices: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(add_comprehensive_commodities_and_indices())