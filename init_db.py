#!/usr/bin/env python
"""
Automated database initialization script.
Runs all populate scripts in the correct order.
"""

import subprocess
import sys

# List of populate scripts to run in order
POPULATE_SCRIPTS = [
    'populate.py',
    'populate_blog.py',
    'populate_challenges.py',
    'populate_ratings.py',
    'populate_blog_and_videos.py'
]

def run_script(script_name):
    """Run a populate script and report status."""
    print(f"\n{'='*60}")
    print(f"Running: {script_name}")
    print('='*60)
    
    try:
        result = subprocess.run([sys.executable, script_name], check=True)
        print(f"✓ {script_name} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {script_name} failed with error code {e.returncode}")
        return False
    except FileNotFoundError:
        print(f"✗ {script_name} not found")
        return False

def main():
    """Run all populate scripts."""
    print("\n" + "="*60)
    print("DATABASE INITIALIZATION")
    print("="*60)
    
    failed_scripts = []
    
    for script in POPULATE_SCRIPTS:
        if not run_script(script):
            failed_scripts.append(script)
    
    print("\n" + "="*60)
    print("INITIALIZATION COMPLETE")
    print("="*60)
    
    if failed_scripts:
        print(f"\n⚠ {len(failed_scripts)} script(s) failed:")
        for script in failed_scripts:
            print(f"  - {script}")
        return 1
    else:
        print("\n✓ All scripts completed successfully!")
        print("\nYour database is now fully populated.")
        print("Run 'python run.py' to start the application.")
        return 0

if __name__ == '__main__':
    sys.exit(main())
