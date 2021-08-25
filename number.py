import typing as t

# TODO: refactor Number entity to work _only_ with binary numbers

class Number(t.NamedTuple):
    number: t.List[int]
    base: int = 10
    bits: int = 8

    @classmethod
    def parse(cls, number, bits=8, base=10):
        result = [0] * bits
        # Go by bits from bigger to smaller
        # The sequence will go from "bits" and end on 0
        for exp in range(bits-1, -1, -1):
            current_exponent = base ** exp
            exp_rest = number % current_exponent
            
            if exp_rest < number:
                result[bits-(exp+1)] = (number - exp_rest) // current_exponent
                number = exp_rest
            
            if number == 0:
                break
        
        return cls(base=base, bits=bits, number=result)

    def __int__(self):
        return sum(map(
            lambda x: (self.base ** x[0]) * x[1],
            zip(range(self.bits-1, -1, -1), self.number)
        ))

    def rebase(self, new_base=None, new_bits=None):
        new_base = new_base or self.base
        new_bits = new_bits or self.bits
        return self.__class__.parse(int(self), base=new_base, bits=new_bits)

    def __add__(self, other: 'Number'):
        a = self
        b = other
        
        assert a.bits == b.bits, 'Cannot add numbers with non-equal coding'
        assert a.base == b.base, 'Cannot add numbers with non-equal coding'
        carry_bit = 0
        result_num = [0] * a.bits
        a_num = a.number
        b_num = b.number
        base = a.base
        bits = a.bits

        for i in range(a.bits -1, -1, -1):
            result_num[i] = (
                (a_num[i] & b_num[i] & carry_bit) |
                ((a_num[i] ^ b_num[i]) ^ carry_bit)
            )
            carry_bit = (
                (a_num[i] & b_num[i]) |
                (a_num[i] & carry_bit) |
                (carry_bit & b_num[i])
            )
        
        return Number(base=base, bits=bits, number=result_num)

number = Number.parse