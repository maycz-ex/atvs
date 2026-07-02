#faturamento de variavel

faturamento = 500
custo = 300
imposto = 0.3
lucro1 = faturamento - custo - imposto * faturamento 
print(f"o lucro1 é {lucro1:.2f}")

faturamento = 988
lucro2 = faturamento - custo - imposto * faturamento
print(f"o lucro2 é {lucro2:.2f}")

print ("o lucro da loja no primeiro mes foi de", lucro1,"e no segundo mes foi de", lucro2)

margem_lucro = lucro2 / faturamento * 100
print(f"a margem de lucro é {margem_lucro:.1f}%")

meta = 42
if margem_lucro >= meta:
    print("meta atingida")
else:
    print("meta não atingida")