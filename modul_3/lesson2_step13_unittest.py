import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

data_test = ['Sergey',
             'Konoplev',
             'sergeyKonoplev@gmail.com']

class AutoTests(unittest.TestCase):
    def test_1(self, link="http://suninjuly.github.io/registration1.html"):
        link = link

        with webdriver.Chrome() as browser:
            browser.get(link)

            browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first name')]").send_keys(data_test[0])
            browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]").send_keys(data_test[1])
            browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys(data_test[2])
            sleep(1)

            browser.find_element(By.XPATH, '//button[@type="submit"]').click()
            self.assertEqual(browser.find_element(By.TAG_NAME, 'h1').text, 'Congratulations! You have successfully registered!', 'Something went wrong')

            sleep(2)
            browser.quit()

    def test_2(self):
        self.test_1("http://suninjuly.github.io/registration2.html")


if __name__ == '__main__':
    unittest.main()

