# conversor_temperatura.py
# Utilitário para conversão de temperatura de Celsius para Fahrenheit

# Captura a temperatura informada pelo usuário
temperatura_celsius = float(input("Digite a temperatura em graus Celsius: "))  # Conversão explícita de string (retornado pelo input) para float

# Realiza o cálculo de conversão utilizando a fórmula: F = (C × 9/5) + 32
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Exibe o resultado formatado com duas casas decimais
print(f"A temperatura convertida é {temperatura_fahrenheit:.2f} graus Fahrenheit.")