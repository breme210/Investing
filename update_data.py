import asyncio
import sys
import os
from datetime import datetime, timedelta
import random

# Add the backend directory to the path
sys.path.append('/app/backend')

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv('/app/backend/.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

async def update_investment_prices():
    """Update investment recommendation prices with realistic market movements"""
    
    # Get all recommendations
    recommendations = await db.investment_recommendations.find().to_list(1000)
    
    for rec in recommendations:
        # Generate realistic price movement (±3% max daily change)
        price_change_percent = random.uniform(-3.0, 3.0)
        
        # Apply volatility based on asset risk level
        volatility_multiplier = {
            "LOW": 0.3,
            "MEDIUM": 0.7, 
            "HIGH": 1.2
        }.get(rec.get("risk_level", "MEDIUM"), 0.7)
        
        price_change_percent *= volatility_multiplier
        
        # Calculate new price
        old_price = rec["current_price"]
        price_change_amount = old_price * (price_change_percent / 100)
        new_price = old_price + price_change_amount
        
        # Ensure reasonable price bounds
        if new_price < old_price * 0.5:  # Don't drop more than 50%
            new_price = old_price * 0.5
        elif new_price > old_price * 2.0:  # Don't rise more than 100%
            new_price = old_price * 2.0
            
        # Update the recommendation
        await db.investment_recommendations.update_one(
            {"id": rec["id"]},
            {
                "$set": {
                    "current_price": round(new_price, 2),
                    "price_change_24h": round(price_change_amount, 2),
                    "price_change_percent": round(price_change_percent, 2),
                    "last_updated": datetime.utcnow()
                }
            }
        )
    
    print(f"✅ Updated prices for {len(recommendations)} investments")

async def update_news_timestamps():
    """Update news article timestamps to keep them fresh"""
    
    # Get all articles
    articles = await db.news_articles.find().to_list(1000)
    
    for i, article in enumerate(articles):
        # Stagger articles over the past 24 hours
        hours_ago = i * 4  # 4 hours between articles
        new_timestamp = datetime.utcnow() - timedelta(hours=hours_ago)
        
        await db.news_articles.update_one(
            {"id": article["id"]},
            {
                "$set": {
                    "publish_date": new_timestamp
                }
            }
        )
    
    print(f"✅ Updated timestamps for {len(articles)} news articles")

async def update_confidence_scores():
    """Slightly adjust confidence scores to simulate market sentiment changes"""
    
    recommendations = await db.investment_recommendations.find().to_list(1000)
    
    for rec in recommendations:
        # Small random adjustment (±5 points max)
        adjustment = random.randint(-5, 5)
        new_confidence = rec["confidence_score"] + adjustment
        
        # Keep within reasonable bounds (50-95)
        new_confidence = max(50, min(95, new_confidence))
        
        await db.investment_recommendations.update_one(
            {"id": rec["id"]},
            {
                "$set": {
                    "confidence_score": new_confidence
                }
            }
        )
    
    print(f"✅ Updated confidence scores for {len(recommendations)} investments")

async def main():
    """Main function to update data"""
    print("🔄 Updating database with fresh market data...")
    
    try:
        await update_investment_prices()
        await update_confidence_scores()
        await update_news_timestamps()
        
        print("\n✨ Database updated successfully!")
        print("   • Investment prices updated with realistic market movements")
        print("   • Confidence scores adjusted for market sentiment")
        print("   • News article timestamps refreshed")
        
    except Exception as e:
        print(f"❌ Error updating database: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())