import os

from selenium import webdriver

# driver_location = "/usr/bin/chromedriver"
# binary_location = "/usr/bin/google-chrome"
#
# options = webdriver.ChromeOptions()
# options.binary_location = binary_location
#
# driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--window-size=1920,1080")
op.add_argument("--headless")
op.add_argument('--disable-dev-shm-usage')
op.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

print("Window size updated")
