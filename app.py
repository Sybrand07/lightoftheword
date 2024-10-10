from flask import Flask, render_template, request, redirect, url_for

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

@app.route('/')
def index():
    return render_template('index.html', title="Light of the Word", quote="You will know the Truth, and the Truth will set you free.")

@app.route('/about')
def about():
    return render_template('index.html#about', title="About Us - Light of the Word")

@app.route('/products')
def get_products():
    return render_template('index.html#products', title="Contact Us - Light of the Word")

@app.route('/contact')
def contact():
    return render_template('index.html#contact', title="Contact Us - Light of the Word")


if __name__ == '__main__':
    app.run(debug=True)
