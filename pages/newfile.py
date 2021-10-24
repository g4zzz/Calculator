
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def main():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    frst_elem = driver.find_element_by_xpath("""//input[@class='gLFyf gsfi']""")
    frst_elem.send_keys("калькулятор")
    time.sleep(3)
    frst_elem.send_keys(Keys.ENTER)
    time.sleep(3)
    calc_elem = driver.find_element_by_xpath("""//div[@class='jlkklc']""")
    calc_elem.send_keys('1*2-3+1')
    time.sleep(2)


    time.sleep(3)
    search = driver.find_element_by_xpath("""//div[@class="XRsWPe UUhRt"]""")
    search.click()
    time.sleep(3)
    num1 = driver.find_element_by_xpath("""//span[@class='vUGUtc']""").text
    num2 = driver.find_element_by_xpath("""//span[@id='cwos']""").text
    return num1, num2

if __name__ == "__main__":
    main()


