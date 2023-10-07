from bank_system import *
from unittest import mock



def test_loan(monkeypatch):
    responses = iter([2000000,60])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert monthly_repayment_loan() == 'The monthly repayment for a loan : 52987.77'

