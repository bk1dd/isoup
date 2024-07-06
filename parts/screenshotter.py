import os
import subprocess

def take_screenshots(video_path, output_folder, num_screenshots):
    # Calculate the duration of the video
    duration_command = [
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1',
        video_path
    ]
    duration = float(subprocess.check_output(duration_command).strip())

    # Calculate the time interval between screenshots
    total_duration = duration - 600  # Excluding first and last 5 minutes
    interval = total_duration / (num_screenshots + 1)

    # Command to take screenshots
    screenshot_command = [
        'ffmpeg', '-i', video_path,
        '-vf', f'trim=300:{duration - 300},fps=1/{interval}',
        f'{output_folder}/screenshot%d.jpg'
    ]

    # Execute the command
    subprocess.run(screenshot_command, check=True)

if __name__ == '__main__':
    # Example usage:
    video_path = '/path/to/scratch/BDMV/movie.m2ts'  # Example path to the video file
    output_folder = '/path/to/tmp/folder_created_by_hasher'  # Example path to output folder
    num_screenshots = 10  # Example number of screenshots to take

    take_screenshots(video_path, output_folder, num_screenshots)
