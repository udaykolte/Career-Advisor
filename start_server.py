#!/usr/bin/env python3
"""
Startup script for the Career & Skills Advisor web application
"""
import sys
import os
import webbrowser
import time
from threading import Timer

def print_welcome():
    print("🚀 Career & Skills Advisor Web Application")
    print("=" * 60)
    print("🎆 Modern Interactive Career Assessment Tool")
    print("=" * 60)
    print()
    print("✨ Features:")
    print("  🎯 Multi-step interactive assessment")
    print("  📊 Visual results with charts and timelines")
    print("  📚 Curated learning resources")
    print("  📱 Mobile-friendly responsive design")
    print()
    print("💻 Server starting at: http://localhost:5000")
    print()
    print("💡 Instructions:")
    print("  1. Wait for 'Running on http://127.0.0.1:5000' message")
    print("  2. Your browser will open automatically")
    print("  3. Fill out the career assessment form")
    print("  4. Get your personalized career guidance!")
    print()
    print("  🛱 Press Ctrl+C to stop the server")
    print("=" * 60)
    print()

def open_browser():
    """Open browser after a short delay"""
    time.sleep(2)  # Wait for server to start
    try:
        webbrowser.open('http://localhost:5000')
        print("🌍 Browser opened automatically!")
    except:
        print("🌍 Please open http://localhost:5000 in your browser")

def main():
    print_welcome()
    
    try:
        # Import and test the app
        from app import app
        
        # Start browser opening timer
        Timer(1.0, open_browser).start()
        
        # Run the Flask application
        print("🔄 Starting Flask server...")
        app.run(debug=True, host='127.0.0.1', port=5000, use_reloader=False)
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("🔧 Please ensure all files are in the correct location:")
        print("   - app.py (main Flask application)")
        print("   - src/career_advisor.py (career logic)")
        print("   - templates/ folder with HTML files")
        print("   - static/ folder with CSS and JS")
    except KeyboardInterrupt:
        print("\n\n👋 Career Advisor server stopped.")
        print("🚀 Thanks for using our career guidance tool!")
        print("🌟 Come back anytime to reassess your career path.")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure Flask is installed: py -m pip install flask")
        print("2. Ensure you're in the project directory")
        print("3. Check that port 5000 is not in use")
        print("4. Run 'py test_app.py' to diagnose issues")
        print("\n🎆 Alternative: Run 'py app.py' directly")

if __name__ == "__main__":
    main()
