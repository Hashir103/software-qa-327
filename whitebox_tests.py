"""
CISC 327 Assignment 5
Nov 24, 2023
Group 23

IMPORTANT, PLEASE READ README.TXT
"""
from main import run_program
import pytest

@pytest.mark.parametrize("testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id, test_cart, expected", [
    # Decision Coverage Testing on Removing Items from Cart
    # Test 1: If Item is not In Cart -> Return 0
    (2,"2", ["example@example.com","12345"], None, "3", "2", "Burger", 1, "McDonalds", None, None, None, 0),
    # Test 2: If Item is in Cart and quantity = 1 -> Return 1
    (2,"2", ["example@example.com","12345"], None, "3", "2", "Sandwich", 1, "McDonalds", None, None, ["Sandwich", 1], 1),
    # Test 3: If Item is in Cart and quantity > 1 -> Return 1
    (2,"2", ["example@example.com","12345"], None, "3", "2", "McGriddle", 1, "McDonalds", None, None, ["McGriddle", 30], 2),

    # Loop Coverage Testing on Restaurant Menus
    # Test 1: If Restaurant has 1 item -> Return Menu Size
    (2,"2", ["example@example.com","12345"], None, "2", None, None, None, "Hashir", None, None, None, 1),
    # Test 2: If Restaurant has 2 items -> Return Menu Size
    (2,"2", ["example@example.com","12345"], None, "2", None, None, None, "IKEA", None, None, None, 2),
    # Test 3: If Restaurant has 3+ items -> Return Menu Size
    (2,"2", ["example@example.com","12345"], None, "2", None, None, None, "McDonalds", None, None, None, 3),
])

def test_run_program(testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id, test_cart, expected):
    assert run_program(testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id, test_cart) == expected