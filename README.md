# Getting the latest transactions mempool.space

<!-- wp:image {"id":1377,"sizeSlug":"large","linkDestination":"none"} -->
<figure class="wp-block-image size-large"><img src="https://keyhunters.ru/wp-content/uploads/2024/03/image-91-1024x437.png" alt="" class="wp-image-1377"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p>Python script that gets the latest transactions from the mempool.space website and saves them into a text file can use the following approach. We will use the library <code>requests</code>to query data from the mempool.space API and <code>json</code>work with the resulting data in JSON format.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>First make sure you have the required libraries installed. If they are not already installed, they can be installed using pip:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>pip install requests</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>Now you can use the following script to get the latest transactions and save them to a text file:</p>
<!-- /wp:paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>import requests
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
fetch_latest_transactions()</code></pre>
<!-- /wp:code -->

<!-- wp:paragraph -->
<p>This script first makes a request to the mempool.space API to get the latest transactions. It then stores this data in a text file, where each transaction is recorded on a separate line in JSON format.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p>Make sure that you have access to the Internet and that the mempool.space website is accessible, as this will determine whether the script will run successfully.</p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>Source: <a href="https://keyhunters.ru/getting-the-latest-transactions-mempool-space" target="_blank" rel="noreferrer noopener">https://keyhunters.ru/getting-the-latest-transactions-mempool-space</a></strong></p>
<!-- /wp:paragraph -->

<!-- wp:paragraph -->
<p><strong>GitHub: <a href="https://github.com/smartiden/Latest-Transactions-mempool.space" target="_blank" rel="noreferrer noopener">https://github.com/smartiden/Latest-Transactions-mempool.space</a></strong></p>
<!-- /wp:paragraph -->
