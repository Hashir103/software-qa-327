"""
CISC 327 Assignment 5
Nov 24, 2023
Group 23

IMPORTANT, PLEASE READ README.TXT
"""
from main import run_program
import pytest

@pytest.mark.parametrize("testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id, expected", [
    '''Decision Coverage Testing on Removing Items from Cart'''
    # Test 1: If Item is not In Cart -> Return 1
    # Test 2: If Item is in Cart -> Return 0
    # Test 3: If Item is in Cart and quantity > 1 -> Return 1
    # Test 4: If Item is in Cart and quantity = 1 -> Return 0

    '''Loop Coverage Testing on Restaurant Menus'''
    # Test 1: If Restaurant has no items -> Return None
    # Test 2: If Restaurant has 1 item -> Return Menu Size
    # Test 3: If Restaurant has 2 items -> Return Menu Size
    # Test 4: If Restaurant has 3+ items -> Return Menu Size
])

def test_run_program(testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id, expected):
    assert run_program(testRun, init_selection, account_info, rest_selection, cust_selection, cart_selection, item, quantity, rest_name, reason, u_id) == expected