import pytest


@pytest.mark.usefixtures("setup")
class TestPurchase:

    def test_purchase_three_items(self):
        self.login_page.open()
        self.login_page.success_login("standard_user", "secret_sauce")

        self.inventory_page.add_item_to_cart("Sauce Labs Backpack")
        self.inventory_page.add_item_to_cart("Sauce Labs Bolt T-Shirt")
        self.inventory_page.add_item_to_cart("Sauce Labs Onesie")
        self.inventory_page.go_to_cart()

        self.cart_page.proceed_to_checkout()
        self.info_page.fill_form('last_name', 'first_name', 'ZIP code', '12345')
        self.info_page.click_continue()

        assert self.checkout_step_two.get_total_price() == "58.29"
