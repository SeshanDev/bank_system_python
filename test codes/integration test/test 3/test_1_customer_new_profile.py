from bank_system import *
from unittest import mock



def test_newprofile(monkeypatch):
    responses = iter(['2','nethmika','kottawa','0784700250','neth123','5000'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert customer_new_profile() == '***** NEW ACCOUNT CREATED! *****'




