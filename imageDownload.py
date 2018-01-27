import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','chemist.settings')
import django
django.setup()

#import for the scripts
import requests #pip install requests
from bs4 import BeautifulSoup   #pip install bs4
import csv
from datetime import datetime
import parse    #pip install parse
from selenium import webdriver  #pip install selenium, then copy chromedriver.exe to the same folder
import time
import re
import urllib.request


#import from app within project
from products.models import Product
from categories.models import Category

def getImagePathFromDatabase():
    productObject = Product.objects.get(productId = '50597')
    imagePath = productObject.imagePath

def imageDownload():
    productObjectList = list(Product.objects.all())
    if productObjectList:
        for productObject in productObjectList:
            time.sleep(0.5)
            try:        
                imagePath = str(productObject.imagePath)
                print(imagePath)
                productCategory = productObject.category
                categoryName = productCategory.name #call object and get its name
                categoryName = str(categoryName.replace(' ',''))    #remove unwanted space
                print(productCategory)
                
                #user regex to get the name of image (05 digits) from the imagePath
                myCompile = re.compile('[\d]{5}')
                mySearch = myCompile.search(imagePath)
                imageFileName = mySearch.group(0) + '.jpg'
                print(imageFileName)    

                imageSavePath = 'static/media/products/' + str(categoryName).lower() + '/images/' + imageFileName
                print(imageSavePath)
                data = urllib.request.urlopen(imagePath).read()
                if data:                    
                    with open( imageSavePath, "wb" ) as code :
                        code.write( data )
                else:
                    pass
            except:
                pass
    else:
        print('no object found')
def setImagePathForProduct():
    productObjectList = list(Product.objects.all())
    if productObjectList:
        for productObject in productObjectList:
            time.sleep(0.5)
            try:        
                productCategory = productObject.category
                categoryName = productCategory.name #call object and get its name
                categoryName = str(categoryName.replace(' ',''))    #remove unwanted space
                print(categoryName)
               
                imageName = str(productObject.productId) + '.jpg'               
                newimagePath = 'products/' + str(categoryName).lower() + '/images/' + imageName
                print(newimagePath)
                
                #set Product.imagePath, then save it
                productObject.imagePath.name = newimagePath
                productObject.save()
            except:
                print('something wrong here need to be fixed')
    else:
        print('no object found')

def main():
   

    #url = 'https://static.chemistwarehouse.com.au/ams/media/pi/50597/hero_150.jpg'
    #imageDownload()    #done already
    setImagePathForProduct()


main()

