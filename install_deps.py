
import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ Successfully installed {package}")
        return True
    except subprocess.CalledProcessError:
        print(f"✗ Failed to install {package}")
        return False

def main():
    """Install required packages."""
    print("Installing required dependencies...")
    
    packages = [
        "flask",
        "flask-sqlalchemy", 
        "google-generativeai",
        "python-dotenv",
        "requests"
    ]
    
    success_count = 0
    for package in packages:
        if install_package(package):
            success_count += 1
    
    print(f"\nInstallation complete: {success_count}/{len(packages)} packages installed successfully")
    
    if success_count == len(packages):
        print("✓ All dependencies installed successfully!")
        print("You can now run the application with: python main.py")
    else:
        print("⚠ Some packages failed to install. The app may not work correctly.")

if __name__ == "__main__":
    main()
