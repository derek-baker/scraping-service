# main.py

from flask import Flask, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

app = Flask(__name__)

# The following options are required to make headless Chrome
# work in a Docker container
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("disable-infobars")
options.add_argument("window-size=1024,768")

# Initialize a new browser
browser = webdriver.Chrome(options=options)


@app.route("/")
def hello_world():
    browser.get("https://google.com")
    file_name = 'test.png'
    browser.save_screenshot(file_name)
    return send_file(file_name)
