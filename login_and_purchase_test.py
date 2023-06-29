from pages.drivers import Drivers
from pages.saucedemo_page import SaucedemoPage

class SaucedemoTest:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.browser = None
        self.saucedemo_page = None

    def setup(self):
        # Step 1: Create a browser instance
        self.browser = Drivers('--ignore-certificate-errors').chrome()
        self.saucedemo_page = SaucedemoPage(driver=self.browser)

    def teardown(self):
        # Step 14: Quit the browser
        self.browser.quit()

    def run(self):
        # Step 2: Setup the test scenario
        self.setup()

        # Step 3: Open the login page
        self.saucedemo_page.go()
        assert self.saucedemo_page.swaglabs_login_logo.text() == 'Swag Labs'

        # Step 4: Login with valid credentials
        self.login()

        # Step 5: Open the menu to access the Logout button
        self.saucedemo_page.burger_menu_button.click()
        assert self.saucedemo_page.logout_sidebar_link.text() == 'Logout', 'Logout link is not displayed.'

        # Step 6: Verify that the inventory page is displayed
        assert self.saucedemo_page.page_title.text() == 'Products', 'Product page is not displayed'
        item_5_inventory = self.saucedemo_page.item_5_title_link_inventory.text()

        # Step 7: Navigate to the product detail page
        self.saucedemo_page.item_5_title_link_inventory.click()
        assert self.saucedemo_page.back_to_products_button.text() == 'Back to products', 'Product detail page not displayed'
        assert self.saucedemo_page.item_5_title_link_detail.text() == item_5_inventory, 'Product name does not correspond'

        # Step 8: Add the item to the cart
        self.saucedemo_page.add_to_cart_item_5.click()
        assert self.saucedemo_page.remove_item_5.text() == 'Remove', 'Remove button is not displayed'

        # Step 9: Navigate to the shopping cart page
        self.saucedemo_page.shopping_cart_button.click()
        assert self.saucedemo_page.page_title.text() == 'Your Cart', 'Your cart page is not displayed'
        assert self.saucedemo_page.item_5.text() == 'Sauce Labs Fleece Jacket', 'Item 5 not added to cart page'

        # Step 10: Continue with the checkout process
        self.saucedemo_page.checkout_button.click()
        assert self.saucedemo_page.page_title.text() == 'Checkout: Your Information', 'Checkout page not displayed'

        # Step 11: Enter required shipping and payment information
        self.enter_shipping_payment_info()

        # Step 12: Proceed to the confirmation page
        self.saucedemo_page.continue_button.click()
        assert self.saucedemo_page.page_title.text() == 'Checkout: Overview', 'Checkout: Overview page not displayed'
        assert self.saucedemo_page.item_5.text() == 'Sauce Labs Fleece Jacket'

        # Step 13: Logout from the website
        self.logout()

        # Step 14: Tear down the test scenario
        self.teardown()

    def login(self):
        # Helper method: Enter login credentials and click login button
        self.saucedemo_page.username_input.input_text(self.username)
        self.saucedemo_page.password_input.input_text(self.password)
        self.saucedemo_page.login_button.click()

    def enter_shipping_payment_info(self):
        # Helper method: Enter shipping and payment information
        self.saucedemo_page.first_name_input_text.input_text('Jan')
        self.saucedemo_page.last_name_input_text.input_text('Novak')
        self.saucedemo_page.postal_code_input_text.input_text('10400')

    def logout(self):
        # Helper method: Logout from the website
        self.saucedemo_page.burger_menu_button.click()
        self.saucedemo_page.logout_sidebar_link.click()
        assert self.saucedemo_page.login_button is not None


# Test data
username = 'standard_user'
password = 'secret_sauce'

# Create and run the test scenario
test_scenario = SaucedemoTest(username, password)
test_scenario.run()
print('test passed')
