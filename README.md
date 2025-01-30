Calculadora Shell Script

Descrição

Este é um script simples de calculadora desenvolvido em Shell Script para sistemas Linux. 
Ele permite que o usuário realize operações matemáticas básicas (adição, subtração, multiplicação e divisão) diretamente no terminal.

Funcionalidades

Permite realizar operações matemáticas entre dois números

Suporta as operações: +, -, *, /

Permite sair digitando sair

Como Usar

1. Criar o Arquivo

Crie o arquivo calculadora.sh e adicione o seguinte código:

#!/bin/bash

while true; do
    echo "Digite o primeiro nÃºmero (ou 'sair' para encerrar):"
    read a

    if [[ "$a" == "sair" ]]; then
        echo "Calculadora encerrada!"
        break
    fi

    echo "Digite a operaÃ§Ã£o (+, -, *, /):"
    read op

    echo "Digite o segundo nÃºmero:"
    read b

    # Realiza a operaÃ§Ã£o usando expr
    if [[ "$op" == "+" ]]; then
        resultado=$(echo "$a + $b" | bc)
    elif [[ "$op" == "-" ]]; then
        resultado=$(echo "$a - $b" | bc)
    elif [[ "$op" == "*" ]]; then
        resultado=$(echo "$a * $b" | bc)
    elif [[ "$op" == "/" ]]; then
        if [[ "$b" -eq 0 ]]; then
            echo "Erro: DivisÃ£o por zero nÃ£o Ã© permitida!"
            continue
        fi
        resultado=$(echo "scale=2; $a / $b" | bc)  # scale=2 mantÃ©m duas casas decimais
    else
        echo "OperaÃ§Ã£o invÃ¡lida!"
        continue
    fi

    echo "Resultado: $resultado"
done

2. Tornar o Arquivo Executável

Antes de executar, altere as permissões para tornar o arquivo executável:

chmod 754 calculadora.sh


3. Executar a Calculadora

Agora, execute o script com o comando:

./calculadora.sh

Permissões do Arquivo

chmod 754 calculadora.sh garante que:

O dono pode ler, escrever e executar (rwx = 7)

O grupo pode ler e executar (r-x = 5)

Outros usuários podem apenas ler (r-- = 4)

Exemplo de Uso

Digite o primeiro número (ou 'sair' para encerrar): 10
Digite a operação (+, -, *, /): +
Digite o segundo número: 5
Resultado: 15


Melhorias Futuras

Adicionar mais operações matemáticas, como potência e raiz quadrada

Criar uma interface gráfica

Salvar o histórico de cálculos

