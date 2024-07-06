import os
import subprocess
import shutil

def calculate_piece_length(file_size):
    # Desired maximum size of the torrent file in bytes (1 MB)
    max_torrent_size = 1024 * 1024

    # Calculate piece length based on file size and desired max torrent size
    piece_length = max(262144, (file_size * 20) // max_torrent_size)
    return piece_length

def create_base_torrent(target_file):
    # Determine paths relative to isoup folder
    scratch_folder = 'scratch/'
    tmp_folder = 'tmp/'

    # Create folder in tmp directory with the target file's name
    target_name = os.path.splitext(os.path.basename(target_file))[0]
    tmp_target_folder = os.path.join(tmp_folder, target_name)
    os.makedirs(tmp_target_folder, exist_ok=True)

    # Check if base torrent file already exists in tmp folder
    base_torrent_path_tmp = os.path.join(tmp_target_folder, f"BASE_{target_name}.torrent")
    if os.path.exists(base_torrent_path_tmp):
        print(f"Reusing hash: Base torrent file 'BASE_{target_name}.torrent' already exists in '{tmp_target_folder}'")
        return

    # Calculate piece length dynamically based on file size
    file_size = os.path.getsize(target_file)
    piece_length = calculate_piece_length(file_size)

    # Construct paths for base torrent creation and move
    base_torrent_path_scratch = os.path.join(scratch_folder, f"BASE_{target_name}.torrent")

    # Create base torrent file in scratch folder
    command = [
        'mktorrent',
        '-v',
        '-l', str(piece_length),  # Use calculated piece length
        '-p',
        '-a', 'http://example.com/announce',  # Replace with actual announce URL
        '-s', '262144',
        '-n', '5',
        target_file,
        '-o', base_torrent_path_scratch
    ]

    subprocess.run(command, check=True)

    # Move base torrent file to tmp directory
    shutil.move(base_torrent_path_scratch, base_torrent_path_tmp)
    print(f"Successfully created base torrent file 'BASE_{target_name}.torrent' in '{tmp_target_folder}'")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 hasher.py /path/to/target.iso")
        sys.exit(1)

    target_file = sys.argv[1]
    create_base_torrent(target_file)
