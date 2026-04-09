# Streamlit Sales App \n This app allows managers to filter and visualize product sales by category.

You are a data analyst who wants to share a simple sales summary with your non-technical manager. Instead of sending a static CSV, you decide to build a small interactive Streamlit app that displays a hardcoded dataset and lets the manager filter it by category using a dropdown.

## Task 1 — Build the App

Create a Python file called sales_app.py that does the following:

- Displays a title and a short subheader describing the app
- Creates a small hardcoded pandas DataFrame with at least 5 rows and 3 columns: Product, Category, and Sales
- Adds a selectbox that lets the user filter the table by Category
- Displays the filtered DataFrame using st.dataframe()

```python3

import streamlit as st
import pandas as pd

# --- Task 1: App Title and Subheader ---
st.title("Monthly Sales Dashboard")
st.subheader("A simple interactive summary for regional sales performance.")

# --- Task 1: Hardcoded Dataset ---
data = {
    "Product": ["Laptop", "Mouse", "Desk Chair", "Monitor", "Keyboard", "Bookshelf"],
    "Category": ["Electronics", "Electronics", "Furniture", "Electronics", "Electronics", "Furniture"],
    "Sales": [1200, 25, 300, 450, 75, 150]
}
df = pd.DataFrame(data)

```


## Task 2 — Add a Sidebar

Move the selectbox filter into a sidebar using st.sidebar. The main content area should only show the filtered table and a line chart of Sales values for the selected category using st.line_chart().

```python3

# --- Task 2: Sidebar Filter ---
# Moving the selectbox to the sidebar
st.sidebar.header("Filters")
categories = ["All"] + list(df["Category"].unique())
selected_category = st.sidebar.selectbox("Select a Category:", categories)

# Logic to filter the dataframe
if selected_category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == selected_category]

# --- Task 1 & 2: Main Content Area ---
st.write(f"### Data for: {selected_category}")
st.dataframe(filtered_df)

# Task 2: Line chart of Sales values
st.write("### Sales Trend")
st.line_chart(filtered_df.set_index("Product")["Sales"])

```