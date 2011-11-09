from unittest.case import TestCase
from meld3.example import element
from selenium import webdriver
from selenium.webdriver.common.by import By
from func_tests.database_manager import DatabaseManager


class TestAddProgrammer(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        dbmanager = DatabaseManager()
        dbmanager.delete_programmers()
        dbmanager.delete_pair_stairs()
        self.driver.close()
        
    def go_to_add_programmer_page(self):
        self.driver.get("http://localhost:8000/add_programmer")

    def add_programmer(self, programmer_name):
        #add name
        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_name')
        programmer_name = programmer_name
        element.send_keys(programmer_name)
        #click on submit
        self.driver.find_element(By.CSS_SELECTOR, '#add_programmer').click()

    def test_should_render_to_add_programmer_page(self):
        #Go to page
        self.go_to_add_programmer_page()
        self.assertEqual(self.driver.title, "Add one programmer")
        self.add_programmer('susan')
        
        #add another programmer
        self.go_to_add_programmer_page()
        self.add_programmer('aimee')
        #Assert Pair Stairs is displayed
        self.driver.get("http://localhost:8000/stairs")
        self.assertIn('susan', self.get_programmers())
        self.assertIn('aimee', self.get_programmers())
        self.assertEqual('0', self.get_times_of_pairs(first = 'susan', second = 'aimee'))

    def test_pairing_times_should_increase_one_when_click_pair(self):
        self.go_to_add_programmer_page()
        self.add_programmer('susan')
        
        self.go_to_add_programmer_page()
        self.add_programmer('aimee')

        self.driver.get("http://localhost:8000/stairs")
        element = self.driver.find_element(By.CSS_SELECTOR, '#susan_aimee')
        old_times = int(element.text)
        element.click()
        self.assertEqual(int(element.text), old_times+1)

        self.driver.get("http://localhost:8000/stairs")
        element = self.driver.find_element(By.CSS_SELECTOR, '#susan_aimee')
        self.assertEqual(int(element.text), old_times+1)


    def get_programmers(self):
        members = []
        member_elements = self.driver.find_elements(By.CSS_SELECTOR, '.programmer_name')
        if member_elements:
            for member_element in member_elements:
                members.append(member_element.text)
        return members

    def get_times_of_pairs(self, first, second):
        element = self.driver.find_element(By.CSS_SELECTOR, '#'+first+'_'+second)
        return element.text

#        element = self.driver.find_element(By.CSS_SELECTOR, '#programmer_name')

        