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

async def create_sample_investment_recommendations():
    """Create sample investment recommendations"""
    
    recommendations = [
        {
            "id": str(uuid.uuid4()),
            "symbol": "AAPL",
            "name": "Apple Inc.",
            "asset_type": "stock",
            "current_price": 189.45,
            "target_price": 215.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 87,
            "timeframe": "12M",
            "analyst": "Sarah Chen",
            "analysis": "Apple continues to demonstrate strong fundamentals with robust iPhone demand, growing services revenue, and expansion into new product categories. The company's ecosystem lock-in effect and strong brand loyalty provide sustainable competitive advantages.",
            "key_factors": [
                "Strong Q4 iPhone sales exceeding expectations",
                "Services revenue growth of 16% year-over-year", 
                "Successful launch of Vision Pro creating new revenue stream",
                "Share buyback program supporting stock price",
                "AI integration across product lineup driving upgrades"
            ],
            "last_updated": datetime.utcnow(),
            "price_change_24h": 2.35,
            "price_change_percent": 1.26,
            "market_cap": "$2.9T",
            "sector": "Technology",
            "technical_indicators": {
                "rsi": 58.3,
                "moving_avg_50": 185.20,
                "moving_avg_200": 175.80,
                "pe_ratio": 28.5,
                "volatility": 0.22
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "MSFT",
            "name": "Microsoft Corporation",
            "asset_type": "stock", 
            "current_price": 378.85,
            "target_price": 420.00,
            "recommendation": "BUY",
            "risk_level": "LOW",
            "confidence_score": 92,
            "timeframe": "12M",
            "analyst": "David Rodriguez",
            "analysis": "Microsoft's dominant position in cloud computing through Azure, combined with AI leadership via OpenAI partnership, positions the company for continued growth. Strong enterprise customer base and recurring revenue model provide stability.",
            "key_factors": [
                "Azure revenue growth of 29% in latest quarter",
                "AI Copilot integration driving Office 365 upgrades",
                "Gaming division showing strong performance", 
                "Enterprise cloud migration accelerating",
                "Strong balance sheet with $75B in cash"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=2),
            "price_change_24h": 4.20,
            "price_change_percent": 1.12,
            "market_cap": "$2.8T",
            "sector": "Technology",
            "technical_indicators": {
                "rsi": 62.1,
                "moving_avg_50": 370.15,
                "moving_avg_200": 340.90,
                "pe_ratio": 32.1,
                "volatility": 0.19
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "NVDA",
            "name": "NVIDIA Corporation",
            "asset_type": "stock",
            "current_price": 875.30,
            "target_price": 1050.00,
            "recommendation": "BUY",
            "risk_level": "HIGH",
            "confidence_score": 85,
            "timeframe": "18M",
            "analyst": "Emily Zhang",
            "analysis": "NVIDIA remains the clear leader in AI chip technology with dominant market share in data center GPUs. Strong demand for AI infrastructure and gaming recovery support continued growth despite high valuation.",
            "key_factors": [
                "AI chip demand exceeding supply capacity",
                "Data center revenue up 200% year-over-year",
                "Gaming segment showing signs of recovery",
                "Strategic partnerships with major cloud providers",
                "Next-gen Blackwell architecture launching 2024"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=5),
            "price_change_24h": -8.45,
            "price_change_percent": -0.95,
            "market_cap": "$2.1T",
            "sector": "Technology",
            "technical_indicators": {
                "rsi": 71.8,
                "moving_avg_50": 820.40,
                "moving_avg_200": 650.75,
                "pe_ratio": 65.2,
                "volatility": 0.45
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "TSLA",
            "name": "Tesla, Inc.",
            "asset_type": "stock",
            "current_price": 248.50,
            "target_price": 200.00,
            "recommendation": "HOLD",
            "risk_level": "HIGH",
            "confidence_score": 68,
            "timeframe": "12M",
            "analyst": "Michael Thompson",
            "analysis": "Tesla faces increasing competition in the EV market while dealing with production challenges and margin pressure. Autonomy and energy storage provide long-term upside but near-term headwinds persist.",
            "key_factors": [
                "Increased EV competition from traditional automakers",
                "Production ramp challenges at new facilities",
                "Margin pressure from price cuts",
                "Autonomous driving progress slower than expected",
                "Energy storage business showing strong growth"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=1),
            "price_change_24h": -3.75,
            "price_change_percent": -1.49,
            "market_cap": "$790B",
            "sector": "Consumer Discretionary",
            "technical_indicators": {
                "rsi": 45.2,
                "moving_avg_50": 255.30,
                "moving_avg_200": 220.15,
                "pe_ratio": 78.3,
                "volatility": 0.38
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "SPY",
            "name": "SPDR S&P 500 ETF Trust",
            "asset_type": "index",
            "current_price": 521.45,
            "target_price": 550.00,
            "recommendation": "BUY",
            "risk_level": "LOW",
            "confidence_score": 79,
            "timeframe": "12M",
            "analyst": "Robert Kim",
            "analysis": "Broad market exposure to 500 largest US companies provides diversified growth potential. Strong corporate earnings, resilient consumer spending, and Fed policy stabilization support continued upward trajectory.",
            "key_factors": [
                "S&P 500 companies showing strong earnings growth",
                "Fed rate cuts expected to boost valuations",
                "Consumer spending remaining resilient",
                "Corporate profit margins stabilizing",
                "Historical long-term performance trend intact"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=3),
            "price_change_24h": 1.85,
            "price_change_percent": 0.36,
            "market_cap": "$2.1T AUM",
            "sector": "Diversified",
            "technical_indicators": {
                "rsi": 55.7,
                "moving_avg_50": 515.20,
                "moving_avg_200": 485.40,
                "volatility": 0.14
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "BTC-USD",
            "name": "Bitcoin",
            "asset_type": "commodity",
            "current_price": 67250,
            "target_price": 85000,
            "recommendation": "BUY",
            "risk_level": "HIGH",
            "confidence_score": 72,
            "timeframe": "18M",
            "analyst": "Alex Morgan",
            "analysis": "Bitcoin continues to gain institutional adoption with ETF approvals driving mainstream acceptance. Halving event and limited supply dynamics support long-term price appreciation despite short-term volatility.",
            "key_factors": [
                "Bitcoin ETF approvals increasing institutional access",
                "Upcoming halving event reducing supply",
                "Corporate treasury adoption continuing",
                "Regulatory clarity improving in major markets",
                "Lightning Network adoption growing"
            ],
            "last_updated": datetime.utcnow() - timedelta(minutes=30),
            "price_change_24h": 1250,
            "price_change_percent": 1.89,
            "market_cap": "$1.3T",
            "sector": "Cryptocurrency",
            "technical_indicators": {
                "rsi": 64.3,
                "moving_avg_50": 62500,
                "moving_avg_200": 45000,
                "volatility": 0.65
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "AMZN",
            "name": "Amazon.com, Inc.",
            "asset_type": "stock",
            "current_price": 155.75,
            "target_price": 180.00,
            "recommendation": "BUY",
            "risk_level": "MEDIUM",
            "confidence_score": 83,
            "timeframe": "12M",
            "analyst": "Jennifer Liu",
            "analysis": "Amazon's AWS dominance in cloud computing combined with e-commerce leadership and emerging AI capabilities position the company for sustained growth. Cost optimization efforts improving profitability.",
            "key_factors": [
                "AWS maintaining 30%+ market share in cloud",
                "E-commerce margins improving through automation",
                "AI integration across business segments",
                "Advertising business growing rapidly",
                "Prime membership loyalty driving recurring revenue"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=4),
            "price_change_24h": 2.10,
            "price_change_percent": 1.37,
            "market_cap": "$1.6T",
            "sector": "Consumer Discretionary",
            "technical_indicators": {
                "rsi": 59.8,
                "moving_avg_50": 151.20,
                "moving_avg_200": 140.85,
                "pe_ratio": 45.2,
                "volatility": 0.26
            }
        },
        {
            "id": str(uuid.uuid4()),
            "symbol": "GOOGL",
            "name": "Alphabet Inc.",
            "asset_type": "stock",
            "current_price": 172.85,
            "target_price": 165.00,
            "recommendation": "HOLD",
            "risk_level": "MEDIUM",
            "confidence_score": 75,
            "timeframe": "12M",
            "analyst": "Kevin Park",
            "analysis": "Google maintains search dominance but faces AI competition and regulatory pressures. Strong cloud growth and YouTube performance offset concerns about core search disruption from generative AI.",
            "key_factors": [
                "Search market share under pressure from AI",
                "Google Cloud growing but trailing competitors",
                "YouTube revenue growth accelerating",
                "Regulatory scrutiny increasing globally",
                "AI investments requiring significant capital"
            ],
            "last_updated": datetime.utcnow() - timedelta(hours=6),
            "price_change_24h": -1.25,
            "price_change_percent": -0.72,
            "market_cap": "$2.1T",
            "sector": "Technology",
            "technical_indicators": {
                "rsi": 48.3,
                "moving_avg_50": 175.40,
                "moving_avg_200": 165.90,
                "pe_ratio": 24.8,
                "volatility": 0.23
            }
        }
    ]
    
    # Clear existing recommendations
    await db.investment_recommendations.delete_many({})
    
    # Insert new recommendations
    await db.investment_recommendations.insert_many(recommendations)
    print(f"✅ Created {len(recommendations)} investment recommendations")

async def create_sample_news_articles():
    """Create sample news articles"""
    
    articles = [
        {
            "id": str(uuid.uuid4()),
            "title": "AI Chip Demand Surges as Tech Giants Race to Build Intelligent Systems",
            "summary": "Major technology companies are investing billions in AI infrastructure, driving unprecedented demand for specialized semiconductors and creating supply chain bottlenecks across the industry.",
            "content": "The artificial intelligence revolution is reshaping the semiconductor industry as tech giants pour unprecedented resources into building intelligent systems. NVIDIA, AMD, and Intel are all reporting record demand for AI-optimized chips, with delivery times extending well into 2025.\n\nThe surge is being driven by companies like Microsoft, Google, and Amazon, who are rapidly expanding their cloud infrastructure to support AI workloads. OpenAI's GPT models alone require thousands of specialized chips to operate at scale.\n\n'We're seeing demand that exceeds anything we've experienced in the past decade,' said Jensen Huang, CEO of NVIDIA, during the company's latest earnings call. The chip maker's data center revenue grew 200% year-over-year, primarily driven by AI applications.\n\nThe bottleneck is creating ripple effects across the tech industry, with some companies delaying product launches while others are exploring alternative chip architectures. This has opened opportunities for emerging players in the semiconductor space.",
            "author": "Sarah Chen",
            "category": "Technology",
            "publish_date": datetime.utcnow() - timedelta(hours=2),
            "image_url": "https://images.unsplash.com/photo-1518709268805-4e9042af2176?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "tags": ["AI", "Semiconductors", "NVIDIA", "Technology", "Supply Chain"],
            "read_time": 4
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Federal Reserve Signals Potential Rate Cuts as Inflation Shows Signs of Cooling",
            "summary": "Recent economic data suggests inflation is moderating faster than expected, prompting Fed officials to hint at possible interest rate reductions in the coming months.",
            "content": "Federal Reserve Chairman Jerome Powell indicated today that the central bank may consider lowering interest rates sooner than previously anticipated, citing encouraging inflation data and concerns about economic growth.\n\nCore inflation dropped to 3.2% in the latest reading, down from a peak of 9.1% in 2022. This marks the sixth consecutive month of declining inflation, bringing it closer to the Fed's 2% target.\n\n'We're seeing clear progress on inflation while the labor market remains resilient,' Powell said during testimony before Congress. 'This gives us flexibility to adjust our monetary policy stance as conditions warrant.'\n\nMarkets rallied on the news, with the S&P 500 gaining 1.8% and bond yields falling across the curve. Interest rate futures now price in a 75% probability of a rate cut at the Fed's next meeting.\n\nEconomists are divided on the timing, with some arguing that premature cuts could reignite inflation, while others worry that keeping rates too high could trigger a recession.",
            "author": "Michael Rodriguez",
            "category": "Financial",
            "publish_date": datetime.utcnow() - timedelta(hours=5),
            "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "tags": ["Federal Reserve", "Interest Rates", "Inflation", "Economy", "Markets"],
            "read_time": 5
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Electric Vehicle Sales Slow as Market Matures and Competition Intensifies",
            "summary": "EV adoption is entering a new phase as early adopters are saturated and traditional automakers launch competitive models, pressuring Tesla's market dominance.",
            "content": "Electric vehicle sales growth is decelerating across major markets as the industry transitions from rapid early adoption to mainstream competition. Tesla, once the undisputed leader, now faces formidable challengers from traditional automakers.\n\nGlobal EV sales grew 18% in Q3, down from 45% growth in the same period last year. The slowdown reflects market saturation among early adopters and increased competition from Ford, GM, Volkswagen, and Chinese manufacturers like BYD.\n\n'The easy growth phase is over,' said automotive analyst Emma Thompson. 'Now it's about winning over mainstream consumers who care more about price, reliability, and charging infrastructure than cutting-edge technology.'\n\nTesla's market share in the US has dropped to 48% from 72% two years ago, though the company remains profitable and continues to expand globally. CEO Elon Musk acknowledged the challenges but emphasized Tesla's advantages in manufacturing scale and autonomous driving technology.\n\nThe industry is also grappling with supply chain constraints for battery materials and the need for expanded charging infrastructure to support mass adoption.",
            "author": "David Kim",
            "category": "Industry News",
            "publish_date": datetime.utcnow() - timedelta(hours=8),
            "image_url": "https://images.unsplash.com/photo-1593941707882-a5bac6861d75?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "tags": ["Electric Vehicles", "Tesla", "Automotive", "Competition", "Market Share"],
            "read_time": 6
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Cloud Computing Giants Report Strong Q4 Results Despite Economic Headwinds",
            "summary": "Amazon Web Services, Microsoft Azure, and Google Cloud all exceeded expectations as enterprises accelerate digital transformation initiatives.",
            "content": "The three major cloud computing platforms delivered robust fourth-quarter results, demonstrating the resilience of enterprise technology spending despite broader economic uncertainty.\n\nAmazon Web Services (AWS) reported 29% revenue growth to $24.2 billion, while Microsoft Azure grew 31% and Google Cloud expanded 35%. The strong performance reflects accelerating enterprise adoption of AI and machine learning services.\n\n'Enterprises are viewing cloud and AI not as optional investments but as competitive necessities,' said Satya Nadella, Microsoft's CEO. The company's AI-powered services, including GitHub Copilot and Office 365 enhancements, are driving significant customer engagement.\n\nGoogle Cloud's standout performance was attributed to its AI offerings, including the Gemini large language model and enterprise AI tools. The division is approaching profitability after years of heavy investment.\n\nAWS, while growing at a slower pace than competitors, maintains the largest market share at approximately 32%. The platform is benefiting from increased demand for machine learning and data analytics services.\n\nAnalysts expect the cloud wars to intensify as artificial intelligence becomes the primary battleground for customer acquisition and retention.",
            "author": "Jennifer Liu",
            "category": "Technology",
            "publish_date": datetime.utcnow() - timedelta(hours=12),
            "image_url": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "tags": ["Cloud Computing", "AWS", "Microsoft", "Google", "AI", "Enterprise"],
            "read_time": 5
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Bitcoin ETF Approvals Drive Cryptocurrency Mainstream Adoption",
            "summary": "The approval of spot Bitcoin ETFs by major financial institutions is bringing cryptocurrency investment to traditional portfolios and retail investors.",
            "content": "The cryptocurrency market reached a significant milestone with the approval and launch of spot Bitcoin exchange-traded funds (ETFs) from major financial institutions including BlackRock, Fidelity, and Grayscale.\n\nSince launching three months ago, these ETFs have attracted over $15 billion in assets, demonstrating strong institutional and retail demand for cryptocurrency exposure through traditional investment vehicles.\n\n'This represents a paradigm shift in how investors access Bitcoin,' said Matthew Sigel, head of digital assets research at VanEck. 'We're seeing pension funds, family offices, and retail advisors allocating to Bitcoin for the first time.'\n\nThe ETF launches have contributed to Bitcoin's price appreciation, with the cryptocurrency gaining 45% since the beginning of the year. Daily trading volumes have increased substantially, indicating growing market participation.\n\nTraditional financial advisors, previously hesitant to recommend cryptocurrency investments, are now incorporating Bitcoin ETFs into client portfolios as a hedge against inflation and currency debasement.\n\nRegulatory clarity continues to improve, with the SEC providing clearer guidelines for cryptocurrency investments and several other crypto ETF applications under review.",
            "author": "Alex Morgan",
            "category": "Financial",
            "publish_date": datetime.utcnow() - timedelta(hours=18),
            "image_url": "https://images.unsplash.com/photo-1518546305927-5a555bb7020d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "tags": ["Bitcoin", "ETF", "Cryptocurrency", "Investment", "BlackRock", "Regulation"],
            "read_time": 4
        },
        {
            "id": str(uuid.uuid4()),
            "title": "Renewable Energy Investments Reach Record Highs as Climate Goals Drive Policy",
            "summary": "Global investments in renewable energy infrastructure are accelerating as governments implement aggressive climate policies and costs continue to decline.",
            "content": "Investment in renewable energy reached a record $1.8 trillion globally in 2024, driven by government climate commitments, declining technology costs, and growing corporate sustainability mandates.\n\nSolar and wind projects accounted for 85% of new energy capacity additions, with solar installations alone growing 35% year-over-year. The International Energy Agency projects renewables will account for 95% of new power generation through 2030.\n\n'We're witnessing the fastest energy transition in human history,' said Dr. Fatih Birol, IEA Executive Director. 'The economics now favor renewable energy in virtually every market globally.'\n\nThe United States' Inflation Reduction Act has spurred $200 billion in clean energy investments, while the European Union's Green Deal is mobilizing €1 trillion for climate initiatives. China continues to dominate manufacturing of solar panels and wind turbines.\n\nEnergy storage technologies are advancing rapidly, with battery costs falling 70% over the past five years. This is enabling greater grid integration of intermittent renewable sources.\n\nTraditional energy companies are adapting their business models, with many oil and gas giants investing heavily in renewable projects and carbon capture technologies.",
            "author": "Emily Zhang",
            "category": "Industry News",
            "publish_date": datetime.utcnow() - timedelta(days=1),
            "image_url": "https://images.unsplash.com/photo-1466611653911-95081537e5b7?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80",
            "tags": ["Renewable Energy", "Climate Change", "Investment", "Solar", "Wind", "Policy"],
            "read_time": 7
        }
    ]
    
    # Clear existing articles
    await db.news_articles.delete_many({})
    
    # Insert new articles
    await db.news_articles.insert_many(articles)
    print(f"✅ Created {len(articles)} news articles")

async def main():
    """Main function to populate database"""
    print("🚀 Populating database with sample data...")
    
    try:
        await create_sample_investment_recommendations()
        await create_sample_news_articles()
        print("\n🎉 Database successfully populated!")
        print("\n📊 Your enhanced platform now has:")
        print("   • 8 Investment recommendations across stocks, ETFs, and crypto")
        print("   • 6 Financial news articles with rich content")
        print("   • Realistic data to showcase all UI/UX enhancements")
        
    except Exception as e:
        print(f"❌ Error populating database: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())