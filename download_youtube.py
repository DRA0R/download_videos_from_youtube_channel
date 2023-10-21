import pytube
import csv

def download_videos_from_csv(csv_file_path):

  with open(csv_file_path, 'r') as f:
    reader = csv.reader(f)
    names_and_urls = [(row[0],row[1].replace("|", "")) for row in reader]

  for item in names_and_urls:
    download_video(item[1], name_video=item[0])

def download_video(url, folder= "./save_videos",name_video='downloaded_video.mp4'):
 """Downloads a single video from YouTube.

 Args:
  url: The URL of the video to download.
  output_path: The path to the output file where the video will be downloaded.
 """

 try:
  yt = pytube.YouTube(url)
  stream = yt.streams.get_highest_resolution() # Get the highest resolution stream
  stream.download(output_path=folder)
  print(f"Video downloaded successfully to {name_video}")
 except Exception as e:
  print(f"Error: {e}")

if __name__ == "__main__":
 csv_file_path = 'video_links.csv'

 download_videos_from_csv(csv_file_path)
