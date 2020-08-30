# main.py

from flask import Flask, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary  # Adds chromedriver binary to path

app = Flask(__name__)

# The following options are required to make headless Chrome
# work in a Docker container
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")

# Initialize a new browser
browser = webdriver.Chrome(chrome_options=chrome_options)


@app.route("/")
def hello_world():
    browser.get("https:google.com")
    file_name = 'test.png'
    browser.save_screenshot(file_name)
    return send_file(file_name)
