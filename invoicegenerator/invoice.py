from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2> Go To Route: /generate_invoice</h2>'


@app.route('/generate_invoice')
def generate_invoice():
    # Sample invoice data (you can replace this with your own data)
    invoice_data = {
        'invoice_number': 'INV-12345',
        'date': 'December 20, 2023',
        'customer_name': 'John Doe',
        'items': [
            {'item_name': 'Product A', 'quantity': 2, 'unit_price': 25},
            {'item_name': 'Product B', 'quantity': 1, 'unit_price': 30},
            {'item_name': 'Product C', 'quantity': 3, 'unit_price': 20},
        ],
        'total': 0  # Calculate total dynamically
    }

    # Calculate total
    total = sum(item['quantity'] * item['unit_price'] for item in invoice_data['items'])
    invoice_data['total'] = total

    return render_template('invoice_template.html', invoice=invoice_data)

if __name__ == '__main__':
    app.run(debug=True)
