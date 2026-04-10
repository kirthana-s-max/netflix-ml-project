# Netflix Data Analysis Project

## Overview
A data analysis and ML pipeline for Netflix titles data with a FastAPI prediction service.

## Commands

### Setup & Dependencies
```bash
pip install pandas numpy matplotlib scikit-learn fastapi uvicorn joblib
```

### Run Pipeline
```bash
python main.py
```
Loads raw data → cleans it → runs EDA → saves cleaned CSV.

### Train Model
```bash
python train_model.py
```
Trains Logistic Regression on cleaned data, outputs `model.pkl`.

### Run API Service
```bash
uvicorn app:app --reload
```
Starts FastAPI server at `http://localhost:8000`.

### Test Libraries
```bash
python test.py
```

## File Descriptions
- `main.py` - Pipeline entry point
- `clean.py` - Data loading & cleaning
- `eda.py` - Exploratory analysis & visualization
- `train_model.py` - Model training script
- `app.py` - FastAPI web service
- `test.py` - Dependency verification

## API Endpoints
- `GET /` - Health check
- `POST /predict` - Predict Movie/TV Show from release year

## Agents

### MainAgent
- Role: Controls the Netflix data pipeline
- Sub-agents:
  - DataCleaningAgent
  - EDAAgent
  - ModelAgent
  - PredictionAgent

### DataCleaningAgent
- Role: Loads and cleans Netflix dataset
- File: clean.py
- Output: netflix_cleaned.csv

### EDAAgent
- Role: Performs exploratory data analysis
- File: eda.py
- Output: charts and insights

### ModelAgent
- Role: Trains Logistic Regression model
- File: train_model.py
- Output: model.pkl

### PredictionAgent
- Role: Runs FastAPI prediction service
- File: app.py
- Endpoint: /predict
