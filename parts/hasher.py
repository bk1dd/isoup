import os
import subprocess
import sys

def calculate_piece_length(file_size):
    piece_length = 20
    while (file_size / (2 ** piece_length)) > (1024 * 1024):
        piece_length += 1
        if piece_length > 28:
            piece_length = 28
            break
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
    tmp_folder = os.path.join("tmp", os.path.basename(target_file))
    tmp_base_torrent_file = os.path.join(tmp_folder, os.path.basename(base_torrent_file))
    
    if not os.path.exists(tmp_folder):
        os.makedirs(tmp_folder)
        
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
        target_file,
        '-o', base_torrent_file
    ]
    
    # Run mktorrent command
    try:
        subprocess.run(command, check=True)
        print(f"Successfully created base torrent file '{os.path.basename(base_torrent_file)}' in 'scratch'.")
        
        # Move the created base torrent file to the tmp folder
        os.rename(base_torrent_file, tmp_base_torrent_file)
        print(f"Moved base torrent file to '{tmp_base_torrent_file}'.")
    except subprocess.CalledProcessError as e:
        print(f"Error creating '{base_torrent_file}': {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hasher.py /path/to/target_file.iso")
        sys.exit(1)
    
    target_file = sys.argv[1]
    create_base_torrent(target_file)
