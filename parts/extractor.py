import os
import sys
import subprocess
import shutil

def extract_iso(iso_file, scratch_folder):
    # Ensure scratch folder exists
    os.makedirs(scratch_folder, exist_ok=True)
    
    # Construct the output folder path
    output_folder = os.path.join(scratch_folder, os.path.splitext(os.path.basename(iso_file))[0])
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # PowerISO command to extract ISO
    poweriso_command = [
        "poweriso",  # Replace with the correct command if necessary (e.g., "/path/to/poweriso")
        "extract",  # Command to extract ISO
        iso_file,  # Input ISO file
        "-o", output_folder  # Output folder
    ]
    
    # Execute the PowerISO command
    try:
        subprocess.run(poweriso_command, check=True)
        print(f"Successfully extracted '{iso_file}' to '{output_folder}'")
    except subprocess.CalledProcessError as e:
        print(f"Error extracting ISO: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Check if ISO file path argument is provided
    if len(sys.argv) < 2:
        print("Usage: python3 extractor.py /path/to/iso_file")
        sys.exit(1)
    
    # Example scratch folder path
    scratch_folder = os.path.join(os.getcwd(), "scratch")  # Adjust as needed
    
    # Get ISO file path from command-line argument
    iso_file = sys.argv[1]
    
    # Call function to extract ISO to scratch folder
    extract_iso(iso_file, scratch_folder)
