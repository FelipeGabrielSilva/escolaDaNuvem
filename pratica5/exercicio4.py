import datetime

hoje = datetime.datetime.today()

print("\n=== CALCULAR IDADE EM DIAS ===\n")

dia = int(input("Informe o seu dia de nascimento: "))
mes = int(input("Informe o seu mês de nascimento: "))
ano = int(input("Informe o seu ano de nascimento: "))

nascimento = datetime.datetime(ano, mes, dia)
diferenca = hoje - nascimento

print(f"A sua idade em dias é {diferenca.days}")