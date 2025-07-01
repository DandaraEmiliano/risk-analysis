
# 📊 Risk Analysis ETL

Este projeto implementa um pipeline de ETL (Extract, Transform, Load) para análise de risco com base em transações financeiras.

## 🔧 Tecnologias Utilizadas

- Python 3.11
- Pandas
- MongoDB

## 📁 Estrutura do Projeto

```
risk_analysis/
│
├── data/
│   └── transacoes.csv         
│
├── etl/
│   ├── extract.py             
│   ├── transform.py          
│   └── load.py                
│
├── main.py                    
├── requirements.txt           
├── .gitignore
└── README.md                
```

## ⚙️ Funcionamento

1. **Extract**: Lê o CSV com dados de transações.
2. **Transform**: Filtra valores acima de R$ 10.000 e classifica o risco:
   - "alto" se valor > R$ 50.000
   - "médio" caso contrário
3. **Load**: Insere os dados tratados no MongoDB (coleção `transacoes_filtradas`).

## 📌 Observações

- O projeto usa virtualenv (`venv311`), que está ignorada no Git.
- Os dados são carregados na base `risco_db`, visível no MongoDB Compass.

## 🚀 Como Executar

```bash
source venv311/bin/activate
python main.py
```

4 registros serão inseridos no MongoDB, conforme a lógica definida.

---

## 👩🏻‍💻 Autora

**Dandara Emiliano**  
[GitHub](https://github.com/DandaraEmiliano) · [LinkedIn](https://linkedin.com/in/dandaraemiliano)

---

## 📝 Licença

Este projeto está sob a licença MIT.
