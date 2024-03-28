import requests
import json

def fetch_latest_transactions():
    # URL to get latest transactions from mempool.space API
    url = "https://mempool.space/api/mempool/recent"

    try:
        # Send a GET request and receive data
        response = requests.get(url)
        response.raise_for_status()  # Checking for request errors
        transactions = response.json()  # Receiving data in JSON format

        # Opening a file for writing
        with open("latest_transactions.txt", "w") as file:
            for transaction in transactions:
                # We record information about each transaction in a file
                file.write(json.dumps(transaction) + "\n")

        print("We record information about each transaction in a file 'latest_transactions.txt'.")

    except requests.RequestException as e:
        print(f"Error while receiving data: {e}")

# Calling the function
fetch_latest_transactions()