import stripe
import os
import json
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY")

def extract_stripe_customers():
    print("Extracting Stripe customers...")
    try:
        customers = stripe.Customer.list(limit=100)
        
        os.makedirs("raw_data", exist_ok=True)
        with open("raw_data/stripe_customers.json", "w") as f:
            json.dump([c.to_dict() for c in customers.auto_paging_iter()], f, indent=2, default=str)
        
        print(f"Success! Saved {len(customers.data)} customers")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_stripe_customers()
