import pytest
from selenium import webdriver
from src.pages.bankTransferModal import BankTransferModal
from src.pages.cartBar import CartBar
from src.pages.creditCardModal import CreditCardModal
from src.pages.deliveryDetailsSection import DeliveryDetailsSection
from src.pages.homePage import HomePage
from src.pages.paymentsMethodsSection import PaymentsMethodsSection
from src.pages.personalAreaPage import PersonalAreaPage
from src.pages.productPage import ProductPage
from src.pages.signInModal import SignInModal
from src.pages.signUpModal import SignUpModal
from src.pages.welcomeToModal import WelcomeToModal
from src.pages.b2bModal import B2BModal
from src.pages.digitalCheckModal import DigitalCheckModal
from src.pages.finTradoModal import FinTradoModal
from src.utils.commonActions import CommonActions

class ChromeDriverSetUp:
    @pytest.fixture()
    def driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://qa.trado.co.il/")
        self.bank_transfer_modal = BankTransferModal(driver)
        self.cart_bar = CartBar(driver)
        self.credit_card_modal = CreditCardModal(driver)
        self.delivery_details_section = DeliveryDetailsSection(driver)
        self.home_page = HomePage(driver)
        self.payments_methods_section = PaymentsMethodsSection(driver)
        self.personal_area_page = PersonalAreaPage(driver)
        self.product_page = ProductPage(driver)
        self.sign_in_modal = SignInModal(driver)
        self.sign_up_modal = SignUpModal(driver)
        self.welcome_to_modal = WelcomeToModal(driver)
        self.b2b_modal = B2BModal(driver)
        self.digital_check_modal = DigitalCheckModal(driver)
        self.fin_trado_modal = FinTradoModal(driver)
        self.common_actions = CommonActions(driver)
        yield driver
        driver.quit()



