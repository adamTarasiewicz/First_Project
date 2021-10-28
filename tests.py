import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://kamil.kwapisz.pl/")
driver.maximize_window()


class TestMainPage(unittest.TestCase):

    def test_check_site_branding_Texts(self):
        title = driver.find_element(By.CLASS_NAME, "site-title").text
        description = driver.find_element(By.CLASS_NAME, "site-description").text

        # verify
        self.assertEqual('KAMIL KWAPISZ', title)
        self.assertEqual('Blog o programowaniu, technologii i biznesie', description)

    def test_check_navbar_container(self):
        main_page_text = driver.find_element(By.ID, "menu-item-28").text
        about_me = driver.find_element(By.ID, "menu-item-30").text
        contact = driver.find_element(By.ID, "menu-item-29").text
        courses = driver.find_element(By.ID, "menu-item-1002").text
        scrape_up = driver.find_element(By.ID, "menu-item-1214").text

        # verify
        self.assertEqual(main_page_text, 'STRONA GŁÓWNA')
        self.assertEqual(about_me, 'O MNIE')
        self.assertEqual(contact, 'KONTAKT')
        self.assertEqual(courses, 'SZKOLENIA')
        self.assertEqual(scrape_up, 'SCRAPEUP')


if __name__ == "__main__":
    unittest.main()
