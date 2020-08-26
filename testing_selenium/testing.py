from selenium import webdriver


# Activate the driver for chrome from PATH.
chrome_browser = webdriver.Chrome("C:/Users/gregb/bin/chromedriver.exe")

# Maximize the window of the given website.
chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

# Make sure the "" is in the website title via HTML.
assert 'Selenium Easy Demo' in chrome_browser.title
show_message_button = chrome_browser.find_element_by_class_name("btn-default")
print(show_message_button.get_attribute('innerHTML'))

assert "Show Message" in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id("user-message")

# Clear the message box if text already present.
user_message.clear()

# Populate message box.
user_message.send_keys("I am extra cool!")

show_message_button.click()
output_message = chrome_browser.find_element_by_id("display")

# Checks that the text is in the output message, else throw error.
assert "I am extra cool" in output_message.text


# chrome_browser.close()
