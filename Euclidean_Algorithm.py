def gcd(a,b):
        """ the euclidean algorithm """
        while a:
                a, b = b%a, a
        return b

