import os
import sys
import bencodepy

def add_announces_and_rename(base_torrent_path, tracker_codes, trackers_file):
    if not os.path.exists(trackers_file):
        print(f"Error: Trackers file '{trackers_file}' not found.")
        return

    # Read announce URLs from trackers.txt
    trackers = {}
    with open(trackers_file, 'r') as f:
        for line in f:
            code, url = line.strip().split(':', 1)
            trackers[code] = url

    # Read the base torrent file
    with open(base_torrent_path, 'rb') as f:
        torrent_data = bencodepy.decode(f.read())

    # Add announce URLs
    for code in tracker_codes:
        if code in trackers:
            if 'announce-list' not in torrent_data:
                torrent_data['announce-list'] = []
            torrent_data['announce-list'].append([trackers[code].encode('utf-8')])

    # Write new torrent files
    torrent_name = os.path.basename(base_torrent_path)
    torrent_name_no_ext = os.path.splitext(torrent_name)[0]
    for code in tracker_codes:
        new_torrent_name = f"{code}_{torrent_name}"
        new_torrent_path = os.path.join('tmp', torrent_name_no_ext, new_torrent_name)
        os.makedirs(os.path.dirname(new_torrent_path), exist_ok=True)
        with open(new_torrent_path, 'wb') as f:
            f.write(bencodepy.encode(torrent_data))
        print(f"Created torrent with announce URL {trackers[code]}: {new_torrent_name}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python3 announcer.py /path/to/base.torrent TRACKER_CODES /path/to/trackers.txt")
        sys.exit(1)

    base_torrent_path = sys.argv[1]
    tracker_codes = sys.argv[2:-1]
    trackers_file = sys.argv[-1]
    add_announces_and_rename(base_torrent_path, tracker_codes, trackers_file)
