import os
import json
import stripe
from dotenv import load_dotenv

load_dotenv()
stripe.api_key = os.getenv("STRIPE_API_KEY") or "sk_test_mockkey12345"

def extract_stripe_customers():
    print("Extracting Stripe customers...")
    
    all_customers = []
    has_more = True
    starting_after = None

    try:
        while has_more:
            response = stripe.customer.list(
                limit=100,
                starting_after=starting_after
            )
            
            customers_page = response.get('data', [])
            all_customers.extend(customers_page)
            
            has_more = response.get('has_more', False)
            
            if has_more and customers_page:
                starting_after = customers_page[-1]['id']
                print(f"Fetched {len(customers_page)} customers. Moving to next page...")
            else:
                print("Fetched final page. Done!")

        os.makedirs("raw_data", exist_ok=True)
        
        with open("raw_data/stripe_customers.json", "w") as f:
            json.dump([c.to_dict() for c in all_customers], f, indent=4)
            
        print(f"Success! Saved {len(all_customers)} customers")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_stripe_customers()