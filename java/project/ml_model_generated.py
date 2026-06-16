import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report
import joblib
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# Load data
df = pd.read_csv("gesture_data.csv")
X_raw = df.drop("label", axis=1)
y = df["label"]

# Feature Engineering: Normalize with wrist (x0, y0)
for i in range(21):
    X_raw[f'x{i}'] -= X_raw['x0']
    X_raw[f'y{i}'] -= X_raw['y0']

# Compute pairwise distances between key points (you can add more)
def compute_distances(df, p1, p2):
    return np.sqrt((df[f'x{p1}'] - df[f'x{p2}'])**2 + (df[f'y{p1}'] - df[f'y{p2}'])**2)

X = pd.DataFrame()
X["thumb_index"] = compute_distances(X_raw, 4, 8)
X["index_middle"] = compute_distances(X_raw, 8, 12)
X["middle_ring"] = compute_distances(X_raw, 12, 16)
X["ring_pinky"] = compute_distances(X_raw, 16, 20)
X["wrist_index"] = compute_distances(X_raw, 0, 8)
X["wrist_pinky"] = compute_distances(X_raw, 0, 20)

# Label encoding
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.2, random_state=42)

# Build MLP model
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(len(encoder.classes_), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=50, batch_size=16, validation_split=0.1)

# Evaluate
y_pred = model.predict(X_test).argmax(axis=1)
print(classification_report(y_test, y_pred, target_names=encoder.classes_))

# Save
model.save("gesture_mlp_model.h5")
joblib.dump(encoder, "gesture_label_encoder.pkl")
joblib.dump(scaler, "gesture_scaler.pkl")
