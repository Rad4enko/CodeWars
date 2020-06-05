#  Task
#  Create a function called one that accepts two params:
#  a sequence
#  a function
#  and returns true only if the function in the params
#  returns true for exactly one (1) item in the sequence.

from random import randint

a_sequence = []
b_sequence = []

for i in range(10):
    a_sequence.append(randint(1, 100))
print(a_sequence)

def bigger_than_ninety():
    for i in range(len(a_sequence)):
        if a_sequence[i] > 90:
            b_sequence.append(a_sequence[i])
    return (b_sequence)
print(bigger_than_ninety())

def one(a_sequence, bigger_than_ninety):
    if len(b_sequence) == 1:
        return True
    else: return False

print(one(a_sequence, bigger_than_ninety))