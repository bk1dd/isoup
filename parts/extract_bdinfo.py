import subprocess
import os

def extract_bdinfo(iso_path, scratch_dir):
    try:
        # Run bdinfo command and save output to a text file
        bdinfo_output_file = os.path.join(scratch_dir, 'bdinfo_output.txt')
        subprocess.run(['bdinfo', iso_path, '-o', bdinfo_output_file], check=True)
        print(f"bdinfo extraction complete. Output saved to: {bdinfo_output_file}")

    except subprocess.CalledProcessError as e:
        print(f"Error running bdinfo: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Replace with actual paths
    iso_path = '/path/to/extracted/ISO'
    scratch_dir = '/path/to/isoup/scratch'

    # Ensure scratch directory exists
    os.makedirs(scratch_dir, exist_ok=True)

    # Run bdinfo extraction
    extract_bdinfo(iso_path, scratch_dir)
