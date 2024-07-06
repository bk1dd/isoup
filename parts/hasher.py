import os
import subprocess
import sys

def calculate_piece_length(file_size):
    # Desired maximum size of the torrent file in bytes (1 MB)
    max_torrent_size = 1024 * 1024

    # Calculate piece length based on file size and desired max torrent size
    piece_length = 20 + (file_size // max_torrent_size)
    
    return piece_length

def create_base_torrent(target_file):
    # Check if target file exists
    if not os.path.isfile(target_file):
        print(f"Error: File '{target_file}' not found.")
        return
    
    # Determine file size
    file_size = os.path.getsize(target_file)
    
    # Calculate piece length based on file size
    piece_length = calculate_piece_length(file_size)
    
    # Set output torrent file path in scratch folder
    base_torrent_file = os.path.join("scratch", f"BASE_{os.path.basename(target_file)}.torrent")
    
    # Check if base torrent file already exists in tmp folder
    tmp_base_torrent_file = os.path.join("tmp", os.path.basename(target_file), os.path.basename(base_torrent_file))
    if os.path.exists(tmp_base_torrent_file):
        print("Reusing hash.")
        return
    
    # Create command for mktorrent
    command = [
        'mktorrent',
        '-v',
        '-l', str(piece_length),
        '-p',
        '-a', 'http://example.com/announce',  # Replace with your announce URL
        '-s', '262144',  # Source size
        '-n', '5',  # Torrent name length
        target_file,
        '-o', base_torrent_file
    ]
    
    # Run mktorrent command
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created base torrent file '{os.path.basename(base_torrent_file)}' in '{os.path.dirname(base_torrent_file)}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating '{base_torrent_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hasher.py /path/to/target_file.iso")
        sys.exit(1)
    
    target_file = sys.argv[1]
    create_base_torrent(target_file)
