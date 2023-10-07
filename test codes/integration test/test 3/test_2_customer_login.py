from bank_system import *
from unittest import mock



def test_login(monkeypatch):
    responses = iter(['2','ses123'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert customer_login() == 'welcome'


