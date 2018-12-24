import requests, bs4
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
try:
    binary = FirefoxBinary('/home/zubair/Downloads/firefox/firefox')
    br = webdriver.Firefox(firefox_binary=binary)
    respons = requests.get('https://www.goodreads.com/quotes')
    respons.raise_for_status()
    bsstring= bs4.BeautifulSoup(respons.text)
    elemens = bsstring.select('.quotes .quote .quoteDetails .quoteText')
    br.get('http:/meanis1.sarahah.com')
    for i in elemens:
        pg = br.find_element_by_id('Send')
        tx = br.find_element_by_id('Text')
        tx.clear()
        tx.send_keys(i.getText())
        pg.click()
        element = WebDriverWait(br, 10).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "text-inherit"),"Thank you for your honesty :)"))
        br.back()
except Exception as exc:
    print('error'+exc.msg)
