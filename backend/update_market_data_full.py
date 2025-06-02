import asyncio
import random
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

async def update_investment_prices():
    """Simulate regular price updates for dynamic market feel"""
    try:
        # Get all investment recommendations
        investments = await db.investment_recommendations.find().to_list(1000)
        print(f"Updating prices for {len(investments)} investments...")
        
        updates_made = 0
        significant_moves = []
        
        for investment in investments:
            # Generate realistic price movements based on asset type and volatility
            asset_type = investment["asset_type"]
            current_price = investment["current_price"]
            volatility = investment.get("technical_indicators", {}).get("volatility", 0.25)
            
            # Different movement ranges by asset type
            if asset_type == "stock":
                # Stocks: -3% to +3% daily range, weighted by volatility
                max_change = 0.03 * (volatility / 0.25)
                price_change_percent = random.uniform(-max_change, max_change)
            elif asset_type == "index":
                # Indices: -1.5% to +1.5% daily range (less volatile)
                price_change_percent = random.uniform(-0.015, 0.015)
            else:  # commodity
                # Commodities: -4% to +4% daily range (more volatile)
                max_change = 0.04
                if investment["symbol"] == "BTC-USD":
                    max_change = 0.06  # Bitcoin even more volatile
                price_change_percent = random.uniform(-max_change, max_change)
            
            # Calculate new price
            price_change_amount = current_price * price_change_percent
            new_price = current_price + price_change_amount
            
            # Ensure positive prices
            if new_price <= 0:
                new_price = current_price * 0.95
                price_change_amount = new_price - current_price
                price_change_percent = price_change_amount / current_price
            
            # Update the investment
            await db.investment_recommendations.update_one(
                {"id": investment["id"]},
                {
                    "$set": {
                        "current_price": round(new_price, 2),
                        "price_change_24h": round(price_change_amount, 2),
                        "price_change_percent": round(price_change_percent * 100, 2),
                        "last_updated": datetime.utcnow()
                    }
                }
            )
            
            updates_made += 1
            
            # Track significant moves (>2% for stocks, >3% for commodities)
            threshold = 0.02 if asset_type in ["stock", "index"] else 0.03
            if abs(price_change_percent) > threshold:
                significant_moves.append({
                    "symbol": investment["symbol"],
                    "name": investment["name"],
                    "change_percent": price_change_percent * 100,
                    "new_price": new_price
                })
        
        print(f"Successfully updated {updates_made} investment prices")
        
        # Show significant moves
        if significant_moves:
            print(f"\nSignificant price movements:")
            for move in sorted(significant_moves, key=lambda x: abs(x["change_percent"]), reverse=True)[:10]:
                direction = "📈" if move["change_percent"] > 0 else "📉"
                print(f"{direction} {move['symbol']}: {move['change_percent']:+.2f}% (${move['new_price']:.2f})")
        
        print(f"\nPrice update completed at {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
        
    except Exception as e:
        print(f"Error updating investment prices: {e}")

async def add_market_update_news():
    """Add a market update news article based on current movements"""
    try:
        # Get some recent price movements
        recent_movers = await db.investment_recommendations.find().sort("last_updated", -1).limit(10).to_list(10)
        
        # Calculate market summary
        positive_moves = len([inv for inv in recent_movers if inv["price_change_percent"] > 0])
        negative_moves = len([inv for inv in recent_movers if inv["price_change_percent"] < 0])
        
        # Create market update article
        market_sentiment = "bullish" if positive_moves > negative_moves else "bearish" if negative_moves > positive_moves else "mixed"
        
        market_update_article = {
            "id": str(uuid.uuid4()),
            "title": f"Market Update: {market_sentiment.title()} Sentiment as Trading Session Ends",
            "summary": f"Today's trading session showed {market_sentiment} sentiment with {positive_moves} gainers and {negative_moves} decliners among major positions.",
            "content": f"""Today's trading session concluded with {market_sentiment} market sentiment as investors digested various economic and corporate developments.

**Market Summary:**
- **Gainers**: {positive_moves} out of 10 major positions advanced
- **Decliners**: {negative_moves} positions closed lower
- **Sentiment**: {market_sentiment.title()} tone dominated trading

**Notable Movements:**
{chr(10).join([f"• **{inv['symbol']}**: {inv['price_change_percent']:+.2f}% to ${inv['current_price']:.2f}" for inv in recent_movers[:5]])}

**Trading Volume:**
Volume levels were {'above' if market_sentiment == 'bullish' else 'below'} average as investors {'embraced' if market_sentiment == 'bullish' else 'showed caution amid'} the market dynamics.

**Sector Performance:**
Technology and growth names {'led the advance' if market_sentiment == 'bullish' else 'faced pressure'} while defensive sectors showed {'mixed' if market_sentiment == 'bullish' else 'relative strength'} performance.

**Market Outlook:**
Looking ahead, investors will focus on upcoming economic data releases and corporate earnings reports for continued market direction.

*This market update is generated based on recent trading activity and price movements.*""",
            "author": "Market Data Team",
            "category": "Market Update",
            "publish_date": datetime.utcnow(),
            "image_url": None,
            "tags": ["Market Update", "Trading", "Stock Market", "Daily Summary"],
            "read_time": 3
        }
        
        # Insert the market update
        await db.news_articles.insert_one(market_update_article)
        print("Added market update news article")
        
    except Exception as e:
        print(f"Error adding market update news: {e}")

async def main():
    try:
        await update_investment_prices()
        await add_market_update_news()
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(main())