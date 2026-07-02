import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar2 = Jar(5)
    assert jar2.capacity == 5
    assert jar2.size == 0

    with pytest.raises(ValueError):
        Jar(-1)

    with pytest.raises(ValueError):
        Jar("not a number")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5
    jar.deposit(5)
    assert jar.size == 10

    with pytest.raises(ValueError):
        jar.deposit(1)  # exceeds capacity


def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(5)  # not enough cookies


def test_capacity():
    jar = Jar(20)
    assert jar.capacity == 20


def test_size():
    jar = Jar(20)
    jar.deposit(7)
    assert jar.size == 7
