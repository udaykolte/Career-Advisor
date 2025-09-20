#!/usr/bin/env python3
"""
Network startup script for the Career & Skills Advisor web application
Optimized for access from any device on the network
"""
import sys
import os
import webbrowser
import time
import socket
import subprocess
from threading import Timer

def get_local_ip():
    """Get the local IP address"""
    try:
        # Connect to a dummy address to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "Unable to detect"

def check_firewall():
    """Check if firewall rule exists"""
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'firewall', 'show', 'rule', 'name=CareerAdvisorApp'], 
                              capture_output=True, text=True)
        return "CareerAdvisorApp" in result.stdout
    except:
        return False

def create_firewall_rule():
    """Attempt to create firewall rule"""
    try:
        result = subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 
                               'name=CareerAdvisorApp', 'dir=in', 'protocol=TCP', 
                               'localport=5000', 'action=allow'], 
                               capture_output=True, text=True)
        return result.returncode == 0
    except:
        return False

def print_network_welcome():
    local_ip = get_local_ip()
    has_firewall_rule = check_firewall()
    
    print("🚀 Career & Skills Advisor - NETWORK MODE")
    print("=" * 75)
    print("🎆 Access from ANY device on your network!")
    print("=" * 75)
    print()
    
    print("✨ Features:")
    print("  🎯 Multi-step interactive assessment")
    print("  📊 Visual results with charts and timelines")  
    print("  📚 Curated learning resources")
    print("  📱 Mobile-friendly responsive design")
    print("  🌐 Works on phones, tablets, laptops, desktops")
    print()
    
    print("💻 Access URLs:")
    print(f"  📍 This Computer: http://localhost:5000")
    print(f"  🌐 Network URL:   http://{local_ip}:5000")
    print()
    
    print("📱 How to Access from Other Devices:")
    print("  1. Make sure all devices are on the SAME WiFi network")
    print(f"  2. Open any web browser on the device")
    print(f"  3. Type this URL: http://{local_ip}:5000")
    print("  4. Bookmark it for easy access!")
    print()
    
    print("🔒 Network Security Status:")
    if has_firewall_rule:
        print("  ✅ Windows Firewall: Configured for network access")
    else:
        print("  ⚠️  Windows Firewall: May block network access")
        print("     💡 If other devices can't connect, run as Administrator")
    print()
    
    print("📱 Devices that can access this:")
    print("  • Android phones and tablets")
    print("  • iPhones and iPads") 
    print("  • Windows laptops/PCs")
    print("  • Mac laptops/desktops")
    print("  • Any device with a web browser!")
    print()
    
    print("💡 Instructions:")
    print("  1. Wait for 'Running on http://0.0.0.0:5000' message")
    print("  2. Browser will open automatically on this computer")
    print(f"  3. Share this URL with others: http://{local_ip}:5000")
    print("  4. Everyone can take the career assessment!")
    print()
    
    print("  🛱 Press Ctrl+C to stop the server")
    print("=" * 75)
    print()

def open_browser():
    """Open browser after a short delay"""
    time.sleep(2)
    # Choose scheme based on presence of certs
    cert_dir = os.path.join(os.path.dirname(__file__), 'certs')
    cert_path = os.path.join(cert_dir, 'cert.pem')
    key_path = os.path.join(cert_dir, 'key.pem')
    scheme = 'https' if os.path.exists(cert_path) and os.path.exists(key_path) else 'http'
    try:
        webbrowser.open(f'{scheme}://localhost:5000')
        print("🌍 Browser opened automatically on this computer!")
        print("🔗 Share the network URL with other devices to let them access it too!")
    except:
        print(f"🌍 Please open {scheme}://localhost:5000 in your browser")

def main():
    print_network_welcome()
    
    # Try to create firewall rule automatically (will only work if running as admin)
    if not check_firewall():
        print("🔧 Attempting to configure Windows Firewall...")
        if create_firewall_rule():
            print("✅ Windows Firewall configured successfully!")
        else:
            print("⚠️  Could not configure Windows Firewall automatically")
            print("   💡 If other devices can't connect, restart as Administrator")
        print()
    
    try:
        # Import and test the app
        try:
            from backend.app import app
        except ImportError:
            from app import app
        
        # Determine SSL context if certs are present
        cert_dir = os.path.join(os.path.dirname(__file__), 'certs')
        cert_path = os.path.join(cert_dir, 'cert.pem')
        key_path = os.path.join(cert_dir, 'key.pem')
        ssl_ctx = None
        if os.path.exists(cert_path) and os.path.exists(key_path):
            ssl_ctx = (cert_path, key_path)
            print("🔐 HTTPS enabled: Using certificates from ./certs")
            print("   - cert:", cert_path)
            print("   - key :", key_path)
        else:
            print("ℹ️  No certificates found in ./certs — starting HTTP (port 5000)")
            print("   Create certs/cert.pem and certs/key.pem to enable HTTPS.")
        
        # Start browser opening timer
        Timer(1.0, open_browser).start()
        
        # Run the Flask application for network access
        print("🔄 Starting Flask server for network access...")
        print("🌐 Server accessible from any device on your network!")
        print()
        app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False, ssl_context=ssl_ctx)
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("🔧 Please ensure all files are in the correct location:")
        print("   - app.py (main Flask application)")
        print("   - src/career_advisor.py (career logic)")
        print("   - templates/ folder with HTML files")
        print("   - static/ folder with CSS and JS")
    except KeyboardInterrupt:
        print("\n\n👋 Career Advisor network server stopped.")
        print("🚀 Thanks for using our career guidance tool!")
        print("🌟 The application worked great across all your devices!")
    except Exception as e:
        print(f"\n❌ Error starting server: {e}")
        print("\n🔧 Troubleshooting:")
        print("1. Make sure Flask is installed: py -m pip install flask")
        print("2. Ensure you're in the project directory")
        print("3. Check that port 5000 is not in use")
        print("4. For network access issues, run as Administrator")
        print("5. Make sure all devices are on the same WiFi network")
        print("6. For HTTPS, generate certs in ./certs (see README HTTPS section)")

if __name__ == "__main__":
    main()
