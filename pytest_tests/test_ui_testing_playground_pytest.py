from UITestingPlaygroundPages import *
import pytest


@pytest.mark.usefixtures('driver')
class TestPageUI:

    def test_text_input_page(self):
        text_input_page = TextInputHelper(self.driver, 'textinput')
        text_input_page.go_to_site()
        button_name = 'Some Button Name'
        text_input_page.enter_button_name(button_name)
        button_name_val = text_input_page.get_button_name()
        assert button_name_val == button_name

    def test_mouse_over_page(self):
        mouse_over_page = MouseOverHelper(self.driver, 'mouseover')
        mouse_over_page.go_to_site()
        mouse_over_page.click_twice()
        assert mouse_over_page.get_counter_value() == '2'

    def test_dynamic_table_page(self):
        dynamic_table_page = DynamicTableHelper(self.driver, 'dynamictable')
        dynamic_table_page.go_to_site()
        table_value = dynamic_table_page.get_table_chrome_cpu_load_value()
        label_value = dynamic_table_page.get_label_chrome_cpu_load_value()
        assert table_value == label_value

    def test_verify_text_page(self):
        verify_text_page = VerifyTextHelper(self.driver, 'verifytext')
        verify_text_page.go_to_site()
        assert verify_text_page.get_text() == 'Welcome UserName!'

    def test_progress_bar_page(self):
        progress_bar_page = ProgressBarHelper(self.driver, 'progressbar')
        progress_bar_page.go_to_site()
        result = progress_bar_page.get_result()
        assert result == '0'

    def test_visibility_page(self):
        visibility_page = VisibilityHelper(self.driver, 'visibility')
        visibility_page.go_to_site()
        visibility_page.hide_button_click()
        assert visibility_page.removed_button_is_visible() == False
        assert visibility_page.zero_width_button_is_visible() == False
        assert visibility_page.overlapped_button_is_visible() == False
        assert visibility_page.opacity_zero_button_is_visible() == False
        assert visibility_page.visibility_hidden_button_is_visible() == False
        assert visibility_page.display_none_button_is_visible() == False
        assert visibility_page.offscreen_button_is_visible() == False

    def test_sample_app_page(self):
        sample_app_page = SampleAppHelper(self.driver, 'sampleapp')
        sample_app_page.go_to_site()
        username = 'TestUser'
        sample_app_page.login(username)
        assert sample_app_page.get_success_message_username() == f'Welcome, {username}!'

    def test_nbsp_page(self):
        nbsp_page = NonBreakingSpaceHelper(self.driver, 'nbsp')
        nbsp_page.go_to_site()
        assert nbsp_page.space_button_is_exist() == False
        assert nbsp_page.nbsp_button_is_exist() == True

    def test_scroll_bars_page(self):
        scroll_bars_page = ScrollBarsHelper(self.driver, 'scrollbars')
        scroll_bars_page.go_to_site()
        result = scroll_bars_page.button_click()
        assert result == 1

    def test_dynamic_id_page(self):
        dynamic_id_page = DynamicIDHelper(self.driver, 'dynamicid')
        dynamic_id_page.go_to_site()
        result = dynamic_id_page.button_click()
        assert result == 1
