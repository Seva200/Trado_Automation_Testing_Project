from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
import allure
from src.locators.homePageLcs import home_lcs


class TestWelcomeToModal(ChromeDriverSetUp):
    @allure.description("the test is verify, if user can close the welcome to modal without choose interest ")
    @allure.severity(severity_level='minor')
    def test_x_btn(self, driver):
        assert self.common_actions.get_attribute_by_class(
            home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        self.welcome_to_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_hide"]) == 'modal_modalWrapper false     '

    @allure.description("the test is verify, if user can choose any interest ")
    def test_choose_interest(self, driver):
        assert self.common_actions.get_attribute_by_class(
            home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        self.welcome_to_modal.choose_coktails()
