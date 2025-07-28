# 🛍️ Interactive Customer Segmentation

An interactive web application for customer segmentation using the K-Means clustering algorithm. This project demonstrates an end-to-end unsupervised learning workflow, allowing users to dynamically explore how changing the number of clusters affects customer groupings in real-time.

![App Screenshot](https://i.postimg.cc/85gv8vTt/Screenshot-2025-07-28-at-9-30-53-AM.png)

---

## ✨ Features

- **Dynamic Cluster Analysis**: Use an interactive slider to change the number of clusters (K) and instantly see the updated results.
- **K-Means Clustering**: Leverages the power of K-Means to identify distinct customer groups based on their annual income and spending habits.
- **Automated Personas**: Generates descriptive personas for each cluster, providing clear, actionable insights into customer behavior.
- **Elbow Method Visualization**: Includes a plot of the Elbow Method to help justify the choice of an optimal 'K'.
- **Clean UI**: A simple and intuitive user interface built with Streamlit.

---

## 🛠️ Tech Stack

- **Python**: The core programming language.
- **Pandas**: For data loading and manipulation.
- **Scikit-learn**: For implementing the K-Means clustering algorithm.
- **Streamlit**: To create and serve the interactive web application.
- **Matplotlib & Seaborn**: For creating the data visualizations.

---

## 📂 Project Structure

```
customer-segmentation-app/
│
├── Mall_Customers.csv  # The customer dataset
│
├── app.py                  # The complete Streamlit web application script
├── requirements.txt        # Python dependencies
└── README.md               # You are here!
```

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/customer-segmentation-app.git](https://github.com/YOUR_USERNAME/customer-segmentation-app.git)
    cd customer-segmentation-app
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the Dataset:**
    - Download the **Mall Customer Segmentation Data** from [this link](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python).
    - Create a `data` folder in your project directory.
    - Place the `Mall_Customers.csv` file inside this new `data` folder.

4.  **Update the File Path in `app.py`:**
    - Open `app.py` and make sure the data loading line points to the correct path:
      `df = load_data('data/Mall_Customers.csv')`

---

## 🖥️ Usage

Once the setup is complete, you can launch the Streamlit web application with a single command.

```bash
streamlit run app.py
```
Your web browser will automatically open to a local URL where the app is running. Use the slider in the sidebar to explore different customer segmentations!

---

## 💡 Future Improvements
This project provides a solid foundation. Here are some ways it could be enhanced:

- **Use More Features**: Incorporate 'Age' and 'Gender' into the clustering and use dimensionality reduction techniques like PCA to visualize the results.
- **Try Other Algorithms**: Experiment with different clustering algorithms like DBSCAN or Hierarchical Clustering to see if they provide more meaningful segments.
- **User Data Upload**: Add a feature to allow users to upload their own datasets for segmentation.
- **Deploy to the Cloud**: Deploy the app to Streamlit Community Cloud to make it publicly accessible.

---

## 📬 Contact

Jaden Isaac – A B.Tech AI & ML student passionate about building useful projects and exploring the world of technology.

Feel free to reach out with any questions or feedback!

- **GitHub**: [github.com/jadenisaac2005](https://github.com/jadenisaac2005)
- **LinkedIn**: [linkedin.com/in/jaden-isaac](https://linkedin.com/in/jaden-isaac)
