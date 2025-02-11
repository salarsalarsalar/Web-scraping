# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestUniversity3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_university3(self):
    self.driver.get("https://www.eduvision.edu.pk/programs-offered-in-engineering-at-bachelor-level-in-pakistan")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Medical Sciences']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Technical']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Computer Sciences & Information Technology']").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4) > .img-responsive")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Management Sciences']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Social Sciences']").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4) > .img-responsive")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Biological & Life Sciences']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Chemical & Material Sciences']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Physics & Numerical Sciences']").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(4) > .img-responsive")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Earth & Environmental Sciences']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Agricultural Sciences']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Religious Studies']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Art & Design']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Media Studies']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Commerce / Finance & Accounting']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Education']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Languages']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Training']").click()
    self.driver.find_element(By.NAME, "Submit").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    self.driver.find_element(By.NAME, "subLevel").click()
    self.driver.find_element(By.NAME, "disciplineType").click()
    dropdown = self.driver.find_element(By.NAME, "disciplineType")
    dropdown.find_element(By.XPATH, "//option[. = 'Professional Other']").click()
    self.driver.find_element(By.NAME, "Submit").click()
  
