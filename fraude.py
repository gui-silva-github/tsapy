import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import keras
from keras import layers
import joblib

# Load data
url = 'creditcard.csv'
dados = pd.read_csv(url)

# dados.describe()

# input and output
X = dados.drop('Class', axis=1)
y = dados['Class']

# Scaler data
scaler = StandardScaler()
X['Amount'] = scaler.fit_transform(X['Amount'].values.reshape(-1, 1))

# train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)

# saving scaler 
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

joblib.dump(scaler, 'scaler.pkl')

# creating model
model = keras.Sequential([
    layers.Dense(32, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid') # retorno binário (0 ou 1)
])

# compiling model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy', keras.metrics.Precision(), keras.metrics.Recall()]
)

# training model
model.fit(X_train, y_train, epochs=30, batch_size=2048, validation_split=0.2)

# evaluating model
y_pred = (model.predict(X_test) > 0.5).astype(int)
print(confusion_matrix(y_test, y_pred)) # acertos de não fraudes, não fraudes que foram acusadas como fraudes, perda de fraudes, identificação de fraudes
print(classification_report(y_test, y_pred)) 

exemplo_transacao = np.array([[406, -2.3122265423263, 1.95199201064158, -1.60985073229769, 3.9979055875468, -5.22187864667764, -1.42654531920595, -2.53738730624579,
                               1.39165724829804, -2.77008927719433, -2.77227214465915, 3.20203320709635, -2.89990738849473, -5.95221881324605, -4.28925378244217,
                               3.89724120274487, -1.14074717980657, -2.83005567450437, -1.68224681808257, 4.16955705037907, 1.26910559061474, 5.17232370861764,
                               -3.50493686052974, -4.65211076182388, 3.20198198514526, 4.45191674731724, 1.77839798284401, 2.61145002567677, -1.43275874698919,
                               0]])

probabilidade = model.predict(exemplo_transacao)[0][0]
print(f'Probabilidade de fraude: {probabilidade:.4f}')

# detecting fraud
fraude = probabilidade > 0.5
print('Fraude detectada?', fraude)

# saving model
model.save('modelo_fraude.h5')

