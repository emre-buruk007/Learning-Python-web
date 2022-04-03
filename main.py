from fetch_youtube_video import fetch_youtube_video
import pandas as pd


def export_to_csv(dataframe):
    dataframe.to_csv('result.csv')


def export_to_xlsx(dataframe):
    dataframe.to_excel('results.xlsx', engine="xlsxwriter")


link = input("Please input the link of a youtube video:\n")

video_data = fetch_youtube_video(link)

data_frame = pd.DataFrame.from_dict(video_data).set_index("VideoName")
export_to_csv(data_frame)
export_to_xlsx(data_frame)
