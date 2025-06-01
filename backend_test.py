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
    """Test the Investment API endpoints with focus on Phase 1 enhancements"""
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
        # Verify the summary data matches Phase 1 requirements
        print("\nInvestment Summary Data:")
        print(f"Total Recommendations: {summary['total_recommendations']}")
        print(f"BUY Recommendations: {summary['recommendations_by_type']['BUY']}")
        print(f"HOLD Recommendations: {summary['recommendations_by_type']['HOLD']}")
        print(f"SELL Recommendations: {summary['recommendations_by_type']['SELL']}")
        print(f"Stocks Count: {summary['assets_by_type']['stocks']}")
        print(f"Indices Count: {summary['assets_by_type']['indices']}")
        print(f"Commodities Count: {summary['assets_by_type']['commodities']}")
        
        # Verify Phase 1 requirements
        phase1_checks = {
            "Total 20 recommendations": summary['total_recommendations'] == 20,
            "15 BUY recommendations": summary['recommendations_by_type']['BUY'] == 15,
            "4 HOLD recommendations": summary['recommendations_by_type']['HOLD'] == 4,
            "1 SELL recommendation": summary['recommendations_by_type']['SELL'] == 1,
            "13 Stocks": summary['assets_by_type']['stocks'] == 13,
            "3 Indices": summary['assets_by_type']['indices'] == 3,
            "4 Commodities": summary['assets_by_type']['commodities'] == 4
        }
        
        print("\nPhase 1 Requirements Check:")
        for check, result in phase1_checks.items():
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
        
        # Check for required stocks
        required_stocks = ["AAPL", "NVDA", "META", "GOOGL", "MSFT", "AMZN", "TSLA", 
                          "CRM", "JPM", "BAC", "V", "UNH", "JNJ"]
        required_indices = ["SPY", "QQQ", "IWM"]
        required_commodities = ["GLD", "SLV", "USO", "BTC-USD"]
        
        found_stocks = [inv["symbol"] for inv in all_investments if inv["asset_type"] == "stock"]
        found_indices = [inv["symbol"] for inv in all_investments if inv["asset_type"] == "index"]
        found_commodities = [inv["symbol"] for inv in all_investments if inv["asset_type"] == "commodity"]
        
        print("\nRequired Stocks Check:")
        for stock in required_stocks:
            print(f"{'✅' if stock in found_stocks else '❌'} {stock}")
            
        print("\nRequired Indices Check:")
        for index in required_indices:
            print(f"{'✅' if index in found_indices else '❌'} {index}")
            
        print("\nRequired Commodities Check:")
        for commodity in required_commodities:
            print(f"{'✅' if commodity in found_commodities else '❌'} {commodity}")
        
        # Check for sectors
        required_sectors = ["Technology", "Financial Services", "Healthcare", "Automotive", 
                           "Consumer Discretionary", "Diversified", "Precious Metals", 
                           "Energy", "Cryptocurrency"]
        
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

def main():
    # Get the backend URL from the frontend .env file
    backend_url = "https://201e85b7-6e5c-4c05-8b17-d262a900ba36.preview.emergentagent.com"
    
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
    
    # Test the Investment API endpoints with focus on Phase 1 enhancements
    test_investment_api(tester)
    
    # Print summary of all tests
    tester.print_summary()
    
    # Return success status
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())