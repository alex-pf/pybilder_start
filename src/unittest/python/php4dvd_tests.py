# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestLoginAddDvdRmDvdLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_add_dvd_rm_dvd_logout(self):
        driver = self.driver
        # Простая проверка авторизации
        driver.get("http://192.168.2.1/php4dvd/")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("My profile").click()
        # Убедились - в h2 страницы есть имя пользователя под которым мы вошли
        self.assertEqual("Edit admin", driver.find_element_by_css_selector("h2").text)
        # Уходим на домашнюю страницу
        driver.find_element_by_link_text("Home").click()
        # Проверка функционала добавления фильма в коллекцию
        # К началу теста мы должны быть авторизованы и на домашней странице
        driver.find_element_by_css_selector("img[alt=\"Add movie\"]").click()
        # Ищем фильм в базе
        driver.find_element_by_id("imdbsearch").clear()
        driver.find_element_by_id("imdbsearch").send_keys("space")
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.find_element_by_link_text("Space").click()
        # Выбрали фильм и сохранили
        driver.find_element_by_css_selector("img[alt=\"Save\"]").click()
        # Переходим на домашнюю страницу
        driver.find_element_by_link_text("Home").click()
        # Убедились - появилась плашка с фильмом
        self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='results']/a/div"))
        # Убедились - название фильма соответствует
        self.assertEqual("Space", driver.find_element_by_xpath("//a/div/div[2]").text)
        # Проверка функционала удаления фильма из коллекции
        # До начала теста мы должны быть авторизованы, фильм должен быть в коллекции, начало теста на домашней странице
        driver.find_element_by_link_text("Home").click()
        driver.find_element_by_xpath("//a/div/div/div").click()
        driver.find_element_by_css_selector("img[alt=\"Remove\"]").click()
        # Подтвердили что хотим удалить фильм
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to remove this[\s\S]$")
        # Вернулись на домашнюю страницу
        driver.find_element_by_link_text("Home").click()
        # Убедились - фильмов в коллекции нет, обновили данные, проверили ещё раз
        # ERROR: Caught exception [ERROR: Unsupported command [getElementIndex | //div[@id='results']/a/div | ]]
        driver.find_element_by_css_selector("img[alt=\"Update all\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [getElementIndex | //div[@id='results']/a/div | ]]
        driver.find_element_by_link_text("Home").click()
        # Проверка функционала выхода
        # На момент начала теста мы должны быть авторизованы под admin
        driver.find_element_by_link_text("My profile").click()
        # Убедились - мы авторизованы под admin
        self.assertEqual("Edit admin", driver.find_element_by_xpath("//h2").text)
        driver.find_element_by_link_text("Log out").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^Are you sure you want to log out[\s\S]$")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

