#!/usr/bin/python3


def fizzbuzz():
        """
    The classic FizzBuzz...
    For multiples of three print Fizz.
    For multiples of five print Buzz.
    For numbers which are multiples of both print FizzBuzz.
    For all other numbers, print them as they are.
    """
print(' '.join([
(i % 3 is 0) * 'Fizz' +
(i % 5 is 0) * 'Buzz' +
(str(i) if i % 3 and i % 5 else "")
for i in range(1, 101)
]), end=" ")
