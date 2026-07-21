import os
import stripe
from flask import Flask, render_template, session, redirect, url_for, request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "ufhwfhdkfjewofi")

stripe.api_key = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")

PRODUCTS = [
    { 
        "id": 1,
        "name": "Wireless Mouse",
        "description": "Ergonomic Wireless Mouse",
        "price": 1999,  
        "image_url": "https://via.placeholder.com/150"
    },
    {
        "id": 2,
        "name": "Mechanical Keyboard",
        "description": "RGB Mechanical Keyboard",
        "price": 5999,  
        "image_url": "https://via.placeholder.com/150"
    },
    {
        "id": 3,
        "name": "USB-C Hub",
        "description": "7-in-1 USB-C Hub",
        "price": 3499,  
        "image_url": "https://via.placeholder.com/150"
    }
]

@app.route('/')
def home():
    formatted_products = [
        {**p, "display_price": p["price"] / 100} for p in PRODUCTS
    ]
    return render_template("home.html", products=formatted_products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get("cart", {})
    product_id_str = str(product_id)

    cart[product_id_str] = cart.get(product_id_str, 0) + 1
    session["cart"] = cart

    return redirect(url_for("home"))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get("cart", {})
    product_id_str = str(product_id)

    if product_id_str in cart:
        if cart[product_id_str] > 1:
            cart[product_id_str] -= 1
        else:
            cart.pop(product_id_str)

    session["cart"] = cart
    return redirect(url_for("cart"))


@app.route('/cart')
def cart():
    cart = session.get("cart", {})
    cart_items = []
    total = 0

    for product in PRODUCTS:
        pid = str(product["id"])
        if pid in cart:
            quantity = cart[pid]
            price_dollars = product["price"] / 100
            subtotal = quantity * price_dollars

            cart_items.append({
                "id": product["id"],
                "name": product["name"],
                "price": price_dollars,
                "quantity": quantity,
                "subtotal": subtotal
            })
            total += subtotal

    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    cart = session.get("cart", {})

    if not cart:
        return "Cart is empty.", 400

    line_items = []

    for product in PRODUCTS:
        product_id = str(product["id"])

        if product_id in cart:
            quantity = cart[product_id]

            line_items.append({
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": product["name"]
                    },
                    "unit_amount": product["price"], 
                },
                "quantity": quantity,
            })

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode="payment",
            success_url=url_for("success", _external=True) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=url_for("cancel", _external=True),
        )

        return redirect(checkout_session.url, code=303)

    except Exception as e:
        return {"error": str(e)}, 500

@app.route("/success")
def success():
    session_id = request.args.get("session_id")

    if not session_id:
        return "Missing session_id.", 400

    try:
        checkout_session = stripe.checkout.Session.retrieve(session_id)

        if checkout_session.payment_status == "paid":
            session.pop("cart", None)  

            return render_template(
                "success.html",
                checkout_session=checkout_session
            )

        return render_template(
            "payment_pending.html",
            checkout_session=checkout_session
        )

    except stripe.error.StripeError as e:
        return f"Stripe error: {str(e)}", 400

@app.route("/cancel")
def cancel():
    return render_template("cancel.html")

@app.route("/webhook", methods=["POST"])
def stripe_webhook():
    payload = request.get_data(as_text=False)
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload=payload,
            sig_header=sig_header,
            secret=STRIPE_WEBHOOK_SECRET,
        )
    except ValueError:
        return "Invalid payload", 400
    except stripe.error.SignatureVerificationError:
        return "Invalid signature", 400

    if event["type"] == "checkout.session.completed":
        pass

    return "", 200

if __name__ == "__main__":
    app.run(debug=True)