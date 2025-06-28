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

# Pool of additional recommendations to add periodically
NEW_RECOMMENDATIONS_POOL = [
    {
        "symbol": "DIS",
        "name": "The Walt Disney Company",
        "asset_type": "stock",
        "current_price": 91.25,
        "target_price": 110.00,
        "recommendation": "BUY",
        "risk_level": "MEDIUM",
        "confidence_score": 76,
        "timeframe": "18M",
        "analyst": "Emma Thompson",
        "analysis": "Disney's streaming strategy and theme park recovery position the company for growth. Content library and brand strength provide competitive moats.",
        "key_factors": [
            "Disney+ subscriber growth in international markets",
            "Theme park attendance recovering to pre-pandemic levels",
            "Strong content pipeline including Marvel and Star Wars",
            "Pricing power in both streaming and parks",
            "ESPN streaming launch creating new revenue opportunities"
        ],
        "sector": "Communication Services",
        "market_cap": "$167B"
    },
    {
        "symbol": "V",
        "name": "Visa Inc.",
        "asset_type": "stock",
        "current_price": 264.75,
        "target_price": 290.00,
        "recommendation": "BUY",
        "risk_level": "LOW",
        "confidence_score": 91,
        "timeframe": "12M",
        "analyst": "Michael Chen",
        "analysis": "Visa's dominant payment network benefits from secular shift to digital payments. Strong moats and recurring revenue model drive consistent growth.",
        "key_factors": [
            "Secular shift from cash to digital payments",
            "Network effects creating strong competitive moats",
            "High-margin business model with predictable revenue",
            "Cross-border payments recovering post-COVID",
            "Emerging markets adoption accelerating"
        ],
        "sector": "Financial Services",
        "market_cap": "$575B"
    },
    {
        "symbol": "AMD",
        "name": "Advanced Micro Devices, Inc.",
        "asset_type": "stock",
        "current_price": 124.85,
        "target_price": 160.00,
        "recommendation": "BUY",
        "risk_level": "HIGH",
        "confidence_score": 81,
        "timeframe": "12M",
        "analyst": "Sarah Kim",
        "analysis": "AMD's competitive positioning in CPUs and growing AI chip portfolio challenge Intel and NVIDIA. Data center growth driving strong demand.",
        "key_factors": [
            "Market share gains in server CPU market",
            "AI chip portfolio competing with NVIDIA",
            "Strong partnerships with major cloud providers",
            "PC market recovery benefiting consumer division",
            "Manufacturing partnership with TSMC ensuring supply"
        ],
        "sector": "Technology",
        "market_cap": "$201B"
    },
    {
        "symbol": "ARKK",
        "name": "ARK Innovation ETF",
        "asset_type": "index",
        "current_price": 48.75,
        "target_price": 65.00,
        "recommendation": "HOLD",
        "risk_level": "HIGH",
        "confidence_score": 63,
        "timeframe": "24M",
        "analyst": "David Park",
        "analysis": "Innovation-focused ETF offers exposure to disruptive technologies but faces volatility from growth stock rotation.",
        "key_factors": [
            "Exposure to genomics, robotics, and AI companies",
            "High conviction portfolio with concentrated positions",
            "Growth stock rotation creating near-term headwinds",
            "Long-term innovation themes intact",
            "Active management approach differentiating from index funds"
        ],
        "sector": "Innovation",
        "market_cap": "$8.2B AUM"
    }
]

# Pool of additional news articles
NEW_NEWS_POOL = [
    {
        "title": "Central Banks Signal Coordinated Approach to Digital Currency Development",
        "summary": "Major central banks are collaborating on digital currency standards as governments worldwide accelerate CBDC development programs.",
        "content": "Central banks from the United States, European Union, Japan, and the United Kingdom announced a coordinated framework for developing central bank digital currencies (CBDCs), marking a significant step toward mainstream digital money adoption...",
        "author": "Richard Thompson",
        "category": "Financial",
        "tags": ["CBDC", "Digital Currency", "Central Banks", "Monetary Policy", "Innovation"],
        "read_time": 6
    },
    {
        "title": "Quantum Computing Breakthrough Promises to Revolutionize Drug Discovery",
        "summary": "Major pharmaceutical companies are partnering with quantum computing firms to accelerate drug development timelines and reduce costs.",
        "content": "IBM, Google, and several biotech companies announced partnerships to leverage quantum computing for molecular simulation and drug discovery...",
        "author": "Dr. Lisa Chen",
        "category": "Technology",
        "tags": ["Quantum Computing", "Pharmaceuticals", "Drug Discovery", "Innovation", "Healthcare"],
        "read_time": 7
    },
    {
        "title": "Autonomous Vehicle Testing Expands to Major Metropolitan Areas",
        "summary": "Self-driving car companies receive approval for expanded testing in New York, Los Angeles, and Chicago as regulatory frameworks evolve.",
        "content": "Waymo, Cruise, and Tesla have received expanded permits to test autonomous vehicles in dense urban environments...",
        "author": "Jennifer Rodriguez",
        "category": "Technology", 
        "tags": ["Autonomous Vehicles", "Self-Driving Cars", "Transportation", "Regulation", "Urban Planning"],
        "read_time": 5
    }
]

