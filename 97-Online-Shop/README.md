# Flask E-Commerce Payment Gateway (Stripe API)

A full-stack e-commerce web application built using Python Flask and integrated with the Stripe Checkout API for secure financial payment processing.

## 🚀 Key Features
* **Session-Based Cart State:** Persists active user carts across routes using Flask encrypted client-side sessions (`session`).
* **Stripe Checkout Integration:** Generates dynamic PCI-compliant checkout sessions using Stripe's REST SDK.
* **Price Standardization Engine:** Normalizes currency representation between internal subunit integers (cents) and user-facing float outputs.
* **Order Fulfillment Pipeline:** Verifies completed transactions via asynchronous session retrieval (`stripe.checkout.Session.retrieve`).

## 🛠️ Stack
* Python 3
* Flask (Backend Server & Templating Engine)
* Stripe API (Payment Processing)
* HTML5 / CSS3 (Jinja2 Rendered Frontend)

## 📁 Repository Structure
```text
.
├── templates/
│   ├── home.html            # Product showcase layout
│   ├── cart.html            # Order breakdown & checkout trigger
│   ├── success.html         # Post-purchase confirmation
│   └── cancel.html          # Abandoned session handler
├── .env                     # Private Stripe keys (Git ignored)
├── .gitignore               # Security exclusions
├── main.py                  # Core web app logic & API routes
└── README.md                # Technical documentation