from bank_system import *
from unittest import mock



def test_deposit(monkeypatch):
    responses = iter(['2','ses123',50000])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert customer_deposit() == '*** BALANCE SUCSSESFULLY DEPOSIT! ***'


