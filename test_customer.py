import pytest

from customer import Customer


class TestClass:

    def test_withdraw(self):
        c = Customer(100.00)

        assert c.withdraw(5.00) == 95.00

    def test_withdraw_over_balance(self):
        """test what happens when the withdraw method is executed for a value larger than the balance"""
        with pytest.raises(RuntimeError) as re:
            c = Customer(50.00)

            c.withdraw(60.00)

            assert str(re.value).startswith("Amount greater")

    def test_deposit(self):
        c = Customer(50.00)

        assert c.deposit(50.00) == 100.00
