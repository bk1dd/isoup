import os
import subprocess
import sys

def create_base_torrent(file_path, verbose=True):
    # Create folder if not exists
    torrent_folder = os.path.join('/APPBOX_DATA/storage/bk1dd/isoup/tmp', os.path.basename(file_path))
    os.makedirs(torrent_folder, exist_ok=True)

    # Define torrent file name
    torrent_name = f"BASE_{os.path.basename(file_path)}.torrent"
    torrent_path = os.path.join(torrent_folder, torrent_name)

    # Check if torrent file already exists, delete if so
    if os.path.exists(torrent_path):
        os.remove(torrent_path)
        if verbose:
            print(f"Deleted existing torrent file: {torrent_path}")

    # Construct mktorrent command
    command = [
        'mktorrent',
        '-v', '-l', '20', '-p',
        '-a', 'http://example.com/announce',
        '-s', '262144', '-n', '5',
        file_path,
        '-o', torrent_path
    ]

    if verbose:
        print(f"Running mktorrent to create base torrent: {' '.join(command)}")

    try:
        subprocess.run(command, check=True)
        print(f"Successfully created base torrent file '{torrent_name}' in '{torrent_folder}'")
    except subprocess.CalledProcessError as e:
        print(f"Error creating base torrent file: {e}")
        raise

# Example usage
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hasher.py /path/to/target_file.iso")
        sys.exit(1)
    
    target_file = sys.argv[1]
    create_base_torrent(target_file)
