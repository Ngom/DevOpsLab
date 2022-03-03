# Tests (copy to tests/test_user_functions.py)
import pytest
import io
from src.user_functions import *

# email testing
def test_email_with_user_input_no_at_sign(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra.adaltas.com'))
    assert get_email_from_input() is None

def test_email_with_user_input_no_dot(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltascom'))
    assert get_email_from_input() is None

def test_email_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('petra@adaltas.com'))
    assert get_email_from_input() == 'petra@adaltas.com'

# user_name testing
def test_username_with_user_input_no_space(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Abi DSTI'))
    assert get_user_name_from_input() is None


def test_username_with_user_input_no_empty(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('\n'))
    assert get_user_name_from_input() is None

def test_username_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('engom'))
    assert get_user_name_from_input() == 'engom'

# password testing
def test_password_with_user_input_bad_lenght(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('869%700000'))
    assert get_password_from_input() is None

def test_password_with_user_input_no_number(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('aBcDe!&yfdgjpqur'))
    assert get_password_from_input() is None

def test_password_with_user_input_no_special_char(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('aBcDe85yfdgjpqur'))
    assert get_password_from_input() is None

def test_password_with_user_input_correct(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('NDe85yfdgjpqur!!44'))
    assert get_password_from_input() == 'NDe85yfdgjpqur!!44'
