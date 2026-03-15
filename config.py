# Configuration settings for the Student Percentage Prediction Model

# Model parameters
MODEL_TYPE = 'linear_regression'  # Options: 'linear_regression', 'decision_tree', etc.
LEARNING_RATE = 0.01
EPOCHS = 1000

# Dataset settings
DATASET_PATH = 'data/students.csv'
TARGET_COLUMN = 'percentage'

# Features to include in the model
FEATURES = ['hours_studied', 'attendance_percentage', 'previous_scores']

# Logging settings
LOGGING_LEVEL = 'INFO'  # Options: 'DEBUG', 'INFO', 'WARNING', 'ERROR'
