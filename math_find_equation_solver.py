from random import shuffle, randint, choice
from typing import List, Tuple
import time
# import sympy

NUMBERS_TO_USE = [3, 4, 2, 7]
SIGNS_TO_USE = ('+', '-', '*', '/')
USE_BRACKETS = True
RESULTS_TO_FIND = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TIME_LIMIT = 10  # limit time (seconds) for find solution


def rng(probability: int, symbol: str) -> str:
    """Returns symbol with probability 0 - 100 %"""
    return symbol if 0 < randint(1, 100) <= probability else ''


def get_numbers(numbers_: List[int]) -> List[str]:
    """Returns combinations of given numbers with different concatenation, positions and signs.
    ex. [1, 2, 3] -> [-32, 1]. Returns minimum 2 numbers"""
    nums = list(map(str, numbers_))
    for _ in range(len(nums) - 2):
        if randint(0, 3) == 0:  # probability 25%
            el = nums.pop(randint(0, len(nums) - 1))
            el2 = nums.pop(randint(0, len(nums) - 1))
            nums.append(el + el2)
    shuffle(nums)
    return [rng(10, '-') + num for num in nums]


def convert_double_signs(expressions_: List[str]) -> None:
    """inline correction for list of expressions: '+-' -> '-', '--' -> '+'"""
    for ind, exp_ in enumerate(expressions_):
        old = exp_
        for i in range(2, len(exp_) - 1):
            if i > len(exp_) - 1:
                break
            if exp_[i] == '-' and exp_[i - 1] == '-':
                exp_ = exp_[0:i - 1] + '+' + exp_[i + 1:]
            elif exp_[i] == '-' and exp_[i - 1] == '+':
                exp_ = exp_[0:i - 1] + '-' + exp_[i + 1:]
        if old != exp_:
            expressions_[ind] = exp_


def get_expression(numbers: List[str], signs: Tuple[str, ...], use_brackets: bool) -> List[str]:
    """Forms list of expressions with combinations of sings and brackets for given numbers list."""
    expressions_ = []

    def sgn(signs_: Tuple[str] = signs):
        """Gives random sign"""
        return choice(signs_)

    def insert_brackets(expr_: list, opening_brackets_index: int, closing_brackets_index: int) -> list:
        """Adds brackets to expression."""
        expr_ = expr_[:]
        expr_.insert(opening_brackets_index, '(')
        expr_.insert(closing_brackets_index, ')')
        return expr_

    expression_ = [el for num in numbers for el in [num, sgn()]]
    expressions_.append("".join(expression_)[:-1])
    if use_brackets:
        if len(numbers) >= 3:
            expressions_.append("".join(insert_brackets(expression_, 0, 4))[:-1])
            expressions_.append("".join(insert_brackets(expression_, 2, 6))[:-1])
        if len(numbers) >= 4:
            expressions_.append("".join(insert_brackets(expression_, 4, 8))[:-1])
            expressions_.append("".join(insert_brackets(expression_, 2, 8))[:-1])
            expressions_.append("".join(insert_brackets(expression_, 0, 6))[:-1])
    return expressions_


if __name__ == '__main__':
    """ Math test solver. You get 4 number, combining them, using signs and brackets you have to create expressions,
    which calculation should lead to requested values.
    """
    print(f'Looking for expressions to get these numbers:', *RESULTS_TO_FIND)
    print(f'Using these numbers:', *NUMBERS_TO_USE)
    print(f'Using these signs:', *SIGNS_TO_USE)
    print(f'Timelimit to find each expression: {TIME_LIMIT} sec.')
    print()
    for expected_result in RESULTS_TO_FIND:
        print(f'Looking for expression to get \033[1;36;48m{expected_result:2}\x1b[0m: ', end='')
        start_time = time.time()
        expressions_found = []
        while time.time() < start_time + TIME_LIMIT and len(expressions_found) < 5:
            expressions = get_expression(get_numbers(NUMBERS_TO_USE), SIGNS_TO_USE, USE_BRACKETS)
            for expression in expressions:
                result = None
                try:
                    result = eval(expression)
                    # result = sympy.sympify(expression)
                except:  # yes, I know it's too broad. But I need an answer only and don't want to handle all errors.
                    pass
                if result == expected_result:
                    expressions_found.append(expression)
        if expressions_found:
            print(f'found {len(expressions_found)} options in {round(time.time() - start_time, 1)} seconds: ', end='')
            convert_double_signs(expressions_found)
            expressions_found.sort(key=lambda x: len(x))
            expressions_found = [expr.rjust(12) for expr in expressions_found[:3]]
            print(*expressions_found, sep='   ')
        else:
            print("Sorry, couldn't find! Try to increase timelimit!")
