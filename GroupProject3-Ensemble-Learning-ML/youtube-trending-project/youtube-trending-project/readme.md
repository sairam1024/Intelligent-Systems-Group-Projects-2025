

#  **README.md — YouTube Trending Prediction using Ensemble Learning**

# **YouTube Trending Prediction (Ensemble Learning Project)**

This project focuses on predicting whether a YouTube video will **trend quickly** (within two days of being published) using **ensemble machine learning models**. The dataset used contains metadata for thousands of trending YouTube videos in the United States, including view counts, likes, comments, tags, category information, and more.

The project applies **Random Forest**, **Gradient Boosting**, and a **Voting Classifier** to compare performance and determine which ensemble method performs best on this classification problem.

---

# ##  Project Structure

```
youtube-trending-project/
│
├── data/
│   └── USvideos.csv
│
├── visuals/
│   ├── correlation_heatmap.png
│   ├── feature_importance.png
│   ├── views_vs_likes.png
│   └── category_counts.png
│
├── Documentation/
│   ├── youtube_trending.docx            # Your final written report
│   └── LLM_Usage_doc.docx               # LLM usage documentation
│
├── youtube_trending.ipynb               # Main Jupyter Notebook (REQUIRED)                            # (Optional helper file)
│
├── README.md                            # REQUIRED
│
└── requirements.txt                     # REQUIRED

```

---

# ##  Dataset Overview

The dataset was sourced from the **Kaggle YouTube Trending Videos Dataset**.
Key columns include:

* `views`, `likes`, `dislikes`, `comment_count`
* `category_id`
* `tags`, `title`, `description`
* `publish_time`, `trending_date`
* `comments_disabled`, `ratings_disabled`

### **Target Variable (`target`)**

A new target column was engineered:

* **1 → Fast Trending** (trended within 2 days of publishing)
* **0 → Slow Trending**

### **Features Used**

* Numerical engagement: *views, likes, dislikes, comments*
* Text-based features: *title length, description length, tag count*
* Categorical: *category_id*

---

# ## 🔧 Preprocessing Steps

* Parsed and standardized date formats
* Removed timezone information from `publish_time`
* Calculated `days_to_trend`
* Engineered text length and tag count features
* Removed duplicate video entries
* Selected model-ready features and removed missing rows

---

# ## Machine Learning Models

### ✔ **Random Forest Classifier**

* Bagging ensemble
* Robust to noise
* Good baseline model

### ✔ **Gradient Boosting Classifier**

* Boosting technique
* Sequential error correction

### ✔ **Voting Classifier (Best Overall)**

Soft-voting combination of Random Forest + Gradient Boosting
→ Achieved **highest accuracy**.

---

# ##  Model Performance

| Model                 | Accuracy          |
| --------------------- | ----------------- |
| Random Forest         | **0.8489**        |
| Gradient Boosting     | **0.8513**        |
| **Voting Classifier** | **0.8552 (Best)** |

###  Notes:

* Ensemble methods performed well but were influenced by natural dataset imbalance.
* Voting Classifier produced the most stable results.

---

# ##  Visualizations

The following visualizations were generated and saved in the `visuals/` folder:

1. **Correlation Heatmap**

   * Relationships between numerical features

2. **Feature Importance Plot (Random Forest)**

   * Views, likes, comments were the most impactful predictors

3. **Views vs Likes Scatter Plot**

   * Shows strong correlation between engagement metrics

4. **Category-wise Trending Count**

   * Distribution of trending videos across different categories

---

# ##  Key Insights

* Videos with higher engagement (views, likes, comments) tend to trend faster.
* Shorter time-to-trend is associated with strong early audience response.
* Ensemble models outperform individual models, especially in noisy datasets.
* Category-based patterns show certain genres trend more frequently.

---

# ##  How to Run This Project

### **1. Install Dependencies**

```bash
pip install pandas numpy seaborn matplotlib scikit-learn
```

### **2. Open the Notebook**

Run the Jupyter notebook inside VS Code or Jupyter Lab:

```
youtube_trending.ipynb
```

### **3. Ensure Dataset Placement**

Place **USvideos.csv** into:

```
/data/USvideos.csv
```

### **4. Run All Cells**

Visualizations and model results will be generated automatically.

---

# ##  LLM Usage Statement

Parts of this project’s structure, documentation, and explanation were created with assistance from an AI language model (ChatGPT).
However:

* All coding was executed and verified manually by the student.
* Model training, evaluation, and debugging were performed interactively by the student.
* The final interpretations, visual selection, and project decisions were made independently.

This complies with course instructions requiring transparency about LLM usage.

---

# ##  Conclusion

This project successfully demonstrates how ensemble learning techniques can be used to model the early trending behavior of YouTube videos. The **Voting Classifier** produced the best performance, achieving an accuracy of **85.52%**.

Although the dataset presents natural class imbalance, the insights gained from engagement metrics and content categories offer valuable understanding of video virality.

Future work may include:

* NLP feature extraction from titles and descriptions
* Oversampling techniques to handle class imbalance
* Deep learning models for engagement prediction

-