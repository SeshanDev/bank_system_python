from bank_system import *
from unittest import mock


def test_balance(monkeypatch):
    responses = iter(['2'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert customer_Account_balance() == 'Current Balance : 35000.00'
