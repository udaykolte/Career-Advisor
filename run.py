#!/usr/bin/env python3
"""
Simple runner script for the Career & Skills Advisor application
"""

import sys
import os

# Add src directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

def main():
    """Main entry point"""
    try:
        from career_advisor import main as advisor_main
        advisor_main()
    except ImportError as e:
        print(f"Error importing application: {e}")
        print("Make sure you're running this from the project root.")
        return 1
    except Exception as e:
        print(f"Error starting application: {e}")
        return 1

if __name__ == '__main__':
    exit(main())