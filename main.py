from fetch_youtube_video import fetch_youtube_video
import pandas as pd

video_data = fetch_youtube_video(input("Please input the link of a youtube video:\n"))

data_frame = pd.DataFrame.from_dict(video_data, orient="index").T
data_frame.to_csv('result.csv', index=True, header=True)
data_frame.to_excel('results.xlsx', engine="xlsxwriter")
print(data_frame)
