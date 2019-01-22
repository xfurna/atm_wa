from selenium import webdriver
import targets
from selenium.webdriver.common.keys import Keys

def drive():
    a = webdriver.Firefox()
    a.get("https://web.whatsapp.com/")
    input("CONTINUE-")
    for i in range(len(targets.recipient)):
        to = a.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/input')
        to.click()
        to.send_keys(targets.recipient[i])
        to.send_keys(Keys.RETURN)
        hr = a.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
        hr.send_keys(targets.msg)
        hit = a.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
        hit.click()
        a.close()
