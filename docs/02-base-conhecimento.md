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
{
  "nome": "João Silva",
  "idade": 35,
  "profissao": "Cuidador de Idosos",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Investir em saúde física e mental reduzindo custos de farmácia",
  "custos_farmácia_atual": 250.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Investir mais em exercício físico",
      "valor_necessario": 400.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Investir em saúde mental",
      "valor_necessario": 500.00,
      "prazo": "2027-03"
    },
    {
      "meta": "Contratar personal trainer",
      "valor_necessario": 300.00,
      "prazo": "2026-12"
    }
  ]
}

TRANSAÇÕES DO CLIENTE:


PRODUTOS DISPONÍVEIS PARA ENSINO:
[
  {
    "nome": "Academia Fitness",
    "categoria": "musculação",
    "aporte_minimo": 99.00,
    "indicado_para": "Sedentários"
  },
  {
    "nome": "Studio movimento",
    "categoria": "Pilates",
    "aporte_minimo": 200.00,
    "indicado_para": "Pessoas ativas há pelo menos 1 mês"
  },
  {
    "nome": "Academia mais saúde",
    "categoria": "dança",
    "aporte_minimo": 60.00,
    "indicado_para": "Iniciantes"
  },
  {
    "nome": "Clínica Saúde Mental",
    "categoria": "psicoterapia",
    "aporte_minimo": 400.00,
    "indicado_para": "Profissionais de saúde"
  },
  {
    "nome": "Box Crossfit",
    "categoria": "crossfit",
    "aporte_minimo": 120.00,
    "indicado_para": "atletas amadores"
  },
  {
    "nome": "Assesoria esportiva",
    "categoria": "corrida de rua",
    "aporte_minimo": 100.00,
    "indicado_para": "Pessoas ativas há pelo menos 2 meses"
  }
]
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
