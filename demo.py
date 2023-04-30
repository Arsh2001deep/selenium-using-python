
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
# PATH="C:/Users/Asus/OneDrive/Desktop/chromedriver.exe"


# driver = webdriver.Chrome(PATH)
# driver.get('http://www.google.com/')


# chatgpt
import openai



openai.api_key = "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"
response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": "write a summmary in one para on How to fix HP printer offline? "}],
        temperature=.7,
    )

# print(response['choices'][0]['message']['content'])



chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get('https://diggo.wtguru.com/submit/')
# print(driver.title)

time.sleep(2)
# driver--.quit()
# element= driver.find_element_by_xpath('//*[@id="primary_menus"]/ul/li[2]/a').sendKeys
# element.click()
# time.sleep(2)


# PRINT response['choices'][0]['message']['content']

url = driver.find_element(By.NAME, 'storyurl')
url.send_keys("https://printersofflines.com/hp-printer-support/")
submiturl= driver.find_element(By.CLASS_NAME, 'btn')
submiturl.click()
# 2nd page
time.sleep(7)
title = driver.find_element(By.NAME, 'storytitle')
title.send_keys("How to fix HP printer offline?")
content = driver.find_element(By.NAME, 'storydesc')
content.send_keys(response['choices'][0]['message']['content'])
tags = driver.find_element(By.NAME, 'storytags')
tags.send_keys("hp printer offline support")
tags.submit()
outputbook=driver.current_url
# print(outputbook)


x = outputbook.split("?")

# print(x,end='\n\n\n')

# print(x[1])



flinks = ["https://links.wtguru.com/submit/",
"https://digg.wtguru.com/submit/",
"https://story.wtguru.com/submit/",
"https://story.wtguru.com/submit/",
"https://stumble.wtguru.com/submit/",
"https://social.wtguru.com/submit/",
"https://bookmark.wtguru.com/submit/",
"https://diggo.wtguru.com/submit/",
"https://news.wtguru.com/submit/",
"https://seo.wtguru.com/submit/"]
# for y in flinks:
#   print(y,"?", x[1], sep="",end='\n\n')

  # Open the file in write mode
with open("output.txt", "a") as file:
    # Loop through numbers from 1 to 10
    # for i in range(1, 11):
        for y in flinks:
        # Write the number to the file
          dem= y+"?"+ x[1] + "\n"
          file.write(dem)
          

driver.quit()