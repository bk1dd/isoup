import os
import subprocess
import sys

def calculate_piece_length(file_size):
    # Desired maximum size of the torrent file in bytes (1 MB)
    max_torrent_size = 1024 * 1024

    # Start with a piece length of 2^15 (32 KB)
    piece_length = 15

    # Increment piece length until the torrent file size is less than 1 MB
    while piece_length <= 28:
        num_pieces = file_size / (2 ** piece_length)
        torrent_size = num_pieces * 20 + 1  # 20 bytes per piece + 1 byte overhead
        if torrent_size <= max_torrent_size:
            break
        piece_length += 1

    # Ensure piece length is within valid range
    piece_length = max(15, min(piece_length, 28))

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
        '-n', '5',  # Torrent name length
        target_file,
        '-o', base_torrent_file
    ]
    
    # Run mktorrent command
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created base torrent file '{os.path.basename(base_torrent_file)}' in '{os.path.dirname(base_torrent_file)}'.")
        
        # Move base torrent file to tmp folder
        os.makedirs(os.path.dirname(tmp_base_torrent_file), exist_ok=True)
        os.rename(base_torrent_file, tmp_base_torrent_file)
    except subprocess.CalledProcessError as e:
        print(f"Error creating '{base_torrent_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hasher.py /path/to/target_file.iso")
        sys.exit(1)
    
    target_file = sys.argv[1]
    create_base_torrent(target_file)
