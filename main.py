# heroku profitcentr
from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from github import Github
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import json
from bs4 import BeautifulSoup
import os
from flask import Flask
import threading
import random
import re
import sys
from io import StringIO

MAX_LOG_MESSAGES = 10  # Maximum number of log messages to display
MAX_PRINT_STATEMENTS = 10  # Maximum number of print statements to display
log_messages = []
stdout_capture = StringIO()
sys.stdout = stdout_capture


account_number = os.getenv("ACCOUNT_NUMBER")
app = Flask(__name__)

@app.route('/')
def hello():
    return f"{'<br>'.join(log_messages[-MAX_LOG_MESSAGES:])}<br>{'<br>'.join(stdout_capture.getvalue().splitlines()[-MAX_PRINT_STATEMENTS:])}"

port = int(os.environ.get("PORT", 5000))

def flask_thread():
    app.run(host="0.0.0.0", port=port)

def running():
    
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    
    #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # Use context manager to handle the WebDriver instance
    with webdriver.Chrome(options=chrome_options) as driver1:
        #driver1.set_window_size(800, 600)
        #driver1.minimize_window()
        driver1.get("https://delionix.com/")
        new_window_size = {'width': 1552, 'height': 840}
        driver1.set_window_size(new_window_size['width'], new_window_size['height'])
        print("Please wait... delionix.com")
        
        
        # Load cookies from file
        with open(f'account_{str(account_number)}.json', 'r') as f:
            cookies = json.load(f)
        #time.sleep(2)
        # Add cookies to the browser session
        for cookie in cookies:
            driver1.add_cookie(cookie)
        #time.sleep(2)
        # Refresh the page to apply cookies
        driver1.refresh()

       
        driver1.execute_script("window.scrollBy(0, 300);")
        time.sleep(1)

        driver1.get("https://delionix.com/members")
        

        money = fgfg = WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.ID, "new-money-ballans"))).text

        print(f"mon:{money}")
        
        driver1.execute_script("window.scrollBy(0, 300);")
       
        WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="mnu_tblock1"]/a[7]'))).click()

        time.sleep(5)
        random_number = random.randint(2, 10)
        driver1.execute_script("window.scrollBy(0, 100);")
        WebDriverWait(driver1, 10).until(                      
                    EC.presence_of_element_located((By.XPATH, f'/html/body/table/tbody/tr[4]/td[2]/div[1]/div[2]/div[3]/div[{random_number}]/table/tbody/tr/td[2]/div[1]/span[1]'))).click()
        
        time.sleep(2)
        
        
        WebDriverWait(driver1, 10).until(
                    EC.presence_of_element_located((By.XPATH, f'/html/body/table/tbody/tr[4]/td[2]/div[1]/div[2]/div[3]/div[{random_number}]/table/tbody/tr/td[2]/div[1]/div/span'))).click()
        
        print("ok")



        window_after = driver1.window_handles[1]
        driver1.switch_to.window(window_after)

        

        time.sleep(5)

        wait = WebDriverWait(driver1, 10).until(
            EC.presence_of_element_located((By.ID, "tmr"))).text
        print(f"Wait: {wait}")
        
       

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)
      
        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.TAB)
        actions.perform()
        time.sleep(0.5)

        actions = webdriver.ActionChains(driver1)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(0.5)

        time.sleep(int(wait) + 3)
        
        WebDriverWait(driver1, 5).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="succes-error"]/table/tbody/tr/td[2]/button'))).click()
        time.sleep(3)

      

        print("Cookies copied successfully..")
        
       

        if float(money) > 15:
            try:
                driver1.get("https://delionix.com/members")
                WebDriverWait(driver1, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="leftcolumn"]/div/div[1]/center/div[2]'))).click()
                time.sleep(3)
                print("1")
                WebDriverWait(driver1, 5).until(               
                    EC.presence_of_element_located((By.XPATH, '//*[@id="aj-content"]/form/center/div[2]/div[6]/div/div/div'))).click()
                time.sleep(2)
                print("2")
                slider = WebDriverWait(driver1, 5).until(
                        EC.presence_of_element_located((By.NAME, "scrol")))
                slider_size = slider.size
                offset = slider_size['width'] * 0.5 
                action = ActionChains(driver1)
                action.click_and_hold(slider).move_by_offset(offset, 0).release().perform()
                time.sleep(4)
                print("3")        
                WebDriverWait(driver1, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="aj-content"]/form/center[2]/input'))).click()
            
                print("widthdraw successful..")
            except:
                pass

        driver1.quit()

        time.sleep(90)

def sdsf():
    while True:
        try:
            running()
        except:
            continue





# Start Flask in a separate thread
flask_thread = threading.Thread(target=flask_thread)
flask_thread.start()



flask_thread1 = threading.Thread(target=sdsf)
flask_thread1.start()






if __name__ == '__main__':
    # This block will only be executed when the script is run directly, not when imported
    try:
        while True:
            pass  # Keep the main thread alive
    except KeyboardInterrupt:
        scheduler.shutdown()


sys.stdout = sys.__stdout__