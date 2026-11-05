import streamlit as st

## Page configuration
st.set_page_config(
    page_title="Python crash course",
    page_icon="🐍",
    layout="wide"
)

## Title, header, sub-header and text
st.title("Pyhton Applications crash course")
st.header("Streamlit Basics")
st.subheader("Build simple web application with python")
st.write("Streamlit lets us turn Python code into interactive web application")

st.markdown("### Markdown also works")
st.caption("This is a small caption.")

### Code, JSON and metric
st.code("print('Hello, Streamlit!!')", language="python")
st.json({
    "Course": "Python",
    "Level": "Beginner"
})

st.metric("Students", 25, "+5")

## Sidebar
st.sidebar.title("Course Menu")
st.sidebar.write("Choose an option below.")
st.sidebar.selectbox(
    "Choose a topic",
    ["Pyhton", "Pandas", "Numpy", "AI Applications"]
)
