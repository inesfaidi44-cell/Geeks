
# Method 1: Import the whole module
import operators

print(operators.addOperator(10, 5))
print(operators.divideOperator(10, 5))


# Method 2: Import specific functions
from operators import addOperator, divideOperator

print(addOperator(10, 5))
print(divideOperator(10, 5))


# Method 3: Import using an alias
import operators as op

print(op.addOperator(10, 5))
print(op.divideOperator(10, 5))
