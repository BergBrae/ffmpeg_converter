import subprocess
import glob
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

CONVERTED_TAG = os.environ.get('CONVERTED_TAG', '(Converted)')

def convert_video(input_path, output_path):
    command = ['ffmpeg', '-i', input_path, '-c:v', 'libx264', '-c:a', 'aac', output_path]
    subprocess.run(command, check=True)
    print(f'Converted {input_path} to {output_path}')

def remove_extension(file):
    return '.'.join(file.split('.')[:-1])

def converted_filename(filepath, converted_tag=CONVERTED_TAG):
    return remove_extension(filepath) + converted_tag + '.mp4'


def run_update(path, converted_tag=CONVERTED_TAG):
    video_filetypes = [f'{path}/**/*.mp4', f'{path}/**/*.avi', f'{path}/**/*.mkv', f'{path}/**/*.mov']
    video_files = []
    for filetype in video_filetypes:
        video_files.extend(glob.glob(filetype, recursive=True))
    video_files = set(video_files)

    for file in video_files:
        if converted_filename(file.replace(converted_tag, '')) not in video_files:
            convert_video(file, converted_filename(file))

if __name__ == '__main__':
    run_update(path='./')
