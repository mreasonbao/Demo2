from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://www.lxshfz.com")
print(browser.page_source)
# browser.close()
