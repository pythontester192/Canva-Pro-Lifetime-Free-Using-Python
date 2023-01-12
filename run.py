from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time

# Configure Chrome options to run in headless mode
options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36")
options.add_argument("--lang=en")
options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Initialize a new web browser instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the website
driver.get("https://www.edukasicampus.net/2022/11/canva-pros-and-cons-review-canva.html")
time.sleep(5)

# Scroll down until the element with the text "Script link" is found
while True:
    try:
        script_link_element = driver.find_element(By.XPATH, "//*[@id='link']")
        # scroll to the element
        actions = ActionChains(driver)
        actions.move_to_element(script_link_element)
        actions.perform()
        break
    except:
        print("Canva Pro Link Not Found!")

# Wait for 60 seconds until the span with the id "link" is found
try:
    print("Trying to find canva pro for you! Please wait 60s...")
    link_span = WebDriverWait(driver, 70).until(EC.presence_of_element_located((By.XPATH, "//*[@id='link']/a")))
    href_link = driver.find_element(By.XPATH, "//*[@id='link']/a").get_attribute("href")
    print("Canva Pro Found!")

    #Print the link of canva pro in a text file
    with open("canva_pro_link.txt", "w") as f:
        f.write(href_link)   
except TimeoutError:
    print("Timeout of 60 seconds reached and canva was not found")

# Close the browser instance
driver.quit()
