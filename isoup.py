import os
import shutil
import sys
from parts import hasher, announcer, extractor, screenshotter, cleanup

def delete_tmp_contents():
    tmp_dir = 'tmp'
    try:
        # Iterate over all files and directories in tmp directory
        for item in os.listdir(tmp_dir):
            item_path = os.path.join(tmp_dir, item)
            # Check if item is a file or directory and delete it
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print(f"Deleted contents of '{tmp_dir}' folder.")
    except OSError as e:
        print(f"Error deleting contents of '{tmp_dir}' folder: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 isoup.py /path/to/iso_file -tk abbreviationsforannounces")
        sys.exit(1)
    
    iso_file = sys.argv[1]
    abbreviations = sys.argv[2:]
    
    # Delete contents of tmp folder
    delete_tmp_contents()
    
    # Run hasher.py to create base torrent
    print("Running hasher.py...")
    hasher.create_base_torrent(iso_file)
    
    # Run announcer.py to add announce URLs and rename torrent
    print("Running announcer.py...")
    announcer.add_announces_and_rename(iso_file, abbreviations)
    
    # Run extractor.py to extract ISO content
    print("Running extractor.py...")
    extractor.extract_iso(iso_file)
    
    # Run screenshotter.py to take screenshots
    num_screenshots = 5  # Example: Replace with actual number from user input
    print(f"Running screenshotter.py to take {num_screenshots} screenshots...")
    screenshotter.take_screenshots(num_screenshots)
    
    # Run cleanup.py to delete contents of scratch folder
    print("Running cleanup.py to delete contents of scratch folder...")
    cleanup.clean_scratch()

if __name__ == "__main__":
    main()
