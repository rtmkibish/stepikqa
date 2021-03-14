from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
  product_page = ProductPage('http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear', browser)
  product_page.open()
  product_page.add_product_to_basket()
  product_page.should_be_product_addition_massage_alert()
  product_page.solve_quiz_and_get_code()
  product_page.should_basket_price_equal_to_product_price()
