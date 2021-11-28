# This example sets up an endpoint using the Flask framework.
# Watch this video to get started: https://youtu.be/7Ul1vfmsDck.

import os
import stripe

from flask import Flask, redirect, render_template

app = Flask(__name__)

stripe.api_key = 'sk_test_51JtarbK5xwh57OW7OrdY1oDAfdVjp7ca2XEAggdpu1OkxRUK9UDyenJbxoUfXFHsSx6FbUdBdaqJT7zXZwB4JIWq00DVGachFp'

@app.route('/')
def index():
    return render_template("checkout.html")

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
  session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='http://localhost:4242/success',
    cancel_url='http://localhost:4242/',
  )

  return redirect(session.url, code=303)

if __name__== '__main__':
    app.run(port=4242)