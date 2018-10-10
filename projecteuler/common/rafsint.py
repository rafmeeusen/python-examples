import pyprimes

class RafsInt:
    __num = 0

    def __init__(self, number):
        if not isinstance (number,int):
            raise Exception('only integers')
        self.__num = number

    def is_prime(self):
        return pyprimes.is_prime(self.__num)

    def is_perfect(self):
        sum_divisors = sum( self.get_proper_positive_divisors() )
        return self.__num == sum_divisors

    def is_even(self):
        if self.__num % 2 == 0:
            return True
        else:
            return False

    def is_odd(self):
        return not self.is_even()

    def is_triangular(self):
        # todo: check prob12
        return True

    def get_prime_factorization_dict(self):
        ''' returns dictionary with prime factorization, e.g. {2:1,3:0,5:0,7:2} '''
        primelist = {}
        divider=2
        primelist[divider]=0
        n = self.__num
        while n > 1:
            if n%divider == 0:
                n=n//divider
                primelist[divider]+=1
            else:
                divider+=1
                primelist[divider]=0
        return primelist

    def get_nr_of_divisors(self):
        ''' sigma_0, as in https://en.wikipedia.org/wiki/Divisor_function '''
        primedividers=self.get_prime_factorization_dict()
        nrdividers=1
        for prime in primedividers.keys():
            exponent=primedividers[prime]
            nrdividers *= (exponent+1)
        return nrdividers

    def get_proper_positive_divisors(self):
        return [1,2]

    def is_deficient(self):
        return True

    def is_abundant(self):
        return False


