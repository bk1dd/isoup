import os
import sys
import subprocess
import shutil

def clear_scratch_folder():
    scratch_folder = 'scratch'
    for filename in os.listdir(scratch_folder):
        file_path = os.path.join(scratch_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

def run_script(script_name, *args):
    command = ['python3', script_name] + list(args)
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running script {script_name}: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 isoup.py /path/to/iso_file.iso -tk <tracker_abbr1> <tracker_abbr2> ...")
        sys.exit(1)
    
    iso_file = sys.argv[1]
    tracker_abbrs = sys.argv[3:]

    print("Deleted contents of 'scratch' folder.")
    clear_scratch_folder()

    print("Running hasher.py...")
    run_script('parts/hasher.py', iso_file)

    print("Running announcer.py...")
    import parts.announcer as announcer
    announcer.add_announces_and_rename(iso_file, tracker_abbrs, 'data/trackers.txt')

if __name__ == "__main__":
    main()
