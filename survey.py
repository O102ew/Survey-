import schedule
import time
from selenium import webdriver


def automated_survey():
    web = webdriver.Chrome()
    web.get("https://es.elarabygroup.com/Closed.aspx")
    time.sleep(5)

    variable1 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_radio_emp_type"]/tbody/tr[1]/td/label')
    variable1.click()
    time.sleep(5)

    variable2 = 80001718
    variable3 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_txt_username"]')
    variable3.send_keys(variable2)
    time.sleep(5)

    variable4 = '007783'
    variable5 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_TXT_CDOE"]')
    variable5.send_keys(variable4)
    time.sleep(3)
    variable1 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_btn_login"]')
    variable1.click()
    time.sleep(3)

    Question1 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_ANSWER_1_0"]')
    Question1.click()
    time.sleep(5)

    Question2 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_ANSWER_3_0"]')
    Question2.click()
    time.sleep(5)

    Question3 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_ANSWER_5_0"]')
    Question3.click()
    time.sleep(5)
    Question4 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_ANSWER_7_0"]')
    Question4.click()
    time.sleep(5)

    variable11 = web.find_element_by_xpath(
        '//*[@id="ContentPlaceHolder1_btn_Finish"]')
    variable11.click()


 schedule.every(1).day.at('15:40').do(automated_survey)
 while True:
    # schedule.run_pending()
    # time.sleep(3)

automated_survey()
