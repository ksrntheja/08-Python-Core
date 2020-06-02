from selenium import webdriver
import time

driver = webdriver.Firefox(
    executable_path='/Code/venv/unittesting/geckodriver')

driver.get('https://www.google.com')

# driver.maximize_window()

print('Title:', driver.title)

print('Current_url', driver.current_url)

driver.refresh()
driver.get(driver.current_url)
print('Current_url after refresh', driver.current_url)

time.sleep(5)

driver.get('moz:lla')
print('Current_url', driver.current_url)

time.sleep(5)

driver.back()
print('After Back Current_url', driver.current_url)

time.sleep(5)

driver.forward()
print('After Forward Current_url', driver.current_url)

driver.close()

# driver.quit()

# $ python3 08SeleniumBasic.py 
# Title: Google
# Current_url https://www.google.com/
# Current_url after refresh https://www.google.com/
# Current_url https://www.mozilla.org/en-US/about/manifesto/
# After Back Current_url https://www.google.com/
# After Forward Current_url https://www.mozilla.org/en-US/about/manifesto/
