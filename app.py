from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.get('https://kschoolclick.netlify.app')
driver.find_element(By.XPATH, '/html/body/main/div[2]/div/span[2]').click()
driver.find_element(
    By.XPATH, '/html/body/main/div/div[2]/input').send_keys('대전원신흥중학교')
driver.find_element(By.XPATH, '/html/body/main/div/div[2]/button').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div/div[1]').click()
actions = ActionChains(driver)
num = 0
print('Starting Click!')
while True:
    try:
        actions.send_keys(
            '                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ')
        actions.perform()
        num = num+1
        if num % 10000 == 0:
            print(num)
    except (KeyboardInterrupt):
        print('contributed '+str(num) + ' times')
        driver.quit()
        break
