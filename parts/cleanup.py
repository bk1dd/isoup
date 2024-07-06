import os
import shutil

def cleanup_scratch(scratch_dir):
    try:
        # Iterate over all files and directories in the scratch directory
        for filename in os.listdir(scratch_dir):
            file_path = os.path.join(scratch_dir, filename)
            
            # Check if the path is a file or directory
            if os.path.isfile(file_path):
                os.remove(file_path)  # Remove file
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # Remove directory recursively
            else:
                print(f"Skipping unknown file type: {file_path}")
        
        print(f"Cleanup complete for {scratch_dir}")

    except Exception as e:
        print(f"Error cleaning up {scratch_dir}: {e}")

if __name__ == '__main__':
    scratch_dir = '/path/to/isoup/scratch'  # Replace with your actual scratch directory path
    cleanup_scratch(scratch_dir)
