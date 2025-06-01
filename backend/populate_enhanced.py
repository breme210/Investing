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

# Enhanced comprehensive investment recommendations
enhanced_recommendations = [
    # TECHNOLOGY STOCKS - 8 total
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
        "analysis": "Apple continues to demonstrate strong fundamentals with robust iPhone sales and expanding services revenue. The company's focus on AI integration across its ecosystem and potential Vision Pro adoption creates multiple growth catalysts. Technical indicators show bullish momentum with RSI at 65 and moving averages trending upward. P/E ratio of 28.5x remains reasonable for a growth stock of this quality.",
        "key_factors": [
            "Strong Q4 earnings beat expectations by 12%",
            "AI integration driving product innovation cycle",
            "Services revenue growing 16% YoY to $22B quarterly",
            "Vision Pro showing early enterprise adoption",
            "Technical breakout above $190 resistance level",
            "P/E ratio attractive at 28.5x vs sector average 32x"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 3.45,
        "price_change_percent": 1.79,
        "market_cap": "$3.01T",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 65.2,
            "moving_avg_50": 188.45,
            "moving_avg_200": 175.20,
            "pe_ratio": 28.5,
            "volatility": 0.24
        }
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
        "analysis": "NVIDIA's dominance in AI chip market continues with datacenter revenue surging 206% YoY. The company benefits from insatiable demand for H100 chips and upcoming H200 architecture. Gaming segment recovering with RTX 4090 demand strong. Technical analysis shows strong uptrend with volume confirmation.",
        "key_factors": [
            "Datacenter revenue up 206% YoY to $18.4B",
            "H100 chips completely sold out through 2024",
            "Gaming recovery with RTX 4090 driving margins",
            "Automotive AI partnerships expanding rapidly",
            "Technical momentum with RSI at 58 (healthy)",
            "Forward P/E of 45x vs 35% revenue growth"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=1),
        "price_change_24h": 12.45,
        "price_change_percent": 1.44,
        "market_cap": "$2.15T",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 58.7,
            "moving_avg_50": 820.15,
            "moving_avg_200": 645.30,
            "pe_ratio": 45.2,
            "volatility": 0.42
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "META",
        "name": "Meta Platforms Inc.",
        "asset_type": "stock",
        "current_price": 485.20,
        "target_price": 520.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 78,
        "timeframe": "6M",
        "analyst": "Michael Torres, CFA",
        "analysis": "Meta's Reality Labs investment is paying off with improved VR adoption and AI integration across Facebook and Instagram driving ad revenue growth. The company has significantly improved efficiency with layoffs reducing operating expenses by 20%. Reels competing effectively with TikTok.",
        "key_factors": [
            "Ad revenue growth accelerating to 25% YoY",
            "Reality Labs losses declining quarter-over-quarter",
            "Instagram Reels gaining market share vs TikTok",
            "AI-powered ad targeting improving ROI",
            "Operating margin expansion to 40%",
            "Technical breakout with volume above $470"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 8.70,
        "price_change_percent": 1.83,
        "market_cap": "$1.23T",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 62.1,
            "moving_avg_50": 465.80,
            "moving_avg_200": 425.60,
            "pe_ratio": 22.4,
            "volatility": 0.35
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "GOOGL",
        "name": "Alphabet Inc. Class A",
        "asset_type": "stock",
        "current_price": 155.75,
        "target_price": 170.00,
        "recommendation": "HOLD",
        "risk_level": "LOW",
        "confidence_score": 72,
        "timeframe": "6M",
        "analyst": "David Kim",
        "analysis": "Google's search dominance remains intact despite AI competition, with cloud segment showing strong 35% growth. YouTube advertising rebounding strongly. However, regulatory pressure increasing and AI integration costs rising. Technical indicators mixed with support at $150.",
        "key_factors": [
            "Search revenue stable at $48B quarterly",
            "Google Cloud growth accelerating to 35% YoY",
            "YouTube ad revenue recovering to $8.1B",
            "Bard AI integration showing early promise",
            "Regulatory scrutiny increasing in US and EU",
            "Technical support holding at $150 level"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": -1.25,
        "price_change_percent": -0.80,
        "market_cap": "$1.96T",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 48.3,
            "moving_avg_50": 152.30,
            "moving_avg_200": 148.75,
            "pe_ratio": 26.1,
            "volatility": 0.28
        }
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
            "Azure cloud growth momentum at 29% YoY",
            "AI integration in productivity suite",
            "Strong enterprise relationships",
            "Steady dividend increases for 19 years",
            "Fair current valuation at 28x P/E"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 1.23,
        "price_change_percent": 0.29,
        "market_cap": "$3.12T",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 52.4,
            "moving_avg_50": 415.80,
            "moving_avg_200": 385.60,
            "pe_ratio": 28.3,
            "volatility": 0.26
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "AMZN",
        "name": "Amazon.com Inc.",
        "asset_type": "stock",
        "current_price": 155.90,
        "target_price": 175.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 81,
        "timeframe": "9M",
        "analyst": "James Miller",
        "analysis": "Amazon's AWS segment driving profitability with 32% operating margins while retail operations improving efficiency. AI integration across services accelerating growth. Prime membership reaching saturation in US but international expansion continuing.",
        "key_factors": [
            "AWS operating margins expanding to 32%",
            "Retail operating income turning positive",
            "Prime membership loyalty remaining strong",
            "Advertising revenue growing 26% YoY",
            "AI services gaining enterprise adoption",
            "Free cash flow generation improving"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 2.80,
        "price_change_percent": 1.83,
        "market_cap": "$1.63T",
        "sector": "Consumer Discretionary",
        "technical_indicators": {
            "rsi": 55.9,
            "moving_avg_50": 152.70,
            "moving_avg_200": 145.20,
            "pe_ratio": 48.3,
            "volatility": 0.38
        }
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
        "analyst": "Elena Rodriguez",
        "analysis": "Tesla maintains EV market leadership despite increased competition. Cybertruck production ramping with 2M+ reservations. Energy storage business growing 40% annually. FSD technology advancing with neural net improvements. High volatility requires careful position sizing.",
        "key_factors": [
            "Cybertruck deliveries beginning Q4 2024",
            "Energy storage deployments up 40% YoY",
            "FSD beta expanding to 160,000 drivers",
            "Supercharger network opening to competitors",
            "China factory producing 1.2M vehicles annually",
            "Forward P/E of 65x vs 25% delivery growth"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": -5.67,
        "price_change_percent": -2.23,
        "market_cap": "$792.3B",
        "sector": "Automotive",
        "technical_indicators": {
            "rsi": 45.2,
            "moving_avg_50": 245.80,
            "moving_avg_200": 255.40,
            "pe_ratio": 65.3,
            "volatility": 0.55
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "CRM",
        "name": "Salesforce Inc.",
        "asset_type": "stock",
        "current_price": 245.67,
        "target_price": 275.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 76,
        "timeframe": "6M",
        "analyst": "Amy Johnson, CFA",
        "analysis": "Salesforce benefits from digital transformation acceleration and AI integration with Einstein platform. Subscription revenue model provides stability with 90%+ renewal rates. Recent acquisitions strengthening data analytics capabilities. Technical momentum building after consolidation.",
        "key_factors": [
            "Subscription revenue growing 11% YoY",
            "Einstein AI platform gaining traction",
            "Customer retention rate above 90%",
            "MuleSoft integration driving value",
            "Operating margin expansion to 20%",
            "Technical breakout pattern forming"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": 3.15,
        "price_change_percent": 1.30,
        "market_cap": "$238.9B",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 59.8,
            "moving_avg_50": 240.20,
            "moving_avg_200": 225.15,
            "pe_ratio": 58.2,
            "volatility": 0.34
        }
    },

    # FINANCIAL SERVICES - 3 total
    {
        "id": str(uuid.uuid4()),
        "symbol": "JPM",
        "name": "JPMorgan Chase & Co.",
        "asset_type": "stock",
        "current_price": 165.45,
        "target_price": 180.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 84,
        "timeframe": "6M",
        "analyst": "Robert Chen, CFA",
        "analysis": "JPMorgan benefits from rising interest rates with net interest income expanding 22% YoY. Credit quality remains strong with charge-offs below historical averages. Investment banking recovering slowly but trading revenues robust. Fortress balance sheet provides flexibility.",
        "key_factors": [
            "Net interest income up 22% YoY to $22.9B",
            "Credit card spending growth at 12% annually",
            "Investment banking fees stabilizing",
            "Trading revenue exceeding expectations",
            "CET1 ratio strong at 15.4%",
            "Dividend yield attractive at 2.8%"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": 2.15,
        "price_change_percent": 1.32,
        "market_cap": "$478.5B",
        "sector": "Financial Services",
        "technical_indicators": {
            "rsi": 67.4,
            "moving_avg_50": 158.20,
            "moving_avg_200": 148.85,
            "pe_ratio": 12.8,
            "volatility": 0.31
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "BAC",
        "name": "Bank of America Corp.",
        "asset_type": "stock",
        "current_price": 34.82,
        "target_price": 38.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 79,
        "timeframe": "6M",
        "analyst": "Jennifer Wu, CFA",
        "analysis": "Bank of America leveraged to rising interest rates with significant deposit base sensitivity. Credit quality metrics improving with charge-off rates declining. Consumer banking franchise strong with digital adoption accelerating. Valuation attractive at 0.9x book value.",
        "key_factors": [
            "Asset sensitivity benefiting from rate rises",
            "Credit losses normalizing below cycle averages",
            "Digital banking adoption at 85%",
            "Consumer deposit growth stabilizing",
            "Valuation discount at 0.9x book value",
            "Efficiency ratio improving to 65%"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=6),
        "price_change_24h": 0.95,
        "price_change_percent": 2.81,
        "market_cap": "$273.1B",
        "sector": "Financial Services",
        "technical_indicators": {
            "rsi": 62.7,
            "moving_avg_50": 33.45,
            "moving_avg_200": 31.80,
            "pe_ratio": 11.2,
            "volatility": 0.35
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "V",
        "name": "Visa Inc. Class A",
        "asset_type": "stock",
        "current_price": 268.90,
        "target_price": 295.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 88,
        "timeframe": "9M",
        "analyst": "Patricia Lee",
        "analysis": "Visa benefits from secular shift to digital payments with network effects creating sustainable moat. Cross-border volume recovering to pre-pandemic levels. New payment technologies like contactless and digital wallets driving growth. Strong margins and capital-light model.",
        "key_factors": [
            "Payment volume growing 10% YoY globally",
            "Cross-border recovery exceeding expectations",
            "Digital wallet adoption accelerating",
            "Operating margins stable at 67%",
            "Buyback program returning 100% of earnings",
            "Network effects strengthening competitive position"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": 4.20,
        "price_change_percent": 1.59,
        "market_cap": "$558.7B",
        "sector": "Financial Services",
        "technical_indicators": {
            "rsi": 64.1,
            "moving_avg_50": 262.35,
            "moving_avg_200": 245.90,
            "pe_ratio": 32.4,
            "volatility": 0.22
        }
    },

    # HEALTHCARE - 2 total
    {
        "id": str(uuid.uuid4()),
        "symbol": "UNH",
        "name": "UnitedHealth Group Inc.",
        "asset_type": "stock",
        "current_price": 525.80,
        "target_price": 565.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 89,
        "timeframe": "6M",
        "analyst": "Dr. Lisa Wong, CFA",
        "analysis": "UnitedHealth demonstrates consistent execution across insurance and Optum segments. Medical cost ratios improving with better utilization management. Optum revenue growing 24% annually with margin expansion. Strong demographic tailwinds from aging population.",
        "key_factors": [
            "Medical cost ratio improving to 82.1%",
            "Optum segment revenue growth at 24% YoY",
            "Medicare Advantage membership expanding 8%",
            "Value-based care contracts growing rapidly",
            "Demographic tailwinds from baby boomer aging",
            "Dividend growth streak of 14 consecutive years"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=6),
        "price_change_24h": 4.25,
        "price_change_percent": 0.81,
        "market_cap": "$489.2B",
        "sector": "Healthcare",
        "technical_indicators": {
            "rsi": 61.8,
            "moving_avg_50": 515.40,
            "moving_avg_200": 485.90,
            "pe_ratio": 24.7,
            "volatility": 0.19
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "JNJ",
        "name": "Johnson & Johnson",
        "asset_type": "stock",
        "current_price": 155.42,
        "target_price": 170.00,
        "recommendation": "HOLD",
        "risk_level": "LOW",
        "confidence_score": 74,
        "timeframe": "6M",
        "analyst": "Dr. Mark Thompson",
        "analysis": "Johnson & Johnson's pharmaceutical segment driving growth with innovative oncology and immunology drugs. Consumer products facing competitive pressure but medical devices recovering post-pandemic. Talc litigation overhang remains but settlement progress positive.",
        "key_factors": [
            "Pharmaceutical revenue growing 5% YoY",
            "Oncology franchise expanding rapidly",
            "Medical device recovery accelerating",
            "R&D pipeline showing promise",
            "Dividend aristocrat with 61-year streak",
            "Litigation risks declining with settlements"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=7),
        "price_change_24h": -0.85,
        "price_change_percent": -0.54,
        "market_cap": "$378.2B",
        "sector": "Healthcare",
        "technical_indicators": {
            "rsi": 47.2,
            "moving_avg_50": 157.80,
            "moving_avg_200": 162.45,
            "pe_ratio": 15.8,
            "volatility": 0.16
        }
    },

    # INDICES - 3 total
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
        "analysis": "S&P 500 shows resilience with strong corporate earnings and economic fundamentals. Technology sector leadership and defensive sector stability provide balanced exposure. Fed policy normalization creating favorable environment. Earnings growth of 8% expected for 2024.",
        "key_factors": [
            "Corporate earnings growth accelerating to 8%",
            "Technology sector outperformance continuing",
            "Economic resilience with low unemployment",
            "Fed policy pivot supporting multiples",
            "Technical momentum with RSI at healthy 58",
            "Election year historical patterns positive"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 2.34,
        "price_change_percent": 0.46,
        "market_cap": "$460.8B",
        "sector": "Diversified",
        "technical_indicators": {
            "rsi": 58.2,
            "moving_avg_50": 510.45,
            "moving_avg_200": 485.90,
            "pe_ratio": 21.8,
            "volatility": 0.16
        }
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
        "analysis": "NASDAQ-100 faces headwinds from high technology valuations despite strong AI theme momentum. Rising interest rates creating pressure on growth multiples. Mega-cap concentration risk with top 10 holdings representing 60% of index.",
        "key_factors": [
            "Technology sector valuations stretched at 28x P/E",
            "AI innovation theme providing growth catalyst",
            "Interest rate sensitivity creating volatility",
            "Mega-cap concentration creating single-stock risk",
            "Cloud computing adoption accelerating",
            "Technical resistance at $450 level holding"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=5),
        "price_change_24h": -1.89,
        "price_change_percent": -0.42,
        "market_cap": "$205.3B",
        "sector": "Technology",
        "technical_indicators": {
            "rsi": 52.7,
            "moving_avg_50": 442.15,
            "moving_avg_200": 425.80,
            "pe_ratio": 28.4,
            "volatility": 0.22
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "IWM",
        "name": "iShares Russell 2000 ETF",
        "asset_type": "index",
        "current_price": 198.45,
        "target_price": 215.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 75,
        "timeframe": "9M",
        "analyst": "Andrea Foster",
        "analysis": "Small-cap stocks positioned for outperformance as economic growth broadens beyond mega-caps. Russell 2000 trading at attractive valuation discount to large-caps. Domestic revenue exposure benefits from reshoring trends.",
        "key_factors": [
            "Valuation discount at 18x P/E vs large-caps 22x",
            "Domestic revenue exposure reducing risks",
            "Reshoring trends benefiting small manufacturers",
            "Consumer spending supporting service companies",
            "Technical base building pattern forming",
            "Historical mean reversion cycle due"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=4),
        "price_change_24h": 1.85,
        "price_change_percent": 0.94,
        "market_cap": "$28.4B",
        "sector": "Diversified",
        "technical_indicators": {
            "rsi": 54.3,
            "moving_avg_50": 195.20,
            "moving_avg_200": 188.75,
            "pe_ratio": 18.2,
            "volatility": 0.28
        }
    },

    # COMMODITIES - 4 total
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
        "analysis": "Gold serves as effective hedge against inflation and currency debasement with central banks increasing purchases by 152% YoY. Technical breakout above $2000/oz level confirmed. Geopolitical tensions supporting safe-haven demand.",
        "key_factors": [
            "Central bank purchases up 152% YoY to 800 tons",
            "Technical breakout confirmed above $2000/oz",
            "Geopolitical risk premium increasing",
            "Dollar weakness supporting gold prices",
            "ETF inflows accelerating to 45 tons monthly",
            "Mining supply growth limited to 1% annually"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=1),
        "price_change_24h": 2.67,
        "price_change_percent": 1.46,
        "market_cap": "$68.2B",
        "sector": "Precious Metals",
        "technical_indicators": {
            "rsi": 68.4,
            "moving_avg_50": 182.30,
            "moving_avg_200": 175.80,
            "pe_ratio": None,
            "volatility": 0.18
        }
    },
    {
        "id": str(uuid.uuid4()),
        "symbol": "SLV",
        "name": "iShares Silver Trust",
        "asset_type": "commodity",
        "current_price": 22.85,
        "target_price": 26.50,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 71,
        "timeframe": "9M",
        "analyst": "Rachel Kim",
        "analysis": "Silver positioned for industrial demand surge from solar panel and EV battery production. Gold-to-silver ratio at 85:1 suggests undervaluation vs historical 60:1 average. Supply deficit projected for third consecutive year.",
        "key_factors": [
            "Industrial demand growing 15% from green tech",
            "Gold-to-silver ratio extended at 85:1",
            "Supply deficit projected at 200M oz annually",
            "Solar panel production driving 40% of demand",
            "EV battery applications expanding rapidly",
            "Technical base formation completing"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=2),
        "price_change_24h": 0.45,
        "price_change_percent": 2.01,
        "market_cap": "$13.8B",
        "sector": "Precious Metals",
        "technical_indicators": {
            "rsi": 58.9,
            "moving_avg_50": 22.15,
            "moving_avg_200": 21.20,
            "pe_ratio": None,
            "volatility": 0.32
        }
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
        "analysis": "Oil prices face pressure from increased US shale production and global economic slowdown concerns. SPR releases continuing despite OPEC+ production cuts. Technical indicators showing bearish momentum with inventory builds exceeding norms.",
        "key_factors": [
            "US shale production increasing 8% YoY",
            "Global economic growth concerns mounting",
            "OPEC+ cuts offset by non-OPEC supply",
            "Strategic reserve releases continuing",
            "Technical breakdown below $80 support",
            "Inventory builds above 5-year averages"
        ],
        "last_updated": datetime.utcnow() - timedelta(hours=3),
        "price_change_24h": -2.45,
        "price_change_percent": -3.01,
        "market_cap": "$4.1B",
        "sector": "Energy",
        "technical_indicators": {
            "rsi": 38.2,
            "moving_avg_50": 82.15,
            "moving_avg_200": 85.40,
            "pe_ratio": None,
            "volatility": 0.42
        }
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
        "analysis": "Bitcoin showing institutional adoption momentum with spot ETF approvals driving $12B inflows. Corporate treasury allocation trend accelerating. Halving event reducing supply inflation to 0.85% annually. Regulatory clarity improving globally.",
        "key_factors": [
            "Bitcoin ETF inflows reaching $12B since approval",
            "Corporate treasury adoption accelerating",
            "Halving event completed reducing supply growth",
            "Regulatory clarity improving in major markets",
            "Technical consolidation near $68K resistance",
            "Lightning Network adoption growing 300% YoY"
        ],
        "last_updated": datetime.utcnow() - timedelta(minutes=30),
        "price_change_24h": 1234.56,
        "price_change_percent": 1.85,
        "market_cap": "$1.33T",
        "sector": "Cryptocurrency",
        "technical_indicators": {
            "rsi": 61.7,
            "moving_avg_50": 65420.80,
            "moving_avg_200": 58950.25,
            "pe_ratio": None,
            "volatility": 0.68
        }
    }
]

async def populate_enhanced_recommendations():
    """Populate database with comprehensive enhanced recommendations"""
    try:
        # Clear existing recommendations
        await db.investment_recommendations.delete_many({})
        print("Cleared existing investment recommendations")
        
        # Insert enhanced recommendations
        result = await db.investment_recommendations.insert_many(enhanced_recommendations)
        print(f"Inserted {len(result.inserted_ids)} enhanced investment recommendations")
        
        # Verify insertion
        count = await db.investment_recommendations.count_documents({})
        print(f"Total recommendations in database: {count}")
        
        # Show comprehensive breakdown
        asset_types = await db.investment_recommendations.distinct("asset_type")
        sectors = await db.investment_recommendations.distinct("sector")
        
        print(f"\nAsset types: {', '.join(asset_types)}")
        print(f"Sectors covered: {', '.join(filter(None, sectors))}")
        
        for asset_type in asset_types:
            count = await db.investment_recommendations.count_documents({"asset_type": asset_type})
            print(f"- {asset_type}: {count} recommendations")
            
        # Recommendation distribution
        buy_count = await db.investment_recommendations.count_documents({"recommendation": "BUY"})
        hold_count = await db.investment_recommendations.count_documents({"recommendation": "HOLD"})
        sell_count = await db.investment_recommendations.count_documents({"recommendation": "SELL"})
        print(f"\nRecommendations: {buy_count} BUY, {hold_count} HOLD, {sell_count} SELL")
        
        # Sample technical indicators
        sample = await db.investment_recommendations.find_one({"symbol": "AAPL"})
        if sample and "technical_indicators" in sample:
            print(f"\nSample technical indicators (AAPL):")
            for key, value in sample["technical_indicators"].items():
                print(f"  {key}: {value}")
        
    except Exception as e:
        print(f"Error populating database: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(populate_enhanced_recommendations())