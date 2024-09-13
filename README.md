# Swing Dance Dataset 
For more info please see our [project website](https://von31.github.io/synNsync/)

## Approach 1: Manual Set up

1. Create a folder with the following structure:
   - `swing_data/raw_data/`
   - `swing_data/processed_data/`
    

2. Download the youtube videos your choice of method into `swing_data/raw_data/` by using the provided list of video links found in `video_links.txt`. Each video can be found by replacing video_link_id in `https://www.youtube.com/watch?v=video_link_id` with the link found in the `video_links.txt` 

   - Example: 
       ```
       https://www.youtube.com/watch?v=laLyyC_RXa4
       ```

3. After the download, run the ffmpeg commands in the `ffmpeg_commands.txt` file to process the videos and save video into the `swing_data/processed_data/` folder


4. Download slahmr output files from : https://drive.google.com/file/d/16XIl-C9pEbsEF6vE8RW_6F3os4doIgER/view?usp=sharing


## Approach 2: Automatic Set up

1. Install required packages

    ```
    pip install pytubefix
    ```

2. Run code to download and process the swing dance dataset
   
    ```
    python get_swing_data.py 
    ```

3. Download slahmr output files from : https://drive.google.com/file/d/16XIl-C9pEbsEF6vE8RW_6F3os4doIgER/view?usp=sharing
