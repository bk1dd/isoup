import os
import subprocess
import shutil

def create_folder_and_torrent(target_file_path, tmp_folder):
    # Extract target file name without extension
    target_file_name = os.path.splitext(os.path.basename(target_file_path))[0]

    # Create new folder path inside tmp folder
    new_folder_path = os.path.join(tmp_folder, target_file_name)
    
    # Create the new folder if it doesn't exist
    os.makedirs(new_folder_path, exist_ok=True)
    
    # Path to store the torrent file inside the new folder
    torrent_file_path = os.path.join(new_folder_path, f"{target_file_name}.torrent")

    # Run mktorrent to create the base torrent file
    # Example command: mktorrent -v -l 20 -p -a http://example.com/announce -s 262144 -n 5 /path/to/target_file -o /path/to/new_folder/target_file.torrent
    mktorrent_command = [
        "mktorrent",
        "-v",  # Verbose output
        "-l", "20",  # Piece length (default: 262144)
        "-p",  # Private torrent
        "-a", "http://example.com/announce",  # Replace with your announce URL
        "-s", "262144",  # Piece size (default: 262144)
        "-n", "5",  # Number of pieces (default: automatic)
        target_file_path,  # Path to the target file
        "-o", torrent_file_path  # Output path for the torrent file
    ]

    # Execute mktorrent command
    subprocess.run(mktorrent_command, check=True)

    # Move the created torrent file to the new folder
    shutil.move(torrent_file_path, new_folder_path)

    print(f"Created folder '{target_file_name}' and base torrent file in '{new_folder_path}'")

if __name__ == "__main__":
    # Example usage:
    target_file_path = "/path/to/your/target_file"
    tmp_folder = "/path/to/your/tmp_folder"

    create_folder_and_torrent(target_file_path, tmp_folder)
