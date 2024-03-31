from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import re
import time
import json


driverbrowser = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
try:
    driverbrowser.get("https://www.flipkart.com/")
    WebDriverWait(driverbrowser, 10).until(EC.title_contains('Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!'))
    search_box = driverbrowser.find_element(By.CLASS_NAME,"Pke_EE")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.submit()

    # mobiles_category = driverbrowser.find_element(By.LINK_TEXT,"Mobiles")

    mobiles_link = WebDriverWait(driverbrowser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '_1jJQdf')))
    print(mobiles_link.text)
    if mobiles_link.text =='Mobiles':
        mobiles_link.click()

    brand_link = WebDriverWait(driverbrowser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3879cV')))
    print(brand_link.text)
    if brand_link.text =='SAMSUNG':
        brand_link.click()


    assured_link = WebDriverWait(driverbrowser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[4]/label/div[1]')))
    print("assured")
    assured_link.click()

    hightoLow_link = WebDriverWait(driverbrowser, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[4]')))
    print(hightoLow_link.text)
    if hightoLow_link.text == 'Price -- High to Low':
        hightoLow_link.click()

    WebDriverWait(driverbrowser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._1AtVbE.col-12-12")))

    # Find all the product divs
    product_divs = driverbrowser.find_elements(By.CSS_SELECTOR, "div._1AtVbE.col-12-12")
    count = 0
    product_name_list = []
    price_list=[]
    product_link_list = []
    # Loop through each product div
    for product_div in product_divs:
        try:    
            if count >= 24:
                break
            else:          
                # Extract product name
                # product_name = product_div.find_element(By.CSS_SELECTOR, "div._4rR01T").text
                product_name = WebDriverWait(driverbrowser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._4rR01T"))).text
                
                # Extract display price
                # display_price = product_div.find_element(By.CSS_SELECTOR, "div._30jeq3._1_WHN1").text
                display_price = WebDriverWait(driverbrowser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._30jeq3._1_WHN1"))).text
                # Extract link to product details page
                # product_link = product_div.find_element(By.CSS_SELECTOR, "a._1fQZEK").get_attribute("href")
                product_link_tag = WebDriverWait(driverbrowser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a._1fQZEK")))
                product_link = product_link_tag.get_attribute("href")
                # Print product information
                print(count)
                print("Product Name:", product_name)
                product_name_list.append(product_name)
                print("Display Price:", display_price)
                price_list.append(display_price)
                print("Link to Product Details Page:", product_link)
                product_link_list.append(product_link)
                print("=" * 50)
                count +=1
            
            
        except Exception as err:
            message = 'Exception: ' + str(err.__class__) + str(err.msg)
            print(json.dumps(message))
    if(len(product_name_list)==24):
        print("Successfully added ")
    time.sleep(10)
except NoSuchElementException as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    print(json.dumps(message))
except Exception as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    print(json.dumps(message))
finally:
    # Stop the driver
    driverbrowser.quit()
# mobiles_category.click()