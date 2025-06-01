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

# Additional popular stocks to create comprehensive coverage
additional_popular_stocks = [
    # More Technology Giants
    {
        "id": str(uuid.uuid4()),
        "symbol": "ORCL",
        "name": "Oracle Corporation",
        "asset_type": "stock",
        "current_price": 112.45,
        "target_price": 125.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 76,
        "timeframe": "9M",
        "analyst": "Database Specialist",
        "analysis": "Oracle benefits from cloud database migration trends and AI integration in enterprise software. Strong recurring revenue base provides stability while cloud growth accelerates.",
        "key_factors": [
            "Cloud applications revenue growing 25% YoY",
            "Database market leadership maintained",
            "AI and machine learning integration expanding",
            "Autonomous database gaining enterprise adoption",
            "Strong cash flow supporting dividend growth",
            "Strategic partnerships with hyperscalers"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": 1.85,
        "price_change_percent": 1.67,
        "market_cap": "$318.5B",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 58.2,
            "moving_avg_50": 110.30,
            "moving_avg_200": 105.80,
            "pe_ratio": 24.6,
            "volatility": 0.28
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "ADBE",
        "name": "Adobe Inc.",
        "asset_type": "stock",
        "current_price": 485.20,
        "target_price": 530.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 81,
        "timeframe": "6M",
        "analyst": "Software Analyst",
        "analysis": "Adobe's creative software suite remains essential for professionals while Document Cloud and Experience Cloud drive enterprise growth. AI integration with Firefly positioning company well for future.",
        "key_factors": [
            "Creative Cloud subscriber growth accelerating",
            "Document Cloud revenue up 18% YoY",
            "Firefly AI integration driving user engagement",
            "Enterprise segment showing strong momentum",
            "Subscription model providing revenue predictability",
            "Digital transformation trends supporting demand"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 7.35,
        "price_change_percent": 1.54,
        "market_cap": "$219.8B",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 64.7,
            "moving_avg_50": 478.90,
            "moving_avg_200": 455.20,
            "pe_ratio": 42.1,
            "volatility": 0.32
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "IBM",
        "name": "International Business Machines Corp.",
        "asset_type": "stock",
        "current_price": 182.65,
        "target_price": 200.00,
        "recommendation": "HOLD",
        "risk_level": "MEDIUM",
        "confidence_score": 68,
        "timeframe": "9M",
        "analyst": "Enterprise Tech Analyst",
        "analysis": "IBM's transformation to hybrid cloud and AI continues with Red Hat integration driving growth. Consulting business stable while legacy mainframe provides cash flow. Valuation reasonable but growth limited.",
        "key_factors": [
            "Red Hat contributing to cloud revenue growth",
            "Consulting revenue showing stability",
            "AI and Watson platform investments ongoing",
            "Mainframe business providing steady cash flow",
            "Dividend yield attractive at 3.8%",
            "Balance sheet strength supporting transformation"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": -0.95,
        "price_change_percent": -0.52,
        "market_cap": "$168.7B",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 48.9,
            "moving_avg_50": 184.20,
            "moving_avg_200": 179.50,
            "pe_ratio": 21.8,
            "volatility": 0.25
        }
    },
    
    # More Consumer Brands
    {
        "id": str(uuid.uuid4()),
        "symbol": "NKE",
        "name": "Nike Inc. Class B",
        "asset_type": "stock",
        "current_price": 105.80,
        "target_price": 120.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 77,
        "timeframe": "9M",
        "analyst": "Consumer Brand Analyst",
        "analysis": "Nike's brand strength and innovation pipeline support long-term growth despite near-term headwinds in China. Direct-to-consumer strategy and digital transformation driving margin expansion.",
        "key_factors": [
            "Direct-to-consumer sales growing 15% annually",
            "Innovation pipeline with new technologies",
            "Digital platform investments showing returns",
            "Brand strength in key demographics maintained",
            "Supply chain optimization reducing costs",
            "International expansion opportunities"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": 2.15,
        "price_change_percent": 2.07,
        "market_cap": "$165.4B",
        "sector": "Consumer Discretionary",
        "technical_indicators": {
            "rsi": 55.6,
            "moving_avg_50": 103.40,
            "moving_avg_200": 98.75,
            "pe_ratio": 28.9,
            "volatility": 0.31
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "SBUX",
        "name": "Starbucks Corporation",
        "asset_type": "stock",
        "current_price": 95.40,
        "target_price": 105.00,
        "recommendation": "HOLD",
        "risk_level": "MEDIUM",
        "confidence_score": 72,
        "timeframe": "6M",
        "analyst": "Restaurant Analyst",
        "analysis": "Starbucks faces near-term challenges in key markets but long-term growth prospects remain intact. New CEO bringing operational focus while international expansion continues.",
        "key_factors": [
            "US same-store sales showing pressure",
            "China market presenting near-term challenges",
            "New leadership focusing on operational efficiency",
            "Loyalty program driving customer retention",
            "Store expansion in international markets",
            "Premium positioning maintained despite competition"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=6),
        "price_change_24h": -1.20,
        "price_change_percent": -1.24,
        "market_cap": "$108.9B",
        "sector": "Consumer Discretionary",
        "technical_indicators": {
            "rsi": 43.2,
            "moving_avg_50": 97.85,
            "moving_avg_200": 101.20,
            "pe_ratio": 25.7,
            "volatility": 0.28
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "DIS",
        "name": "The Walt Disney Company",
        "asset_type": "stock",
        "current_price": 112.30,
        "target_price": 125.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 74,
        "timeframe": "9M",
        "analyst": "Media Analyst",
        "analysis": "Disney's streaming strategy showing progress with Disney+ subscriber growth while parks business remains strong. Content pipeline and franchise strength provide competitive advantages.",
        "key_factors": [
            "Disney+ reaching profitability targets",
            "Parks and experiences revenue recovering strongly",
            "Content franchise strength unmatched",
            "Streaming bundle strategy gaining traction",
            "Cost reduction initiatives showing results",
            "International expansion opportunities"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": 1.85,
        "price_change_percent": 1.68,
        "market_cap": "$205.3B",
        "sector": "Communication Services",
        "technical_indicators": {
            "rsi": 57.4,
            "moving_avg_50": 110.60,
            "moving_avg_200": 105.90,
            "pe_ratio": 35.8,
            "volatility": 0.33
        }
    },
    
    # Industrial Stocks
    {
        "id": str(uuid.uuid4()),
        "symbol": "BA",
        "name": "The Boeing Company",
        "asset_type": "stock",
        "current_price": 205.40,
        "target_price": 230.00,
        "recommendation": "HOLD",
        "risk_level": "HIGH",
        "confidence_score": 65,
        "timeframe": "12M",
        "analyst": "Aerospace Analyst",
        "analysis": "Boeing continues recovery from 737 MAX issues with production ramping up. Defense business provides stability while commercial aviation recovery supports long-term outlook. Execution risks remain.",
        "key_factors": [
            "737 MAX production increases continuing",
            "Commercial aviation demand recovering",
            "Defense portfolio providing stable cash flow",
            "Supply chain challenges being addressed",
            "Regulatory oversight increasing costs",
            "Cash flow generation improving gradually"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=7),
        "price_change_24h": -2.85,
        "price_change_percent": -1.37,
        "market_cap": "$122.8B",
        "sector": "Industrials",
        "technical_indicators": {
            "rsi": 46.1,
            "moving_avg_50": 208.70,
            "moving_avg_200": 215.30,
            "pe_ratio": -12.5,  # Negative due to losses
            "volatility": 0.42
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "CAT",
        "name": "Caterpillar Inc.",
        "asset_type": "stock",
        "current_price": 285.90,
        "target_price": 310.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 79,
        "timeframe": "6M",
        "analyst": "Industrial Analyst",
        "analysis": "Caterpillar benefits from infrastructure spending and mining activity while services business provides recurring revenue. Strong pricing power and operational efficiency driving margins.",
        "key_factors": [
            "Infrastructure spending supporting equipment demand",
            "Mining segment showing strong activity",
            "Services revenue providing recurring income",
            "Pricing power in key product categories",
            "Operational efficiency improvements ongoing",
            "Energy transition creating new opportunities"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": 3.45,
        "price_change_percent": 1.22,
        "market_cap": "$148.5B",
        "sector": "Industrials",
        "technical_indicators": {
            "rsi": 61.8,
            "moving_avg_50": 282.40,
            "moving_avg_200": 275.60,
            "pe_ratio": 14.2,
            "volatility": 0.27
        }
    },
    
    # More Healthcare
    {
        "id": str(uuid.uuid4()),
        "symbol": "ABBV",
        "name": "AbbVie Inc.",
        "asset_type": "stock",
        "current_price": 165.30,
        "target_price": 180.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 78,
        "timeframe": "9M",
        "analyst": "Pharma Analyst",
        "analysis": "AbbVie successfully diversifying beyond Humira with strong pipeline in oncology and immunology. Dividend yield attractive while growth prospects improve with new drug approvals.",
        "key_factors": [
            "Post-Humira portfolio showing strong growth",
            "Oncology pipeline with multiple promising candidates",
            "Immunology franchise expanding beyond Humira",
            "Dividend yield attractive at 3.8%",
            "Strong cash flow supporting R&D investments",
            "Recent acquisitions strengthening pipeline"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=6),
        "price_change_24h": 2.40,
        "price_change_percent": 1.47,
        "market_cap": "$291.8B",
        "sector": "Healthcare",
        "technical_indicators": {
            "rsi": 59.7,
            "moving_avg_50": 162.80,
            "moving_avg_200": 155.40,
            "pe_ratio": 15.4,
            "volatility": 0.22
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "TMO",
        "name": "Thermo Fisher Scientific Inc.",
        "asset_type": "stock",
        "current_price": 548.70,
        "target_price": 590.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 82,
        "timeframe": "6M",
        "analyst": "Life Sciences Analyst",
        "analysis": "Thermo Fisher benefits from life sciences research growth and biopharma development trends. Strong market position in analytical instruments and reagents provides competitive moat.",
        "key_factors": [
            "Life sciences research spending increasing",
            "Biopharma services segment growing strongly",
            "COVID testing revenue stabilizing at higher base",
            "Analytical instruments market leadership",
            "Acquisition strategy adding capabilities",
            "Emerging markets expansion continuing"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": 8.20,
        "price_change_percent": 1.52,
        "market_cap": "$214.6B",
        "sector": "Healthcare",
        "technical_indicators": {
            "rsi": 62.3,
            "moving_avg_50": 542.90,
            "moving_avg_200": 520.80,
            "pe_ratio": 28.7,
            "volatility": 0.24
        }
    },
    
    # More Financial Services
    {
        "id": str(uuid.uuid4()),
        "symbol": "AXP",
        "name": "American Express Company",
        "asset_type": "stock",
        "current_price": 185.40,
        "target_price": 205.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 80,
        "timeframe": "6M",
        "analyst": "Financial Services Analyst",
        "analysis": "American Express benefits from strong consumer spending by affluent customers and travel recovery. Fee-based revenue model provides stability while credit quality remains strong.",
        "key_factors": [
            "Consumer spending by affluent customers strong",
            "Travel and entertainment recovery continuing",
            "Fee-based revenue providing stability",
            "Credit quality metrics remaining favorable",
            "Millennial and Gen Z acquisition increasing",
            "Digital platform investments showing returns"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": 3.85,
        "price_change_percent": 2.12,
        "market_cap": "$138.7B",
        "sector": "Financial Services",
        "technical_indicators": {
            "rsi": 65.8,
            "moving_avg_50": 181.20,
            "moving_avg_200": 172.90,
            "pe_ratio": 16.8,
            "volatility": 0.29
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "MA",
        "name": "Mastercard Incorporated Class A",
        "asset_type": "stock",
        "current_price": 425.60,
        "target_price": 460.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 86,
        "timeframe": "6M",
        "analyst": "Payments Analyst",
        "analysis": "Mastercard benefits from global shift to electronic payments with network effects creating competitive moat. Cross-border transaction recovery and new payment technologies driving growth.",
        "key_factors": [
            "Electronic payment adoption accelerating globally",
            "Cross-border transactions recovering strongly",
            "Network effects strengthening competitive position",
            "New payment technologies gaining adoption",
            "Emerging markets providing growth opportunities",
            "Strong cash flow supporting shareholder returns"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 6.40,
        "price_change_percent": 1.53,
        "market_cap": "$408.9B",
        "sector": "Financial Services",
        "technical_indicators": {
            "rsi": 66.2,
            "moving_avg_50": 419.30,
            "moving_avg_200": 395.70,
            "pe_ratio": 33.1,
            "volatility": 0.23
        }
    },
    
    # Energy & Materials
    {
        "id": str(uuid.uuid4()),
        "symbol": "CVX",
        "name": "Chevron Corporation",
        "asset_type": "stock",
        "current_price": 152.30,
        "target_price": 165.00,
        "recommendation": "HOLD",
        "risk_level": "MEDIUM",
        "confidence_score": 71,
        "timeframe": "6M",
        "analyst": "Energy Analyst",
        "analysis": "Chevron maintains disciplined capital allocation while benefiting from Permian Basin production growth. Strong balance sheet and dividend policy attractive to income investors.",
        "key_factors": [
            "Permian Basin production growing efficiently",
            "Capital discipline maintaining strong returns",
            "Dividend sustainability well-covered by cash flow",
            "Downstream operations providing integration benefits",
            "Balance sheet strength among sector leaders",
            "Energy transition investments selective and strategic"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=6),
        "price_change_24h": -1.45,
        "price_change_percent": -0.94,
        "market_cap": "$292.1B",
        "sector": "Energy",
        "technical_indicators": {
            "rsi": 51.7,
            "moving_avg_50": 154.80,
            "moving_avg_200": 158.20,
            "pe_ratio": 13.9,
            "volatility": 0.26
        }
    },
    
    # Communication Services
    {
        "id": str(uuid.uuid4()),
        "symbol": "T",
        "name": "AT&T Inc.",
        "asset_type": "stock",
        "current_price": 20.45,
        "target_price": 22.00,
        "recommendation": "HOLD",
        "risk_level": "MEDIUM",
        "confidence_score": 66,
        "timeframe": "9M",
        "analyst": "Telecom Analyst",
        "analysis": "AT&T focuses on wireless and broadband after media spin-offs. Dividend cut allows for debt reduction and network investments. Recovery story depends on execution of simplified strategy.",
        "key_factors": [
            "Wireless subscriber trends stabilizing",
            "5G network investments showing progress",
            "Debt reduction efforts ongoing after dividend cut",
            "Broadband fiber expansion accelerating",
            "Simplified business model post-media spin-offs",
            "Competitive pressures in wireless market"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=7),
        "price_change_24h": 0.15,
        "price_change_percent": 0.74,
        "market_cap": "$146.8B",
        "sector": "Communication Services",
        "technical_indicators": {
            "rsi": 49.3,
            "moving_avg_50": 20.25,
            "moving_avg_200": 19.85,
            "pe_ratio": 18.2,
            "volatility": 0.21
        }
    },
    
    # Utilities
    {
        "id": str(uuid.uuid4()),
        "symbol": "NEE",
        "name": "NextEra Energy Inc.",
        "asset_type": "stock",
        "current_price": 68.90,
        "target_price": 75.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 77,
        "timeframe": "9M",
        "analyst": "Utilities Analyst",
        "analysis": "NextEra Energy leads in renewable energy development while maintaining stable utility operations. Clean energy transition provides long-term growth catalyst with predictable cash flows.",
        "key_factors": [
            "Renewable energy development leadership",
            "Regulated utility providing stable cash flow",
            "Clean energy transition creating opportunities",
            "Dividend growth track record of 29 years",
            "ESG credentials attracting institutional investment",
            "Technology innovation in energy storage"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": 1.25,
        "price_change_percent": 1.85,
        "market_cap": "$139.2B",
        "sector": "Utilities",
        "technical_indicators": {
            "rsi": 58.4,
            "moving_avg_50": 67.80,
            "moving_avg_200": 65.40,
            "pe_ratio": 22.6,
            "volatility": 0.19
        }
    }
]

async def add_popular_stocks():
    """Add more popular stocks to create comprehensive coverage"""
    try:
        # Get current count
        current_count = await db.investment_recommendations.count_documents({})
        print(f"Current recommendations in database: {current_count}")
        
        # Insert additional popular stocks
        result = await db.investment_recommendations.insert_many(additional_popular_stocks)
        print(f"Added {len(result.inserted_ids)} additional popular stocks")
        
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
            
        # Show sector breakdown for stocks
        stock_sectors = {}
        stocks = await db.investment_recommendations.find({"asset_type": "stock"}).to_list(1000)
        for stock in stocks:
            sector = stock.get("sector", "Unknown")
            stock_sectors[sector] = stock_sectors.get(sector, 0) + 1
            
        print(f"\nStock breakdown by sector:")
        for sector, count in sorted(stock_sectors.items()):
            print(f"- {sector}: {count} stocks")
            
        # Recommendation distribution
        buy_count = await db.investment_recommendations.count_documents({"recommendation": "BUY"})
        hold_count = await db.investment_recommendations.count_documents({"recommendation": "HOLD"})
        sell_count = await db.investment_recommendations.count_documents({"recommendation": "SELL"})
        print(f"\nRecommendations: {buy_count} BUY, {hold_count} HOLD, {sell_count} SELL")
        
        # Sample of all symbols now included
        all_stocks = await db.investment_recommendations.find({"asset_type": "stock"}).to_list(1000)
        symbols = sorted([stock["symbol"] for stock in all_stocks])
        print(f"\nAll stock symbols now included ({len(symbols)} total):")
        print(", ".join(symbols))
        
    except Exception as e:
        print(f"Error adding stocks: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(add_popular_stocks())