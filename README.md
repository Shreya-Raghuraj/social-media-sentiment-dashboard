# Social Media Sentiment Dashboard

##  Overview

The Social Media Sentiment Dashboard is a Streamlit-based web application that analyzes social media tweets and classifies them into Positive, Negative, and Neutral sentiments. The dashboard provides interactive visualizations to help users understand sentiment distribution within a dataset.

---

##  Features

- Upload and analyze tweet datasets
- Text preprocessing and cleaning
- Sentiment analysis
- Interactive dashboard using Streamlit
- Sentiment distribution charts
- Dataset filtering and exploration

---

##  Technologies Used

- Python
- Streamlit
- Pandas
- Matplotlib
- Plotly

---

## 📂 Project Structure

```
social-media-sentiment-dashboard/
│
├── data/
│   ├── raw/
│   │   └── tweets.csv
│   └── processed/
│       └── sentiment.csv
│
├── modules/
│   ├── data_collection.py
│   ├── filters.py
│   ├── sentiment.py
│   └── visualizations.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Shreya-Raghuraj/social-media-sentiment-dashboard.git
```

Move into the project folder

```bash
cd social-media-sentiment-dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📊 Workflow

1. Load tweet dataset.
2. Clean and preprocess text.
3. Perform sentiment analysis.
4. Save processed data.
5. Visualize sentiment distribution using Streamlit.

---

## 📁 Dataset

The project uses a CSV dataset containing social media tweets stored in:

```
data/raw/tweets.csv
```

The processed dataset is stored in:

```
data/processed/sentiment.csv
```

---

## 👥 Contributors

- Shreya Raghuraj
- Vanshika
- Arpana
- Avika
