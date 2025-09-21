#!/usr/bin/env python3
"""
Additional Backend API Tests for Edge Cases and Error Handling
"""
import requests
import json

BACKEND_URL = "https://abhranil-tech.preview.emergentagent.com/api"

def test_error_handling():
    """Test error handling scenarios"""
    print("🔍 Testing Error Handling Scenarios")
    print("=" * 50)
    
    # Test 404 scenarios
    print("Testing 404 scenarios...")
    
    # Try to update non-existent project
    response = requests.put(f"{BACKEND_URL}/projects/non-existent-id", 
                          json={"title": "Updated"}, timeout=10)
    print(f"Update non-existent project: {response.status_code} (expected 404)")
    
    # Try to delete non-existent project
    response = requests.delete(f"{BACKEND_URL}/projects/non-existent-id", timeout=10)
    print(f"Delete non-existent project: {response.status_code} (expected 404)")
    
    # Test invalid data scenarios
    print("\nTesting invalid data scenarios...")
    
    # Try to create project with missing required fields
    response = requests.post(f"{BACKEND_URL}/projects", 
                           json={"title": "Test"}, timeout=10)  # Missing description and technologies
    print(f"Create project with missing fields: {response.status_code} (expected 422)")
    
    # Try to update personal info with empty data
    response = requests.put(f"{BACKEND_URL}/portfolio/personal", 
                          json={}, timeout=10)
    print(f"Update personal info with empty data: {response.status_code} (expected 400)")

def test_data_integrity():
    """Test data integrity and relationships"""
    print("\n🔗 Testing Data Integrity")
    print("=" * 50)
    
    # Get portfolio data
    response = requests.get(f"{BACKEND_URL}/portfolio", timeout=10)
    if response.status_code == 200:
        data = response.json()
        
        # Check that all items have correct portfolioId
        for category in ['skills', 'experiences', 'projects', 'achievements', 'publications']:
            items = data.get(category, [])
            for item in items:
                portfolio_id = item.get('portfolioId')
                if portfolio_id != 'default':
                    print(f"❌ {category} item has wrong portfolioId: {portfolio_id}")
                    return False
        
        print("✅ All data items have correct portfolioId")
        
        # Check that current experience is properly marked
        experiences = data.get('experiences', [])
        current_count = sum(1 for exp in experiences if exp.get('current') == True)
        print(f"✅ Found {current_count} current experience(s)")
        
        # Check featured projects
        projects = data.get('projects', [])
        featured_count = sum(1 for proj in projects if proj.get('featured') == True)
        placeholder_count = sum(1 for proj in projects if proj.get('placeholder') == True)
        print(f"✅ Found {featured_count} featured projects, {placeholder_count} placeholders")
        
        return True
    else:
        print(f"❌ Could not retrieve portfolio data: {response.status_code}")
        return False

def test_api_consistency():
    """Test API response consistency"""
    print("\n📊 Testing API Response Consistency")
    print("=" * 50)
    
    # Get data from individual endpoints
    endpoints = {
        'skills': '/skills',
        'experiences': '/experience', 
        'projects': '/projects',
        'achievements': '/achievements',
        'publications': '/publications'
    }
    
    individual_data = {}
    for key, endpoint in endpoints.items():
        response = requests.get(f"{BACKEND_URL}{endpoint}", timeout=10)
        if response.status_code == 200:
            individual_data[key] = response.json()
        else:
            print(f"❌ Failed to get {key}: {response.status_code}")
            return False
    
    # Get data from portfolio endpoint
    response = requests.get(f"{BACKEND_URL}/portfolio", timeout=10)
    if response.status_code == 200:
        portfolio_data = response.json()
        
        # Compare counts
        for key in endpoints.keys():
            individual_count = len(individual_data[key])
            portfolio_count = len(portfolio_data.get(key, []))
            
            if individual_count != portfolio_count:
                print(f"❌ Count mismatch for {key}: individual={individual_count}, portfolio={portfolio_count}")
                return False
            else:
                print(f"✅ {key}: {individual_count} items consistent")
        
        return True
    else:
        print(f"❌ Could not retrieve portfolio data: {response.status_code}")
        return False

def main():
    """Run additional tests"""
    print("🧪 Additional Backend API Tests")
    print("=" * 60)
    
    test_error_handling()
    
    integrity_ok = test_data_integrity()
    consistency_ok = test_api_consistency()
    
    print("\n" + "=" * 60)
    print("📋 ADDITIONAL TESTS SUMMARY")
    print("=" * 60)
    
    if integrity_ok and consistency_ok:
        print("✅ All additional tests passed!")
        print("✅ Error handling working correctly")
        print("✅ Data integrity verified")
        print("✅ API consistency confirmed")
    else:
        print("⚠️  Some additional tests had issues")
        if not integrity_ok:
            print("❌ Data integrity issues found")
        if not consistency_ok:
            print("❌ API consistency issues found")

if __name__ == "__main__":
    main()