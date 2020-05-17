from selenium import webdriver

import random
import time

browser = webdriver.Firefox()


#You need to modify the url based on which topic you would like to work with. In this case, the title is mustafa kemal atatürk in EksiSozluk. The url indicates that issue.

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="

pageCount = 1

entries = []

entryCount = 1


while pageCount <= 10: # In this case, this script will take the entries that are under first 10 pages. You can change this value as any page of number that you want.

    
    newUrl = url + str(pageCount)

    browser.get(newUrl)

    elements = browser.find_elements_by_css_selector(".content")

    for element in elements:
        entries.append(element.text)

    time.sleep(2)

    pageCount += 1


# You need to change the name of the file. This file will contain entries that you would like to see after running the script.

with open("entries_ALL35.txt","w",encoding = "UTF-8") as file:

    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("*************************\n")
        entryCount += 1




browser.close()

