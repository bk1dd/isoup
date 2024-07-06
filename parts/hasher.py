import os
import sys
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
    base_torrent_name = f"BASE_{target_file_name}.torrent"
    torrent_file_path = os.path.join(new_folder_path, base_torrent_name)

    # Run mktorrent to create the base torrent file
    mktorrent_command = [
        "mktorrent",
        "-v",  # Verbose output
        "-l", "20",  # Piece length (default: 262144)
        "-p",  # Private torrent
        "-a", "http://example.com/announce",  # Replace with your default announce URL
        "-s", "262144",  # Piece size (default: 262144)
        "-n", "5",  # Number of pieces (default: automatic)
        target_file_path,  # Path to the target file
        "-o", torrent_file_path  # Output path for the torrent file
    ]

    # Execute mktorrent command
    try:
        subprocess.run(mktorrent_command, check=True)
        print(f"Successfully created base torrent file '{base_torrent_name}' in '{new_folder_path}'")
    except subprocess.CalledProcessError as e:
        print(f"Error creating base torrent file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if target file path argument is provided
    if len(sys.argv) < 2:
        print("Usage: python3 01hasher.py /path/to/target_file")
        sys.exit(1)

    # Example tmp folder path
    tmp_folder = os.path.join(os.getcwd(), "..", "tmp")  # Adjust as needed

    # Get target file path from command-line argument
    target_file_path = sys.argv[1]

    # Call function to create folder and base torrent
    create_folder_and_torrent(target_file_path, tmp_folder)
