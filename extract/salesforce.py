import os
import requests
from typing import Any
from dotenv import load_dotenv

load_dotenv()


class SalesforceExtractor:
    def __init__(self):
        self.instance_url = os.getenv("SALESFORCE_INSTANCE_URL")
        self.access_token = os.getenv("SALESFORCE_ACCESS_TOKEN")
        self.api_version = os.getenv("SALESFORCE_API_VERSION", "v61.0")

        if not self.instance_url:
            raise ValueError("SALESFORCE_INSTANCE_URL is not configured")

        if not self.access_token:
            raise ValueError("SALESFORCE_ACCESS_TOKEN is not configured")

        self.base_url = (
            f"{self.instance_url}/services/data/{self.api_version}"
        )

        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }

    def get_records(self, soql: str) -> list[dict[str, Any]]:
        """
        Execute a Salesforce SOQL query and fetch all records
        using Salesforce pagination.
        """

        url = f"{self.base_url}/query"
        params = {"q": soql}

        all_records = []

        while url:
            response = requests.get(
                url,
                headers=self.headers,
                params=params,
                timeout=30,
            )

            if response.status_code != 200:
                raise RuntimeError(
                    f"Salesforce API error "
                    f"{response.status_code}: {response.text}"
                )

            data = response.json()

            records = data.get("records", [])
            all_records.extend(records)

            # Salesforce gives nextRecordsUrl when more records exist
            next_url = data.get("nextRecordsUrl")

            if next_url:
                url = f"{self.instance_url}{next_url}"
                params = None
            else:
                url = None

        return all_records

    def get_customers(self) -> list[dict[str, Any]]:
        """
        Extract customer/business information from Salesforce.
        """

        soql = """
            SELECT
                Id,
                Name,
                Phone,
                Website,
                Industry,
                BillingCity,
                BillingState,
                BillingCountry
            FROM Account
            ORDER BY CreatedDate ASC
        """

        return self.get_records(soql)


if __name__ == "__main__":
    extractor = SalesforceExtractor()

    records = extractor.get_customers()

    print(f"Total records extracted: {len(records)}")

    for record in records[:5]:
        print(record)