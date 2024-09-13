import argparse
import os
from tqdm import tqdm
import subprocess
from pytubefix import YouTube
from pytubefix.cli import on_progress



def download_videos(video_links_path):
  
    with open(video_links_path) as f:
          video_ids = f.readlines() 
  
    raw_data_destination = 'swing_data/raw_data/'
    os.makedirs(raw_data_destination, exist_ok=True)
      
    for video_name in tqdm(video_ids, desc='Downloading Videos'):
      video_name = video_name.strip()
      video_url = f'https://www.youtube.com/watch?v={video_name}'
      vid_path = f"{video_name}.mp4"
      youtube_video = YouTube(video_url, on_progress_callback = on_progress)
      youtube_video.streams.get_highest_resolution().download(output_path = raw_data_destination, filename= vid_path)
      
def trim_videos(ffmpeg_commands_path):
  
    with open(ffmpeg_commands_path) as f:
        ffmpeg_commands = f.readlines() 
    
    processed_data_destination = 'swing_data/processed_data/'
    os.makedirs(processed_data_destination, exist_ok=True)
    
    for command in tqdm(ffmpeg_commands, desc='Trimming Videos'):
      command = command.strip()
      subprocess.call(command, shell=True)

def main(args):
  

  if args.video_links_path is None:
    raise ValueError('Please provide the path to the video links')
  else:
    download_videos( args.video_links_path )
    
  if args.ffmpeg_commands_path is None:
    raise ValueError('Please provide the path to the ffmpeg commands')
  else:
    trim_videos(args.ffmpeg_commands_path)

    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Video data download')

    parser.add_argument('--video_links_path', type=str, help='path to the video links', default="video_links.txt")
    parser.add_argument('--ffmpeg_commands_path', type=str, help='path to the ffmpeg for trimming the videos', default="ffmpeg_commands.txt")

    args = parser.parse_args()
    main(args)