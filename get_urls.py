import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

channel_url = 'enter_url_channel'
#channel_url = 'https://www.youtube.com/@luciusfox9508/videos'

def get_all_url_name_of_channel():
    try:
        browser.get(channel_url)
        video_links = []
        name_links = []
        #Xpath name title all videos
        element_xpath = "/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[1]"
        element = browser.find_element(By.XPATH,element_xpath)
        element.click()
        # Scroll down to load more videos (you may need to customize this)
        for _ in range(4):
            browser.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
            time.sleep(1)
            browser.implicitly_wait(5)
        time.sleep(2)
        # Find and collect video links
        video_elements = browser.find_elements(By.ID, 'video-title-link')
        for video_element in video_elements:
            video_link = video_element.get_attribute('href')
            name_link = video_element.get_attribute('title')
            video_links.append(video_link)
            name_links.append(name_link)

        # Define the name of the output file
        output_file = 'video_links.csv'        
        #Write the video links to the output file
        with open(output_file, "w", newline="") as f:
            writer = csv.writer(f)

            writer.writerow(["name_links", "video_links"])
            for index in range(len(video_links)):
                writer.writerow([name_links[index], video_links[index]])

        print(f"Video links have been saved to {output_file}")
    except Exception as e:
        print("[ ERROR ]", str(e))
    else:
        print('[ OK ]')
