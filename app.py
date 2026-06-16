import streamlit as st
import pandas as pd
from backend import run_backend

st.set_page_config(page_title="AI Dashboard Generator", layout="wide")

st.title("📊 AI-Powered Business Dashboard Generator")
st.write("Upload a CSV file to generate a full analytics dashboard using AI.")

# File upload UI
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:

    # Read CSV for preview
    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # When button is clicked
    if st.button("Generate Dashboard"):
        with st.spinner("Generating dashboard... Please wait..."):

            # Save uploaded file temporarily
            temp_path = "uploaded_temp.csv"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Call your backend
            html_code = run_backend(temp_path)

        st.success("Dashboard generated successfully!")

        # Show dashboard inside Streamlit
        st.components.v1.html(html_code, height=900, scrolling=True)

        # Download option
        st.download_button(
            label="⬇️ Download Dashboard HTML",
            data=html_code,
            file_name="dashboard1.html",
            mime="text/html"
        )
