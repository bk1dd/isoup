import os
import sys
import subprocess
import shutil
import parts.announcer as announcer

def delete_tmp_folder_contents():
    tmp_folder = os.path.join(os.getcwd(), "tmp")
    for root, dirs, files in os.walk(tmp_folder):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))
    print("Deleted contents of 'tmp' folder.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 isoup.py /path/to/target_file.iso -tk <tracker abbreviations>")
        sys.exit(1)

    iso_file = sys.argv[1]
    tracker_abbrs = sys.argv[3:]
    
    # Delete tmp folder contents
    delete_tmp_folder_contents()
    
    # Run hasher.py
    print("Running hasher.py...")
    subprocess.run(['python3', 'parts/hasher.py', iso_file])

    # Run announcer.py
    print("Running announcer.py...")
    announcer.add_announces_and_rename(iso_file, tracker_abbrs)

    # Cleanup (if necessary)
    print("Cleaning up temporary directory...")
    # Add your cleanup code here if needed

if __name__ == "__main__":
    main()
