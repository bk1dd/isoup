import os
import sys
import shutil  # Add this import for shutil module

def add_announces_and_rename(base_torrent_path, trackers_file):
    # Check if the base torrent file exists
    if not os.path.isfile(base_torrent_path):
        print(f"Error: Base torrent file '{base_torrent_path}' not found.")
        return
    
    # Read trackers from file
    trackers = read_trackers(trackers_file)
    
    # Add trackers to the base torrent file
    for tracker_abbr, announce_url in trackers.items():
        new_torrent_name = f"{tracker_abbr}_{os.path.basename(base_torrent_path)}"
        new_torrent_path = os.path.join(os.path.dirname(base_torrent_path), new_torrent_name)
        
        # Copy base torrent to new path
        try:
            shutil.copy(base_torrent_path, new_torrent_path)
        except IOError as e:
            print(f"Error copying torrent file: {e}")
            continue
        
        # Add announce URL to the new torrent file
        command = f"transmission-edit -a {announce_url} {new_torrent_path}"
        os.system(command)
        
        print(f"Added announce '{announce_url}' to '{new_torrent_path}'")

def read_trackers(trackers_file):
    trackers = {}
    try:
        with open(trackers_file, 'r') as f:
            for line in f:
                if line.strip():  # Check if the line is not empty
                    parts = line.strip().split(':', 1)
                    if len(parts) == 2:
                        tracker_abbr = parts[0].strip()
                        announce_url = parts[1].strip()
                        trackers[tracker_abbr] = announce_url
                    else:
                        print(f"Invalid line in trackers file: {line}")
    except FileNotFoundError:
        print(f"Trackers file '{trackers_file}' not found.")
    return trackers

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 announcer.py <base_torrent_path> <trackers_file>")
        sys.exit(1)
    
    base_torrent_path = sys.argv[1]
    trackers_file = sys.argv[2]
    
    add_announces_and_rename(base_torrent_path, trackers_file)

if __name__ == "__main__":
    main()
