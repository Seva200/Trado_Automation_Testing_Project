from src.utils.commonActions import CommonActions
from src.locators.welcomeToModalLcs import welcome_to_lcs
class WelcomeToModal(CommonActions):


    def x_btn_click(self):
        CommonActions.click_on_locator(self, welcome_to_lcs["x_btn"])
    def save_btn_click(self):
        CommonActions.click_on_locator(self, welcome_to_lcs["save_btn"])
    def choose_coktails(self):
        CommonActions.click_on_locator(self, welcome_to_lcs["cocktail"])
        WelcomeToModal.save_btn_click(self)
    def choose_restaurants(self):
        CommonActions.click_on_locator(self, welcome_to_lcs["restaurants"])
        WelcomeToModal.save_btn_click(self)
