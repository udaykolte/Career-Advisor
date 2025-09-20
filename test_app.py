#!/usr/bin/env python3
"""Complete test script for the Career & Skills Advisor web application"""

import sys
from app import app, WebCareerAdvisor

def test_career_advisor_logic():
    """Test the core career advisor logic"""
    print("🧠 Testing Career Advisor Logic...")
    
    advisor = WebCareerAdvisor()
    
    # Test form data processing
    test_form_data = {
        'name': 'Test User',
        'education': "Bachelor's Degree",
        'field': 'Computer Science',
        'skills': 'Python, JavaScript, Communication',
        'interests': 'I love programming and building web applications',
        'career_goals': 'I want to become a software developer',
        'timeline': '1 year'
    }
    
    try:
        # Process user data
        user_profile = advisor.process_user_data(test_form_data)
        print("✅ Form data processing: SUCCESS")
        
        # Get analysis results
        results = advisor.get_analysis_results()
        print("✅ Analysis results generation: SUCCESS")
        
        # Verify results structure
        required_keys = ['user_profile', 'strengths', 'career_suggestions', 'recommended_skills', 'resources', 'roadmap', 'advice']
        for key in required_keys:
            if key in results:
                print(f"✅ Results contain {key}: SUCCESS")
            else:
                print(f"❌ Results missing {key}: FAILED")
                return False
        
        print(f"✅ Found {len(results['career_suggestions'])} career suggestions")
        print(f"✅ Found {len(results['recommended_skills'])} recommended skills")
        print(f"✅ Found {len(results['resources'])} learning resources")
        
        return True
        
    except Exception as e:
        print(f"❌ Career advisor logic error: {e}")
        return False

def test_flask_routes():
    """Test Flask routes"""
    print("\n🌐 Testing Flask Routes...")
    
    client = app.test_client()
    
    try:
        # Test home page
        response = client.get('/')
        if response.status_code == 200:
            print("✅ Home page (GET /): SUCCESS")
        else:
            print(f"❌ Home page failed with status {response.status_code}")
            return False
        
        # Test about page
        response = client.get('/about')
        if response.status_code == 200:
            print("✅ About page (GET /about): SUCCESS")
        else:
            print(f"❌ About page failed with status {response.status_code}")
            return False
        
        # Test form submission
        test_data = {
            'name': 'Test User',
            'education': "Bachelor's Degree",
            'field': 'Computer Science',
            'skills': 'Python, JavaScript, Communication',
            'interests': 'I love programming and building web applications',
            'career_goals': 'I want to become a software developer',
            'timeline': '1 year'
        }
        
        response = client.post('/assess', data=test_data, follow_redirects=True)
        if response.status_code == 200:
            print("✅ Form submission (POST /assess): SUCCESS")
        else:
            print(f"❌ Form submission failed with status {response.status_code}")
            return False
        
        # Test results page (should work after form submission)
        with client.session_transaction() as sess:
            if 'results' in sess:
                response = client.get('/results')
                if response.status_code == 200:
                    print("✅ Results page (GET /results): SUCCESS")
                else:
                    print(f"❌ Results page failed with status {response.status_code}")
                    return False
        
        # Test session clear
        response = client.get('/clear')
        if response.status_code == 302:  # Should redirect
            print("✅ Session clear (GET /clear): SUCCESS")
        else:
            print(f"❌ Session clear failed with status {response.status_code}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Flask routes error: {e}")
        return False

def test_static_files():
    """Test static file serving"""
    print("\n📁 Testing Static Files...")
    
    client = app.test_client()
    
    try:
        # Test CSS file
        response = client.get('/static/css/style.css')
        if response.status_code == 200:
            print("✅ CSS file serving: SUCCESS")
        else:
            print(f"❌ CSS file failed with status {response.status_code}")
            return False
        
        # Test JavaScript file
        response = client.get('/static/js/app.js')
        if response.status_code == 200:
            print("✅ JavaScript file serving: SUCCESS")
        else:
            print(f"❌ JavaScript file failed with status {response.status_code}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Static files error: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Career & Skills Advisor Tests")
    print("=" * 50)
    
    tests = [
        ("Career Advisor Logic", test_career_advisor_logic),
        ("Flask Routes", test_flask_routes), 
        ("Static Files", test_static_files)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"\n✅ {test_name}: ALL TESTS PASSED")
            else:
                print(f"\n❌ {test_name}: SOME TESTS FAILED")
        except Exception as e:
            print(f"\n❌ {test_name}: ERROR - {e}")
    
    print("\n" + "=" * 50)
    print(f"🎯 TEST SUMMARY: {passed}/{total} test suites passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! Your application is ready to run!")
        print("\n🚀 To start the application:")
        print("   py start_server.py")
        print("   Then open: http://localhost:5000")
        return True
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)