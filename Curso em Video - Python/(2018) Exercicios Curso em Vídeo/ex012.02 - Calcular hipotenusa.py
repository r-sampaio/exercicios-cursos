# from math import pow, sqrt  # import math
from math import hypot
cAd = float(input('Qual a medida do cateto adjacente? '))
cOp = float(input('Qual a medida do cateto oposto? '))
hi = hypot(cAd, cOp)
# cA = pow(cAd, 2)  # cA = math.pow(cAd,2)
# cO = pow(cOp, 2)  # cO = math.pow(cOp,2)
# hipo = cA + cO  #hipo = (cOp ** 2 + cAd ** 2) ** (1,2)
# final = sqrt(hipo)  # final = math.sqrt(hipo)
# print('O valor da hipotenusa sera {:.2f}'.format(final))
# print('O valor da hipotenusa sera {:.2f}'.format(hipo))
print('O valor da hipotenusa sera {:.2f}'.format(hi))