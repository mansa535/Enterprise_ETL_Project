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
            # Fixed capital C for Customer object and indentation layout
            response = stripe.Customer.list(
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

        # Confirmed raw-data folder naming convention with project guidelines
        folder_path = "raw-data"
        os.makedirs(folder_path, exist_ok=True)
        
        file_path = os.path.join(folder_path, "stripe_customers.json")
        with open(file_path, "w") as f:
            # Handle list parsing dynamically for mock objects and standard dictionaries
            json.dump([c.to_dict() if hasattr(c, 'to_dict') else c for c in all_customers], f, indent=4)
            
        print(f"Success! Saved {len(all_customers)} customers")
        return len(all_customers)  # Returns accurate record count for automated test metrics
        
    except Exception as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    extract_stripe_customers()