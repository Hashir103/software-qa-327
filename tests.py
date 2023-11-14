"""
CISC 327 Assignment 4
Nov 14, 2023
Group 23

IMPORTANT, PLEASE READ README.TXT
"""
from main import run_program
import pytest

@pytest.mark.parametrize("testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id, expected", [
    # Test 1: Checks if the program can successfully retrieve a Restaurant's menu correctly
    (True, "2", ["example@example.com","12345"], None, "2", None, None, None, "McDonalds", None, None, {'Big Mac': 5.99, 'McChicken': 4.99, 'McNuggets': 6.99}),
    # Test 2: Checks if the program can successfully retrieve all Restaurant's in our collection
    (True,"2", ["example@example.com","12345"], None, "1", None, None, None, None, None, None, True)
])

def test_run_program(testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id, expected):
    assert run_program(testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id) == expected