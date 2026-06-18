# Base de Conhecimento

## Prompt sugerido para esta etapa
Preciso organizar a base de conhecimento do meu agente financeiro educativo em saúde. Tenho estes arquivos de dados em .json e .csv [Liste os arquivos]. Me ajude a: (1) entender o que cada arquivo contem, (2) decidir como usar cada um, e (3) criar um exemplo de contexto formatado para incluir no prompt.

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Para que serve a Mari? |
|---------|---------|---------------------|
| `perfil_usuario.json` | JSON | Personalizar explicações sobre as dúvidas e necessidades de aprendizado do usuário |
| `produtos_saude.json` | JSON | Sugerir produtos adequados ao perfil do usuário, para que possam ser explicados ao usuário |
| `transacoes.csv` | CSV | Analisar padrão de gastos de saúde (farmárcia e academia) do usuário e usar essas informações de forma didática |

---

## Adaptações nos Dados

Os produtos/serviços de saúde, o perfil do usuário e o as transações mensais foram alimentados: lista de academias ou outros investimentos em saúde, dados pessoais e transações dos últimos 3 meses foram adicionadas a esses 3 arquivos respectivamente.

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
with open('data/perfil_usuario.json', 'r', encoding='utf-8' as f:
  perfil = json.load(f)

with open('data/produtos_saude.json', 'r', encoding='utf-8' as f:
  produtos = json.load(f) 
```

### Como os dados são usados no prompt?
Para simplificar, podemos injetar os dados no nosso prompt, garantindo que o agente tenha um melhor contexto possível, lembrando que em soluções mais robustas, o ideal é que essas informações segam carregadas dinamicamente para que possamos ganhar flexibilidade, e não precise mudar manualmente caso os dados mudem.

```text
DADOS DO PERFIL DO USUÁRIO (data/perfil_usuario.json):
{
  "nome": "João Silva",
  "idade": 35,
  "profissao": "Cuidador de Idosos",
  "renda_mensal": 5000.00,
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

TRANSAÇÕES DO USUÁRIO (data/transacoes.csv):

mês,data,descrição,categoria,valor,tipo
Março,2026-03-01,Salário,receita,5000.00,entrada
Março,2026-03-02,Aluguel,moradia,1200.00,saida
Março,2026-03-03,Supermercado,alimentacao,450.00,saida
Março,2026-03-05,Netflix,lazer,55.90,saida
Março,2026-03-07,Farmácia,saúde,259.00,saida
Março,2026-03-10,Restaurante,alimentacao,120.00,saida
Março,2026-03-12,Uber,transporte,45.00,saida
Março,2026-03-15,Conta de Luz,moradia,180.00,saida
Março,2026-03-25,Combustível,transporte,250.00,saida


mês,data,descrição,categoria,valor,tipo
Abril,2026-04-01,Salário,receita,5000.00,entrada
Abril,2026-04-02,Aluguel,moradia,1200.00,saida
Abril,2026-04-03,Supermercado,alimentacao,500.00,saida
Abril,2026-04-05,Netflix,lazer,55.90,saida
Abril,2026-04-07,Farmácia,saúde,159.00,saida
Abril,2026-04-10,Restaurante,alimentacao,120.00,saida
Abril,2026-04-12,Uber,transporte,45.00,saida
Abril,2026-04-15,Conta de Luz,moradia,180.00,saida
Abril,2026-04-20,Academia,saúde,99.00,saida
Abril,2026-04-25,Combustível,transporte,250.00,saida


mês,data,descricao,categoria,valor,tipo
Maio,2026-05-01,Salário,receita,5000.00,entrada
Maio,2026-05-02,Aluguel,moradia,1200.00,saida
Maio,2026-05-03,Supermercado,alimentacao,550.00,saida
Maio,2026-05-05,Netflix,lazer,55.90,saida
Maio,2026-05-07,Farmácia,saúde,109.00,saida
Maio,2026-05-10,Restaurante,alimentacao,120.00,saida
Maio,2026-05-12,Uber,transporte,45.00,saida
Maio,2026-05-15,Conta de Luz,moradia,180.00,saida
Maio,2026-05-20,Academia,saúde,99.00,saida
Maio,2026-05-25,Combustível,transporte,250.00,saida

PRODUTOS DISPONÍVEIS PARA ENSINO (data/produtos_financeiros.json):
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

O exemplo de contexto montado abaixo foi baseado nos dados originais da base de conhecimento, mas o sintetize deixando apenas as informações mais relevantes, otimizando o consumo de tokens. Porém, é importante ter todas as informações relevantes disponíveis.

```
Dados do Cliente:
- Nome: João Silva
- Objetivo principal: investir em saúde física e mental
- Meta de gastos: Diminuir gastos farmácia, aumentar gastos saúde física e mental
- Saldo disponível: R$ 5.000

Gastos em saúde iniciais:
- Gastos farmácia atual (março): 250.00
- Gastos em saúde física ou mental (março 2026): 0.00
- Gastos em saúde física em maio 2026: 99.00
- Gastos em saúde mental em maio 2026: 0.00

Produtos/Serviços em saúde a serem investidos:
- Academia (musculação)
- Academia (dança)
- Studio (Pilates)
- Clínica (Terapia)
- Box (Crossfit)
- Assessoria (Corrida)

```
