# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Para que serve a Mari? |
|---------|---------|---------------------|
| `perfil_investidor.json` | JSON | Personalizar explicações sobre as dúvidas e necessidades de aprendizado do usuário |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil do usuário, para que possam ser explicados ao usuário |
| `transacoes.csv` | CSV | Analisar padrão de gastos de saúde (farmárcia e academia) do usuário e usar essas informações de forma didática |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os produtos de saúde, o perfil do usuário e o as transações mensais foram alimentados: lista de academias, dados pessoais e transações de 3 meses foram adicionadas a esses 3 arquivos respectivamente.

---

## Estratégia de Integração

### Como os dados são carregados?
Existem duas possibilidades: injetar os dados diretamente no prompt (Crtl + c, Crtl + v), ou carregar os arquivos via código, como no exemplo abaixo:

```python
import pandas as pd
import json

#CSV
transações - pd.read_csv('data/transacoes.csv')

#JSON
with open('data/perfil_investidor.json', 'r', encoding='utf-8' as f:
  perfil = json.load(f)

with open('data/produtos_financeiros.json', 'r', encoding='utf-8' as f:
  produtos = json.load(f) 
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

```text
DADOS DO PERFIL DO CLIENTE:


TRANSAÇÕES DO CLIENTE:


PRODUTOS DISPONÍVEIS PARA ENSINO:
```

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
