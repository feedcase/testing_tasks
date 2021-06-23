import unittest
from selenium import webdriver
import os

from UITestingPlaygroundPages import *


class TestPageUI(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):

        # capabilities = {
        #     "browserName": "chrome",
        #     "browserVersion": "90.0",
        #     "selenoid:options": {
        #         "enableVNC": True,
        #         "enableVideo": False
        #     }
        # }
        #
        # driver = webdriver.Remote(
        #     command_executor="http://localhost:4444/wd/hub",
        #     desired_capabilities=capabilities)
        driver_location = '/usr/bin/chromedriver'
        binary_location = '/usr/bin/google-chrome'
        options = webdriver.ChromeOptions()
        options.binary_location = binary_location
        driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)
        driver.maximize_window()
        cls.driver = driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_mouse_over_page(self):
        mouse_over_page = MouseOverHelper(self.driver, 'mouseover')
        mouse_over_page.go_to_site()
        mouse_over_page.click_twice()
        self.assertEqual(mouse_over_page.get_counter_value(), '2')

    def test_text_input_page(self):
        text_input_page = TextInputHelper(self.driver, 'textinput')
        text_input_page.go_to_site()
        button_name = 'Some Button Name'
        text_input_page.enter_button_name(button_name)
        button_name_val = text_input_page.get_button_name()
        self.assertEqual(button_name_val, button_name)

    def test_dynamic_table_page(self):
        dynamic_table_page = DynamicTableHelper(self.driver, 'dynamictable')
        dynamic_table_page.go_to_site()
        table_value = dynamic_table_page.get_table_chrome_cpu_load_value()
        label_value = dynamic_table_page.get_label_chrome_cpu_load_value()
        self.assertEqual(table_value, label_value)

    def test_verify_text_page(self):
        verify_text_page = VerifyTextHelper(self.driver, 'verifytext')
        verify_text_page.go_to_site()
        self.assertEqual(verify_text_page.get_text(), 'Welcome UserName!')

    def test_progress_bar_page(self):
        progress_bar_page = ProgressBarHelper(self.driver, 'progressbar')
        progress_bar_page.go_to_site()
        result = progress_bar_page.get_result()
        self.assertEqual(result, '0')

    def test_visibility_page(self):
        visibility_page = VisibilityHelper(self.driver, 'visibility')
        visibility_page.go_to_site()
        visibility_page.hide_button_click()
        self.assertFalse(visibility_page.removed_button_is_visible())
        self.assertFalse(visibility_page.zero_width_button_is_visible())
        self.assertFalse(visibility_page.overlapped_button_is_visible())
        self.assertFalse(visibility_page.opacity_zero_button_is_visible())
        self.assertFalse(visibility_page.visibility_hidden_button_is_visible())
        self.assertFalse(visibility_page.display_none_button_is_visible())
        self.assertFalse(visibility_page.offscreen_button_is_visible())

    def test_sample_app_page(self):
        sample_app_page = SampleAppHelper(self.driver, 'sampleapp')
        sample_app_page.go_to_site()
        username = 'TestUser'
        sample_app_page.login(username)
        self.assertEqual(sample_app_page.get_success_message_username(), f'Welcome, {username}!')

    def test_nbsp_page(self):
        nbsp_page = NonBreakingSpaceHelper(self.driver, 'nbsp')
        nbsp_page.go_to_site()
        self.assertFalse(nbsp_page.space_button_is_exist())
        self.assertTrue(nbsp_page.nbsp_button_is_exist())

    def test_scroll_bars_page(self):
        scroll_bars_page = ScrollBarsHelper(self.driver, 'scrollbars')
        scroll_bars_page.go_to_site()
        result = scroll_bars_page.button_click()
        self.assertTrue(result)

    def test_dynamic_id_page(self):
        dynamic_id_page = DynamicIDHelper(self.driver, 'dynamicid')
        dynamic_id_page.go_to_site()
        result = dynamic_id_page.button_click()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
