'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou
"Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
'''

data = str(input())
values = data.split(' ')
first_value = int(values[0])
second_value = int(values[1])



if(second_value > first_value):
    resul = second_value / first_value
    if(first_value * resul == second_value and second_value % first_value == 0):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
else:
    result = first_value / second_value
    if(second_value * result == first_value and first_value % second_value == 0):
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

