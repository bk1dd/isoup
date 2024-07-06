import os
import shutil
import subprocess
import sys

def clear_scratch_folder():
    # Clear contents of the scratch folder
    scratch_folder = "scratch"
    for filename in os.listdir(scratch_folder):
        file_path = os.path.join(scratch_folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f"Error cleaning up {file_path}: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 isoup.py <iso_file_path> -tk <tracker_abbreviations>")
        sys.exit(1)
    
    iso_file = sys.argv[1]
    tracker_abbrs = sys.argv[3:]
    trackers_file = 'data/trackers.txt'
    
    clear_scratch_folder()
    
    # Run hasher.py
    print("Running hasher.py...")
    try:
        subprocess.run(['python3', 'parts/hasher.py', iso_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running hasher.py: {e}")
        sys.exit(1)
    
    # Run announcer.py
    print("Running announcer.py...")
    try:
        subprocess.run(['python3', 'parts/announcer.py', iso_file, trackers_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running announcer.py: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
