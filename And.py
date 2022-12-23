from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=720x1280')
options.add_argument("disable-gpu")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver=webdriver.Chrome(options=options)
print('Driver loaded')

driver.get('https://kschoolclick.netlify.app')
driver.find_element(By.XPATH, '/html/body/main/div[2]/div/span[2]').click()
driver.find_element(
    By.XPATH, '/html/body/main/div/div[2]/input').send_keys('대전원신흥중학교')
driver.find_element(By.XPATH, '/html/body/main/div/div[2]/button').click()
# time.sleep(10)
#WebDriverWait(driver, 1000).until(EC.invisibility_of_element_located((By.XPATH, '/html/body/main/div/div[3]/div')))
WebDriverWait(driver, 1000).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/div/div[3]/div/div[1]')))
driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div/div[1]').click()
actions = ActionChains(driver)
num = 0
hund=1
print('Starting Click!')
while True:
    try:
        actions.send_keys(' ')
        actions.perform()
        num = num+1
        
        time.sleep(0.05)
        if num % 1000 == 0:
            print(num*hund)
            num=0
            hund = hund+1
    except (KeyboardInterrupt):
        print('contributed '+str(num) + ' times')
        driver.quit()
        break
