import subprocess
import time
import os
import sys

def launch_furmark():
    """Launch FurMark for GPU stress testing"""
    # Update this path to your FurMark installation
    furmark_path = r"C:\Program Files (x86)\Geeks3D\Furmark\FurMark.exe"
    
    # FurMark command line arguments for multi-GPU testing
    args = [
        furmark_path,
        "/nogui",      # Run without GUI
        "/msaa=8",     # 8x Anti-aliasing
        "/width=1920", # Resolution width
        "/height=1080",# Resolution height
        "/gpu_temp",   # Monitor GPU temperature
        "/max_time=0", # Run indefinitely
        "/multi_gpu"   # Enable multi-GPU testing
    ]
    
    try:
        subprocess.Popen(args)
        print("FurMark launched successfully")
    except Exception as e:
        print(f"Error launching FurMark: {e}")

def launch_prime95():
    """Launch Prime95 for CPU stress testing"""
    # Update this path to your Prime95 installation
    prime95_path = r"C:\Program Files\Prime95\prime95.exe"
    
    try:
        subprocess.Popen([prime95_path, "-t"])  # -t flag for torture test
        print("Prime95 launched successfully")
    except Exception as e:
        print(f"Error launching Prime95: {e}")

def main():
    print("Starting stress test suite...")
    
    # Launch FurMark for GPU stress
    launch_furmark()
    time.sleep(5)  # Wait for FurMark to initialize
    
    # Launch Prime95 for CPU stress
    launch_prime95()
    
    print("\nBoth stress tests are running.")
    print("Press Ctrl+C to stop the tests...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping stress tests...")
        # Kill FurMark and Prime95 processes
        os.system("taskkill /f /im FurMark.exe")
        os.system("taskkill /f /im prime95.exe")

if __name__ == "__main__":
    main()
