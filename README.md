# Transaction Safe API

This project is designed to detect fraudulent credit card transactions using machine learning techniques. The dataset, sourced from Kaggle, contains transaction data with features such as Time, V1, V2, ..., and a Class column that indicates whether a transaction is fraudulent (1) or legitimate (0).

<hr>

## Recursos

- Machine Learning Model: The model is built using Python and trained on the Kaggle dataset to predict fraud based on transaction features.
- Flask Framework: The project uses Flask to create a simple API service to serve the model's predictions.
- PHP Integration: The API is integrated with a PHP backend, where data is sent via an index.php file using the command php -S localhost:8000 for local server testing and API calls.
- Fraud Prediction: The Flask-based Python API accepts incoming transaction data, processes it through the trained model, and returns a prediction on whether the transaction is fraudulent or not.

<hr>

## Estrutura do Projeto

- Data preprocessing: Clean and prepare the Kaggle dataset for model training.
- Model training: Both traditional machine learning models and deep learning models are trained and evaluated.
- Flask API: An API built with Flask to expose the fraud detection service.
- PHP Interface: A simple PHP script to interact with the Flask API, allowing for easy integration with web platforms.

<hr>

## Imagens em Excel do .csv



<hr>

## Como rodar?

1. Clone the repository.
2. Change directory:
```bash
cd tsapy
```
3. Run the Flask app to serve the machine learning model:
```bash
python app.py
```
4. In another terminal, navigate to the PHP file and run the server:
```bash
php -S localhost:8000
```
5. You can now send transaction data (via POST request) to the Flask API, and receive a prediction on whether the transaction is fraudulent or not. OBS: You need to change directly in index.php the "valores".

<hr>

## Tecnologias

![Google Colab](https://img.shields.io/badge/Google%20Colab-%23F9A825.svg?style=for-the-badge&logo=googlecolab&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![PHP](https://img.shields.io/badge/php-%23777BB4.svg?style=for-the-badge&logo=php&logoColor=white)

<hr>

## Inspiração 

This project is inspired by Kaggle's Credit Card Fraud Detection dataset, which contains anonymized transaction data. The goal is to create an accurate and scalable fraud detection system using modern machine learning tools.

![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)

URL: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud/data