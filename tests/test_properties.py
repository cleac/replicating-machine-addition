from number import Number

from unittest import TestCase
from random import randint

class TestRepresentation(TestCase):

    def test_representation_isomoprhicity(self):
        for _ in range(10):
            number = randint(0, 65535)
            base = randint(2, 64)
            self.assertEqual(
                number,
                int(Number.parse(number, base=base, bits=8))
            )

    def test_number_ternal_correct_representation(self):
        # 0 * 3^0 + 2 * 3^1 + 2 * 9 + 0 * 3^0
        self.assertEqual(
            [0, 2, 2, 0],
            Number.parse(24, base=3, bits=4).number
        )

    def test_negative_number(self):
        a = -1 * randint(1, 255)
        self.assertEqual(int(Number.parse(a)), a)

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