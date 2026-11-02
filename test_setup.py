#!/usr/bin/env python3
"""
Test script to verify the Smart Water Quality Monitoring application setup.
This script tests that all components are working correctly.
"""

import sys
import os
import json
from pathlib import Path

def test_backend():
    """Test the Flask backend"""
    print("Testing Flask Backend...")
    
    # Test if we can import the Flask app
    try:
        sys.path.append(os.path.join(os.getcwd(), 'backend'))
        from app import app, water_quality_data
        print("✅ Flask app imports successfully")
    except ImportError as e:
        print(f"❌ Failed to import Flask app: {e}")
        return False
    
    # Test data structure
    if len(water_quality_data) == 8:
        print(f"✅ Contains {len(water_quality_data)} areas as expected")
    else:
        print(f"❌ Expected 8 areas, got {len(water_quality_data)}")
        return False
    
    # Test data format
    sample_area = list(water_quality_data.keys())[0]
    sample_data = water_quality_data[sample_area]
    expected_keys = {'area', 'turbidity', 'ph', 'tds', 'status'}
    
    if set(sample_data.keys()) == expected_keys:
        print("✅ Data structure is correct")
    else:
        print(f"❌ Data structure mismatch. Expected: {expected_keys}, Got: {set(sample_data.keys())}")
        return False
    
    print("✅ Backend tests passed!\n")
    return True

def test_frontend():
    """Test the React frontend"""
    print("Testing React Frontend...")
    
    # Check if build was successful
    build_dir = Path('frontend/build')
    if build_dir.exists() and (build_dir / 'index.html').exists():
        print("✅ React build exists")
    else:
        print("❌ React build not found")
        return False
    
    # Check critical files exist
    src_dir = Path('frontend/src')
    critical_files = [
        'App.tsx',
        'components/Header.tsx',
        'components/AreaSelector.tsx',
        'components/WaterQualityTable.tsx',
        'components/Footer.tsx',
        'types/WaterQuality.ts'
    ]
    
    missing_files = []
    for file_path in critical_files:
        if not (src_dir / file_path).exists():
            missing_files.append(file_path)
    
    if not missing_files:
        print("✅ All React components exist")
    else:
        print(f"❌ Missing files: {missing_files}")
        return False
    
    # Check CSS files
    css_files = [
        'App.css',
        'components/Header.css',
        'components/AreaSelector.css',
        'components/WaterQualityTable.css',
        'components/Footer.css'
    ]
    
    missing_css = []
    for css_file in css_files:
        if not (src_dir / css_file).exists():
            missing_css.append(css_file)
    
    if not missing_css:
        print("✅ All CSS files exist")
    else:
        print(f"❌ Missing CSS files: {missing_css}")
        return False
    
    print("✅ Frontend tests passed!\n")
    return True

def test_project_structure():
    """Test overall project structure"""
    print("Testing Project Structure...")
    
    required_files = [
        'README.md',
        'backend/app.py',
        'backend/requirements.txt',
        'frontend/package.json',
        'frontend/src/App.tsx'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if not missing_files:
        print("✅ All required files exist")
    else:
        print(f"❌ Missing required files: {missing_files}")
        return False
    
    print("✅ Project structure tests passed!\n")
    return True

def main():
    """Run all tests"""
    print("🧪 Testing Smart Water Quality Monitoring Application")
    print("=" * 60)
    
    tests = [
        test_project_structure,
        test_backend,
        test_frontend
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("=" * 60)
    if all(results):
        print("🎉 ALL TESTS PASSED! Your application is ready to run.")
        print("\n📋 Next steps:")
        print("1. Start the backend: cd backend && python app.py")
        print("2. In a new terminal, start frontend: cd frontend && npm start")
        print("3. Open http://localhost:3000 in your browser")
        return 0
    else:
        print("❌ Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
