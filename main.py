from fetch_youtube_video import fetch_youtube_video
import pandas as pd

link = input("Please input the link of a youtube video:\n")

video_data = fetch_youtube_video(link)

data_frame = pd.DataFrame.from_dict(video_data)
data_frame.to_csv('result.csv', index=False, header=True)
data_frame.to_excel('results.xls', index=False, header=True)
print(data_frame)
