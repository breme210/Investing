import asyncio
import uuid
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path
import random

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Regular news updates with fresh content
fresh_news_articles = [
    {
        "id": str(uuid.uuid4()),
        "title": "Breaking: Fed Signals Potential Rate Cut Amid Economic Softening",
        "summary": "Federal Reserve officials hint at possible interest rate reduction following weaker-than-expected economic data, signaling potential shift in monetary policy stance.",
        "content": """Federal Reserve officials signaled today that interest rate cuts may be on the horizon following a series of economic indicators showing softening conditions across multiple sectors.

**Key Economic Indicators:**
- **Employment Growth**: Job creation slowed to 180,000 in December, below expectations of 220,000
- **Inflation Trends**: Core PCE inflation fell to 2.8%, approaching the Fed's 2% target
- **Consumer Spending**: Retail sales declined 0.3% month-over-month, indicating consumer caution
- **Manufacturing Data**: ISM Manufacturing PMI dropped to 47.8, signaling contraction

**Fed Officials' Comments:**
Chair Powell noted during today's speech: "We are carefully monitoring economic conditions and remain prepared to adjust our policy stance as needed to support our dual mandate of price stability and full employment."

**Market Implications:**
Financial markets responded positively to the dovish signals:
- **Bond Markets**: 10-year Treasury yields fell 15 basis points to 3.85%
- **Equity Markets**: S&P 500 rallied 1.8% on rate cut expectations
- **Dollar Impact**: US Dollar weakened against major currencies
- **Gold Response**: Precious metals surged 2.1% on lower rate expectations

**Sector Analysis:**
**Winners**: Interest-sensitive sectors like Real Estate (REITs up 3.2%) and Utilities (up 2.8%) led the rally
**Losers**: Financial sector banks declined 1.5% on net interest margin concerns

**Economic Outlook:**
Economists suggest the Fed may implement 2-3 rate cuts totaling 75 basis points in 2024 if economic conditions continue to soften. However, officials emphasized data-dependent approach.

**Next Catalysts**: February FOMC meeting will be closely watched for formal policy shifts.""",
        "author": "Federal Reserve Desk",
        "category": "Economic Policy",
        "publish_date": datetime.utcnow() - timedelta(minutes=30),
        "image_url": None,
        "tags": ["Federal Reserve", "Interest Rates", "Economic Policy", "Monetary Policy"],
        "read_time": 4
    },
    {
        "id": str(uuid.uuid4()),
        "title": "AI Chip Shortage Intensifies as Demand Surges 300% Year-Over-Year",
        "summary": "Semiconductor industry faces unprecedented demand for AI-specific chips, creating supply bottlenecks and driving up prices across the technology sector.",
        "content": """The global semiconductor industry is grappling with an unprecedented surge in demand for artificial intelligence chips, with orders increasing 300% year-over-year according to industry data released today.

**Supply Chain Pressures:**
Major chip manufacturers report order backlogs extending 18-24 months for high-end AI processors. TSMC, the world's largest contract manufacturer, announced plans to increase production capacity by 40% to meet demand.

**Key Market Dynamics:**
- **H100 Demand**: NVIDIA's H100 chips command $40,000+ per unit with 6-month wait times
- **Alternative Solutions**: AMD, Intel ramping competing AI chip production
- **Cloud Giants**: Microsoft, Google, Amazon increasing internal chip development
- **Geopolitical Factors**: Export restrictions affecting China market dynamics

**Company Impact Analysis:**
**NVIDIA**: Trading at 52-week highs, forward P/E of 45x justified by revenue growth
**Advanced Micro Devices**: Gaining market share with MI300 series competitive positioning
**Taiwan Semiconductor**: Capacity utilization at 95%+ with margin expansion
**Applied Materials**: Equipment demand surging for AI chip fabrication

**Investment Implications:**
Semiconductor ETF (SMH) up 28% year-to-date, outperforming broader technology indices. Analysts recommend selective positioning in:
- **Pick-and-Shovel Plays**: Equipment manufacturers (AMAT, LRCX)
- **Memory Suppliers**: High-bandwidth memory providers (MU, SK Hynix)
- **Design Software**: EDA tools companies (CDNS, SNPS)

**Long-term Outlook:**
Industry forecasts suggest AI chip demand will grow 45% annually through 2027, driven by:
- Enterprise AI adoption accelerating
- Autonomous vehicle deployment
- Edge computing requirements
- Scientific research applications

**Risk Factors:**
- Potential economic slowdown reducing enterprise IT spending
- Geopolitical tensions affecting supply chains
- Technology shifts toward more efficient architectures

The shortage is expected to persist through 2025 as production capacity expansion lags demand growth.""",
        "author": "Semiconductor Industry Reporter",
        "category": "Technology",
        "publish_date": datetime.utcnow() - timedelta(hours=2),
        "image_url": None,
        "tags": ["AI", "Semiconductors", "Supply Chain", "NVIDIA", "Technology"],
        "read_time": 5
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Energy Transition Accelerates: Renewable Investments Hit Record $2.8 Trillion",
        "summary": "Global renewable energy investments reach unprecedented levels as countries and corporations accelerate decarbonization efforts amid favorable policy environment.",
        "content": """Global renewable energy investments reached a record $2.8 trillion in 2024, representing a 15% increase from the previous year as the energy transition accelerates worldwide.

**Investment Breakdown:**
- **Solar Power**: $1.1 trillion (39% of total investment)
- **Wind Energy**: $890 billion (32% of total investment)
- **Energy Storage**: $420 billion (15% of total investment)
- **Grid Infrastructure**: $280 billion (10% of total investment)
- **Other Technologies**: $110 billion (4% of total investment)

**Regional Leadership:**
**Asia-Pacific**: Led global investments with $1.2 trillion, driven by China's massive solar deployment
**Europe**: Contributed $780 billion, focusing on offshore wind development
**North America**: Invested $650 billion, emphasizing grid modernization and storage
**Other Regions**: $170 billion combined investment

**Corporate Participation:**
Major corporations announced ambitious renewable commitments:
- **Microsoft**: $15 billion renewable energy agreement, largest corporate deal
- **Amazon**: 250 new renewable projects across 18 countries
- **Google**: Achieved 24/7 carbon-free energy in 5 data center regions
- **Apple**: Expanded supplier clean energy program to 95% of manufacturing

**Technology Developments:**
**Solar Efficiency**: Next-generation panels achieving 26% efficiency in commercial applications
**Wind Technology**: Offshore turbines reaching 15MW capacity with improved reliability
**Storage Solutions**: Battery costs declining 20% annually, enabling grid-scale deployment
**Green Hydrogen**: Production costs approaching parity with fossil fuel alternatives

**Market Impact:**
Renewable energy stocks outperformed broader markets:
- **NextEra Energy**: Up 18% on renewable development pipeline
- **Enphase Energy**: Solar inverter demand driving 25% revenue growth
- **Vestas Wind**: Order backlog reaching record 18-month levels

**Policy Support:**
Government initiatives accelerating adoption:
- **US Inflation Reduction Act**: $370 billion in clean energy incentives
- **European Green Deal**: €1 trillion investment framework
- **China's 14th Five-Year Plan**: 50% renewable electricity target by 2025

**Investment Outlook:**
Industry analysts project continued growth with $3.5 trillion investments expected in 2025, driven by:
- Technology cost reductions
- Favorable financing conditions
- Corporate sustainability commitments
- Grid reliability requirements

**Challenges Remaining:**
- Intermittency management requiring storage solutions
- Grid infrastructure upgrades for renewable integration
- Supply chain constraints for critical materials
- Permitting delays in key markets

The energy transition represents the largest capital deployment in human history, creating significant investment opportunities across the renewable value chain.""",
        "author": "Energy Transition Team",
        "category": "Energy Markets",
        "publish_date": datetime.utcnow() - timedelta(hours=4),
        "image_url": None,
        "tags": ["Renewable Energy", "ESG", "Climate Change", "Energy Transition", "Investments"],
        "read_time": 6
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Cryptocurrency Market Volatility Spikes as Regulatory Clarity Emerges",
        "summary": "Major cryptocurrency movements follow regulatory announcements from key jurisdictions, creating both opportunities and challenges for digital asset investors.",
        "content": """Cryptocurrency markets experienced significant volatility today following regulatory announcements from major jurisdictions, with Bitcoin trading in a $5,000 range as investors digest implications for the digital asset ecosystem.

**Regulatory Developments:**
**United States**: SEC Chairman announced comprehensive framework for cryptocurrency regulation, providing clarity on:
- **Spot ETF Approvals**: Additional Bitcoin ETFs approved, bringing total AUM to $45 billion
- **Staking Services**: Guidance on staking as investment contracts
- **DeFi Protocols**: Regulatory perimeter for decentralized finance applications
- **Stablecoin Rules**: Reserve requirements and audit standards

**European Union**: MiCA (Markets in Crypto-Assets) regulation implementation timeline accelerated, affecting:
- Exchange licensing requirements
- Consumer protection standards
- Anti-money laundering compliance
- Stablecoin issuance frameworks

**Market Response:**
**Bitcoin**: Rallied to $72,500 before settling at $69,200, up 3.2% on regulatory clarity
**Ethereum**: Outperformed with 5.8% gains on DeFi regulatory framework
**Altcoins**: Mixed performance with compliance-focused tokens leading
**Stablecoins**: USDC gained market share amid reserve transparency requirements

**Institutional Activity:**
Corporate adoption accelerating amid regulatory clarity:
- **MicroStrategy**: Added 2,000 Bitcoin to treasury, total holdings 190,000 BTC
- **Tesla**: Resumed Bitcoin payments for select products
- **BlackRock**: IBIT ETF reached $15 billion AUM in record time
- **Fidelity**: Expanded cryptocurrency services to wealth management clients

**Technical Analysis:**
**Bitcoin**: Breaking through $70,000 resistance with volume confirmation
**Support Levels**: Strong bid interest at $65,000-67,000 range
**Resistance**: Next target at $75,000 based on previous highs
**Options Activity**: Call options skew indicating bullish sentiment

**Market Infrastructure:**
**Trading Volumes**: 24-hour volume exceeded $120 billion across major exchanges
**Liquidity**: Bid-ask spreads tightened on increased institutional participation
**Custody Solutions**: Prime brokerage services expanding for institutional clients
**Payment Rails**: Lightning Network transactions up 200% month-over-month

**Investment Themes:**
**Regulatory Winners**: Compliant exchanges and custody providers outperforming
**DeFi Evolution**: Protocols adapting to regulatory requirements showing resilience
**Infrastructure Plays**: Companies providing blockchain infrastructure seeing renewed interest
**Traditional Finance**: Banks and asset managers entering crypto space

**Risk Considerations:**
- Regulatory implementation timelines creating uncertainty
- Market concentration in Bitcoin and Ethereum
- Environmental concerns affecting proof-of-work cryptocurrencies
- Technological risks in emerging protocols

**Outlook:**
Analysts suggest regulatory clarity will drive institutional adoption, potentially supporting $80,000 Bitcoin price target by year-end. However, execution risks and broader economic conditions remain key variables.""",
        "author": "Digital Assets Desk",
        "category": "Cryptocurrency",
        "publish_date": datetime.utcnow() - timedelta(hours=6),
        "image_url": None,
        "tags": ["Bitcoin", "Cryptocurrency", "Regulation", "SEC", "Digital Assets"],
        "read_time": 5
    },
    {
        "id": str(uuid.uuid4()),
        "title": "Healthcare Innovation Surge: Gene Therapy Breakthroughs Drive Biotech Rally",
        "summary": "Revolutionary gene therapy treatments show unprecedented success rates in clinical trials, sparking investor enthusiasm and regulatory fast-track approvals.",
        "content": """The biotechnology sector surged today following announcements of breakthrough gene therapy results from multiple clinical trials, with several treatments showing cure rates exceeding 90% for previously untreatable conditions.

**Clinical Breakthrough Highlights:**
**Sickle Cell Disease**: CRISPR-based therapy achieved 95% success rate in Phase 3 trials
**Hemophilia**: Gene therapy eliminated bleeding episodes in 88% of patients
**Inherited Blindness**: Novel treatment restored functional vision in 78% of participants
**Rare Cancers**: CAR-T cell therapies showing complete remission in aggressive tumors

**Company Performance:**
**CRISPR Therapeutics**: Shares rallied 28% on sickle cell therapy data
**Bluebird Bio**: Up 45% following FDA approval pathway announcement
**Moderna**: Gained 12% on mRNA platform expansion into gene therapy
**Gilead Sciences**: Advanced 8% on CAR-T manufacturing improvements

**Investment Implications:**
Biotech ETF (IBB) surged 6.2%, outperforming broader healthcare indices:
- **Platform Technologies**: CRISPR and base editing companies leading gains
- **Manufacturing**: Cell therapy production companies seeing premium valuations
- **Delivery Systems**: Lipid nanoparticle and viral vector specialists advancing
- **Diagnostics**: Companion diagnostic developers gaining traction

**Regulatory Environment:**
FDA's accelerated approval pathways supporting innovation:
- **Breakthrough Therapy Designation**: 40% increase in applications year-over-year
- **Regenerative Medicine Advanced Therapy**: Fast-track process for cell therapies
- **Pediatric Priority**: Enhanced review for rare childhood diseases
- **Real-World Evidence**: Post-market data collection reducing approval timelines

**Market Dynamics:**
**Venture Capital**: $18 billion invested in biotech startups, 25% increase from 2023
**IPO Pipeline**: 35 biotech companies planning public offerings in next 6 months
**Partnership Activity**: Big pharma increasing collaboration with biotech innovators
**Geographic Trends**: US maintaining leadership with 60% of global gene therapy development

**Technology Convergence:**
**AI Integration**: Machine learning accelerating drug discovery timelines
- **Protein Folding**: AlphaFold advancing target identification
- **Clinical Trial Design**: AI optimizing patient selection and endpoints
- **Manufacturing**: Automated systems reducing production costs by 40%

**Commercial Outlook:**
Gene therapy market projected to reach $180 billion by 2030:
- **Oncology**: 45% of market share with CAR-T and tumor infiltrating lymphocytes
- **Rare Diseases**: 30% of market with high-value orphan indications
- **Inherited Disorders**: 25% of market with one-time cure potential

**Investment Risks:**
- High development costs requiring substantial capital
- Regulatory approval uncertainty despite fast-track pathways
- Manufacturing complexity limiting commercialization
- Reimbursement challenges for high-cost therapies

**Key Catalysts Ahead:**
- **Q1 2024**: Multiple Phase 3 readouts for leading gene therapies
- **FDA Advisory Panels**: Critical regulatory milestones for approval decisions
- **Commercial Launches**: First-generation therapies entering broader markets
- **International Expansion**: European and Asian regulatory submissions

The convergence of scientific breakthroughs and supportive regulatory environment positions biotechnology for sustained outperformance, with selective opportunities in platform technologies and commercial-stage companies.""",
        "author": "Biotech Research Team",
        "category": "Healthcare Innovation",
        "publish_date": datetime.utcnow() - timedelta(hours=8),
        "image_url": None,
        "tags": ["Biotechnology", "Gene Therapy", "Healthcare", "CRISPR", "FDA"],
        "read_time": 6
    }
]

