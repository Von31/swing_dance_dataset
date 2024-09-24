# Swing Dance Dataset 

https://github.com/user-attachments/assets/b86e3dbc-4939-4117-a0ce-82e477654fcd

Swing Dance dataset is a large-scale dataset comprising about 30 hours of swing dance videos with 680 unique couple subjects represented as 3D humans. We lifted each video into 4D using [SLAHMR](https://github.com/vye16/slahmr) to extract the 3D human motion in the world. 
This data was used for unary and dyadic human motion prediction. For more info please see our [synNsync project website](https://von31.github.io/synNsync/).


## Approach 1: Manual Set up

1. Create a folder with the following structure:
   - `swing_data/raw_data/` - contains  unprocessed web scraped videos 
   - `swing_data/processed_data/`  - contains processed videos with trimmed intro and outros
   - `swing_data/slahmr`  - contains .npz files of the 4D humans annotations of the processed data 


2. Download the youtube videos using your choice of method into `swing_data/raw_data/` by using the provided list of video links found in `video_links.txt`. Each video can be found by replacing video_link_id in `https://www.youtube.com/watch?v=video_link_id` with the link found in the `video_links.txt` 

   - Example: 
       ```
       https://www.youtube.com/watch?v=laLyyC_RXa4
       ```

3. After the download, run the ffmpeg commands in the `ffmpeg_commands.txt` file to process the videos and save video into the `swing_data/processed_data/` folder

4. Download SLAHMR output files from this [URL](https://drive.google.com/file/d/16XIl-C9pEbsEF6vE8RW_6F3os4doIgER/view?usp=sharing) and unzip into `swing_data/slahmr`


## Approach 2: Automatic Set up

1. Install required packages

    ```
    pip install pytubefix
    pip install gdown
    ```

2. Run code to download and process the swing dance dataset
   
    ```
    python get_swing_data.py 
    ```

## Swing Dance SLAHMR output (4D humans annotations):
  - The naming convention of the files are : `swing_data/slahmr/dancing_<video_link>_<start_frame>_<end_frame>.npz`
  - Size of the Data: 2.43 GB
    


## License
See [License](./LICENSE).

