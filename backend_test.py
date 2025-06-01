import requests
import unittest
import sys
from datetime import datetime

class NewsAPITester:
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

def main():
    # Get the backend URL from the frontend .env file
    backend_url = "https://201e85b7-6e5c-4c05-8b17-d262a900ba36.preview.emergentagent.com"
    
    print(f"Testing API at: {backend_url}")
    tester = NewsAPITester(backend_url)
    
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
    
    # Test 3: Get all news articles
    success, all_articles = tester.run_test(
        "Get All News Articles",
        "GET",
        "api/news",
        200
    )
    
    if success and all_articles:
        print(f"Found {len(all_articles)} news articles")
        
        # Test 4: Get news categories
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
            
            # Test 5: Filter news by category
            if len(categories) > 0:
                test_category = categories[0]['category']
                tester.run_test(
                    f"Filter News by Category: {test_category}",
                    "GET",
                    "api/news",
                    200,
                    params={"category": test_category}
                )
        
        # Test 6: Get individual news article
        if len(all_articles) > 0:
            article_id = all_articles[0]['id']
            tester.run_test(
                f"Get Individual News Article (ID: {article_id})",
                "GET",
                f"api/news/{article_id}",
                200
            )
            
            # Test 7: Test invalid article ID
            tester.run_test(
                "Get Invalid News Article",
                "GET",
                "api/news/invalid-id-12345",
                404
            )
    
    # Print summary of all tests
    tester.print_summary()
    
    # Return success status
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())