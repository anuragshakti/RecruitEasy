import subprocess
import sys

def install_dependencies():
    try:
        subprocess.call([sys.executable, '-m', 'pip', 'install', 'tkinter', 'sqlite3'])  # Add other dependencies as needed
        print("Dependencies installed successfully.")
    except Exception as e:
        print(f"Error installing dependencies: {e}")

if __name__ == "__main__":
    install_dependencies()
