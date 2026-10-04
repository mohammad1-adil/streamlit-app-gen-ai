import streamlit as st

st.set_page_config(
    page_title="Python Crash Course",
    page_icon="🐍",
    layout="wide"
)

st.title("Python Applications Crash Course")
st.header("Streamlit Basics")
st.subheader("Build simple web applications with Python")

st.write("Streamlit lets us turn Python code into an interactive web application.")

st.markdown("### Markdown also works")
st.caption("This is a small caption.")

# ------------------------------------------------------------
# 3. Code, JSON and metric
# ------------------------------------------------------------
st.code("print('Hello, Streamlit!')", language="python")

st.json({
    "course": "Python",
    "level": "Beginner"
})

st.metric("Students", 25, "+5")

# ------------------------------------------------------------
# 4. Sidebar
# ------------------------------------------------------------
st.sidebar.title("Course Menu")
st.sidebar.write("Choose an option below.")

topic = st.sidebar.selectbox(
    "Choose a topic",
    ["Python", "Pandas", "NumPy", "AI Applications"]
)

st.write("Selected topic:", topic)
