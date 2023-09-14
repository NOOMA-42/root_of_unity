from py_ecc.fields.field_elements import FQ as Field
import py_ecc.bn128 as b

primitive_root = 5

def is_primitive_root(g, p):
    prime_divisors = [2, 3, 13, 29, 983, 11003, 237073, 405928799, 1670836401704629, 13818364434197438864469338081]
    for q in prime_divisors:
        if pow(g, (p-1) // q, p) == 1:
            return False
    return True

def get_prime_divisors(n):
    # This is too slow for large numbers
    i = 2
    divisors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            divisors.add(i)
    if n > 1:
        divisors.add(n)
    return divisors

class Scalar(Field):
    field_modulus = b.curve_order
    # Gets the first root of unity of a given group order
    @classmethod
    def root_of_unity(cls, group_order: int):
        return Scalar(primitive_root) ** ((cls.field_modulus - 1) // group_order)

    # Gets the full list of roots of unity of a given group order
    @classmethod
    def roots_of_unity(cls, group_order: int):
        o = [Scalar(1), cls.root_of_unity(group_order)]
        while len(o) < group_order:
            o.append(o[-1] * o[1])
        return o

if __name__ == '__main__':
    for g in range(2, 10):
        if is_primitive_root(g, b.curve_order):
            print(g)
    print(g)

    # 
    rou1 = Scalar.roots_of_unity(4)
    print(rou1)
    # 
    rou2 = Scalar.roots_of_unity(16) 