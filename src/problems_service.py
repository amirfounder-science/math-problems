from math import factorial
from random import *


def build_addition_problem():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    sum = n1 + n2

    p = '{} + {}'.format(n1, n2)
    s = sum

    return p, s


def build_subtraction_problem():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    difference = n1 - n2

    p = '{} - {}'.format(n1, n2)
    s = difference

    return p, s


def build_multiplication_problem():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    product = n1 * n2

    p = '{} * {}'.format(n1, n2)
    s = product

    return p, s


def build_division_problem():
    n1 = randint(1, 100)
    n2 = randint(1, 100)
    quotient = n1 / n2
    quotient = round(quotient, 2)

    p = '{} / {}'.format(n1, n2)
    s = quotient

    return p, s


def build_exponents_problem():
    base = randint(1, 100)
    exponent = randint(1, 10)
    power = pow(base, exponent)

    p = '{} ^ {}'.format(base, exponent)
    s = power

    return p, s


def build_probability_problem():
    total_outcomes = randint(10, 100)
    favorable_outcomes = randint(10, 100)

    while total_outcomes < favorable_outcomes:
        favorable_outcomes = randint(10, 100)

    probability = total_outcomes / favorable_outcomes

    p = 'P(A) = {} / {}'.format(favorable_outcomes, total_outcomes)
    s = probability

    return p, s


def build_factorial_problem():
    start = randint(1, 100)
    current = start
    result = start

    while current > 1:
        result *= current - 1
        current -= 1

    p = '{}!'.format(start)
    s = result

    return p, s


def build_combinations_problem():
    r = randint(1, 10)
    n = randint(10, 100)

    total_combinations = factorial(n) / (factorial(r) * factorial(n - r))
    total_combinations = int(total_combinations)

    p = 'C({}, {})'.format(n, r)
    s = total_combinations

    return p, s


def build_permutations_problem():
    pass
