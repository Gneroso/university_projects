from from_decimal_to import signed, one_complement, two_complement, excess
from to_decimal import (signed as signed_to_decimal,
                        one_complement as one_complement_to_decimal,
                        two_complement as two_complement_to_decimal,
                        excess as excess_to_decimal)


#print signed(-5)
#print one_complement(-5)
#print two_complement(-128)
# print one_complement_to_decimal('11111110')
# print two_complement_to_decimal('10000001')
print excess_to_decimal('10000000')
