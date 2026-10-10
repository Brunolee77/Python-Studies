# Quanto custa viver no Brasil?

## Análise da relação entre renda per capita e custo da cesta básica nas capitais brasileiras

Este projeto apresenta uma análise exploratória da relação entre a renda domiciliar per capita e o valor da cesta básica nas capitais brasileiras.

O objetivo é identificar diferenças entre as capitais quanto ao comprometimento da renda com a cesta básica e observar como esses valores se relacionam.

## Dados utilizados

### Renda domiciliar per capita

- Fonte: **IBGE — PNAD Contínua 2025**
- Indicador: rendimento nominal mensal domiciliar per capita
- Abrangência: Unidades da Federação

### Cesta básica

- Dados referentes às **27 capitais brasileiras**
- Período analisado: **dezembro de 2025**
- Indicador principal: valor da cesta básica em reais

Os dados foram organizados em arquivos CSV e tratados com Python para possibilitar a integração e análise das informações.

## Tecnologias utilizadas

- **Python** — linguagem utilizada no desenvolvimento do projeto
- **Pandas** — tratamento, organização e análise dos dados
- **NumPy** — cálculos e operações numéricas
- **Matplotlib** — criação das visualizações
- **Jupyter Notebook** — desenvolvimento e documentação da análise

## Análises realizadas

Durante o projeto foram realizadas as seguintes análises:

- Tratamento e organização dos dados de renda e cesta básica.
- Integração dos dados por Unidade da Federação.
- Cálculo do percentual da renda per capita correspondente ao valor da cesta básica.
- Cálculo da média do indicador Cesta sobre Renda.
- Classificação das capitais entre valores acima e abaixo da média.
- Identificação das capitais mais distantes da média.
- Comparação dos valores das cestas básicas entre as capitais.
- Criação de gráficos para facilitar a interpretação dos resultados.

## Principais resultados

- A média do indicador **Cesta sobre Renda** foi de **35,18%**.
- Das 27 capitais analisadas, **11 apresentaram valores acima da média** e **16 ficaram abaixo da média**.
- **São Luís** apresentou o maior percentual de cesta básica em relação à renda per capita, com **51,63%**.
- **Brasília** apresentou o menor percentual, com **15,74%**.
- Brasília também apresentou o maior afastamento abaixo da média, enquanto São Luís apresentou o maior afastamento acima da média.
- Os resultados mostram diferenças relevantes entre as capitais na relação entre renda domiciliar per capita e valor da cesta básica.

## Limitações da análise

Os dados de renda utilizados estão disponíveis por Unidade da Federação, enquanto os dados da cesta básica correspondem às capitais. Portanto, a comparação representa uma relação entre a renda domiciliar per capita da UF e o valor da cesta básica observado em sua capital.

Além disso, a cesta básica é apenas um dos componentes das despesas de uma família. O indicador utilizado não representa o custo de vida completo de cada capital, pois não considera outras despesas, como moradia, transporte, saúde, educação e lazer.

Dessa forma, os resultados devem ser interpretados como uma análise exploratória da relação entre renda e custo da cesta básica, e não como um ranking definitivo de custo de vida.

## Como executar o projeto

1. Clone este repositório:

```bash
git clone URL_DO_REPOSITORIO

pip install pandas numpy matplotlib

**Mas atenção:** no seu README, você precisa ter os três acentos graves (```), porque eles fazem o GitHub mostrar os comandos como código.

E **não precisa colocar** minhas explicações como:

> "Perfeito! Agora vamos fechar..."

ou

> "⚠️ Não coloque a URL..."

Essas partes são só orientações para você.

Depois de colar, me manda um print que eu confiro se a formatação ficou certinha. 👍