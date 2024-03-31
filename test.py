import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options as ChromeOptions

# The webdriver management will be handled by the browserstack-sdk
# so this will be overridden and tests will run browserstack -
# without any changes to the test files!
options = ChromeOptions()
options.set_capability('sessionName', 'FlipKart Assignment Test')
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.flipkart.com/")
    WebDriverWait(driver, 10).until(EC.title_contains('Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!'))
    search_box = driver.find_element(By.CLASS_NAME,"Pke_EE")
    search_box.send_keys("Samsung Galaxy S10")
    search_box.submit()

    # mobiles_category = driver.find_element(By.LINK_TEXT,"Mobiles")

    mobiles_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '_1jJQdf')))
    print(mobiles_link.text)
    if mobiles_link.text =='Mobiles':
        mobiles_link.click()

    brand_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, '_3879cV')))
    print(brand_link.text)
    if brand_link.text =='SAMSUNG':
        brand_link.click()


    assured_link = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div/div[1]/div/div[1]/div/section[4]/label/div[1]')))
    print("assured")
    assured_link.click()

    hightoLow_link = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div/div[2]/div[1]/div/div/div[3]/div[4]')))
    print(hightoLow_link.text)
    if hightoLow_link.text == 'Price -- High to Low':
        hightoLow_link.click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._1AtVbE.col-12-12")))

    # Find all the product divs
    product_divs = driver.find_elements(By.CSS_SELECTOR, "div._1AtVbE.col-12-12")
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
                
                product_name = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._4rR01T"))).text
                
                # Extract display price
                
                display_price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div._30jeq3._1_WHN1"))).text
                # Extract link to product details page
                
                product_link_tag = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a._1fQZEK")))
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
        # Set the status of test as 'passed' if item is added to cart
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All the Details about samsung mobile assured products are feteched"}}')
    else:
        # Set the status of test as 'failed' if item is not added to cart
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Not able to fetch the details of the products"}}')
except NoSuchElementException as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
except Exception as err:
    message = 'Exception: ' + str(err.__class__) + str(err.msg)
    driver.execute_script(
        'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
finally:
    # Stop the driver
    driver.quit()
