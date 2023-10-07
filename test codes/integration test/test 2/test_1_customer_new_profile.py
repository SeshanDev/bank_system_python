from bank_system import *
from unittest import mock



def test_newprofile(monkeypatch):
    responses = iter(['1','seshan','athurugiriya','0784700850','ses123','5000'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    assert customer_new_profile() == '***** NEW ACCOUNT CREATED! *****'




