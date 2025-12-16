# 📊 Dashboard de Vendas

Este projeto consiste em um **dashboard interativo de vendas** desenvolvido com **Streamlit**, utilizando dados obtidos a partir de uma **API externa**. O objetivo é visualizar métricas de receita, quantidade de vendas, desempenho por estado, categoria e vendedores, de forma clara e interativa.

---

## 🚀 Tecnologias Utilizadas

* **Python 3.12.10**
* **Streamlit** – Criação da aplicação web interativa
* **Pandas** – Manipulação e análise de dados
* **Requests** – Consumo da API
* **Plotly Express** – Visualização de dados interativa

---

## 🌐 Fonte de Dados

Os dados são consumidos da seguinte API:

```
https://labdados.com/produtos
```

Ela retorna informações como:

* Data da compra
* Preço
* Local da compra (estado)
* Categoria do produto
* Vendedor
* Latitude e longitude

---

## 📌 Funcionalidades do Dashboard

### 🔹 Métricas Gerais

* **Receita total**
* **Quantidade total de vendas**

### 🔹 Visualizações

* 🗺️ **Mapa de Receita por Estado**
  Mostra a distribuição geográfica da receita no Brasil.

* 📈 **Receita Mensal**
  Evolução da receita ao longo dos meses, separada por ano.

* 🏆 **Top Estados por Receita**
  Ranking dos estados com maior faturamento.

* 🧾 **Receita por Categoria de Produto**

* 👥 **Top Vendedores**

  * Por receita
  * Por quantidade de vendas
  * Quantidade de vendedores exibidos é ajustável pelo usuário

---

## 🧭 Estrutura do Dashboard

O dashboard é dividido em **3 abas**:

### 1️⃣ Receita

* Métricas principais
* Mapa de receita por estado
* Receita mensal
* Receita por categoria

### 2️⃣ Quantidade de Vendas

* Métricas resumidas de volume de vendas

### 3️⃣ Vendedores

* Ranking de vendedores por receita
* Ranking de vendedores por quantidade de vendas
* Filtro dinâmico para escolher o número de vendedores exibidos

---

## ▶️ Como Executar o Projeto

1. Clone este repositório:

```bash
git clone <url-do-repositorio>
```

2. Instale as dependências:

```bash
pip install streamlit pandas requests plotly
```

3. Execute a aplicação:

```bash
streamlit run app.py
```

> ⚠️ Certifique-se de que o arquivo principal esteja nomeado como `app.py` (ou ajuste o comando conforme o nome do arquivo).

---

## 📝 Observações

* O layout está configurado para **tela larga** (`wide`).
* Os valores monetários são formatados automaticamente para melhor leitura.
* Todos os gráficos são **interativos**.

---

## 📚 Possíveis Melhorias Futuras

* Filtros por período
* Exportação de dados
* Autenticação de usuários
* Cache da API para melhor performance

---

👨‍💻 Projeto ideal para estudos de **Data Science**, **Data Visualization** e **Streamlit**.
