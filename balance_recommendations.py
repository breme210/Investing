import asyncio
import sys
import os
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

async def balance_recommendations():
    """Convert some HOLD recommendations to SELL for better balance"""
    
    # Get all HOLD recommendations
    hold_recs = await db.investment_recommendations.find({"recommendation": "HOLD"}).to_list(1000)
    
    # Convert 3-4 HOLD to SELL
    sell_candidates = random.sample(hold_recs, min(4, len(hold_recs)))
    
    for rec in sell_candidates:
        # Lower the target price to justify SELL recommendation
        new_target = rec["current_price"] * random.uniform(0.80, 0.95)
        
        # Lower confidence score
        new_confidence = random.randint(55, 70)
        
        # Update to SELL with appropriate reasoning
        await db.investment_recommendations.update_one(
            {"id": rec["id"]},
            {
                "$set": {
                    "recommendation": "SELL",
                    "target_price": round(new_target, 2),
                    "confidence_score": new_confidence,
                    "analysis": rec["analysis"] + " However, current valuation appears stretched and near-term headwinds may pressure performance."
                }
            }
        )
        print(f"✅ Updated {rec['symbol']} to SELL recommendation")

async def main():
    try:
        await balance_recommendations()
        
        # Get final summary
        summary = await db.investment_recommendations.aggregate([
            {
                "$group": {
                    "_id": "$recommendation",
                    "count": {"$sum": 1}
                }
            }
        ]).to_list(10)
        
        print("\n📊 Final recommendation distribution:")
        for item in summary:
            print(f"   • {item['_id']}: {item['count']}")
            
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())