n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('A soma desses valores eh {}'.format(n1+n2))
print('='*30)
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma eh {}. A multiplicacao eh {}. A divisao eh {}. A divisao inteira eh {}. A potencia eh {}.'.format(s, m, d, di, e))
print('='*50)
print('A soma eh {}.\nA multiplicacao eh {}.\nA divisao eh {:.3f}.\nA divisao inteira eh {}.\nA potencia eh {}.'.format(s, m, d, di, e))
print('='*50)
print('A soma eh {}, a multiplicacao eh {}, a divisao eh {}'.format(s, m, d), end=' ')
print('A divisao inteira eh {}, a potencia eh {}'.format(di, e))