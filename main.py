from fetch_youtube_video import fetch_youtube_video
import pandas as pd


def export_to_csv(dataframe):
    dataframe.to_csv('result.csv', index=True, header=True)


def export_to_xlsx(dataframe):
    data_frame.to_excel('results.xlsx', engine="xlsxwriter")


video_data = fetch_youtube_video(input("Please input the link of a youtube video:\n"))

data_frame = pd.DataFrame.from_dict(video_data, orient="index").T
export_to_csv(data_frame)
export_to_xlsx(data_frame)
