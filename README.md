# 🎬 Movie Recommendation AI Chatbot

A simple, command-line AI chatbot that recommends movies based on your favorite films. Provide a film you like, and the chatbot will suggest 10 other movies you might enjoy!

---

## 🌟 About The Project

This project is a content-based recommendation system built in Python. It leverages metadata associated with movies—such as genres, keywords, cast, and crew—to identify and suggest films with similar characteristics. The chatbot provides an easy-to-use, interactive command-line interface for getting movie recommendations.

### Built With
* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Scikit-learn](https://scikit-learn.org/stable/)

---

## 🤔 How It Works

The recommendation engine is built on the concept of **content-based filtering**. The core logic involves these steps:

1.  **Data Preprocessing**: The script loads the movie data, merges the movie and credit datasets, and cleans the text-based features (genres, keywords, cast, director). All relevant metadata is combined into a single string or "soup" for each movie.

2.  **Vectorization**: The text "soup" for all movies is converted into a numerical matrix using a **TF-IDF Vectorizer**. This process transforms each movie's metadata into a feature vector in a high-dimensional space.

3.  **Similarity Calculation**: The **Cosine Similarity** metric is used to calculate the similarity between each pair of movie vectors. Movies with a higher cosine similarity score are considered more alike.

4.  **Recommendation**: When you input a movie title, the system finds its corresponding vector and returns the 10 movies with the highest similarity scores.

---

## 🚀 Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites

* Python 3.x installed on your system.
* pip (Python package installer).

### Installation

1.  **Clone the repository**
    ```sh
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```

2.  **Download the Dataset**
    * This repository does not include the dataset files due to their size.
    * You must download the "TMDB 5000 Movie Dataset" from **[Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-5000-movie-dataset)**.
    * After unzipping the download, place the two required files, `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`, into the root of this project folder.

3.  **Install Python packages**
    * Install the necessary libraries using the `requirements.txt` file.
    ```sh
    pip install -r requirements.txt
    ```

---

## 🎮 Usage

Once the setup is complete, run the chatbot with the following command:

```sh
python movie.py
```
*(Replace `movie.py` with the name of your Python script if it's different)*

The chatbot will greet you and prompt you to enter a movie title.

**Example Interaction:**
```
Enter a movie title you like: The Dark Knight

Great! If you liked 'The Dark Knight', you might also enjoy these movies:
  1. The Dark Knight Rises
  2. Batman Begins
  3. Batman
  4. Batman Returns
  5. The Prestige
  6. Suicide Squad
  7. Batman & Robin
  8. Man of Steel
  9. Sin City
  10. Batman Forever
```

---
## 💡 Future Improvements

* [ ] Develop a web-based UI using Flask or Django.
* [ ] Implement other recommendation algorithms (e.g., Collaborative Filtering).
* [ ] Integrate a more advanced NLP model to understand conversational queries.
* [ ] Deploy the application as a web service.

---
## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
## 🙏 Acknowledgments
* This project uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-5000-movie-dataset) available on Kaggle.
* Inspiration from various data science tutorials and articles.
