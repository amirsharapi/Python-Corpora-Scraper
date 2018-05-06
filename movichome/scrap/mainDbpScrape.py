import selenium
from movichome import models
from django.shortcuts import render
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class dbp:
    def scrapeItem(self, userkeyword):
        # userkeyword = input("\nEnter keyword to search here : ")
        # print(userkeyword)

        dbpDefinition = ""

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('window-size=1200x600')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get('http://prpm.dbp.gov.my/')

        #find the search box and prompt the word
        element = driver.find_element_by_xpath('//*[@id="MainContent_txtCarian"]')
        element.send_keys(userkeyword)

        #Scrape the data and display and done!
        element = driver.find_element_by_xpath('//*[@id="MainContent_cmd_search"]').click()
        word_definition = driver.find_element_by_xpath('//*[@id="1"]')
        dbpDefinition = word_definition.text
        print("Result dia "+dbpDefinition)
        models.PageScrape.objects.create(description=dbpDefinition)
        return dbpDefinition



        
        
