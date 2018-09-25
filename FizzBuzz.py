def fizzbuzz(max):
    result = map(lambda x:  'FizzBuzz' if x % 15 == 0 \
    else 'Fizz' if x % 3 == 0\
    else 'Buzz' if x % 5 == 0\
    else x, list(range(1, max+1)))
    return list(result)