Following the instructions provided on Stripe Checkout docs (https://stripe.com/docs/payments/accept-a-payment?integration=checkout#create-product-prices-upfront)

Stripe Checkout is a Stripe product that allows a user to integrate a simple payment flow on their web app in order to receive payments.

In this demo, when the Checkout button is clicked on a locally hosted Flask web app, a Stripe payment session is instantiated for a $20 charge for 1 tee shirt.

###Setup requirements
- Stripe account and API keys. Ensure that the account has an account name or business name. This may be updated via the Stripe dashboard.
- install flask, and stripe in the project virtual environment (env)
- Stripe test card details

###Using Environment variables
- Stripe API key are loaded using environment variables for security.
- Create a .env file on the same level directory as the server.py file.
- Put the Stripe secret keys and publishable keys here. 

###Running locally
- Run the application locally on port 4242 

###Project demo
- Watch a demo of the project on YouTube. 