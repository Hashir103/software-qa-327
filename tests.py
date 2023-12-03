"""
CISC 327 Assignment 6
Dec 1, 2023
Group 23

IMPORTANT, PLEASE READ README.TXT
"""
from main import run_program
import pytest

@pytest.mark.parametrize("testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id, test_cart, expected", [
    # All of our Blackbox/Whitebox Tests can be run on a daily basis. Additionally, all of these are important for the functionality of our program. As a result, we've merged all of these together for our daily test script.

    # Test 1: Check a failed test of Logging In by entering incorrect password
    (1,"2", ["example@example.com","1234"], None, None, None, None, None, None, None, None, None, False),
    # Test 1: Check a failed test of Logging In by entering incorrect email
    (1,"2", ["exampleexample.com","1234"], None, None, None, None, None, None, None, None, None, False),
    # Test 2: Checks if the program can successfully retrieve a Restaurant's menu correctly
    (1, "2", ["example@example.com","12345"], None, "2", None, None, None, "McDonalds", None, None, None, {'Big Mac': 5.99, 'McChicken': 4.99, 'McNuggets': 6.99}),
    # Test 3: Checks if the program can successfully retrieve all Restaurant's in our collection
    (1,"2", ["example@example.com","12345"], None, "1", None, None, None, None, None, None, None, True),

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