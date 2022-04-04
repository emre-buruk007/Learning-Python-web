from fetch_youtube_video import fetch_youtube_video
import pandas as pd


def export_to_csv(data):
    data.to_csv('result.csv')


def export_to_excel(data):
    data.to_excel('results.xlsx', engine='xlsxwriter')


video_data = fetch_youtube_video(input("Please input the link of a youtube video:\n"))

data_frame = pd.DataFrame.from_dict(video_data).set_index('VideoName')

export_to_csv(data_frame)
export_to_excel(data_frame)
