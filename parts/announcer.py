import os
import shutil

def add_announces_and_rename(base_torrent_path, trackers_file):
    # Check if trackers_file exists
    if not os.path.isfile(trackers_file):
        print(f"Error: Trackers file '{trackers_file}' not found.")
        return
    
    # Read abbreviations and URLs from trackers_file
    with open(trackers_file, 'r') as f:
        for line in f:
            if line.strip():  # Check if line is not empty
                parts = line.strip().split(':')
                if len(parts) == 2:
                    abbreviation, announce_url = parts
                    # Append abbreviation to the base torrent filename
                    new_torrent_path = os.path.join(os.path.dirname(base_torrent_path),
                                                    f"{abbreviation}_{os.path.basename(base_torrent_path)}")
                    
                    # Copy base torrent to new filename with abbreviation
                    try:
                        shutil.copy(base_torrent_path, new_torrent_path)
                        print(f"Created torrent '{os.path.basename(new_torrent_path)}' with announce URL: {announce_url}")
                    except Exception as e:
                        print(f"Error creating torrent with abbreviation '{abbreviation}': {e}")
                else:
                    print(f"Invalid line format in trackers file: {line}")

def main():
    import sys
    if len(sys.argv) < 3:
        print("Usage: python announcer.py /path/to/base_torrent_file /path/to/trackers.txt")
        sys.exit(1)
    
    base_torrent_path = sys.argv[1]
    trackers_file = sys.argv[2]
    add_announces_and_rename(base_torrent_path, trackers_file)

if __name__ == "__main__":
    main()
