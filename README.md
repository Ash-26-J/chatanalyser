# Chat Analyser

This project presents a comprehensive chat analyser designed to provide in-depth insights into group chat conversations. Leveraging machine learning techniques, it visualizes various parameters of the chat data, offering a deeper understanding of communication patterns and sentiments.

## Features

The analyser provides the following visualized representations:

* **Word Cloud:** Highlights the most frequently used words in the chat.
* **Bar Graphs:** Illustrates various metrics such as message frequency per user, most active times, etc.
* **Line Graphs:** Shows trends over time, like message volume progression.
* **Pie Chart:** Represents proportions of different categories (e.g., message types).
* **Donut Graph:** Similar to a pie chart but with an empty center, often used for highlighting proportions.
* **Heat Map:** Visualizes message activity based on time of day and day of the week.

## Machine Learning & Sentiment Analysis

This project is primarily driven by machine learning for its analytical capabilities. A key component, also a part of a larger major project, is a **sentiment analysis** module that assesses the emotional tone of messages within the chat.

## Technologies Used

The following tools and libraries are integral to this project:

* **Data Manipulation:**
    * `pandas`: For efficient data structuring and manipulation.
    * `re`: For regular expression operations, particularly useful in text processing.
* **Data Visualization:**
    * `seaborn`: For creating aesthetically pleasing statistical graphics.
    * `matplotlib`: A foundational library for creating static, animated, and interactive visualizations.
    * `WordCloud`: To generate word cloud visualizations.
* **Natural Language Processing & Sentiment Analysis:**
    * `TextBlob`: A simple API for common natural language processing (NLP) tasks, including sentiment analysis.
* **Utility:**
    * `collections`: Provides high-performance container datatypes.
* **User Interface:**
    * `streamlit`: Utilized for building a user-friendly and interactive web application, chosen over frameworks like Flask or FastAPI for its rapid prototyping capabilities.

## How to Run

To get this chat analyser up and running on your local machine, follow these simple steps:

1.  **Download the Project:**
    Clone this repository to your local machine using Git:
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
    (Replace `your-username` and `your-repository-name` with the actual GitHub details.)

2.  **Install Dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```
    (You'll need to create a `requirements.txt` file containing all the libraries listed above, one per line. For example: `pandas`, `re`, `seaborn`, `matplotlib`, `wordcloud`, `textblob`, `streamlit`.)

3.  **Run the Application:**
    Navigate to the project's root directory in your terminal and execute the following command:
    ```bash
    streamlit run app.py
    ```
    This will open the application in your default web browser.

---
