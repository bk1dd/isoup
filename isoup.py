import os
import sys
import subprocess
import shutil

def delete_tmp_folder_contents():
    tmp_folder = 'tmp'
    if os.path.exists(tmp_folder):
        for filename in os.listdir(tmp_folder):
            file_path = os.path.join(tmp_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 isoup.py /path/to/iso_file.iso -tk TRACKER_CODES")
        sys.exit(1)

    iso_file = sys.argv[1]
    tracker_codes = sys.argv[3:]

    delete_tmp_folder_contents()
    print("Deleted contents of 'tmp' folder.")

    # Run hasher.py
    print("Running hasher.py...")
    subprocess.run(['python3', 'parts/hasher.py', iso_file])

    # Run announcer.py
    print("Running announcer.py...")
    import parts.announcer as announcer
    trackers_file = os.path.join("data", "trackers.txt")
    announcer.add_announces_and_rename(iso_file, tracker_codes, trackers_file)

    print("Completed.")

if __name__ == "__main__":
    main()
