# Selenium-Taking-AllEntries-in-Eksisozluk

Using Selenium to take entries under a specific title in EksiSozluk. (Learn-by-doing mini project)
In this case which is "mustafa kemal atatürk" title in EksiSozluk. 


You need to install;
  * FireFox Web Browser
  * Gecko Driver (https://github.com/mozilla/geckodriver/releases)
  * Selenium (pip install selenium)
  * Python
  
In addition, you need to add the directory of geckodriver.exe(comes from the extraction of zip file) to PATH variable. Otherwise, It won't work.

+ eksisozluk_title_take_entries.py = It would be better if you look at the code and modify it based on your needs ;

  title = you need to modify the url based on the explanation that was mentioned on the code as a comment.
  
  pageNumber = you can modify the pageNumber in while loop(as mentioned on the code). If you update this value as current number of pages in Eksisozluk, you will get all the entries under a specific title.
  

+ txt file = This script will contain all the entries under a specific title that you are selected. Do not forget to modify the url.

  I tried to explain the steps with comments in eksisozluk_title_take_entries.py. Happy Coding!
