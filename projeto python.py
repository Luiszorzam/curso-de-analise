while True:

  # Solicita a entrada do usuário

  num1 = input("Digite o primeiro número (ou 'sair' para encerrar): ")



  if num1.lower() == "sair": # Verifica se o usuário quer sair

    print("Calculadora encerrada!")

    break

  if not num1.isdigit(): # Verifica se a entrada é um número

    print("Entrada inválida! Por favor, digite um número.")

    continue

  num1 = float(num1) # Converte para número



  ope = input("Digite a operação (+, -, *, /): ")



  if ope not in ["+", "-", "*", "/"]: # Verifica se a operação é válida

    print("Operação inválida! Por favor, escolha entre +, -, *, /.")

    continue

  num2 = input("Digite o segundo número: ")



  if not num2.isdigit(): # Verifica se a entrada é um número

    print("Entrada inválida! Por favor, digite um número.")

    continue

  num2 = float(num2)

  # Realiza a operação

  if ope == "+":

    resultado = num1 + num2

  elif ope == "-":

    resultado = num1 - num2

  elif ope == "*":

    resultado = num1 * num2

  elif ope == "/":

    if num2 == 0: # Trata divisão por zero

      print("Erro: Divisão por zero não é permitida!")

      continue

    resultado = num1 / num2

  print(f"O resultado de {num1} {ope} {num2} é: {resultado}")