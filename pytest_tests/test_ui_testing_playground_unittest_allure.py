import unittest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from UITestingPlaygroundPages import *


class TestPageUI(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome('./driver/chromedriver.exe')
        driver.maximize_window()
        self.driver = driver

    @allure.feature('UI Testing Playground')
    @allure.story('Starting MouseOver page test')
    def test_mouse_over_page(self):
        mouse_over_page = MouseOverHelper(self.driver, 'mouseover')
        with allure.step('MouseOver page opening'):
            mouse_over_page.go_to_site()
        with allure.step('Twice link clicking'):
            mouse_over_page.click_twice()
        with allure.step('Take a screenshot of the page with count of clicks'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Asserting of the expected result with gotten'):
            self.assertEqual(mouse_over_page.get_counter_value(), '2')

    @allure.feature('UI Testing Playground')
    @allure.story('Starting TextInput page test')
    def test_text_input_page(self):
        text_input_page = TextInputHelper(self.driver, 'textinput')
        with allure.step('TextInput page opening'):
            text_input_page.go_to_site()
        button_name = 'Some Button Name'
        with allure.step('Button name entering'):
            text_input_page.enter_button_name(button_name)
        with allure.step('Take a screenshot of the page with new button name'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Button name getting'):
            button_name_val = text_input_page.get_button_name()
        with allure.step('Asserting our button name with gotten'):
            self.assertEqual(button_name_val, button_name)

    @allure.feature('UI Testing Playground')
    @allure.story('Starting DynamicTable page test')
    def test_dynamic_table_page(self):
        dynamic_table_page = DynamicTableHelper(self.driver, 'dynamictable')
        with allure.step('DynamicTable page opening'):
            dynamic_table_page.go_to_site()
        with allure.step('Take a screenshot of the page with table & label'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Getting Chrome CPU load value from the table'):
            table_value = dynamic_table_page.get_table_chrome_cpu_load_value()
        with allure.step('Getting Chrome CPU load value from the label tag'):
            label_value = dynamic_table_page.get_label_chrome_cpu_load_value()
        with allure.step('Asserting the table value with the label value of Chrome CPU load'):
            self.assertEqual(table_value, label_value)

    @allure.feature('UI Testing Playground')
    @allure.story('Starting VerifyText page test')
    def test_verify_text_page(self):
        verify_text_page = VerifyTextHelper(self.driver, 'verifytext')
        with allure.step('VerifyText page opening'):
            verify_text_page.go_to_site()
        with allure.step('Text getting for verification'):
            text = verify_text_page.get_text()
        with allure.step('Asserting the expected value with gotten'):
            self.assertEqual(text, 'Welcome UserName!')

    @allure.feature('UI Testing Playground')
    @allure.story('Starting ProgressBar page test')
    def test_progress_bar_page(self):
        progress_bar_page = ProgressBarHelper(self.driver, 'progressbar')
        with allure.step('ProgressBar page opening'):
            progress_bar_page.go_to_site()
        with allure.step('Result value getting'):
            result = progress_bar_page.get_result()
        with allure.step('Take a screenshot of stopped progressbar'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Checking that progress bar were stopped at 75%'):
            self.assertEqual(result, '0')

    @allure.feature('UI Testing Playground')
    @allure.story('Starting Visibility page test')
    def test_visibility_page(self):
        visibility_page = VisibilityHelper(self.driver, 'visibility')
        with allure.step('Visibility page opening'):
            visibility_page.go_to_site()
        with allure.step('Clicking on "Hide" button'):
            visibility_page.hide_button_click()
        with allure.step('Visibility of "Removed" button checking'):
            self.assertFalse(visibility_page.removed_button_is_visible())
        with allure.step('Visibility of "Zero width" button checking'):
            self.assertFalse(visibility_page.zero_width_button_is_visible())
        with allure.step('Visibility of "Overlapped" button checking'):
            self.assertFalse(visibility_page.overlapped_button_is_visible())
        with allure.step('Visibility of "Zero opacity" button checking'):
            self.assertFalse(visibility_page.opacity_zero_button_is_visible())
        with allure.step('Visibility of "Hidden visibility" button checking'):
            self.assertFalse(visibility_page.visibility_hidden_button_is_visible())
        with allure.step('Visibility of "None displayed" button checking'):
            self.assertFalse(visibility_page.display_none_button_is_visible())
        with allure.step('Visibility of "Offscreen" button checking'):
            self.assertFalse(visibility_page.offscreen_button_is_visible())

    @allure.feature('UI Testing Playground')
    @allure.story('Starting SampleApp page test')
    def test_sample_app_page(self):
        sample_app_page = SampleAppHelper(self.driver, 'sampleapp')
        with allure.step('SampleApp page opening'):
            sample_app_page.go_to_site()
        username = 'TestUser'
        with allure.step('Login in with "TestUser" as username and "pwd" as password'):
            sample_app_page.login(username)
        with allure.step('take a screenshot of the page with an authorized user'):
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
        with allure.step('Welcome message getting'):
            welcome_message = sample_app_page.get_success_message_username()
        with allure.step('Asserting the welcome message with the expected message'):
            self.assertEqual(welcome_message, f'Welcome, {username}!')

    @allure.feature('UI Testing Playground')
    @allure.story('Starting NBSP page test')
    def test_nbsp_page(self):
        nbsp_page = NonBreakingSpaceHelper(self.driver, 'nbsp')
        with allure.step('NBSP page opening'):
            nbsp_page.go_to_site()
        with allure.step('Checking that the button are non-accessible via locator without nbsp'):
            self.assertFalse(nbsp_page.space_button_is_exist())
        with allure.step('Checking that the button are accessible via locator with nbsp'):
            self.assertTrue(nbsp_page.nbsp_button_is_exist())

    @allure.feature('UI Testing Playground')
    @allure.story('Starting ScrollBars page test')
    def test_scroll_bars_page(self):
        scroll_bars_page = ScrollBarsHelper(self.driver, 'scrollbars')
        with allure.step('ScrollBars page opening'):
            scroll_bars_page.go_to_site()
        with allure.step('Automated scrolling and click on the button'):
            result = scroll_bars_page.button_click()
        with allure.step('Checking that click on the button were successful'):
            self.assertTrue(result)

    @allure.feature('UI Testing Playground')
    @allure.story('Starting DynamicID page test')
    def test_dynamic_id_page(self):
        dynamic_id_page = DynamicIDHelper(self.driver, 'dynamicid')
        with allure.step('DynamicID page opening'):
            dynamic_id_page.go_to_site()
        with allure.step('Click on the button with dynamic id'):
            result = dynamic_id_page.button_click()
        with allure.step('Checking that click on button were successful'):
            self.assertTrue(result)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
