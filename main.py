"""
Root Launcher for AI Writing - Smart Air Writing System
"""

import sys
import os

# Add air-writing-recognition to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "air-writing-recognition"))

if __name__ == "__main__":
    from main import SmartAirWritingSystem
    app = SmartAirWritingSystem()
    app.run()
