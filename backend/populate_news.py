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

# Sample news articles with relevant categories and content
sample_articles = [
    {
        "id": str(uuid.uuid4()),
        "title": "Revolutionary AI Breakthrough: New Language Model Achieves 99% Accuracy",
        "summary": "Researchers have developed a groundbreaking AI language model that demonstrates unprecedented accuracy in natural language understanding and generation.",
        "content": """A team of researchers at a leading tech institute has announced a major breakthrough in artificial intelligence with the development of a new language model that achieves 99% accuracy in various natural language processing tasks.

The new model, trained on diverse datasets spanning multiple languages and domains, represents a significant leap forward in AI capabilities. Unlike previous models, this system demonstrates remarkable consistency across different types of text generation, translation, and comprehension tasks.

Key features of the breakthrough include:
- Enhanced contextual understanding
- Improved reasoning capabilities  
- Better handling of nuanced language patterns
- Reduced computational requirements

The research team believes this advancement could revolutionize how we interact with AI systems and pave the way for more sophisticated applications in education, healthcare, and business automation.

Early testing shows the model performing exceptionally well in complex scenarios that previously challenged even the most advanced AI systems. The team plans to publish their findings in the upcoming International Conference on Machine Learning.""",
        "author": "Dr. Sarah Chen",
        "category": "Technology",
        "publish_date": datetime.utcnow() - timedelta(days=1),
        "image_url": None,
        "tags": ["AI", "Machine Learning", "Research", "Innovation"],
        "read_time": 3
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Major Platform Update: Enhanced Security and Performance Features",
        "summary": "Our latest platform update introduces advanced security measures and significant performance improvements to deliver a better user experience.",
        "content": """We're excited to announce the release of our latest platform update, bringing enhanced security features and substantial performance improvements to all users.

**Security Enhancements:**
- Advanced encryption protocols for data transmission
- Multi-factor authentication support
- Enhanced API security with rate limiting
- Improved access control mechanisms

**Performance Improvements:**
- 40% faster page load times
- Optimized database queries reducing response time by 60%
- Enhanced caching strategies
- Streamlined user interface for better accessibility

**New Features:**
- Real-time collaboration tools
- Advanced analytics dashboard
- Improved mobile responsiveness
- Enhanced notification system

All users will automatically receive these updates over the next 48 hours. No action is required on your part, though we recommend reviewing the new security settings in your account preferences.

Our development team has been working tirelessly to ensure these updates maintain the highest standards of reliability while introducing powerful new capabilities. We believe these improvements will significantly enhance your daily workflow and overall platform experience.

For detailed documentation on the new features, please visit our updated help center or contact our support team.""",
        "author": "Product Team",
        "category": "Product Updates",
        "publish_date": datetime.utcnow() - timedelta(days=3),
        "image_url": None,
        "tags": ["Security", "Performance", "Update", "Features"],
        "read_time": 4
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Industry Report: The Future of Remote Work in Tech Companies",
        "summary": "A comprehensive analysis of remote work trends in the technology sector reveals significant shifts in how companies approach distributed teams.",
        "content": """A new industry report examining remote work trends across 500+ technology companies reveals fascinating insights about the future of distributed teams and workplace flexibility.

**Key Findings:**

**Adoption Rates:**
- 87% of tech companies now offer full remote work options
- 45% have adopted hybrid models
- Only 8% require full-time office presence

**Productivity Metrics:**
- Remote teams show 23% higher productivity in coding tasks
- Collaboration tools usage increased by 340%
- Employee satisfaction scores improved by 31%

**Challenges and Solutions:**
Companies report that the biggest challenges include maintaining team culture and onboarding new employees. However, innovative solutions are emerging:
- Virtual reality meeting spaces
- AI-powered collaboration assistants
- Advanced project management systems
- Digital team-building platforms

**Technology Investments:**
Organizations are investing heavily in infrastructure to support remote work:
- Cloud computing services (95% adoption)
- Cybersecurity tools (89% increase in budget)
- Communication platforms (78% upgraded)
- Digital whiteboarding solutions (67% new adoption)

**Future Predictions:**
Experts predict that by 2026, remote work will become the default option for most tech roles, with companies competing on the quality of their digital workplace experience rather than physical office amenities.

The report also highlights the growing importance of work-life balance in talent retention, with remote work capabilities now ranking as the second most important factor for job seekers in the technology sector.""",
        "author": "Industry Analysis Team",
        "category": "Industry News",
        "publish_date": datetime.utcnow() - timedelta(days=5),
        "image_url": None,
        "tags": ["Remote Work", "Technology", "Industry Trends", "Productivity"],
        "read_time": 5
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Company Milestone: Reaching 100,000 Active Users Worldwide",
        "summary": "We're proud to announce that our platform has reached 100,000 active users across 50 countries, marking a significant milestone in our growth journey.",
        "content": """Today marks a special day in our company's history as we celebrate reaching 100,000 active users worldwide. This incredible milestone represents more than just a number – it's a testament to the trust and support of our amazing community.

**Our Growth Journey:**
When we started this company three years ago, we had a simple vision: to create a platform that would empower individuals and teams to achieve more through intelligent automation and seamless collaboration.

**Milestones Along the Way:**
- Month 6: 1,000 users
- Year 1: 10,000 users  
- Year 2: 50,000 users
- Today: 100,000 users across 50 countries

**What This Means:**
Our global community now spans across six continents, with users from diverse backgrounds and industries finding value in our platform. From small startups to large enterprises, freelancers to Fortune 500 companies, our user base represents the full spectrum of modern digital work.

**User Impact Statistics:**
- Over 2 million projects completed
- 15 million hours of work automated
- 98% user satisfaction rate
- Average time savings of 4 hours per week per user

**Looking Forward:**
This milestone is just the beginning. We're committed to continuing our mission of making powerful tools accessible to everyone. In the coming months, we'll be introducing:
- Advanced AI-powered features
- Enhanced collaboration tools
- Mobile application improvements
- Expanded integration capabilities

**Thank You:**
None of this would have been possible without our incredible users, dedicated team, and supportive investors. Your feedback, suggestions, and continued trust drive us to innovate and improve every day.

Here's to the next 100,000 users and beyond!""",
        "author": "CEO & Founder",
        "category": "Company News",
        "publish_date": datetime.utcnow() - timedelta(days=7),
        "image_url": None,
        "tags": ["Milestone", "Growth", "Community", "Achievement"],
        "read_time": 4
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Open Source Initiative: Contributing to Developer Community",
        "summary": "We're launching our open source initiative to give back to the developer community and foster innovation through collaborative development.",
        "content": """We're excited to announce the launch of our Open Source Initiative, a comprehensive program designed to contribute to the developer community and foster innovation through collaborative development.

**Why Open Source Matters:**
Open source software has been the backbone of technological innovation for decades. It enables developers worldwide to collaborate, learn, and build upon each other's work, creating better solutions for everyone.

**Our Commitment:**
As part of this initiative, we're open sourcing several key components of our platform:

**Released Projects:**
1. **Aurora UI Components** - A comprehensive React component library
2. **DataFlow Engine** - High-performance data processing tools
3. **SecureAuth SDK** - Authentication and authorization utilities
4. **CloudSync API** - Multi-cloud synchronization framework

**Community Benefits:**
- Free access to enterprise-grade tools
- Comprehensive documentation and tutorials
- Regular updates and maintenance
- Community support forums
- Contribution guidelines for developers

**Getting Involved:**
We encourage developers of all skill levels to participate:
- **Beginners:** Start with documentation improvements and bug reports
- **Intermediate:** Contribute features and enhancements
- **Advanced:** Help with architecture decisions and code reviews

**Impact Goals:**
Our aim is to:
- Support 10,000+ developers in their projects
- Create educational resources for learning modern development practices
- Foster a collaborative community around our tools
- Drive innovation in the broader tech ecosystem

**Recognition Program:**
We'll be recognizing outstanding contributors through:
- Monthly contributor spotlights
- Conference speaking opportunities
- Exclusive beta access to new features
- Direct collaboration with our engineering team

**Next Steps:**
All projects are available on our GitHub organization with MIT licensing. We've also prepared comprehensive onboarding materials and contribution guides to help new contributors get started quickly.

Join us in building the future of development tools, one commit at a time.""",
        "author": "Engineering Team",
        "category": "Company News",
        "publish_date": datetime.utcnow() - timedelta(days=10),
        "image_url": None,
        "tags": ["Open Source", "Developer Community", "Innovation", "Collaboration"],
        "read_time": 4
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Emerging Technologies: The Rise of Edge Computing in IoT",
        "summary": "Edge computing is transforming the Internet of Things landscape by bringing processing power closer to data sources, reducing latency and improving efficiency.",
        "content": """Edge computing is rapidly emerging as a game-changing technology in the Internet of Things (IoT) ecosystem, fundamentally transforming how we process and analyze data from connected devices.

**What is Edge Computing?**
Edge computing brings computation and data storage closer to the location where it's needed, improving response times and saving bandwidth. Instead of sending all data to centralized cloud servers, processing happens at the "edge" of the network.

**Why It Matters for IoT:**
Traditional IoT architectures face several challenges:
- High latency when sending data to distant cloud servers
- Bandwidth limitations with millions of connected devices
- Privacy concerns with sensitive data transmission
- Reliability issues when connectivity is poor

**Edge Computing Solutions:**
Edge computing addresses these challenges by:
- Processing data locally on IoT devices or nearby edge servers
- Reducing data transmission requirements by 80-90%
- Enabling real-time decision making
- Improving data privacy and security

**Real-World Applications:**

**Smart Manufacturing:**
- Predictive maintenance with millisecond response times
- Quality control through real-time image analysis
- Autonomous robotic systems

**Smart Cities:**
- Traffic optimization with instant data processing
- Emergency response systems with local decision making
- Energy grid management with distributed intelligence

**Healthcare:**
- Patient monitoring with immediate alert systems
- Medical device automation for critical care
- Remote surgery with ultra-low latency requirements

**Autonomous Vehicles:**
- Real-time object detection and collision avoidance
- Local traffic pattern analysis
- Instant decision making for safety systems

**Market Growth:**
Industry analysts predict the edge computing market will grow from $12 billion in 2023 to $87 billion by 2030, with IoT applications driving the majority of this growth.

**Challenges and Future Outlook:**
While promising, edge computing faces challenges including:
- Standardization across different platforms
- Security management for distributed systems
- Cost considerations for edge infrastructure
- Skills gap in edge computing development

**The Future:**
As 5G networks become more prevalent and IoT devices become more sophisticated, edge computing will become essential infrastructure for next-generation applications requiring real-time processing and ultra-low latency.""",
        "author": "Tech Research Team",
        "category": "Technology",
        "publish_date": datetime.utcnow() - timedelta(days=14),
        "image_url": None,
        "tags": ["Edge Computing", "IoT", "Technology Trends", "Innovation"],
        "read_time": 6
    }
]

async def populate_database():
    """Populate the database with sample news articles"""
    try:
        # Clear existing news articles
        await db.news_articles.delete_many({})
        print("Cleared existing news articles")
        
        # Insert sample articles
        result = await db.news_articles.insert_many(sample_articles)
        print(f"Inserted {len(result.inserted_ids)} news articles")
        
        # Verify insertion
        count = await db.news_articles.count_documents({})
        print(f"Total articles in database: {count}")
        
        # Show categories
        categories = await db.news_articles.distinct("category")
        print(f"Categories available: {', '.join(categories)}")
        
    except Exception as e:
        print(f"Error populating database: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(populate_database())