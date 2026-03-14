import unittest
from selenium import webdriver

class BaseTest(unittest.TestCase):


    def setUp(self):
        # Initial preconditions
        # 1. Main page is opened
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/index.php")

    def test_open_page(self):
        # simple assertion to keep browser open long enough to verify title/url
        self.assertIn("localhost", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

