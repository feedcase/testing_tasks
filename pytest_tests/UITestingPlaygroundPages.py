from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TextInputLocators:
    LOCATOR_TEXT_INPUT = (By.XPATH, "/html//input[@id='newButtonName']")
    LOCATOR_BUTTON = (By.XPATH, "/html//button[@id='updatingButton']")


class DynamicIDLocators:
    LOCATOR_BUTTON = (By.XPATH, "/html//section//button[@class='btn btn-primary']")


class ScrollBarsLocators:
    LOCATOR_HIDING_BUTTON = (By.XPATH, "/html//button[@id='hidingButton']")


class DynamicTableLocators:
    LOCATOR_TASK_MANAGER_TABLE_ROWS = (By.XPATH, "/html//div[@role='rowgroup']/div[@role='row']")
    LOCATOR_CHROME_CPU = (By.XPATH, "/html//section//p[@class='bg-warning']")


class VerifyTextLocators:
    LOCATOR_CONTAINS_WELCOME = (By.XPATH, "//span[normalize-space(.)='Welcome UserName!']")


class ProgressBarLocators:
    LOCATOR_START_BUTTON = (By.XPATH, "/html//button[@id='startButton']")
    LOCATOR_STOP_BUTTON = (By.XPATH, "/html//button[@id='stopButton']")
    LOCATOR_RESULT = (By.XPATH, "/html//p[@id='result']")
    LOCATOR_PROGRESS_BAR = (By.XPATH, "/html//div[@id='progressBar']")


class VisibilityLocators:
    LOCATOR_HIDE_BUTTON = (By.XPATH, "/html//button[@id='hideButton']")
    LOCATOR_REMOVED_BUTTON = (By.XPATH, "/html//button[@id='removedButton']")
    LOCATOR_ZERO_WIDTH_BUTTON = (By.XPATH, "/html//button[@id='zeroWidthButton']")
    LOCATOR_OVERLAPPED_BUTTON = (By.XPATH, "/html//button[@id='overlappedButton']")
    LOCATOR_HIDING_LAYER = (By.XPATH, '//*[@id="hidingLayer"]')
    LOCATOR_OPACITY_ZERO_BUTTON = (By.XPATH, "/html//button[@id='transparentButton']")
    LOCATOR_VISIBILITY_HIDDEN_BUTTON = (By.XPATH, "/html//button[@id='invisibleButton']")
    LOCATOR_DISPLAY_NONE_BUTTON = (By.XPATH, "/html//button[@id='notdisplayedButton']")
    LOCATOR_OFFSCREEN_BUTTON = (By.XPATH, "/html//button[@id='offscreenButton']")


class SampleAppLocators:
    LOCATOR_SUCCESS_MESSAGE = (By.XPATH, "/html//label[@id='loginstatus']")
    LOCATOR_USERNAME_FIELD = (By.XPATH, "/html//section/div[@class='container']//input[@name='UserName']")
    LOCATOR_PASSWORD_FIELD = (By.XPATH, "/html//section/div[@class='container']//input[@name='Password']")
    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "/html//button[@id='login']")


class MouseOverLocators:
    LOCATOR_LINK = (By.XPATH, "/html//section//a[text()='Click me']")
    LOCATOR_CLICK_COUNTER = (By.XPATH, "/html//span[@id='clickCount']")


class NonBreakingSpaceLocators:
    LOCATOR_SPACE_BUTTON = (By.XPATH, "//button[text()='My Button']")
    LOCATOR_NBSP_BUTTON = (By.XPATH, "//button[text()='My\xa0Button']")


class TextInputHelper(BasePage):

    def enter_button_name(self, button_name):
        input_field = self.find_element(TextInputLocators.LOCATOR_TEXT_INPUT)
        input_field.click()
        input_field.send_keys(button_name)
        button = self.find_element(TextInputLocators.LOCATOR_BUTTON)
        button.click()

    def get_button_name(self):
        return self.find_element(TextInputLocators.LOCATOR_BUTTON).text


class ScrollBarsHelper(BasePage):

    def button_click(self):
        button = self.find_element(ScrollBarsLocators.LOCATOR_HIDING_BUTTON)
        button.click()
        return True


class DynamicIDHelper(BasePage):

    def button_click(self):
        button = self.find_element(DynamicIDLocators.LOCATOR_BUTTON)
        button.click()
        return True


