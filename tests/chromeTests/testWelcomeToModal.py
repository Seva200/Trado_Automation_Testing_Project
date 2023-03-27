from src.utils.drivers.chromeDriverSetUp import ChromeDriverSetUp
from src.locators.homePageLcs import home_lcs
class TestWelcomeToModal(ChromeDriverSetUp):
    def test_X_btn(self, driver):
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        self.welcome_to_modal.x_btn_click()
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_hide"]) == 'modal_modalWrapper false     '

    def test_choose_interest(self, driver):
        assert self.common_actions.get_attribute_by_class(home_lcs["modal_open"]) == "modal_modalWrapper false modal_open    "
        self.welcome_to_modal.choose_coktails()



