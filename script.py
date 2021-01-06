from selenium import webdriver
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://sinfo.kmutt.ac.th')
while(True):
	if browser.title == "Under Construction":
		time.sleep(0.2)
		browser.refresh()
		pass
	else:
		break
