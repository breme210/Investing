import requests
import unittest
import sys
from datetime import datetime

class APITester:
    def __init__(self, base_url):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.test_results = []

    def run_test(self, name, method, endpoint, expected_status, data=None, params=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        
        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, params=params)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            
            success = response.status_code == expected_status
            
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                result = {
                    "name": name,
                    "status": "PASSED",
                    "expected": expected_status,
                    "actual": response.status_code
                }
                
                # Try to get JSON response
                try:
                    result["response"] = response.json()
                except:
                    result["response"] = "Non-JSON response"
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                result = {
                    "name": name,
                    "status": "FAILED",
                    "expected": expected_status,
                    "actual": response.status_code
                }
                
                # Try to get error message
                try:
                    result["error"] = response.json()
                except:
                    result["error"] = response.text[:200] + "..." if len(response.text) > 200 else response.text
            
            self.test_results.append(result)
            return success, response.json() if success and response.headers.get('content-type', '').startswith('application/json') else {}
            
        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.test_results.append({
                "name": name,
                "status": "ERROR",
                "error": str(e)
            })
            return False, {}

    def print_summary(self):
        """Print a summary of all test results"""
        print("\n" + "="*50)
        print(f"📊 TEST SUMMARY: {self.tests_passed}/{self.tests_run} tests passed")
        print("="*50)
        
        for result in self.test_results:
            status_icon = "✅" if result["status"] == "PASSED" else "❌"
            print(f"{status_icon} {result['name']}")
            
            if result["status"] != "PASSED":
                if "expected" in result and "actual" in result:
                    print(f"   Expected: {result['expected']}, Got: {result['actual']}")
                if "error" in result:
                    print(f"   Error: {result['error']}")
            
            print("-"*50)

def test_news_api(tester):
    """Test the News API endpoints"""
    print("\n📰 TESTING NEWS API ENDPOINTS")
    print("="*50)
    
    # Get all news articles
    success, all_articles = tester.run_test(
        "Get All News Articles",
        "GET",
        "api/news",
        200
    )
    
    if success and all_articles:
        print(f"Found {len(all_articles)} news articles")
        
        # Get news categories
        success, categories = tester.run_test(
            "Get News Categories",
            "GET",
            "api/news/categories/list",
            200
        )
        
        if success and categories:
            print(f"Found {len(categories)} news categories:")
            for cat in categories:
                print(f"  - {cat['category']}: {cat['count']} articles")
            
            # Filter news by category
            if len(categories) > 0:
                test_category = categories[0]['category']
                tester.run_test(
                    f"Filter News by Category: {test_category}",
                    "GET",
                    "api/news",
                    200,
                    params={"category": test_category}
                )
        
        # Get individual news article
        if len(all_articles) > 0:
            article_id = all_articles[0]['id']
            tester.run_test(
                f"Get Individual News Article (ID: {article_id})",
                "GET",
                f"api/news/{article_id}",
                200
            )
            
            # Test invalid article ID
            tester.run_test(
                "Get Invalid News Article",
                "GET",
                "api/news/invalid-id-12345",
                404
            )

