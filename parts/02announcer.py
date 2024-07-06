import os
import sys
import subprocess
import shutil

def add_announces_and_rename(base_torrent_path, trackers_file):
    # Read announce URLs and abbreviations from trackers.txt
    announce_urls = {}
    with open(trackers_file, 'r') as f:
        for line in f:
            abbreviation, announce_url = line.strip().split(':')
            announce_urls[abbreviation.strip()] = announce_url.strip()

    # Iterate over announce URLs and create new torrents
    for abbreviation, announce_url in announce_urls.items():
        # Create new torrent file name with abbreviation
        new_torrent_name = f"{abbreviation}_{os.path.basename(base_torrent_path)}"
        new_torrent_path = os.path.join(os.path.dirname(base_torrent_path), new_torrent_name)

        # Copy base torrent to new torrent file
        shutil.copyfile(base_torrent_path, new_torrent_path)

        # Add announce URL to new torrent file
        mktorrent_command = [
            "mktorrent",
            "-v",  # Verbose output
            "-a", announce_url,  # Add announce URL
            "-o", new_torrent_path,  # Output path for the new torrent file
            base_torrent_path  # Path to the base torrent file
        ]

        # Execute mktorrent command
        try:
            subprocess.run(mktorrent_command, check=True)
            print(f"Successfully added announce '{announce_url}' to '{new_torrent_path}'")
        except subprocess.CalledProcessError as e:
            print(f"Error adding announce to '{new_torrent_path}': {e}")
            sys.exit(1)

if __name__ == "__main__":
    # Check if base torrent file path and trackers file path arguments are provided
    if len(sys.argv) < 3:
        print("Usage: python3 02announcer.py /path/to/base.torrent /path/to/trackers.txt")
        sys.exit(1)

    # Get base torrent file path and trackers file path from command-line arguments
    base_torrent_path = sys.argv[1]
    trackers_file = sys.argv[2]

    # Call function to add announces and rename torrents
    add_announces_and_rename(base_torrent_path, trackers_file)
