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