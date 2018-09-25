import unittest
import FizzBuzz

FIZZBUZZ_30 = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11,
'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz',
22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz']
class Test_class:
    def test_fizzbuzz(self):
        assert FizzBuzz.fizzbuzz(30) == FIZZBUZZ_30 
    def test_proerly_execute_a_block(self):
        assert FizzBuzz.fizzbuzz(20) == FIZZBUZZ_30[0:20]
    def test_Fixnum_types_for_integers(self):
        tmp=filter(lambda x: type(x)==int,FizzBuzz.fizzbuzz(5))
        assert list(tmp)==[1,2,4]




