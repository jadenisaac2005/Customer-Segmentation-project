import pandas as pd
import streamlit as st
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# --- Page Configuration ---
st.set_page_config(
    page_title="Customer Segmentation App",
    page_icon="🛍️",
    layout="wide"
)

# --- Data Loading ---
@st.cache_data
def load_data(path):
    """Loads the customer dataset from a CSV file."""
    df = pd.read_csv(path)
    return df

df = load_data('Mall_Customers.csv')
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# --- App Title ---
st.title("🛍️ Interactive Customer Segmentation")

# --- Sidebar for User Input ---
st.sidebar.header("Clustering Controls")
k = st.sidebar.slider("Select number of clusters (K)", min_value=2, max_value=10, value=5)

# --- K-Means Clustering ---
kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# Add cluster labels to the original data
X['Cluster'] = y_kmeans
centroids = kmeans.cluster_centers_

# --- Main Page Visualization ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header(f"Customer Segments (K={k})")
    # Create a scatter plot for the clusters
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.scatterplot(
        x='Annual Income (k$)',
        y='Spending Score (1-100)',
        hue='Cluster',
        data=X,
        palette='viridis',
        s=100,
        ax=ax
    )
    # Plot the centroids
    ax.scatter(centroids[:, 0], centroids[:, 1], s=300, c='red', marker='X', label='Centroids')
    ax.set_title('Customer Segments')
    ax.legend()
    st.pyplot(fig)

# --- Display Cluster Personas ---
with col2:
    st.header("Cluster Personas")
    for i in range(k):
        # Get the center of the current cluster
        center_income = centroids[i][0]
        center_score = centroids[i][1]

        # Simple logic to create personas
        income_level = "High" if center_income > 65 else "Low" if center_income < 40 else "Average"
        score_level = "High" if center_score > 60 else "Low" if center_score < 40 else "Average"

        st.subheader(f"Cluster {i}: {income_level} Income, {score_level} Spending")
        st.write(f"- Average Annual Income: ${center_income:.1f}k")
        st.write(f"- Average Spending Score: {center_score:.1f}")

# --- Elbow Method (in an expander) ---
with st.expander("Why K=5? See the Elbow Method"):
    wcss = []
    for i in range(1, 11):
        kmeans_elbow = KMeans(n_clusters=i, init='k-means++', random_state=42)
        kmeans_elbow.fit(X.drop(columns=['Cluster']))
        wcss.append(kmeans_elbow.inertia_)

    fig_elbow, ax_elbow = plt.subplots(figsize=(10, 6))
    ax_elbow.plot(range(1, 11), wcss, marker='o')
    ax_elbow.set_title('The Elbow Method')
    ax_elbow.set_xlabel('Number of clusters (K)')
    ax_elbow.set_ylabel('WCSS')
    st.pyplot(fig_elbow)
