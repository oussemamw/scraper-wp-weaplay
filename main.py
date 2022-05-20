from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()
driver.get('https://www.weaplay.com/')
driver1 = webdriver.Chrome()




def carawl(link):

    driver1.get(link)
    time.sleep(4)
    e = driver1.find_element_by_class_name("td-post-content")
    download_link = e.find_elements_by_tag_name("a")
    
    driver1.get(download_link[1].get_attribute("href"))
    time.sleep(7)
    e = driver1.find_element_by_class_name("col-md-8")
    download_link = e.find_element_by_tag_name("a").get_attribute("href")
    
    
    name=random.randrange(20, 5000, 3)
    f = open(str(name)+".txt", "a")
    
        
    f.write("%s\n" % download_link)
    f.close()
    
    
    print('Done')
counter=1   
while True:
    links = driver.find_elements_by_class_name("td-module-meta-info")
    
    for i in links:
        try:
            l=i.find_element_by_tag_name('a').get_attribute("href")
            carawl(l)
            time.sleep(5)
        except:
            print(l)


    counter=counter+1
    driver1.get("https://www.weaplay.com/page/"+str(counter))
    
    time.sleep(5)




