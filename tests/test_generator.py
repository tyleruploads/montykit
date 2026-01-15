import pytest
from montykit.generator import (
    gen_id,
    gen_uuid,
    gen_password,
    gen_first_name,
    gen_first_names,
    gen_full_name,
    gen_phone
)


def test_gen_id_properties():
    result = gen_id(length=15)
    assert len(result) == 15
    assert result.isdigit()


def test_gen_uuid_format():
    result = gen_uuid()
    assert len(result) == 36
    assert result.count("-") == 4


def test_gen_password_complexity():
    length = 20
    result = gen_password(length=length)
    assert len(result) == length
    assert any(c.isupper() for c in result) or any(c.islower() for c in result)


def test_gen_first_name():
    name = gen_first_name()
    assert isinstance(name, str)
    assert len(name) > 0


def test_gen_first_names_list():
    amount = 5
    names = gen_first_names(amount=amount)
    assert isinstance(names, list)
    assert len(names) == amount
    assert all(isinstance(n, str) for n in names)


def test_gen_full_name_variants():
    name_simple = gen_full_name(middle=False)
    name_with_middle = gen_full_name(middle=True)
    assert len(name_simple.split()) == 2
    assert len(name_with_middle.split()) >= 3


def test_gen_phone_format():
    phone = gen_phone()
    assert len(phone) == 10
