
from number import Number

from unittest import TestCase
from random import randint


class TestAddition(TestCase):
    def test_add_numbers(self):
        base = 10
        a = randint(1, 255)
        b = randint(1, 255)

        a_coded = Number.parse(a, base=base)
        b_coded = Number.parse(b, base=base)

        result = a + b
        self.assertEqual(int(a_coded + b_coded), result)

    def test_add_neative(self):
        base = 10
        a = randint(1, 255)
        b = randint(-255, -1)

        a_coded = Number.parse(a, base=base)
        b_coded = Number.parse(b, base=base)

        result = a + b
        self.assertEqual(int(a_coded + b_coded), result)


class TestSubstraction(TestCase):
    def test_substract_numbers(self):
        base = 10
        a = randint(1, 255)
        b = randint(1, 255)

        a_coded = Number.parse(a, base=base)
        b_coded = Number.parse(b, base=base)

        result = a - b
        self.assertEqual(int(a_coded - b_coded), result)