async def add_random_recommendation():
    """Add a new recommendation from the pool"""
    if not NEW_RECOMMENDATIONS_POOL:
        return
    
    # Select a random recommendation from the pool
    new_rec = random.choice(NEW_RECOMMENDATIONS_POOL)
    NEW_RECOMMENDATIONS_POOL.remove(new_rec)
    
    # Add required fields
    new_rec.update({
        "id": str(uuid.uuid4()),
        "last_updated": datetime.utcnow(),
        "price_change_24h": round(random.uniform(-3, 3), 2),
        "price_change_percent": round(random.uniform(-2.5, 2.5), 2),
        "technical_indicators": {
            "rsi": round(random.uniform(30, 80), 1),
            "moving_avg_50": round(new_rec["current_price"] * random.uniform(0.95, 1.05), 2),
            "moving_avg_200": round(new_rec["current_price"] * random.uniform(0.90, 1.10), 2),
            "pe_ratio": round(random.uniform(15, 45), 1),
            "volatility": round(random.uniform(0.15, 0.35), 2)
        }
    })
    
    await db.investment_recommendations.insert_one(new_rec)
    print(f"✅ Added new recommendation: {new_rec['symbol']} - {new_rec['name']}")

async def add_random_news():
    """Add a new news article from the pool"""
    if not NEW_NEWS_POOL:
        return
    
    # Select a random article from the pool
    new_article = random.choice(NEW_NEWS_POOL)
    NEW_NEWS_POOL.remove(new_article)
    
    # Add required fields
    new_article.update({
        "id": str(uuid.uuid4()),
        "publish_date": datetime.utcnow(),
        "image_url": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab"
    })
    
    await db.news_articles.insert_one(new_article)
    print(f"✅ Added new news article: {new_article['title'][:50]}...")

async def update_existing_data():
    """Update existing recommendations and news with fresh data"""
    
    # Update investment prices and confidence scores
    recommendations = await db.investment_recommendations.find().to_list(1000)
    updated_count = 0
    
    for rec in recommendations:
        # Generate realistic price movement
        volatility = rec.get("technical_indicators", {}).get("volatility", 0.25)
        price_change_percent = random.uniform(-2.0, 2.0) * volatility
        
        old_price = rec["current_price"]
        price_change_amount = old_price * (price_change_percent / 100)
        new_price = max(old_price * 0.7, min(old_price * 1.5, old_price + price_change_amount))
        
        # Small confidence adjustment
        confidence_adjustment = random.randint(-3, 3)
        new_confidence = max(50, min(95, rec["confidence_score"] + confidence_adjustment))
        
        await db.investment_recommendations.update_one(
            {"id": rec["id"]},
            {
                "$set": {
                    "current_price": round(new_price, 2),
                    "price_change_24h": round(price_change_amount, 2),
                    "price_change_percent": round(price_change_percent, 2),
                    "confidence_score": new_confidence,
                    "last_updated": datetime.utcnow()
                }
            }
        )
        updated_count += 1
    
    print(f"✅ Updated {updated_count} investment recommendations")
    
    # Update news timestamps
    articles = await db.news_articles.find().to_list(1000)
    for i, article in enumerate(articles):
        # Stagger articles over recent period
        hours_ago = i * 2  # 2 hours between articles
        new_timestamp = datetime.utcnow() - timedelta(hours=hours_ago)
        
        await db.news_articles.update_one(
            {"id": article["id"]},
            {"$set": {"publish_date": new_timestamp}}
        )
    
    print(f"✅ Updated {len(articles)} news article timestamps")

async def smart_recommendation_updates():
    """Intelligently update some recommendations based on market conditions"""
    
    # Simulate market conditions affecting certain sectors
    market_conditions = random.choice([
        "tech_rally", "energy_surge", "defensive_rotation", "growth_momentum", "value_play"
    ])
    
    recommendations = await db.investment_recommendations.find().to_list(1000)
    
    sector_multipliers = {
        "tech_rally": {"Technology": 1.5, "Healthcare": 0.8, "Energy": 0.7},
        "energy_surge": {"Energy": 1.8, "Technology": 0.9, "Financial Services": 1.2},
        "defensive_rotation": {"Consumer Staples": 1.3, "Healthcare": 1.2, "Technology": 0.8},
        "growth_momentum": {"Technology": 1.4, "Communication Services": 1.3, "Energy": 0.9},
        "value_play": {"Financial Services": 1.4, "Energy": 1.3, "Technology": 0.9}
    }
    
    current_multipliers = sector_multipliers.get(market_conditions, {})
    
    for rec in recommendations:
        sector = rec.get("sector", "Diversified")
        multiplier = current_multipliers.get(sector, 1.0)
        
        # Apply sector-specific movement
        base_change = random.uniform(-1.5, 1.5)
        sector_adjusted_change = base_change * multiplier
        
        old_price = rec["current_price"]
        price_change_amount = old_price * (sector_adjusted_change / 100)
        new_price = max(old_price * 0.8, min(old_price * 1.3, old_price + price_change_amount))
        
        await db.investment_recommendations.update_one(
            {"id": rec["id"]},
            {
                "$set": {
                    "current_price": round(new_price, 2),
                    "price_change_24h": round(price_change_amount, 2),
                    "price_change_percent": round(sector_adjusted_change, 2),
                    "last_updated": datetime.utcnow()
                }
            }
        )
    
    print(f"✅ Applied {market_conditions} market condition updates")

async def main():
    """Main function for regular updates"""
    print("🔄 Running comprehensive data update...")
    
    try:
        # Regular data updates
        await update_existing_data()
        
        # Smart market-based updates
        await smart_recommendation_updates()
        
        # Occasionally add new content (30% chance)
        if random.random() < 0.3:
            await add_random_recommendation()
        
        if random.random() < 0.3:
            await add_random_news()
        
        # Get final counts
        rec_count = await db.investment_recommendations.count_documents({})
        news_count = await db.news_articles.count_documents({})
        
        print(f"\n✨ Update completed!")
        print(f"   • {rec_count} total investment recommendations")
        print(f"   • {news_count} total news articles")
        print(f"   • All prices and data refreshed with market movements")
        
    except Exception as e:
        print(f"❌ Error during update: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())