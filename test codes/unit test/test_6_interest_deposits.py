from bank_system import *
from unittest import mock



def test_interestdeposit(monkeypatch):
    responses = iter(['1','ses123'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert interest_deposits() == '*** your monthly interest is SUCSSESFULLY DEPOSITED!  try again next month ***'

