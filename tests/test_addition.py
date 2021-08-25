
from number import Number

from unittest import TestCase
from random import randint


class TestAddition(TestCase):
    def test_numbers_are_addded_correctly(self):
        base = 10
        a = randint(1, 255)
        b = randint(1, 255)

        a_coded = Number.parse(a, base=base)
        b_coded = Number.parse(b, base=base)

        result = a + b
        self.assertEqual(int(a_coded + b_coded), result)


class TestIsSemigroup(TestCase):
    def test_numbers_addition_commutates(self):
        base = randint(2, 10)
        a = randint(1, 255)
        b = randint(1, 255)

        a_coded = Number.parse(a, base=base)
        b_coded = Number.parse(b, base=base)

        self.assertEqual(int(a_coded + b_coded), int(b_coded + a_coded))

    def test_numbers_have_identity(self):
        base = randint(2, 10)
        a = randint(1, 255)
        a_coded = Number.parse(a, base=base)

        identity = Number.parse(0, base=base)

        self.assertEqual(int(a_coded + identity), a)
        self.assertEqual(int(identity + a_coded), a)
        self.assertEqual(int(identity), 0)