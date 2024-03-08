from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

LINK_TO_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSf9Z0_Fq9CjVYG0jH-ic3lVGOppF7zhfBlKQ-H4YqQhJaCJlQ/viewform?usp=sf_link"

website = requests.get(url="https://appbrewery.github.io/Zillow-Clone/").text

soup = BeautifulSoup(website,"html.parser")

prices = [x.text[:6] for x in soup.find_all("span", class_ = "PropertyCardWrapper__StyledPriceLine" )]
address = [x.text.strip().replace("|","") for x in soup.find_all("address")]
links = [x['href'] for x in soup.select(".property-card-link")]


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url=LINK_TO_FORM)



for i in range(len(prices)):
    time.sleep(3)
    price_button = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    address_button = driver.find_element(By.XPATH,
                                         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    property_link_button = driver.find_element(By.XPATH,
                                               '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    price_button.send_keys(prices[i])
    address_button.send_keys(address[i])
    property_link_button.send_keys(links[i])
    submit_button.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.refresh()


