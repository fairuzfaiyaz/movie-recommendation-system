# 🎬 CineMatch — Movie Recommendation System

An intelligent movie recommendation system built with Python, Machine Learning, and Streamlit. CineMatch analyzes movie ratings and genres to help users discover movies they may enjoy.

## 📌 Project Overview

CineMatch is a machine learning project developed using the **MovieLens 100K dataset**. It explores different recommendation techniques, from popularity-based recommendations to personalized collaborative filtering.

The project demonstrates how recommendation systems process user preferences, calculate similarities, predict ratings, and recommend relevant movies.

## ✨ Recommendation Techniques

### 1. Popularity-Based Filtering

Recommends movies based on their ratings and popularity.

Uses a weighted rating formula to balance average ratings with the number of user ratings:

\[
WR = \frac{v}{v+m}R + \frac{m}{v+m}C
\]

Where:

- `R` = Average movie rating
- `v` = Number of ratings for the movie
- `m` = Minimum rating threshold
- `C` = Overall average rating

### 2. Content-Based Filtering

Recommends movies with similar genres.

- Extracts movie genre features.
- Creates a movie-feature matrix.
- Calculates cosine similarity between movies.
- Finds movies with similar genre combinations.

### 3. User-Based Collaborative Filtering

Recommends movies based on the preferences of similar users.

- Creates a user-item rating matrix.
- Calculates user similarity using cosine similarity.
- Identifies similar users.
- Predicts ratings using similarity-weighted ratings.
- Recommends movies based on predicted preferences.

## 📊 Dataset

**MovieLens 100K Dataset**

Source: [GroupLens Research — MovieLens 100K](https://grouplens.org/datasets/movielens/100k/)

Dataset statistics:

| Description   | Quantity |
| ------------- | -------: |
| Movies        |    1,682 |
| Users         |      943 |
| Ratings       |  100,000 |
| Rating scale  |      1–5 |
| Training data |   80,000 |
| Testing data  |   20,000 |

The dataset contains movie ratings, movie information, and genre classifications.

## 📈 Model Evaluation

The user-based collaborative filtering model was evaluated using an 80/20 train-test split.

| Evaluation Metric | Global Average Baseline | Collaborative Filtering |
| ----------------- | ----------------------: | ----------------------: |
| MAE               |                  0.9420 |              **0.8149** |
| RMSE              |                  1.1239 |              **1.0316** |

The collaborative filtering model achieved lower prediction errors than the global-average baseline.

- MAE improvement: approximately **13.49%**
- RMSE improvement: approximately **8.21%**

These results indicate that incorporating similarities between users improves rating predictions compared with using a single global average.

## 🛠️ Technologies Used

- **Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Data Visualization:** Matplotlib, Seaborn
- **Web Application:** Streamlit
- **Development Environment:** VS Code, Jupyter Notebook
- **Dataset:** MovieLens 100K

## 📁 Project Structure

```text
movie-recommendation-system/
│
├── dataset/
│   └── ml-100k/
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   └── ...
│
├── models/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/movie-recommendation-system.git
```

### 2. Navigate to the project directory

```bash
cd movie-recommendation-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

## 🚀 Current Development Status

- [x] MovieLens 100K dataset download and loading
- [x] Exploratory Data Analysis
- [x] Popularity-based recommendation
- [x] Content-based filtering
- [x] User-based collaborative filtering
- [x] Training and testing dataset split
- [x] MAE and RMSE evaluation
- [x] Comparison against global-average baseline
- [x] Initial Streamlit application and dashboard
- [ ] Interactive movie search
- [ ] Popularity-based recommendations in the web app
- [ ] Content-based recommendations in the web app
- [ ] Personalized recommendations in the web app
- [ ] Final application testing and improvements

## 🎯 Project Objectives

- Understand how recommendation systems work.
- Explore different recommendation algorithms.
- Apply similarity measures to movie and user data.
- Predict user ratings using collaborative filtering.
- Evaluate recommendation performance using MAE and RMSE.
- Build an interactive web application using Streamlit.

## 👨‍💻 Author

**Fairuz Faiyaz**

Computer Science and Engineering Student

- GitHub: [@fairuzfaiyaz](https://github.com/fairuzfaiyaz)

---

_Developed as a hands-on Machine Learning project._
