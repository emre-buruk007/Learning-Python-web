from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


link = input("Please input the link of a youtube video:\n")
driver = webdriver.Chrome(ChromeDriverManager().install())


def fetch_youtube_video(link):

    driver.get(link)

    video_title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/h1/yt-formatted-string'))).text
    video_views = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="count"]/ytd-video-view-count-renderer/span[1]'))).text
    upload_date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="info-strings"]/yt-formatted-string'))).text
    modified_views_string = video_views[:-6]  # -6 is to cut out " views" from the received result
    views_as_int = int(modified_views_string.replace(',', ''))  # this is to remove the comma so the number can be freely parsed to int

    collected_data = {
        "VideoName": video_title,
        "Views": views_as_int,
        "Date": upload_date
    }
    print(collected_data)
    return collected_data


fetch_youtube_video(link)
