from flask import Flask, render_template

app = Flask(__name__)

# Bakery Products ka Data
bakery_items = [
    {"name": "Velvet Cupcake", "price": "220", "img": "https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?w=500"},
    {"name": "Chocolate Donut", "price": "150", "img": "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=500"},
    {"name": "Blueberry Muffin", "price": "300", "img": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?w=500"},
    {"name": "Strawberry Cake", "price": "1800", "img": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=500"}
]

@app.route('/')
def index():
    # Ab ye 'templates' folder mein index.html ko dhoonde ga
    return render_template('index.html', items=bakery_items)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5015)