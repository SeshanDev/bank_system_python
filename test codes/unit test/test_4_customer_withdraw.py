from bank_system import *
from unittest import mock



def test_withdraw(monkeypatch):
    responses = iter(['1','ses123',10000])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert customer_withdraw() == '*** WITHDRAWAL SUCCESS! ***'

