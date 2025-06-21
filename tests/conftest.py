import pytest

from models.cart import Cart
from models.product import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)

@pytest.fixture
def cart(product):
    return Cart()