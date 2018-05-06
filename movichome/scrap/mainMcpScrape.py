import selenium
from movichome import models
from django.shortcuts import render
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class mcp:
    def scrapeItem(self, userkeyword):
        #userkeyword = input("\nEnter keyword to search here : ")
        #print(userkeyword)

        mcpDefinition_1 = ""
        mcpDefinition_2 = ""

        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1200x600')
        driver = webdriver.Chrome(chrome_options=options)

        #initial webdriver and go to url
        driver.get('http://mcp.anu.edu.au/Q/standard.html')

        #find the checkbox and tick
        element = driver.find_element_by_xpath('//*[@id="wrap2"]/x/form/div/div[1]/table/tbody/tr[1]/td[2]/input').click()

        #find the search box and send keys
        element = driver.find_element_by_xpath('//*[@id="wrap2"]/x/form/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/input')
        element.send_keys(userkeyword)
        element = driver.find_element_by_xpath('//*[@id="wrap2"]/x/form/div/div[2]/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/input').click()

        #Scrape the data and display
        words_list = driver.find_element_by_xpath('//*[@id="wrap2"]/div[2]/pre')
        print(words_list.text)

        #for i in words_list():
            

        #Scrape the data and display(words_text)
        words_texts = driver.find_element_by_xpath('//*[@id="wrap2"]/div[4]/pre')
        print(words_texts.text)

        mcpDefinition_1 = words_list.text
        mcpDefinition_2 = words_texts.text
        models.PageScrape.objects.create(description=mcpDefinition_1,description_2=mcpDefinition_2)
        return
