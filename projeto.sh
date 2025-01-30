
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
