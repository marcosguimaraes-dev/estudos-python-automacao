# Projeto 01 - Calculadora de  Lucro líquido (Motorista de App)
print("== CALCULADORA DE LUCRO DÍARIO ==")

faturamento = float(input("Faturamento bruto do dia (R$):"))
km_rodados = float(input("Quilómetos rodados no dia:"))
preco_combustivel = float(input("Preço do combustível por litro (R$):"))
consumo_carro = float(input("Consumo médio do carro (km/l):"))

litros_gastos = km_rodados / consumo_carro
custo_combustivel = litros_gastos * preco_combustivel
lucro_liquido = faturamento - custo_combustivel

print("-" * 35)
print(f"Gasto com combustível: R$ {custo_combustivel:.2f}")
print(f"Lucro líquido do dia: R$ {lucro_liquido: .2f}")