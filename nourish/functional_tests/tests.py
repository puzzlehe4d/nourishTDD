from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# isolation in between tests
from django.test import LiveServerTestCase

class NewUserTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        #allow for browser to load (for now)
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('fridge_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_create_a_persisted_storage(self):
        self.browser.get(self.live_server_url)

        #User can add groups; enter fridge name in input and see it in table
        input_box = self.browser.find_element_by_id('id_new_fridge') 
        input_box.send_keys('Fridge_user1')

        #when Enter is hit, user is taken to a new url where the Fridge list exists 
        input_box.send_keys(Keys.ENTER)
        user1_fridge_url = self.browser.current_url
        self.assertRegex(user1_fridge_url, '/fridges/.+')
        title = self.browser.find_element_by_tag_name('title').text
        self.assertIn(title, 'Fridge_user1')

        self.browser.quit()
        self.browser = webdriver.Firefox()

        self.browser.get(self.live_server_url)
        # page_text = self.browser.find_element_by_tag_name('body').text
        # self.assertNotIn('Fridge_user1', page_text)

        input_box = self.browser.find_element_by_id('id_new_fridge')     
        input_box.send_keys('Fridge_user2')

        #when Enter is hit, user is taken to a new url where the Fridge list exists 
        input_box.send_keys(Keys.ENTER)

        user2_fridge_url = self.browser.current_url
        self.assertRegex(user1_fridge_url, '/fridges/.+')
        self.assertNotEqual(user2_fridge_url, user1_fridge_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Fridge_user1', page_text)
        self.assertIn('Fridge_user2', page_text)


