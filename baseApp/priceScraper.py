

import requests #pip install requests
from bs4 import BeautifulSoup   #pip install bs4
import csv
from datetime import datetime
import parse    #pip install parse
from selenium import webdriver  #pip install selenium, then copy chromedriver.exe to the same folder
import time
import re


imgRootpath_chemist = 'https://static.chemistwarehouse.com.au/ams/media/pi'
imgRootpath_regex = re.compile(imgRootpath_chemist)

def getStockPrice(urlPath):
    driver = webdriver.Chrome()
    driver.get(urlPath)
    #driver.refresh()
    time.sleep(20)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    htmlFile = open('chemist.txt','w+', encoding='utf-8')
    htmlFile.write(soup.prettify())

    sticker = ''
    #tr_target = 'tr' + str(sticker)
    a_tag_list = soup.find_all('a', {'class':"product-container"})  #locate all a with class = ''
    
    #initiate a empty list of products
    product_list = []
    #now, find data from each a_tag object from the above list
    if a_tag_list:  #if the list was found
        #iterate the list and save info into product_list
        for a_tag in a_tag_list:
            try:

                product_name_list = a_tag.find_all('div', {'class':'product-name'})
                if product_name_list:
                    product_name = product_name_list[0].text
                else:
                    product_name = "Unkown_product_name"
                    
                product_current_price_list = a_tag.find_all('span', {'class':'Price'})
                if product_current_price_list:
                    product_current_price = product_current_price_list[0].text
                    
                else:
                    product_current_price = 'unkown_price'

                product_save_price_list = a_tag.find_all('span', {'class':'Save'})
                if product_save_price_list:
                    product_save_price = product_save_price_list[0].text
                    
                else:
                    product_save_price = 'unknown_save_price'

                #imgSrcList = a_tag.find_all('img', {'src': re.compile('*\/hero_150.jpg')})
                #if imgSrcList:
                #    product_image_url = imgSrcList[0]['src']
                #else:
                #    product_image_url = 'unkonw_image_url'
                product_list.append([product_name,product_current_price,product_save_price])
            except AttributeError:
                print('cannot find infor for this div')
        #receivedTime = datetime.now().strftime("%H:%M:%S")
        #stockData = [receivedTime]
        #for i in range(0, len(tdtag)):
        #    stockData.append(tdtag[i].text)
    else:
        print('can not find the div with class = "Product"')
    
    return product_list

def main():
    chemist_vitatmin_url = ("http://www.chemistwarehouse.com.au/Shop-Online/81/Vitamins")
    vitamin_product_list = getStockPrice(chemist_vitatmin_url)
    file = open('vitamine.txt','a+', encoding='utf-8')
    for product in vitamin_product_list:
        for info in product:
            file.write("%s\t" % info)  
            file.write('\n')
            
    file.close()
   
    
main()

   



