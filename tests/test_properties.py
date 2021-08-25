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