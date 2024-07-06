import sys
import os

def add_announces_and_rename(base_torrent_path, trackers_file):
    # Check if the trackers_file exists
    if not os.path.exists(trackers_file):
        print(f"Error: Trackers file '{trackers_file}' not found.")
        return
    
    # Read announce URLs from trackers_file
    announces = []
    with open(trackers_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('#') or not line:
                continue
            abbrev, url = line.split(':', 1)
            abbrev = abbrev.strip()
            url = url.strip()
            announces.append((abbrev, url))

    # Append announces to base torrent name
    base_torrent_dir = os.path.dirname(base_torrent_path)
    base_torrent_name = os.path.basename(base_torrent_path)
    for abbrev, url in announces:
        new_torrent_name = f"{abbrev}_{base_torrent_name}"
        new_torrent_path = os.path.join(base_torrent_dir, new_torrent_name)
        
        # Copy base torrent to new name with appended abbreviation
        os.rename(base_torrent_path, new_torrent_path)
        print(f"Added announce: {url}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 announcer.py /path/to/base.torrent /path/to/trackers.txt")
        sys.exit(1)
    
    base_torrent_path = sys.argv[1]
    trackers_file = sys.argv[2]
    
    add_announces_and_rename(base_torrent_path, trackers_file)
