import streamlit as st

def render_ui():
    st.sidebar.header("Controls")
    algo_name = st.sidebar.radio("Select Algorithm", ["Sobel", "Laplacian", "Canny"])

    params = {}
    
    if algo_name == "Sobel":
        params["ksize"] = st.sidebar.slider("Kernel Size", 1, 7, 3, step=2)
        params["direction"] = st.sidebar.radio("Gradient Direction", ["X", "Y", "Both"])

    elif algo_name == "Laplacian":
        params["ksize"] = st.sidebar.slider("Kernel Size", 1, 7, 3, step=2)

    elif algo_name == "Canny":
        params["lower"] = st.sidebar.slider("Lower Threshold", 0, 255, 100)
        params["upper"] = st.sidebar.slider("Upper Threshold", 0, 255, 200)
        params["sigma"] = st.sidebar.slider("Sigma (Gaussian Blur)", 0.0, 3.0, 1.0)

    return algo_name, params
