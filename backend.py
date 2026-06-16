import pandas as pd
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load API key
load_dotenv(override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_backend(file_path):
    # Load CSV file
    df = pd.read_csv(file_path)
    summary = df.describe(include='all').to_dict()

    system_prompt = """
    You are a data visualization expert.
    Your task is to generate a full business analytics dashboard in HTML 
    (similar style to the uploaded 'Ganesh Coffee Store Dashboard').

    Requirements:
    - Use modern CSS (rounded cards, gradients, shadows)
    - Use Chart.js for all graphs
    - Use responsive layout
    - Include insights, summaries, recommendations
    - Output only clean HTML + CSS + JS (no markdown)
    """

    user_prompt = f"""
    Here is the dataset summary: {summary}

    Here is the first 20 rows: {df.head(100).to_dict()}

    Generate a complete HTML dashboard.
    Include charts such as:
    - Donut chart for category distribution
    - Bar chart for issues
    - Line chart for trends
    - Tables
    - Insight boxes
    """

    response = client.chat.completions.create(
        model="gpt-5.1",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    # Extract HTML
    html_code = response.choices[0].message.content

    # Save to file
    with open("dashboard1.html", "w", encoding="utf-8") as f:
        f.write(html_code)

    return html_code
