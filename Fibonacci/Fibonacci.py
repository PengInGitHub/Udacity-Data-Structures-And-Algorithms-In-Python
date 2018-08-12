"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions.

Fn = Fn-1 + Fn-2
With F0 = 0, F1 = 1

For example:
fib_seq = []
fib_seq[0] = 0
fib_seq[1] = 1
fib_seq[2] = 1
fib_seq[3] = 2
fib_seq[4] = 3
fib_seq[5] = 5
fib_seq[6] = 8
fib_seq[7] = 13
fib_seq[8] = 21
fib_seq[9] = 34
"""
def get_fib_loop(position):
    """if position == 0:
        return 0
    elif position == 1:
        return 1"""
    if position == 0 or position == 1:
        return position    
    else:
        first, second, counter = 0, 1, 3
        next = first + second
        while (counter <= position):
            first, second = second, next
            next = first + second
            counter += 1
        return next


def get_fib(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position-1) + get_fib(position-2)
    
def get_fib_solution(position):
    if position == 0 or position == 1:
        return position
    else:
        return get_fib_solution(position-1) + get_fib_solution(position-2)
# Test cases
print get_fib_loop(9)#34
print get_fib_loop(11)#89
print get_fib_loop(0)#0
print get_fib_loop(1)#1
print get_fib_loop(2)#1
print get_fib_loop(3)#2
