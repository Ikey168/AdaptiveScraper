import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin



def scrape_website(url):

    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    
    # Make a GET request to the URL
    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all text from the page
        all_text = soup.get_text()

        # Print or store the extracted text
        print(all_text)
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Replace 'https://example.com' with the URL of the website you want to scrape
scrape_website('https://www.bpigs.com/')