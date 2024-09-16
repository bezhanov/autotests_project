import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.links import Links
from base.base_page import BasePage

class DashboardPage(BasePage):

  PAGE_URL = Links.DASHBOARD_PAGE

  MY_INFO_BUTTON = ("xpath", "//span[text()='My Info']")

  @allure.step("Click on 'My Info' link")
  def click_my_info_link(self):
    self.wait.until(EC.element_to_be_clickable(self.MY_INFO_BUTTON)).click()