def test_investment_api(tester):
    """Test the Investment API endpoints with focus on expanded stock coverage"""
    print("\n💹 TESTING INVESTMENT API ENDPOINTS")
    print("="*50)
    
    # Test 1: Get investment summary
    success, summary = tester.run_test(
        "Get Investment Summary",
        "GET",
        "api/investments/summary",
        200
    )
    
    if success and summary:
        # Verify the summary data matches expanded requirements
        print("\nInvestment Summary Data:")
        print(f"Total Recommendations: {summary['total_recommendations']}")
        print(f"BUY Recommendations: {summary['recommendations_by_type']['BUY']}")
        print(f"HOLD Recommendations: {summary['recommendations_by_type']['HOLD']}")
        print(f"SELL Recommendations: {summary['recommendations_by_type']['SELL']}")
        print(f"Stocks Count: {summary['assets_by_type']['stocks']}")
        print(f"Indices Count: {summary['assets_by_type']['indices']}")
        print(f"Commodities Count: {summary['assets_by_type']['commodities']}")
        
        # Verify expanded requirements
        expanded_checks = {
            "Total 46 recommendations": summary['total_recommendations'] == 46,
            "33 BUY recommendations": summary['recommendations_by_type']['BUY'] == 33,
            "12 HOLD recommendations": summary['recommendations_by_type']['HOLD'] == 12,
            "1 SELL recommendation": summary['recommendations_by_type']['SELL'] == 1,
            "39 Stocks": summary['assets_by_type']['stocks'] == 39,
            "3 Indices": summary['assets_by_type']['indices'] == 3,
            "4 Commodities": summary['assets_by_type']['commodities'] == 4
        }
        
        print("\nExpanded Coverage Requirements Check:")
        for check, result in expanded_checks.items():
            print(f"{'✅' if result else '❌'} {check}")
    
    # Test 2: Get investment asset types
    success, asset_types = tester.run_test(
        "Get Investment Asset Types",
        "GET",
        "api/investments/types/list",
        200
    )
    
    if success and asset_types:
        print(f"\nFound {len(asset_types)} asset types:")
        for asset_type in asset_types:
            print(f"  - {asset_type['asset_type']}: {asset_type['count']} investments")
    
    # Test 3: Get all investment recommendations
    success, all_investments = tester.run_test(
        "Get All Investment Recommendations",
        "GET",
        "api/investments",
        200
    )
    
    if success and all_investments:
        print(f"\nFound {len(all_investments)} investment recommendations")
        
        # Check for required stocks by category
        tech_giants = ["AAPL", "NVDA", "MSFT", "GOOGL", "AMZN", "META", "AMD", "CRM", "ORCL", "ADBE", "IBM"]
        financial_services = ["JPM", "BAC", "WFC", "GS", "V", "AXP", "MA"]
        healthcare_leaders = ["UNH", "JNJ", "PFE", "ABBV", "TMO"]
        consumer_brands = ["KO", "WMT", "NKE", "SBUX", "DIS", "HD"]
        energy = ["XOM", "CVX"]
        industrials = ["BA", "CAT"]
        communication = ["NFLX", "T", "VZ"]
        utilities = ["NEE"]
        automotive = ["TSLA"]
        
        required_indices = ["SPY", "QQQ", "IWM"]
        required_commodities = ["GLD", "SLV", "USO", "BTC-USD"]
        
        found_stocks = [inv["symbol"] for inv in all_investments if inv["asset_type"] == "stock"]
        found_indices = [inv["symbol"] for inv in all_investments if inv["asset_type"] == "index"]
        found_commodities = [inv["symbol"] for inv in all_investments if inv["asset_type"] == "commodity"]
        
        # Check Technology Giants
        print("\nTechnology Giants Check:")
        for stock in tech_giants:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
        
        # Check Financial Services
        print("\nFinancial Services Check:")
        for stock in financial_services:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
        
        # Check Healthcare Leaders
        print("\nHealthcare Leaders Check:")
        for stock in healthcare_leaders:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
        
        # Check Consumer Brands
        print("\nConsumer Brands Check:")
        for stock in consumer_brands:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
        
        # Check Other Sectors
        print("\nEnergy Sector Check:")
        for stock in energy:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
            
        print("\nIndustrials Sector Check:")
        for stock in industrials:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
            
        print("\nCommunication Sector Check:")
        for stock in communication:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
            
        print("\nUtilities Sector Check:")
        for stock in utilities:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
            
        print("\nAutomotive Sector Check:")
        for stock in automotive:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
            
        print("\nRequired Indices Check:")
        for index in required_indices:
            print(f"{'✅' if index in found_indices else '❌'} {index}")
            
        print("\nRequired Commodities Check:")
        for commodity in required_commodities:
            print(f"{'✅' if commodity in found_commodities else '❌'} {commodity}")
        
        # Check for sectors
        required_sectors = [
            "Technology", "Financial Services", "Healthcare", "Consumer Discretionary", 
            "Energy", "Industrials", "Communication Services", "Utilities", "Automotive",
            "Diversified", "Precious Metals", "Energy", "Cryptocurrency"
        ]
        
        found_sectors = set()
        for inv in all_investments:
            if inv.get("sector"):
                found_sectors.add(inv["sector"])
        
        print("\nRequired Sectors Check:")
        for sector in required_sectors:
            print(f"{'✅' if sector in found_sectors else '❌'} {sector}")
        
        # Test 4: Filter investments by asset type
        for asset_type in ["stock", "index", "commodity"]:
            success, filtered_investments = tester.run_test(
                f"Filter Investments by Asset Type: {asset_type}",
                "GET",
                "api/investments",
                200,
                params={"asset_type": asset_type}
            )
            
            if success:
                print(f"Found {len(filtered_investments)} {asset_type} investments")
        
        # Test 5: Get individual investment recommendation
        if len(all_investments) > 0:
            # Get a stock recommendation
            stock_rec = next((inv for inv in all_investments if inv["asset_type"] == "stock"), None)
            if stock_rec:
                success, stock_detail = tester.run_test(
                    f"Get Stock Investment Detail (ID: {stock_rec['id']})",
                    "GET",
                    f"api/investments/{stock_rec['id']}",
                    200
                )
                
                if success:
                    # Check for enhanced data in the stock detail
                    has_technical_indicators = stock_detail.get("technical_indicators") is not None
                    key_factors_count = len(stock_detail.get("key_factors", []))
                    analysis_length = len(stock_detail.get("analysis", ""))
                    
                    print("\nStock Detail Enhanced Data Check:")
                    print(f"{'✅' if has_technical_indicators else '❌'} Has technical indicators")
                    print(f"{'✅' if key_factors_count >= 6 else '❌'} Has 6+ key factors ({key_factors_count})")
                    print(f"{'✅' if analysis_length > 300 else '❌'} Has detailed analysis ({analysis_length} chars)")
            
            # Get a commodity recommendation
            commodity_rec = next((inv for inv in all_investments if inv["asset_type"] == "commodity"), None)
            if commodity_rec:
                tester.run_test(
                    f"Get Commodity Investment Detail (ID: {commodity_rec['id']})",
                    "GET",
                    f"api/investments/{commodity_rec['id']}",
                    200
                )
            
            # Test invalid investment ID
            tester.run_test(
                "Get Invalid Investment Recommendation",
                "GET",
                "api/investments/invalid-id-12345",
                404
            )

