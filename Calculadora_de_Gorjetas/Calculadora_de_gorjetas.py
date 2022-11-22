#   Se a conta for R$ 150,00 dividida entre 5 pessoas, com 12% de gorjeta
#   Cada pessoa deverá pagar (R$ 150,00 / 5) * 1,12 = 33,6
#   Arredonda o resultado para 2 casas decimais = 33,60
print("Bem-vindo à calculadora de gorjetas!")
conta= float(input("qual foi a conta total: R$"))
gorjeta= int(input("Quanta gorjeta você gostaria de dar? 10, 12 ou 15? "))
pessoa = int(input("Quantas pessoas para dividir a conta?"))
percent_gorjeta = gorjeta / 100
valor_total_da_gorjeta = conta*percent_gorjeta
total_conta = conta + valor_total_da_gorjeta
conta_por_pessoa= total_conta / pessoa
valor_final= round(conta_por_pessoa, 2)
valor_final= "{:.2f}".format(valor_final)
print(f"cada pessoa deve pagar: R${valor_final}")