class DynamicTableHelper(BasePage):

    def get_table_chrome_cpu_load_value(self):
        rows = self.find_elements(DynamicTableLocators.LOCATOR_TASK_MANAGER_TABLE_ROWS)
        col_headers = rows[0].text.split()
        col_number = [col_headers.index(val) for val in col_headers if val == 'CPU'][0]
        row_number = [rows.index(row) for row in rows if 'Chrome' in row.text][0]
        return self.find_element((By.XPATH, f"//div[@role='table']/div[3]/div[{row_number}]/span[{int(col_number)+1}]")).text

    def get_label_chrome_cpu_load_value(self):
        return self.find_element(DynamicTableLocators.LOCATOR_CHROME_CPU).text.split(':')[1].split()[0]


class VerifyTextHelper(BasePage):

    def get_text(self):
        return self.find_element(VerifyTextLocators.LOCATOR_CONTAINS_WELCOME).text


class ProgressBarHelper(BasePage):

    def get_result(self):
        start_button = self.find_element(ProgressBarLocators.LOCATOR_START_BUTTON)
        start_button.click()
        stop_button = self.find_element(ProgressBarLocators.LOCATOR_STOP_BUTTON)
        while True:
            progress_bar = self.find_element(ProgressBarLocators.LOCATOR_PROGRESS_BAR)
            if progress_bar.text == '75%':
                stop_button.click()
                return self.find_element(ProgressBarLocators.LOCATOR_RESULT).text.split(',')[0].split(':')[1].split()[0]


class VisibilityHelper(BasePage):

    def hide_button_click(self):
        button = self.find_element(VisibilityLocators.LOCATOR_HIDE_BUTTON)
        button.click()

    def removed_button_is_visible(self):
        try:
            button = self.find_element(VisibilityLocators.LOCATOR_REMOVED_BUTTON)
        except:
            return False

    def zero_width_button_is_visible(self):
        button = self.find_element(VisibilityLocators.LOCATOR_ZERO_WIDTH_BUTTON)
        width = button.value_of_css_property('width')
        if width == '0px':
            return False

    def overlapped_button_is_visible(self):
        layer = self.find_element(VisibilityLocators.LOCATOR_HIDING_LAYER)
        styles = layer.get_property('style')
        if 'left' in styles and 'top' in styles:
            return False

    def opacity_zero_button_is_visible(self):
        button = self.find_element(VisibilityLocators.LOCATOR_OPACITY_ZERO_BUTTON)
        opacity = button.value_of_css_property('opacity')
        print(opacity)
        if opacity == '0':
            return False

    def visibility_hidden_button_is_visible(self):
        button = self.find_element(VisibilityLocators.LOCATOR_VISIBILITY_HIDDEN_BUTTON)
        visibility = button.value_of_css_property('visibility')
        if visibility == 'hidden':
            return False

    def display_none_button_is_visible(self):
        button = self.find_element(VisibilityLocators.LOCATOR_DISPLAY_NONE_BUTTON)
        display = button.value_of_css_property('display')
        if display == 'none':
            return False

    def offscreen_button_is_visible(self):
        button = self.find_element(VisibilityLocators.LOCATOR_OFFSCREEN_BUTTON)
        left = button.value_of_css_property('left')
        top = button.value_of_css_property('top')
        if left == top:
            return False


class SampleAppHelper(BasePage):

    def login(self, username):
        username_field = self.find_element(SampleAppLocators.LOCATOR_USERNAME_FIELD)
        username_field.click()
        username_field.send_keys(username)
        password_field = self.find_element(SampleAppLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys('pwd')
        submit_button = self.find_element(SampleAppLocators.LOCATOR_SUBMIT_BUTTON)
        submit_button.click()

    def get_success_message_username(self):
        return self.find_element(SampleAppLocators.LOCATOR_SUCCESS_MESSAGE).text


class MouseOverHelper(BasePage):

    def click_twice(self):
        for i in range(2):
            link = self.find_element(MouseOverLocators.LOCATOR_LINK)
            link.click()

    def get_counter_value(self):
        return self.find_element(MouseOverLocators.LOCATOR_CLICK_COUNTER).text


class NonBreakingSpaceHelper(BasePage):

    def space_button_is_exist(self):
        try:
            button = self.find_element(NonBreakingSpaceLocators.LOCATOR_SPACE_BUTTON, time=1)
        except:
            return False
        else:
            return True

    def nbsp_button_is_exist(self):
        try:
            button = self.find_element(NonBreakingSpaceLocators.LOCATOR_NBSP_BUTTON)
        except:
            return False
        else:
            return True
