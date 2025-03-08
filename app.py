from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
from datetime import datetime

app = Flask(__name__)

# Mock data for products
products = [
    {
        "id": 1,
        "name": "Poster - 'John 14:6'",
        "description": "Jesus said: 'I am the way, the truth, and the life.'",
        "price": 450,
        "image": "poster1.jpg"
    },
    {
        "id": 2,
        "name": "Canvas - 'Psalm 23'",
        "description": "The Lord is my shepherd; I shall not want.",
        "price": 650,
        "image": "canvas1.jpg"
    },
    {
        "id": 3,
        "name": "Scripture - 'John 8:32'",
        "description": "'You will know the truth, and the truth will set you free.'",
        "price": 500,
        "image": "scripture1.jpg"
    }
]

# Define the path to the Excel file
excel_file = 'static/content/index.xlsx'

def load_excel_data(file_path):
    """Load the Excel file and return a dictionary of DataFrames, one per sheet."""
    return pd.read_excel(file_path, sheet_name=None)

def generate_html_content(data):
    """Generate HTML content dynamically from Excel data."""
    html_output = """
    <!-- Right Side: Bible Study Content -->
    <div class="inspiration-content">
    """
    
    for topic, df in data.items():
        topic_id = topic.lower().replace(" ", "-")
        html_output += f'<div id="{topic_id}" class="content-section">'
        html_output += f'<h3>{topic.replace("-", " ").title()}</h3>'
        
        for _, row in df.iterrows():
            if pd.isna(row['Nr.']):  # Stop if an empty row is reached
                break
            subtopic_number = int(row['Nr.'])
            subtopic = row['Subtopic']
            filename = row['Filename']
            summary = row['Summary']
            source = row['Source'] if 'Source' in row and not pd.isna(row['Source']) else "Unknown"
            date = row['Date'] if 'Date' in row and not pd.isna(row['Date']) else "No Date Provided"

             # Format the date to remove time if it's in datetime format
            if isinstance(date, str):
                formatted_date = date
            else:
                formatted_date = date.strftime('%Y-%m-%d') if isinstance(date, datetime) else "No Date Provided"
    
            # Generate the main content
            html_output += f"""
            
            <button class="accordion" data-file="{filename}" data-date="{date}">{subtopic}</button>
            <div class="accordion-content">
                <div class="content-placeholder">Loading...</div>
                <p class="content-date">Date: {formatted_date}</p>
            </div>
            """
        
        html_output += "</div>\n"  # Close topic div
    
    html_output += "</div>"  # Close inspiration-content div
    return html_output

# Load Excel data
data = load_excel_data(excel_file)

# Generate HTML content
html_content = generate_html_content(data)

# Save to an HTML file
output_file = os.path.join("templates", "generated_content.html")
with open(output_file, "w", encoding="utf-8") as file:
    file.write(html_content)

print(f"HTML content generated successfully: {output_file}")

@app.route('/')
def index():
    return render_template('index.html', title="Light of the Word", quote="You will know the Truth, and the Truth will set you free.")

@app.route('/about')
def about():
    return render_template('index.html#about', title="About Us - Light of the Word")

@app.route('/products')
def get_products():
    return render_template('index.html#products', title="Products - Light of the Word")

@app.route('/inspiration')
def inspiration():
    return render_template('inspiration.html', title="Inspiration - Light of the Word")

@app.route('/contact')
def contact():
    return render_template('index.html#contact', title="Contact Us - Light of the Word")


if __name__ == '__main__':
    app.run(debug=True)

