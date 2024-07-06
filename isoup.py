import os
import sys
import subprocess

# Path constants
ISOPATH = sys.argv[1] if len(sys.argv) > 1 else None
TRACKER_ABBREVIATIONS = sys.argv[2:] if len(sys.argv) > 2 else []

# Directories
ISOUUID = os.path.splitext(os.path.basename(ISOPATH))[0]
BASEDIR = os.path.dirname(os.path.realpath(__file__))
TMPDIR = os.path.join(BASEDIR, 'tmp')
SCRATCHDIR = os.path.join(BASEDIR, 'scratch')
PARTSDIR = os.path.join(BASEDIR, 'parts')

def create_tmp_directory():
    """Create a temporary directory for this ISO."""
    tmp_isouuid_dir = os.path.join(TMPDIR, ISOUUID)
    os.makedirs(tmp_isouuid_dir, exist_ok=True)
    return tmp_isouuid_dir

def run_hasher(iso_path, tmp_dir):
    """Run hasher.py to create base .torrent file."""
    hasher_script = os.path.join(PARTSDIR, 'hasher.py')
    subprocess.run(['python3', hasher_script, iso_path, tmp_dir])

def run_announcer(tmp_dir, tracker_abbreviations):
    """Run announcer.py to create multiple .torrent files with different announces."""
    announcer_script = os.path.join(PARTSDIR, 'announcer.py')
    subprocess.run(['python3', announcer_script, tmp_dir] + tracker_abbreviations)

def main():
    if not ISOPATH or not os.path.isfile(ISOPATH):
        print("Error: Provide a valid path to the ISO file.")
        return

    # Create temporary directory
    tmp_dir = create_tmp_directory()

    try:
        # Run hasher.py
        print("Running hasher.py...")
        run_hasher(ISOPATH, tmp_dir)

        # Run announcer.py with provided tracker abbreviations
        print("Running announcer.py...")
        run_announcer(tmp_dir, TRACKER_ABBREVIATIONS)

        # Add more scripts as needed, e.g., extractor.py, screenshotter.py, cleanup.py

    except Exception as e:
        print(f"Error: {e}")

    finally:
        # Clean up temporary directory
        if tmp_dir and os.path.exists(tmp_dir):
            print("Cleaning up temporary directory...")
            subprocess.run(['python3', os.path.join(PARTSDIR, 'cleanup.py'), tmp_dir])

if __name__ == "__main__":
    main()

