from fastapi import FastAPI, APIRouter, HTTPException, Query
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid
from datetime import datetime


ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Create the main app without a prefix
app = FastAPI()

# Create a router with the /api prefix
api_router = APIRouter(prefix="/api")


# Define Models
class StatusCheck(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class StatusCheckCreate(BaseModel):
    client_name: str

# News Models
class NewsArticle(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    summary: str
    content: str
    author: str
    category: str
    publish_date: datetime = Field(default_factory=datetime.utcnow)
    image_url: Optional[str] = None
    tags: List[str] = []
    read_time: int = 5  # estimated read time in minutes

class NewsArticleResponse(BaseModel):
    id: str
    title: str
    summary: str
    content: str
    author: str
    category: str
    publish_date: datetime
    image_url: Optional[str] = None
    tags: List[str] = []
    read_time: int

# Add your routes to the router instead of directly to app
@api_router.get("/")
async def root():
    return {"message": "Hello World"}

@api_router.post("/status", response_model=StatusCheck)
async def create_status_check(input: StatusCheckCreate):
    status_dict = input.dict()
    status_obj = StatusCheck(**status_dict)
    _ = await db.status_checks.insert_one(status_obj.dict())
    return status_obj

@api_router.get("/status", response_model=List[StatusCheck])
async def get_status_checks():
    status_checks = await db.status_checks.find().to_list(1000)
    return [StatusCheck(**status_check) for status_check in status_checks]

# News API Endpoints
@api_router.get("/news", response_model=List[NewsArticleResponse])
async def get_news_articles(category: Optional[str] = Query(None)):
    query = {}
    if category:
        query["category"] = category
    
    articles = await db.news_articles.find(query).sort("publish_date", -1).to_list(100)
    return [NewsArticleResponse(**article) for article in articles]

@api_router.get("/news/{article_id}", response_model=NewsArticleResponse)
async def get_news_article(article_id: str):
    article = await db.news_articles.find_one({"id": article_id})
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return NewsArticleResponse(**article)

@api_router.get("/news/categories/list")
async def get_news_categories():
    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    categories = await db.news_articles.aggregate(pipeline).to_list(100)
    return [{"category": cat["_id"], "count": cat["count"]} for cat in categories]

# Include the router in the main app
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()
