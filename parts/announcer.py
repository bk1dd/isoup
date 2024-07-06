import os
import shutil
import sys

def add_announces_and_rename(base_torrent_path, trackers_file):
    # Check if trackers_file exists
    if not os.path.exists(trackers_file):
        print(f"Error: Trackers file '{trackers_file}' not found.")
        return
    
    # Open trackers file and read announce URLs
    with open(trackers_file, 'r') as f:
        lines = f.readlines()
        announce_urls = [line.strip().split(':')[1] for line in lines if line.strip().startswith('AB')]
    
    if not announce_urls:
        print("Error: No announce URLs found in trackers file.")
        return
    
    # Extract torrent name from base_torrent_path
    torrent_name = os.path.basename(base_torrent_path)
    
    # Create new torrent name with abbreviations
    for line in lines:
        if line.strip().startswith('AB'):
            abbreviation = line.strip().split(':')[0]
            new_torrent_name = f"{abbreviation}_{torrent_name}"
            break
    
    # Set path for new torrent file in tmp folder
    tmp_folder = os.path.join('tmp', os.path.dirname(base_torrent_path))
    new_torrent_path = os.path.join(tmp_folder, new_torrent_name)
    
    # Copy base torrent file to new location with new name
    try:
        shutil.copy(base_torrent_path, new_torrent_path)
        print(f"Successfully copied base torrent to '{new_torrent_path}'.")
    except shutil.Error as e:
        print(f"Error copying torrent file: {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 announcer.py base_torrent_path trackers_file")
        sys.exit(1)
    
    base_torrent_path = sys.argv[1]
    trackers_file = sys.argv[2]
    
    add_announces_and_rename(base_torrent_path, trackers_file)

if __name__ == "__main__":
    main()
