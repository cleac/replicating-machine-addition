from number import Number

def add(a: Number, b: Number) -> Number:
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


def add_book(a: Number, b: Number) -> Number:
    ...



print(add(Number.parse(1, base=2), Number.parse(2, base=2)))
# print(add(5, 9))
# print(add(0b11111111111111111111, 0b00000001))

# print(timeit(lambda: add(0b11111111111111111111, 0b00000001)))
# print(timeit(lambda: add(1, 1)))