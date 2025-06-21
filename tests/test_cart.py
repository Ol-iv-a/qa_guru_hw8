import pytest

class TestCart:
    """
    тесты на методы класса Cart
    """
    def test_add_product(self, cart, product):
        cart.add_product(product, 5)
        assert cart.products[product] == 5
        cart.add_product(product, 1)
        assert cart.products[product] == 6
        pass

    def test_remove_product(self, cart, product):
        cart.add_product(product,5)
        cart.remove_product(product,1)
        assert cart.products[product] == 4

    def test_remove_product_equal_exist_in_cart(self, cart, product):
        count = 10
        cart.add_product(product,count)
        cart.remove_product(product,count)
        assert cart.products[product] == 0


    def test_remove_product_more_then_exist(self, cart, product):
        cart.add_product(product,5)
        cart.remove_product(product,6)
        assert product not in cart.products

    def test_remove_product_without_count(self, cart, product):
        cart.add_product(product,5)
        cart.remove_product(product)
        assert product not in cart.products

    def test_clear_cart(self,cart, product):
        cart.add_product(product,5)
        product_exists_in_cart = product in cart.products
        cart.clear()
        product_not_exists_in_cart = product in cart.products
        assert product_exists_in_cart != product_not_exists_in_cart

    def test_total_price(self, cart, product):
        product.price = product.price
        quantity = 10
        cart.add_product(product,quantity)
        assert cart.get_total_price() == product.price * quantity

    def test_buy_products(self, cart, product):
        product_quantity = product.quantity
        cart.add_product(product,5)
        cart.buy()
        assert product.quantity == product_quantity - 5 and product not in cart.products


    def test_buy_more_products(self, cart, product):
        max_quantity = product.quantity
        cart.add_product(product, max_quantity+1)
        with pytest.raises(ValueError) as exc:
            cart.buy()
        assert exc.typename == "ValueError"
        assert str(exc.value) == "Недостаточно продукта"