def test_investment_qa_api(tester):
    """Test the Investment Q&A API endpoints with expanded stock coverage"""
    print("\n🤖 TESTING INVESTMENT Q&A API ENDPOINTS")
    print("="*50)
    
    # Test 1: Ask about a specific stock (AAPL)
    success, aapl_response = tester.run_test(
        "Ask about AAPL",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Should I buy AAPL?", "user_id": "test_user"}
    )
    
    if success and aapl_response:
        print("\nAAPL Question Response Analysis:")
        # Check if the response contains key elements
        contains_buy_rec = "BUY" in aapl_response["answer"]
        contains_target_price = "$" in aapl_response["answer"] and "target price" in aapl_response["answer"].lower()
        contains_aapl_symbol = "AAPL" in aapl_response["relevant_symbols"]
        confidence_score = aapl_response["confidence"]
        has_sources = len(aapl_response["sources"]) > 0
        
        print(f"{'✅' if contains_buy_rec else '❌'} Contains BUY recommendation")
        print(f"{'✅' if contains_target_price else '❌'} Contains target price")
        print(f"{'✅' if contains_aapl_symbol else '❌'} References AAPL symbol")
        print(f"{'✅' if confidence_score >= 0.5 else '❌'} Has confidence score ({confidence_score})")
        print(f"{'✅' if has_sources else '❌'} Has sources")
    
    # Test 2: Ask about Adobe (ADBE)
    success, adbe_response = tester.run_test(
        "Ask about Adobe",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "What's Adobe's outlook?", "user_id": "test_user"}
    )
    
    if success and adbe_response:
        print("\nAdobe Question Response Analysis:")
        # Check if the response contains key elements
        contains_buy_rec = "BUY" in adbe_response["answer"]
        contains_adbe_symbol = "ADBE" in adbe_response["relevant_symbols"]
        
        print(f"{'✅' if contains_buy_rec else '❌'} Contains BUY recommendation")
        print(f"{'✅' if contains_adbe_symbol else '❌'} References ADBE symbol")
    
    # Test 3: Ask about Boeing (BA)
    success, ba_response = tester.run_test(
        "Ask about Boeing risk",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "How risky is Boeing?", "user_id": "test_user"}
    )
    
    if success and ba_response:
        print("\nBoeing Risk Question Response Analysis:")
        # Check if the response contains key elements
        contains_high_risk = "HIGH" in ba_response["answer"]
        contains_ba_symbol = "BA" in ba_response["relevant_symbols"]
        
        print(f"{'✅' if contains_high_risk else '❌'} Mentions HIGH risk level")
        print(f"{'✅' if contains_ba_symbol else '❌'} References BA symbol")
    
    # Test 4: Ask about Nike (NKE)
    success, nke_response = tester.run_test(
        "Ask about Nike",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Is Nike a good investment?", "user_id": "test_user"}
    )
    
    if success and nke_response:
        print("\nNike Question Response Analysis:")
        # Check if the response contains key elements
        contains_buy_rec = "BUY" in nke_response["answer"]
        contains_nke_symbol = "NKE" in nke_response["relevant_symbols"]
        
        print(f"{'✅' if contains_buy_rec else '❌'} Contains BUY recommendation")
        print(f"{'✅' if contains_nke_symbol else '❌'} References NKE symbol")
    
    # Test 5: Ask about Disney (DIS)
    success, dis_response = tester.run_test(
        "Ask about Disney",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "What do you think about Disney?", "user_id": "test_user"}
    )
    
    if success and dis_response:
        print("\nDisney Question Response Analysis:")
        # Check if the response contains key elements
        contains_analysis = len(dis_response["answer"]) > 100
        contains_dis_symbol = "DIS" in dis_response["relevant_symbols"]
        
        print(f"{'✅' if contains_analysis else '❌'} Contains detailed analysis")
        print(f"{'✅' if contains_dis_symbol else '❌'} References DIS symbol")
    
    # Test 6: Ask about Oracle (ORCL)
    success, orcl_response = tester.run_test(
        "Ask about Oracle",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Should I invest in Oracle?", "user_id": "test_user"}
    )
    
    if success and orcl_response:
        print("\nOracle Question Response Analysis:")
        # Check if the response contains key elements
        contains_recommendation = any(word in orcl_response["answer"] for word in ["BUY", "HOLD", "SELL"])
        contains_orcl_symbol = "ORCL" in orcl_response["relevant_symbols"]
        
        print(f"{'✅' if contains_recommendation else '❌'} Contains recommendation")
        print(f"{'✅' if contains_orcl_symbol else '❌'} References ORCL symbol")
    
    # Test 7: Ask about tech stocks
    success, tech_response = tester.run_test(
        "Ask about tech stocks",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "What tech stocks do you recommend?", "user_id": "test_user"}
    )
    
    if success and tech_response:
        print("\nTech Stocks Question Response Analysis:")
        # Check if the response contains key elements
        tech_giants = ["AAPL", "NVDA", "MSFT", "GOOGL", "AMZN", "META", "AMD", "CRM", "ORCL", "ADBE", "IBM"]
        mentioned_tech_stocks = [symbol for symbol in tech_giants if symbol in tech_response["answer"]]
        
        print(f"{'✅' if len(mentioned_tech_stocks) >= 3 else '❌'} Lists multiple tech stocks ({len(mentioned_tech_stocks)})")
        print(f"Tech stocks mentioned: {', '.join(mentioned_tech_stocks)}")
    
    # Test 8: Ask about financial sector
    success, financial_response = tester.run_test(
        "Ask about financial sector",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Show me financial sector options", "user_id": "test_user"}
    )
    
    if success and financial_response:
        print("\nFinancial Sector Question Response Analysis:")
        # Check if the response contains key elements
        financial_stocks = ["JPM", "BAC", "WFC", "GS", "V", "AXP", "MA"]
        mentioned_financial_stocks = [symbol for symbol in financial_stocks if symbol in financial_response["answer"]]
        
        print(f"{'✅' if len(mentioned_financial_stocks) >= 2 else '❌'} Lists multiple financial stocks ({len(mentioned_financial_stocks)})")
        print(f"Financial stocks mentioned: {', '.join(mentioned_financial_stocks)}")
    
    # Test 9: Ask about healthcare investments
    success, healthcare_response = tester.run_test(
        "Ask about healthcare investments",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "What about healthcare investments?", "user_id": "test_user"}
    )
    
    if success and healthcare_response:
        print("\nHealthcare Investments Question Response Analysis:")
        # Check if the response contains key elements
        healthcare_stocks = ["UNH", "JNJ", "PFE", "ABBV", "TMO"]
        mentioned_healthcare_stocks = [symbol for symbol in healthcare_stocks if symbol in healthcare_response["answer"]]
        
        print(f"{'✅' if len(mentioned_healthcare_stocks) >= 2 else '❌'} Lists multiple healthcare stocks ({len(mentioned_healthcare_stocks)})")
        print(f"Healthcare stocks mentioned: {', '.join(mentioned_healthcare_stocks)}")
    
    # Test 10: Ask about consumer stocks
    success, consumer_response = tester.run_test(
        "Ask about consumer stocks",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Any good consumer stocks?", "user_id": "test_user"}
    )
    
    if success and consumer_response:
        print("\nConsumer Stocks Question Response Analysis:")
        # Check if the response contains key elements
        consumer_stocks = ["KO", "WMT", "NKE", "SBUX", "DIS", "HD"]
        mentioned_consumer_stocks = [symbol for symbol in consumer_stocks if symbol in consumer_response["answer"]]
        
        print(f"{'✅' if len(mentioned_consumer_stocks) >= 2 else '❌'} Lists multiple consumer stocks ({len(mentioned_consumer_stocks)})")
        print(f"Consumer stocks mentioned: {', '.join(mentioned_consumer_stocks)}")
    
    # Test 11: Ask about portfolio diversification
    success, portfolio_response = tester.run_test(
        "Ask about portfolio diversification",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "How should I build a diversified portfolio?", "user_id": "test_user"}
    )
    
    if success and portfolio_response:
        print("\nPortfolio Diversification Question Response Analysis:")
        # Check if the response contains key elements
        contains_sectors = "sector" in portfolio_response["answer"].lower()
        contains_multiple_sectors = sum(1 for sector in ["Technology", "Financial", "Healthcare", "Consumer", "Energy"] if sector in portfolio_response["answer"]) >= 3
        
        print(f"{'✅' if contains_sectors else '❌'} Discusses sectors")
        print(f"{'✅' if contains_multiple_sectors else '❌'} References multiple sectors")
    
    # Test 12: Ask about top stock picks
    success, top_picks_response = tester.run_test(
        "Ask about top stock picks",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "What are your top 10 stock picks?", "user_id": "test_user"}
    )
    
    if success and top_picks_response:
        print("\nTop Stock Picks Question Response Analysis:")
        # Check if the response contains key elements
        contains_multiple_stocks = len(top_picks_response["relevant_symbols"]) >= 5
        
        print(f"{'✅' if contains_multiple_stocks else '❌'} Lists multiple stocks ({len(top_picks_response['relevant_symbols'])})")
        print(f"Stocks mentioned: {', '.join(top_picks_response['relevant_symbols'])}")
    
    # Test 13: Ask about strongest sectors
    success, sectors_response = tester.run_test(
        "Ask about strongest sectors",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Which sectors look strongest?", "user_id": "test_user"}
    )
    
    if success and sectors_response:
        print("\nStrongest Sectors Question Response Analysis:")
        # Check if the response contains key elements
        contains_multiple_sectors = sum(1 for sector in ["Technology", "Financial", "Healthcare", "Consumer", "Energy"] if sector in sectors_response["answer"]) >= 2
        
        print(f"{'✅' if contains_multiple_sectors else '❌'} Analyzes multiple sectors")
    
    # Test 14: Stock comparison - Apple vs Microsoft
    success, comparison_response = tester.run_test(
        "Compare Apple vs Microsoft",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Should I buy Apple or Microsoft?", "user_id": "test_user"}
    )
    
    if success and comparison_response:
        print("\nApple vs Microsoft Comparison Analysis:")
        # Check if the response contains key elements
        contains_aapl = "AAPL" in comparison_response["answer"]
        contains_msft = "MSFT" in comparison_response["answer"]
        contains_comparison = any(word in comparison_response["answer"].lower() for word in ["versus", "compared", "comparison", "vs"])
        
        print(f"{'✅' if contains_aapl else '❌'} Mentions AAPL")
        print(f"{'✅' if contains_msft else '❌'} Mentions MSFT")
        print(f"{'✅' if contains_comparison else '❌'} Provides comparison")
    
    # Test 15: Stock comparison - Netflix vs Disney
    success, streaming_response = tester.run_test(
        "Compare Netflix vs Disney",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Netflix vs Disney for streaming exposure?", "user_id": "test_user"}
    )
    
    if success and streaming_response:
        print("\nNetflix vs Disney Comparison Analysis:")
        # Check if the response contains key elements
        contains_nflx = "NFLX" in streaming_response["answer"]
        contains_dis = "DIS" in streaming_response["answer"]
        contains_streaming = "streaming" in streaming_response["answer"].lower()
        
        print(f"{'✅' if contains_nflx else '❌'} Mentions NFLX")
        print(f"{'✅' if contains_dis else '❌'} Mentions DIS")
        print(f"{'✅' if contains_streaming else '❌'} Discusses streaming business")
    
    # Test 16: Stock comparison - JPMorgan vs Bank of America
    success, banks_response = tester.run_test(
        "Compare JPMorgan vs Bank of America",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "JPMorgan vs Bank of America?", "user_id": "test_user"}
    )
    
    if success and banks_response:
        print("\nJPMorgan vs Bank of America Comparison Analysis:")
        # Check if the response contains key elements
        contains_jpm = "JPM" in banks_response["answer"]
        contains_bac = "BAC" in banks_response["answer"]
        
        print(f"{'✅' if contains_jpm else '❌'} Mentions JPM")
        print(f"{'✅' if contains_bac else '❌'} Mentions BAC")
    
    # Test 17: Thematic investment - AI stocks
    success, ai_stocks_response = tester.run_test(
        "Ask about AI stocks",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Best AI stocks to buy?", "user_id": "test_user"}
    )
    
    if success and ai_stocks_response:
        print("\nAI Stocks Question Response Analysis:")
        # Check if the response contains key elements
        ai_related_stocks = ["NVDA", "MSFT", "GOOGL", "META"]
        mentioned_ai_stocks = [symbol for symbol in ai_related_stocks if symbol in ai_stocks_response["answer"]]
        
        print(f"{'✅' if len(mentioned_ai_stocks) >= 2 else '❌'} Mentions AI-related stocks ({len(mentioned_ai_stocks)})")
        print(f"AI stocks mentioned: {', '.join(mentioned_ai_stocks)}")
    
    # Test 18: Thematic investment - Digital transformation
    success, digital_response = tester.run_test(
        "Ask about digital transformation stocks",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Which stocks benefit from digital transformation?", "user_id": "test_user"}
    )
    
    if success and digital_response:
        print("\nDigital Transformation Stocks Analysis:")
        # Check if the response contains key elements
        digital_stocks = ["MSFT", "AMZN", "CRM", "ADBE"]
        mentioned_digital_stocks = [symbol for symbol in digital_stocks if symbol in digital_response["answer"]]
        
        print(f"{'✅' if len(mentioned_digital_stocks) >= 2 else '❌'} Mentions digital transformation stocks ({len(mentioned_digital_stocks)})")
    
    # Test 19: Thematic investment - Dividend stocks
    success, dividend_response = tester.run_test(
        "Ask about dividend stocks",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Best dividend stocks?", "user_id": "test_user"}
    )
    
    if success and dividend_response:
        print("\nDividend Stocks Question Analysis:")
        # Check if the response contains key elements
        dividend_stocks = ["JNJ", "KO", "XOM", "VZ", "T", "IBM"]
        mentioned_dividend_stocks = [symbol for symbol in dividend_stocks if symbol in dividend_response["answer"]]
        
        print(f"{'✅' if len(mentioned_dividend_stocks) >= 2 else '❌'} Mentions dividend stocks ({len(mentioned_dividend_stocks)})")
    
    # Test 20: Risk-based question - Safest stocks
    success, safe_stocks_response = tester.run_test(
        "Ask about safest stocks",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "What are the safest large-cap stocks?", "user_id": "test_user"}
    )
    
    if success and safe_stocks_response:
        print("\nSafest Stocks Question Analysis:")
        # Check if the response contains key elements
        contains_low_risk = "LOW" in safe_stocks_response["answer"]
        
        print(f"{'✅' if contains_low_risk else '❌'} Mentions LOW risk stocks")
    
    # Test 21: Risk-based question - High-growth opportunities
    success, growth_response = tester.run_test(
        "Ask about high-growth opportunities",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Show me high-growth opportunities?", "user_id": "test_user"}
    )
    
    if success and growth_response:
        print("\nHigh-Growth Opportunities Question Analysis:")
        # Check if the response contains key elements
        growth_stocks = ["NVDA", "TSLA", "META", "AMD"]
        mentioned_growth_stocks = [symbol for symbol in growth_stocks if symbol in growth_response["answer"]]
        
        print(f"{'✅' if len(mentioned_growth_stocks) >= 1 else '❌'} Mentions growth stocks ({len(mentioned_growth_stocks)})")
    
    # Test 22: Risk-based question - Volatile stocks
    success, volatile_response = tester.run_test(
        "Ask about volatile stocks",
        "POST",
        "api/investments/ask",
        200,
        data={"question": "Most volatile stocks in your coverage?", "user_id": "test_user"}
    )
    
    if success and volatile_response:
        print("\nVolatile Stocks Question Analysis:")
        # Check if the response contains key elements
        contains_high_risk = "HIGH" in volatile_response["answer"]
        volatile_stocks = ["TSLA", "NVDA", "AMD", "BTC-USD"]
        mentioned_volatile_stocks = [symbol for symbol in volatile_stocks if symbol in volatile_response["answer"]]
        
        print(f"{'✅' if contains_high_risk else '❌'} Mentions HIGH risk")
        print(f"{'✅' if len(mentioned_volatile_stocks) >= 1 else '❌'} Identifies volatile options ({len(mentioned_volatile_stocks)})")

def main():
    # Get the backend URL from the frontend .env file
    backend_url = "https://f331cb83-b6cd-4e1b-a4a7-993eac227251.preview.emergentagent.com"
    
    print(f"Testing API at: {backend_url}")
    tester = APITester(backend_url)
    
    # Test 1: Root API endpoint
    tester.run_test(
        "Root API Endpoint",
        "GET",
        "api",
        200
    )
    
    # Test 2: Status API endpoint
    tester.run_test(
        "Status API Endpoint",
        "POST",
        "api/status",
        200,
        data={"client_name": "API Tester"}
    )
    
    # Test the News API endpoints
    test_news_api(tester)
    
    # Test the Investment API endpoints with focus on expanded stock coverage
    test_investment_api(tester)
    
    # Test the Investment Q&A API endpoints with expanded stock coverage
    test_investment_qa_api(tester)
    
    # Print summary of all tests
    tester.print_summary()
    
    # Return success status
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())
