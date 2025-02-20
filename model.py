import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
from imblearn.over_sampling import RandomOverSampler

# Load dataset
data = pd.read_csv("blooddonation_dataset.csv")

# Separate features and target variable
X = data.drop(columns=["Eligible"])
Y = data["Eligible"]

# Apply Random Oversampling to balance the dataset
oversampler = RandomOverSampler(random_state=0)
X_resampled, Y_resampled = oversampler.fit_resample(X, Y)

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_resampled, Y_resampled, test_size=0.2, random_state=0)

# Initialize and train the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, Y_train)

# Make predictions
y_predict = model.predict(X_test)

# Evaluate model accuracy
accuracy = accuracy_score(Y_test, y_predict)
print(f"Model Accuracy: {accuracy:.2f}")

# Save the trained model
joblib.dump(model, "blood_model.pkl")
print("Model trained and saved successfully.")
