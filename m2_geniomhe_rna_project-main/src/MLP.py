import pandas as pd
import numpy as np
from keras import regularizers
from keras.callbacks import EarlyStopping
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.models import load_model


# Load training and test data
train_data = pd.read_csv('../data/angles/TrainingSetMatrix/all_training_matrix_one_hot_encoded.csv')
test_data = pd.read_csv('../data/angles/TestSetMatrix/all_test_matrix_one_hot_encoded.csv')

train_labels = pd.read_csv('../data/angles/TrainingSet_classes.csv')
test_labels = pd.read_csv('../data/angles/TestSet_classes.csv')

# Converting to numpy arrays
X_train = train_data.values
X_test = test_data.values

y_train = train_labels['classe'].values
y_test = test_labels['classe'].values

# Converting Labels to Categories
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# Resizing data
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')

nb_features = 4
opt = 'Adam'
hidden1_drop = 0.1
hidden2_drop =0.2
hidden3_drop =0.2
input_drop =0.5
lambda_l1 =0.01
size_batch=250
nb_epochs=500

# Create & train the Deep MLP model with 4 hidden layers
model = Sequential()

# Add the first hidden layer
model.add(Dense(30, input_dim = nb_features, activation='relu', kernel_regularizer=regularizers.l1(lambda_l1)))
#model.add(Activation('relu'))
#model.add(Dropout(params['input_drop']))

# Add the second hidden layer
model.add(Dense(20, activation='relu', kernel_regularizer=regularizers.l2(lambda_l1)))
model.add(Dropout(hidden1_drop))

# Add the third hidden layer
model.add(Dense(20, activation='relu', kernel_regularizer=regularizers.l1(lambda_l1)))
model.add(Dropout(hidden2_drop))

# Add the fourth hidden layer
model.add(Dense(20, activation='relu', kernel_regularizer=regularizers.l1(lambda_l1)))
model.add(Dropout(hidden3_drop))

# # Add the output layer
model.add(Dense(16, activation='softmax', kernel_regularizer=regularizers.l1(lambda_l1)))

# For a multi-class classification problem
model.compile(optimizer=opt,
              loss='categorical_crossentropy',
              metrics=['accuracy'])
#  kernel_regularizer=regularizers.l2(0.01),
               # activity_regularizer=regularizers.l1(0.01))))

es = EarlyStopping(monitor='val_acc', mode='max', verbose=1, patience = 30)

# Calculate the MAE before training
y_pred_before_training = model.predict(X_test)
mae_before_training = mean_absolute_error(y_test, y_pred_before_training)
print("MAE avant l'entraînement : ", mae_before_training)

history = model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size = size_batch, epochs=nb_epochs, verbose=1, callbacks=[es])
score = model.evaluate(X_test, y_test, batch_size=size_batch, verbose=1)
print("Scores on test set: loss=%s accuracy=%s" % tuple(score))

# Calculate the MAE after training
y_pred_after_training = model.predict(X_test)
mae_after_training = mean_absolute_error(y_test, y_pred_after_training)
print("MAE après l'entraînement : ", mae_after_training)

# Save model
model.save('../data/angles/model.h5')
