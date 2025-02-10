import operators

print(operators.addOperator(1,2))

print(operators.divideOperator(1,2))


import operators as op 
print(op.addOperator(3,4))

from operators import divideOperator as divOp

print(divOp(5,8))
