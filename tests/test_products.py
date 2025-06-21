import pytest


class TestProducts:

    def test_product_check_quantity(self, product):
        # проверки на метод check_quantity
        assert product.check_quantity(1000) == True
        assert product.check_quantity(1001) == False
        assert product.check_quantity(0) == True
        assert product.check_quantity(-1) == False
        pass

    def test_product_buy(self, product):
        # проверки на метод buy
        initial_quantity = product.quantity
        product.buy(10)
        assert product.quantity == initial_quantity - 10
        pass

    def test_product_buy_more_than_available(self, product):
        # проверки на метод buy, которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as exc:
            product.buy(product.quantity + 1)
        assert exc.typename == "ValueError"
        assert str(exc.value) == "Недостаточно продукта"
        pass
