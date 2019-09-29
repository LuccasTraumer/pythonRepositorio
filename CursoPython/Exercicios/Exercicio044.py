'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros

'''
print('============== Loja do TRÄUMER =====================')

produto = float(input('Preço do Produto: R$ '))
print(''' Formas de PAGAMENTO
 [1] á Vista Dinheiro/Cheque
 [2] á Vista no Cartão 
 [3] 2x Vezes no Cartão
 [4] 3x ou Mais  no Cartão
 ''')
forma = int(input('Qual a Opção: '))

if forma == 1:
    print('Sua Compra será de {} , Vai ficar {} no final'.format(produto,(produto-(produto*10)/100)))
elif forma == 2:
    print('Sua Compra no Cartão de {} , Vai ficar {} no final '.format(produto,(produto-(produto*5)/100)))
elif forma == 3:
    print('Sua Compra de {} em 2x no Cartão irá ficar {} '.format(produto,produto))
elif forma == 4:
    parcelas = int(input('Quantas Parcelas: '))
    juros =(produto*20)/100
    print('Sua Compra de {} em {}x no Cartão , serão parcelas de {}  '.format(produto,parcelas,(produto+juros)/parcelas))
    print('Sua Compra de {} com Juros ira ficar {}'.format(produto,produto+juros))