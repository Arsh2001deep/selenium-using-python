from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)


# Set up the browser driver
# driver = webdriver.Chrome('/path/to/chromedriver')

# Define a list of URLs of the websites to fill the form on
urls = ['https://mighty-men.mn.co/spaces/9349800/feed', 'https://network-89217.mn.co/spaces/9350713/feed']

# Loop through the list of URLs and fill the form on each website
for url in urls:
    # Navigate to the website
    driver.get(url)
    time.sleep(4)

    #Clicking on the signin button
    signin = driver.find_element(By.ID, 'sign-in-button')
    signin.click()
    time.sleep(2)


    # Fill up the form
    email = driver.find_element(By.NAME, 'email')
    email.send_keys("joeyt6570@gmail.com")
    pswd = driver.find_element(By.NAME, 'password')
    pswd.send_keys("@rshDEEP11")
    pswd.submit()
    time.sleep(4)


    #Clicking on the create post button ...this is part where i m facing a trouble
    createpost= driver.find_element(By.XPATH ,'//p[@id="content-region"]')
    createpost.click()
    createpost.innerhtml = "Hello world! This is my first post using Selenium Python."
    time.sleep(2)
    # //p[@id="content-region"]

 
    
    
  

# Close the browser
driver.quit()


















# sigin= driver.find_element(By.CLASS_NAME, 'basic-box-primary-action-button mighty-btn-square-large mighty-btn-filled-theme-color-button')
# sigin.click()
# https://wellthbuilders.mn.co/
# https://network-89217.mn.co/posts/35396109
# https://drippynews.mn.co/posts/35396117
# https://masses-of-entrepreneurs.mn.co/posts/35396125
# https://andrew-brown.mn.co/posts/35396135
# https://diy-vision.mn.co/spaces/9350067/feed
# https://digimac-technologies.mn.co/posts/35396145
# https://ground-breaker-media-group.mn.co/posts/35396152
# https://jomijomig.mn.co/posts/35396157
# https://curlebrity.mn.co/posts/35396166
# https://ultrasbook.mn.co/posts/35396170
# https://facial546.mn.co/posts/35396176
# https://yiff-scan-brasil.mn.co/posts/35396182
# https://itravel.mn.co/posts/35396190
# https://fnetchat.com/post/405184_to-find-the-ip-address-of-a-hp-printer-print-a-configuration-page-from-the-print.html
# https://coding-playground.mn.co/posts/35396228
# https://audiencemojo.mn.co/posts/35396234
# https://realfirefighters.mn.co/posts/35396248
# https://american-habits.mn.co/posts/35396254
# https://network-1061063.mn.co/posts/35396257
# https://pimpmyairgun.mn.co/posts/35396262
# https://freedomlifestyle.mn.co/posts/35396266
# https://tawasol1.mn.co/posts/35396270
# https://click-funnels.mn.co/posts/35396275
# https://network-21664.mn.co/posts/35396283
# https://network-43623.mn.co/posts/35396290
# https://edpt200.mn.co/posts/35396295
# https://jasa-seo.mn.co/posts/35396301
# https://globalaffairs.mn.co/posts/35396305
# https://sisters-and-brothers-networking.mn.co/posts/35396315
# https://wecanchat.mn.co/posts/35396320
# https://you-noob.mn.co/posts/35396324
# https://primal-dread.mn.co/posts/35396329
# https://good-stewards.mn.co/posts/35396353
# https://mjengomagazine.mn.co/spaces/9350493/feed
# https://chatclub.mn.co/posts/35396361
# https://ourownnetwork.mn.co/posts/35396370
# https://nethxt.mn.co/posts/35396381
# https://profilebook.mn.co/posts/35396407
# https://mighty-men.mn.co/posts/35396419
# https://productinn.mn.co/posts/35396424
# https://nordic-future.mn.co/posts/35396435
# https://facial546.mn.co/posts/35396440
# https://linkeei.com/post/95089_to-find-the-ip-address-of-a-hp-printer-print-a-configuration-page-from-the-print.html
# https://edpt200.mn.co/posts/35401554
# https://jasa-seo.mn.co/posts/35401568
# https://globalaffairs.mn.co/posts/35401574
# https://sisters-and-brothers-networking.mn.co/posts/35401577
# https://wecanchat.mn.co/posts/35401586
# https://you-noob.mn.co/posts/35401599
# https://primal-dread.mn.co/posts/35401611
# https://good-stewards.mn.co/posts/35401627
# https://mjengomagazine.mn.co/posts/35401632
# https://chatclub.mn.co/posts/35401636
# https://ourownnetwork.mn.co/posts/35401641
# https://infiniteabundance.mn.co/posts/35401659
# https://nethxt.mn.co/posts/35401665
# https://profilebook.mn.co/posts/35401670
# https://mighty-men.mn.co/posts/35401676
# https://productinn.mn.co/posts/35401682
# https://nordic-future.mn.co/posts/35401694
# https://facial546.mn.co/posts/35401704