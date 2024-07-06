import os
import shutil

def add_announces_and_rename(base_torrent_path, trackers_file):
    # Check if the base torrent file exists
    if not os.path.exists(base_torrent_path):
        print(f"Error: Base torrent file '{base_torrent_path}' not found.")
        return
    
    # Read trackers from file
    trackers = read_trackers(trackers_file)
    if not trackers:
        print(f"No trackers found in '{trackers_file}'.")
        return
    
    # Process each tracker
    for abbrev, url in trackers.items():
        # Formulate new torrent file name with abbreviation
        new_torrent_name = f"{abbrev}_{os.path.basename(base_torrent_path)}"
        new_torrent_path = os.path.join(os.path.dirname(base_torrent_path), new_torrent_name)
        
        # Check if the renamed torrent file already exists
        if os.path.exists(new_torrent_path):
            print(f"Torrent file '{new_torrent_path}' already exists. Skipping.")
            continue
        
        # Copy base torrent to new location with abbreviation
        try:
            shutil.copy(base_torrent_path, new_torrent_path)
            print(f"Created torrent file '{new_torrent_path}'.")
        except Exception as e:
            print(f"Error creating '{new_torrent_path}': {e}")

def read_trackers(trackers_file):
    trackers = {}
    try:
        with open(trackers_file, 'r') as f:
            for line in f:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    abbrev = parts[0].strip()
                    url = parts[1].strip()
                    trackers[abbrev] = url
    except FileNotFoundError:
        print(f"Error: Trackers file '{trackers_file}' not found.")
    return trackers

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python announcer.py <base_torrent_path> <trackers_file>")
        sys.exit(1)
    
    base_torrent_path = sys.argv[1]
    trackers_file = sys.argv[2]
    
    add_announces_and_rename(base_torrent_path, trackers_file)
