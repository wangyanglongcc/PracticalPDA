
from decimal import Decimal,ROUND_HALF_UP

print(round(11.245,2))

def round(number, ndigits=2):
    assert isinstance(ndigits,int),'请输入一个正整数'
    _num = Decimal(str(number))
    _num = _num.quantize(Decimal('0.{}'.format('0'*ndigits)),rounding=ROUND_HALF_UP)
    return _num
print(round(11.245,2))