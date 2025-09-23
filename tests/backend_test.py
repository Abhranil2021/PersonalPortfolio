#!/usr/bin/env python3
"""
Comprehensive Backend API Testing for Portfolio System
Tests all CRUD operations and data integrity
"""
import requests
import json
import sys
import os
from datetime import datetime

# Get backend URL from environment
BACKEND_URL = "https://abhranil-tech.preview.emergentagent.com/api"

class PortfolioAPITester:
    def __init__(self):
        self.base_url = BACKEND_URL
        self.test_results = []
        self.created_items = {
            'projects': [],
            'skills': [],
            'experiences': [],
            'achievements': [],
            'publications': []
        }
        
    def log_result(self, test_name, success, message, response_data = None):
        """Log test result"""
        result = {
            'test': test_name,
            'success': success,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        if response_data:
            result['response_data'] = response_data
        self.test_results.append(result)
        
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status}: {test_name} - {message}")
        
    def test_api_health(self):
        """Test basic API health"""
        try:
            response = requests.get(f"{self.base_url}/", timeout = 10)
            if response.status_code == 200:
                data = response.json()
                self.log_result("API Health Check", True, f"API is running: {data.get('message', 'OK')}")
                return True
            else:
                self.log_result("API Health Check", False, f"API returned status {response.status_code}")
                return False
        except Exception as e:
            self.log_result("API Health Check", False, f"API connection failed: {str(e)}")
            return False
    
    def test_get_portfolio(self):
        """Test GET /api/portfolio - Most important endpoint"""
        try:
            response = requests.get(f"{self.base_url}/portfolio", timeout = 10)
            if response.status_code == 200:
                data = response.json()
                
                # Verify data structure
                required_keys = ['portfolio', 'skills', 'experiences', 'projects', 'achievements', 'publications']
                missing_keys = [key for key in required_keys if key not in data]
                
                if missing_keys:
                    self.log_result("Get Portfolio", False, f"Missing keys in response: {missing_keys}")
                    return False
                
                # Verify personal info
                portfolio = data.get('portfolio', {})
                personal = portfolio.get('personal', {})
                if personal.get('name') != 'ABHRANIL DAS':
                    self.log_result("Get Portfolio", False, f"Expected name 'ABHRANIL DAS', got '{personal.get('name')}'")
                    return False
                
                # Count data items
                skills_count = len(data.get('skills', []))
                exp_count = len(data.get('experiences', []))
                proj_count = len(data.get('projects', []))
                ach_count = len(data.get('achievements', []))
                pub_count = len(data.get('publications', []))
                
                self.log_result("Get Portfolio", True, 
                    f"Portfolio data retrieved successfully - Skills: {skills_count}, "
                    f"Experience: {exp_count}, Projects: {proj_count}, "
                    f"Achievements: {ach_count}, Publications: {pub_count}",
                    {'counts': {'skills': skills_count, 'experiences': exp_count, 
                               'projects': proj_count, 'achievements': ach_count, 'publications': pub_count}})
                return True
                
            elif response.status_code == 404:
                self.log_result("Get Portfolio", False, "Portfolio not found - data may not be migrated")
                return False
            else:
                self.log_result("Get Portfolio", False, f"Unexpected status code: {response.status_code}")
                return False
                
        except Exception as e:
            self.log_result("Get Portfolio", False, f"Request failed: {str(e)}")
            return False
    
    def test_get_skills(self):
        """Test GET /api/skills"""
        try:
            response = requests.get(f"{self.base_url}/skills", timeout = 10)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    expected_categories = ["Programming", "ML Frameworks", "AI Specializations", "Data & Analytics", "LLM & GenAI Tools"]
                    found_categories = [skill.get('title') for skill in data]
                    
                    self.log_result("Get Skills", True, 
                        f"Retrieved {len(data)} skill categories: {found_categories}")
                    return True
                else:
                    self.log_result("Get Skills", False, "Response is not a list")
                    return False
            else:
                self.log_result("Get Skills", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Get Skills", False, f"Request failed: {str(e)}")
            return False
    
    def test_get_experience(self):
        """Test GET /api/experience"""
        try:
            response = requests.get(f"{self.base_url}/experience", timeout = 10)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    # Look for current role at Adani AI Labs
                    current_roles = [exp for exp in data if exp.get('current') == True]
                    adani_role = [exp for exp in data if 'Adani AI Labs' in exp.get('company', '')]
                    
                    self.log_result("Get Experience", True, 
                        f"Retrieved {len(data)} experiences, {len(current_roles)} current, "
                        f"Adani role found: {len(adani_role) > 0}")
                    return True
                else:
                    self.log_result("Get Experience", False, "Response is not a list")
                    return False
            else:
                self.log_result("Get Experience", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Get Experience", False, f"Request failed: {str(e)}")
            return False
    
    def test_get_projects(self):
        """Test GET /api/projects"""
        try:
            response = requests.get(f"{self.base_url}/projects", timeout = 10)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    featured_projects = [proj for proj in data if proj.get('featured') == True]
                    placeholder_projects = [proj for proj in data if proj.get('placeholder') == True]
                    
                    self.log_result("Get Projects", True, 
                        f"Retrieved {len(data)} projects, {len(featured_projects)} featured, "
                        f"{len(placeholder_projects)} placeholders")
                    return True
                else:
                    self.log_result("Get Projects", False, "Response is not a list")
                    return False
            else:
                self.log_result("Get Projects", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Get Projects", False, f"Request failed: {str(e)}")
            return False
    
    def test_get_achievements(self):
        """Test GET /api/achievements"""
        try:
            response = requests.get(f"{self.base_url}/achievements", timeout = 10)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    kaggle_achievements = [ach for ach in data if 'Kaggle' in ach.get('title', '')]
                    
                    self.log_result("Get Achievements", True, 
                        f"Retrieved {len(data)} achievements, Kaggle achievements: {len(kaggle_achievements)}")
                    return True
                else:
                    self.log_result("Get Achievements", False, "Response is not a list")
                    return False
            else:
                self.log_result("Get Achievements", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Get Achievements", False, f"Request failed: {str(e)}")
            return False
    
    def test_get_publications(self):
        """Test GET /api/publications"""
        try:
            response = requests.get(f"{self.base_url}/publications", timeout = 10)
            if response.status_code == 200:
                data = response.json()
                if isinstance(data, list):
                    ieee_pubs = [pub for pub in data if 'IEEE' in pub.get('publication', '')]
                    
                    self.log_result("Get Publications", True, 
                        f"Retrieved {len(data)} publications, IEEE publications: {len(ieee_pubs)}")
                    return True
                else:
                    self.log_result("Get Publications", False, "Response is not a list")
                    return False
            else:
                self.log_result("Get Publications", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Get Publications", False, f"Request failed: {str(e)}")
            return False
    
    def test_get_export(self):
        """Test GET /api/export"""
        try:
            response = requests.get(f"{self.base_url}/export", timeout = 10)
            if response.status_code == 200:
                data = response.json()
                # Should have same structure as portfolio endpoint
                required_keys = ['portfolio', 'skills', 'experiences', 'projects', 'achievements', 'publications']
                missing_keys = [key for key in required_keys if key not in data]
                
                if missing_keys:
                    self.log_result("Export Data", False, f"Missing keys in export: {missing_keys}")
                    return False
                
                self.log_result("Export Data", True, "Export endpoint working correctly")
                return True
            else:
                self.log_result("Export Data", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Export Data", False, f"Request failed: {str(e)}")
            return False
    
    def test_update_personal_info(self):
        """Test PUT /api/portfolio/personal"""
        try:
            update_data = {
                "tagline": "AI/ML Specialist • Data Scientist • Machine Learning Engineer (Updated)"
            }
            
            response = requests.put(
                f"{self.base_url}/portfolio/personal", 
                json = update_data, 
                timeout = 10
            )
            
            if response.status_code == 200:
                # Verify the update by getting portfolio
                verify_response = requests.get(f"{self.base_url}/portfolio", timeout = 10)
                if verify_response.status_code == 200:
                    data = verify_response.json()
                    updated_tagline = data.get('portfolio', {}).get('personal', {}).get('tagline', '')
                    
                    if "(Updated)" in updated_tagline:
                        self.log_result("Update Personal Info", True, "Personal info updated successfully")
                        return True
                    else:
                        self.log_result("Update Personal Info", False, "Update not reflected in data")
                        return False
                else:
                    self.log_result("Update Personal Info", False, "Could not verify update")
                    return False
            else:
                self.log_result("Update Personal Info", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Update Personal Info", False, f"Request failed: {str(e)}")
            return False
    
    def test_update_about_section(self):
        """Test PUT /api/portfolio/about"""
        try:
            update_data = {
                "description": "AI/ML specialist with a strong foundation in data science and machine learning engineering. Updated description for testing purposes."
            }
            
            response = requests.put(
                f"{self.base_url}/portfolio/about", 
                json = update_data, 
                timeout = 10
            )
            
            if response.status_code == 200:
                self.log_result("Update About Section", True, "About section updated successfully")
                return True
            else:
                self.log_result("Update About Section", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Update About Section", False, f"Request failed: {str(e)}")
            return False
    
    def test_create_project(self):
        """Test POST /api/projects"""
        try:
            project_data = {
                "title": "Test Project for API Testing",
                "description": "This is a test project created during API testing to verify CRUD operations.",
                "technologies": ["Python", "FastAPI", "MongoDB", "Testing"],
                "github": "https://github.com/test/test-project",
                "demo": "https://test-demo.com",
                "featured": False,
                "placeholder": True,
                "order": 999
            }
            
            response = requests.post(
                f"{self.base_url}/projects", 
                json = project_data, 
                timeout = 10
            )
            
            if response.status_code == 200:
                data = response.json()
                project_id = data.get('id')
                if project_id:
                    self.created_items['projects'].append(project_id)
                    self.log_result("Create Project", True, f"Project created with ID: {project_id}")
                    return True
                else:
                    self.log_result("Create Project", False, "No project ID returned")
                    return False
            else:
                self.log_result("Create Project", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Create Project", False, f"Request failed: {str(e)}")
            return False
    
    def test_update_project(self):
        """Test PUT /api/projects/{id}"""
        if not self.created_items['projects']:
            self.log_result("Update Project", False, "No project available to update")
            return False
            
        try:
            project_id = self.created_items['projects'][0]
            update_data = {
                "title": "Updated Test Project for API Testing",
                "description": "This project has been updated during API testing."
            }
            
            response = requests.put(
                f"{self.base_url}/projects/{project_id}", 
                json = update_data, 
                timeout = 10
            )
            
            if response.status_code == 200:
                self.log_result("Update Project", True, f"Project {project_id} updated successfully")
                return True
            else:
                self.log_result("Update Project", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Update Project", False, f"Request failed: {str(e)}")
            return False
    
    def test_delete_project(self):
        """Test DELETE /api/projects/{id}"""
        if not self.created_items['projects']:
            self.log_result("Delete Project", False, "No project available to delete")
            return False
            
        try:
            project_id = self.created_items['projects'][0]
            
            response = requests.delete(f"{self.base_url}/projects/{project_id}", timeout = 10)
            
            if response.status_code == 200:
                self.created_items['projects'].remove(project_id)
                self.log_result("Delete Project", True, f"Project {project_id} deleted successfully")
                return True
            else:
                self.log_result("Delete Project", False, f"Status code: {response.status_code}")
                return False
        except Exception as e:
            self.log_result("Delete Project", False, f"Request failed: {str(e)}")
            return False
    
    def test_data_migration_verification(self):
        """Verify that mock data was properly migrated"""
        try:
            response = requests.get(f"{self.base_url}/portfolio", timeout = 10)
            if response.status_code != 200:
                self.log_result("Data Migration Verification", False, "Could not retrieve portfolio data")
                return False
                
            data = response.json()
            
            # Check expected data counts
            expected_counts = {
                'skills': 5,  # 5 skill categories
                'experiences': 3,  # 3 experiences including current Adani role
                'projects': 5,  # 3 real + 2 placeholders
                'achievements': 3,  # 3 achievements
                'publications': 2  # 2 publications
            }
            
            actual_counts = {
                'skills': len(data.get('skills', [])),
                'experiences': len(data.get('experiences', [])),
                'projects': len(data.get('projects', [])),
                'achievements': len(data.get('achievements', [])),
                'publications': len(data.get('publications', []))
            }
            
            mismatches = []
            for key, expected in expected_counts.items():
                actual = actual_counts[key]
                if actual != expected:
                    mismatches.append(f"{key}: expected {expected}, got {actual}")
            
            if mismatches:
                self.log_result("Data Migration Verification", False, 
                    f"Data count mismatches: {', '.join(mismatches)}")
                return False
            
            # Check specific data integrity
            portfolio = data.get('portfolio', {})
            personal = portfolio.get('personal', {})
            
            if personal.get('name') != 'ABHRANIL DAS':
                self.log_result("Data Migration Verification", False, 
                    f"Wrong name: expected 'ABHRANIL DAS', got '{personal.get('name')}'")
                return False
            
            # Check for current Adani role
            experiences = data.get('experiences', [])
            current_roles = [exp for exp in experiences if exp.get('current') == True]
            adani_roles = [exp for exp in experiences if 'Adani AI Labs' in exp.get('company', '')]
            
            if len(current_roles) != 1:
                self.log_result("Data Migration Verification", False, 
                    f"Expected 1 current role, found {len(current_roles)}")
                return False
                
            if len(adani_roles) != 1:
                self.log_result("Data Migration Verification", False, 
                    f"Expected 1 Adani role, found {len(adani_roles)}")
                return False
            
            self.log_result("Data Migration Verification", True, 
                "All expected data found with correct structure and counts")
            return True
            
        except Exception as e:
            self.log_result("Data Migration Verification", False, f"Verification failed: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all tests in sequence"""
        print("🚀 Starting Portfolio Backend API Tests")
        print(f"Testing against: {self.base_url}")
        print("=" * 60)
        
        # Basic connectivity tests
        if not self.test_api_health():
            print("❌ API health check failed. Stopping tests.")
            return False
        
        # Core GET endpoint tests
        self.test_get_portfolio()
        self.test_get_skills()
        self.test_get_experience()
        self.test_get_projects()
        self.test_get_achievements()
        self.test_get_publications()
        self.test_get_export()
        
        # Data migration verification
        self.test_data_migration_verification()
        
        # CRUD operation tests
        self.test_update_personal_info()
        self.test_update_about_section()
        self.test_create_project()
        self.test_update_project()
        self.test_delete_project()
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for result in self.test_results if result['success'])
        failed = len(self.test_results) - passed
        
        print(f"Total Tests: {len(self.test_results)}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        
        if failed > 0:
            print("\n🔍 FAILED TESTS:")
            for result in self.test_results:
                if not result['success']:
                    print(f"   • {result['test']}: {result['message']}")
        
        return failed == 0

def main():
    """Main test execution"""
    tester = PortfolioAPITester()
    success = tester.run_all_tests()
    
    # Save detailed results
    with open('/app/test_results_detailed.json', 'w') as f:
        json.dump(tester.test_results, f, indent = 2)
    
    print(f"\n📝 Detailed results saved to: /app/test_results_detailed.json")
    
    if success:
        print("\n🎉 All tests passed! Portfolio API is working correctly.")
        sys.exit(0)
    else:
        print("\n⚠️  Some tests failed. Check the results above.")
        sys.exit(1)

if __name__ == "__main__":
    main()