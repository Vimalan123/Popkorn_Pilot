# 🎬 PopKorn_pilot -Movie Recommendation System

## 📌 Overview

CineMatch AI is a content-based movie recommendation system developed using Python and Machine Learning techniques. The application recommends movies similar to a user's favorite movie by analyzing movie metadata such as genres, keywords, cast, and directors.

This project demonstrates how Machine Learning can be used to build personalized recommendation systems using real-world movie data.

---

## ✨ Features

* 🎥 Movie recommendations based on content similarity
* 🤖 Interactive chatbot-style command-line interface
* ⚡ Fast recommendation generation
* 📊 Uses Machine Learning techniques for similarity matching
* 🛠 Easy setup and execution

---

## 🧰 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## 🧠 How It Works

### 1. Data Collection

The project uses the TMDB 5000 Movie Dataset.

### 2. Data Preprocessing

* Merges movie and credits datasets
* Extracts genres, cast, keywords, and director information
* Cleans and processes textual data
* Combines relevant information into a single feature set

### 3. Feature Engineering

TF-IDF Vectorization converts movie metadata into numerical vectors.

### 4. Similarity Calculation

Cosine Similarity is used to calculate similarity scores between movies.

### 5. Recommendation Generation

When a user enters a movie title, the system identifies the most similar movies and recommends the top matches.

---

## 📂 Dataset Setup

This project uses the TMDB 5000 Movie Dataset.

### Download the Dataset

Download the dataset from Kaggle:

https://www.kaggle.com/datasets/tmdb/tmdb-5000-movie-dataset

### Important Setup Instructions

The dataset is downloaded as a ZIP archive.

After downloading:

1. Extract the ZIP file.
2. Locate the following files:

   * `tmdb_5000_movies.csv`
   * `tmdb_5000_credits.csv`
3. Copy both CSV files into the root directory of the project.

**Important:** Both CSV files must be placed in the same folder as the Python source files.

### Project Structure

```text
CineMatch-AI/
│
├── movie.py
├── requirements.txt
├── tmdb_5000_movies.csv
├── tmdb_5000_credits.csv
├── README.md
└── LICENSE
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/CineMatch-AI.git
cd CineMatch-AI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python movie.py
```

Replace `movie.py` with your actual Python filename if different.

---

## 💻 Example Usage

```text
Enter a movie title: The Dark Knight
```

Output:

```text
Top Movie Recommendations:

1. The Dark Knight Rises
2. Batman Begins
3. Batman
4. The Prestige
5. Man of Steel
6. Batman Returns
7. Batman Forever
8. Suicide Squad
9. Sin City
10. Batman & Robin
```

---

## 🎯 Future Enhancements

* Develop a Flask-based web application
* Add movie posters and ratings
* Implement collaborative filtering
* User authentication and profiles
* Cloud deployment
* AI-powered conversational recommendations

---


---

## 📜 License

This project is intended for educational and learning purposes.

Feel free to fork, modify, and improve the project.