async def add_fresh_news_content():
    """Add fresh news content to simulate regular updates"""
    try:
        # Get current news count
        current_count = await db.news_articles.count_documents({})
        print(f"Current news articles in database: {current_count}")
        
        # Add fresh news articles
        result = await db.news_articles.insert_many(fresh_news_articles)
        print(f"Added {len(result.inserted_ids)} fresh news articles")
        
        # Verify new total
        new_count = await db.news_articles.count_documents({})
        print(f"Total news articles now: {new_count}")
        
        # Show latest articles
        latest_articles = await db.news_articles.find().sort("publish_date", -1).limit(10).to_list(10)
        print(f"\nLatest 10 articles:")
        for i, article in enumerate(latest_articles, 1):
            time_ago = datetime.utcnow() - article["publish_date"]
            if time_ago.total_seconds() < 3600:
                time_str = f"{int(time_ago.total_seconds() / 60)} minutes ago"
            else:
                time_str = f"{int(time_ago.total_seconds() / 3600)} hours ago"
            print(f"{i}. {article['title'][:60]}... ({time_str})")
        
        # Show category breakdown
        categories = await db.news_articles.distinct("category")
        print(f"\nNews categories: {', '.join(categories)}")
        
        for category in categories:
            count = await db.news_articles.count_documents({"category": category})
            print(f"- {category}: {count} articles")
            
    except Exception as e:
        print(f"Error adding fresh news: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(add_fresh_news_content())