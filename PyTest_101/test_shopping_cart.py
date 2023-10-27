
from shopping_cart import ShoppingCart
from item_database import ItemDatabase
import pytest
from unittest.mock import Mock


@pytest.fixture  # Pass an argument to test cases that need it
def cart():
    # Have all testcase setup code here
    return ShoppingCart(5)

def test_can_add_item_to_cart(cart):
    cart.add("orange")
    assert cart.size() == 1


def test_when_item_added_then_cart_contains_item(cart):
    cart.add("orange")
    assert "orange" in cart.get_items()


def test_when_add_more_than_max_items_should_fail(cart):
    for _ in range(5):
        cart.add("banana")
    with pytest.raises(OverflowError):
        cart.add("banana")


def test_can_get_total_price(cart):
    print("Testing can get total price")
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()

    # Mocking
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        elif item == "orange":
            return 1.5
        else:
            return 0.0

    item_database.get = Mock(side_effect=mock_get_item)
    assert cart.get_total_price(item_database) == 2.5

