from selenium import webdriver

import random
import time

browser = webdriver.Firefox()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1

entries = []

entryCount = 1


while pageCount <= 10:

    
    newUrl = url + str(pageCount)

    browser.get(newUrl)

    elements = browser.find_elements_by_css_selector(".content")

    for element in elements:
        entries.append(element.text)

    time.sleep(2)

    pageCount += 1


with open("entries_ALL35.txt","w",encoding = "UTF-8") as file:

    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("*************************\n")
        entryCount += 1



    

"""
for entry in entries:
    print(str(entryCount) + "*********************************")
    print(element.text)
    entryCount += 1
"""

browser.close()
#browser.get(url)

#time.sleep(5)


"""
elements = browser.find_elements_by_css_selector('.content')
"""
"""
for element in elements:
    print("*****************")
    print(element.text) #class'ın içindeki text'i yani entry'i alır.
"""

#browser.close()

