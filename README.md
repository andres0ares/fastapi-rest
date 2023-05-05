# API para o Desafio ImpulsoGov

Criar uma API em FastAPI com um endpoint que retorne o horario atual dos fusos horários (-3 GMT) e (GMT – 5).
Implementar os fuso horários como um parâmetro da sua API.

Você pode acessar a API aqui: https://api-fastapi.oandre.com/

Como padrão retorna o horário dos fusos GMT-3 e GMT-5.
Exibe mais horários por meio do parâmetro GMT, com uma string de números inteiros separados por vígula.

Exemplo:
?GMT=-3,3,5,-2
retornará os horários dos fusos: GMT-3, GMT+3, GMT+5 e GMT-2
test clicando aqui: https://api-fastapi.oandre.com/?GMT=-3,3,5,-2

O código principal está do arquivo:
./main.py

## Scripts disponíveis

### `pip install fastapi`

Instala o fastapi

### `pip install "uvicorn[standard]"`

Instala o uvicorn que funciona como server

### `uvicorn main:app --reload`

Roda o app em modo de desenvolvimento