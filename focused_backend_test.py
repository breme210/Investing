import requests
import json
import sys

# Get the backend URL from the frontend .env file
with open('/app/frontend/.env', 'r') as f:
    for line in f:
        if line.startswith('REACT_APP_BACKEND_URL='):
            BACKEND_URL = line.strip().split('=')[1].strip('"\'')
            break

# Ensure we have a backend URL
if not BACKEND_URL:
    print("Error: Could not find REACT_APP_BACKEND_URL in frontend/.env")
    sys.exit(1)

# Add /api prefix to all endpoints
API_URL = f"{BACKEND_URL}/api"

print(f"Testing backend API at: {API_URL}")
print("=" * 80)

def test_endpoint(method, endpoint, data=None, expected_status=200, description=""):
    """Test an API endpoint and return the response"""
    url = f"{API_URL}{endpoint}"
    print(f"\nTesting {method} {url}")
    print(f"Description: {description}")
    
    try:
        if method.upper() == "GET":
            response = requests.get(url)
        elif method.upper() == "POST":
            response = requests.post(url, json=data)
        else:
            print(f"Unsupported method: {method}")
            return None
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code != expected_status:
            print(f"❌ Expected status {expected_status}, got {response.status_code}")
            return None
        
        try:
            json_response = response.json()
            print(f"Response: {json.dumps(json_response, indent=2)}")
            return json_response
        except ValueError:
            print(f"Response is not JSON: {response.text[:100]}...")
            return response.text
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return None

def run_tests():
    """Run all API tests"""
    test_results = {}
    
    # Test 1: Basic health check endpoint
    print("\n1. Testing basic health check endpoint")
    health_response = test_endpoint(
        "GET", 
        "/", 
        expected_status=200,
        description="Basic health check endpoint"
    )
    test_results["health_check"] = health_response is not None and "message" in health_response
    
    # Test 2: Investment summary endpoint
    print("\n2. Testing investment summary endpoint")
    summary_response = test_endpoint(
        "GET", 
        "/investments/summary", 
        expected_status=200,
        description="Get investment summary statistics"
    )
    test_results["investment_summary"] = summary_response is not None and "total_recommendations" in summary_response
    
    # Test 3: AI Q&A endpoint
    print("\n3. Testing AI Q&A endpoint")
    question_data = {
        "question": "Should I buy AAPL?",
        "user_id": "test_user"
    }
    qa_response = test_endpoint(
        "POST", 
        "/investments/ask", 
        data=question_data,
        expected_status=200,
        description="AI-powered investment Q&A"
    )
    test_results["investment_qa"] = qa_response is not None and "answer" in qa_response
    
    # Test 4: News endpoints
    print("\n4. Testing news endpoints")
    news_response = test_endpoint(
        "GET", 
        "/news", 
        expected_status=200,
        description="Get news articles"
    )
    test_results["news"] = news_response is not None and isinstance(news_response, list)
    
    categories_response = test_endpoint(
        "GET", 
        "/news/categories/list", 
        expected_status=200,
        description="Get news categories"
    )
    test_results["news_categories"] = categories_response is not None and isinstance(categories_response, list)
    
    # Test 5: Investments endpoint
    print("\n5. Testing investments endpoint")
    investments_response = test_endpoint(
        "GET", 
        "/investments", 
        expected_status=200,
        description="Get investment recommendations"
    )
    test_results["investments"] = investments_response is not None and isinstance(investments_response, list)
    
    # Print summary
    print("\n" + "=" * 80)
    print("TEST RESULTS SUMMARY")
    print("=" * 80)
    
    all_passed = True
    for test_name, result in test_results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        if not result:
            all_passed = False
        print(f"{test_name}: {status}")
    
    print("\nOverall Status:", "✅ ALL TESTS PASSED" if all_passed else "❌ SOME TESTS FAILED")
    print("=" * 80)
    
    return test_results, all_passed

if __name__ == "__main__":
    results, passed = run_tests()
    sys.exit(0 if passed else 1)