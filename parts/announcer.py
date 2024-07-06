import os
import shutil
import sys

def add_announces_and_rename(base_torrent_path, trackers_file):
    if not os.path.exists(trackers_file):
        print(f"Error: Trackers file '{trackers_file}' not found.")
        return

    with open(trackers_file, 'r') as f:
        lines = f.readlines()

    if not lines:
        print(f"Error: No announce URLs found in trackers file '{trackers_file}'.")
        return

    for line in lines:
        line = line.strip()
        if not line:
            continue
        abbreviation, announce_url = line.split(':', 1)
        new_torrent_path = os.path.join(os.path.dirname(base_torrent_path), f"{abbreviation}_{os.path.basename(base_torrent_path)}")
        try:
            shutil.copy(base_torrent_path, new_torrent_path)
            print(f"Copied '{os.path.basename(base_torrent_path)}' to '{os.path.basename(new_torrent_path)}'.")
        except Exception as e:
            print(f"Error copying '{os.path.basename(base_torrent_path)}': {e}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 announcer.py <base_torrent_path> <trackers_file>")
        sys.exit(1)

    base_torrent_path = sys.argv[1]
    trackers_file = sys.argv[2]
    add_announces_and_rename(base_torrent_path, trackers_file)

if __name__ == "__main__":
    main()
