# Netflix Data Analysis & Prediction API

A data analysis and machine learning pipeline for Netflix titles with a FastAPI prediction service.

## Overview

This project loads, cleans, and analyzes Netflix titles data, trains a classification model to predict content type (Movie vs TV Show), and exposes predictions via a REST API.

## Features

- **Data Pipeline**: Load raw CSV → Clean → EDA → Save cleaned data
- **ML Model**: Logistic Regression classifier for Movie/TV Show prediction
- **REST API**: FastAPI service with prediction endpoint
- **Visualizations**: Distribution histograms and analysis charts

## Quick Start

### 1. Install Dependencies

```bash
pip install pandas numpy matplotlib scikit-learn fastapi uvicorn joblib requests
```

### 2. Run the Pipeline

```bash
python main.py
```

This loads raw data, cleans it, runs EDA, and saves `netflix_cleaned.csv`.

### 3. Train the Model

```bash
python train_model.py
```

Trains a Logistic Regression model and saves `model.pkl` and `label_encoder.pkl`.

### 4. Start the API

```bash
uvicorn app:app --reload
```

API runs at `http://localhost:8000`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Health check |
| `/predict` | GET | Predict Movie/TV Show |
| `/docs` | GET | Interactive API documentation |

### Predict Example

```bash
curl "http://localhost:8000/predict?release_year=2020"
```

Response:
```json
{
  "release_year": 2020,
  "prediction": "Movie"
}
```

## Project Structure

```
├── main.py           # Pipeline entry point
├── clean.py          # Data loading and cleaning
├── eda.py            # Exploratory data analysis
├── train_model.py    # Model training script
├── app.py            # FastAPI web service
├── test.py           # Library verification
├── netflix_titles.csv      # Raw dataset
├── netflix_cleaned.csv     # Cleaned dataset
├── model.pkl              # Trained model
├── label_encoder.pkl     # Label encoder
└── eda_distributions.png  # EDA visualization
```

## Data Flow

```
netflix_titles.csv
    ↓
main.py (clean.py + eda.py)
    ↓
netflix_cleaned.csv
    ↓
train_model.py
    ↓
model.pkl + label_encoder.pkl
    ↓
app.py (FastAPI)
    ↓
/predict endpoint
```

## Dataset

| Metric | Value |
|--------|-------|
| Total Titles | 8,807 |
| Movies | 6,131 (70%) |
| TV Shows | 2,676 (30%) |
| Release Year Range | 1925 - 2021 |

## Model Performance

- **Algorithm**: Logistic Regression
- **Accuracy**: ~69%
- **Features**: release_year
- **Target**: Movie (0) / TV Show (1)

## Requirements

- Python 3.8+
- pandas
- numpy
- matplotlib
- scikit-learn
- fastapi
- uvicorn
- joblib
- requests

## License

MIT
