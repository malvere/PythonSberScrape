import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://megamarket.ru/catalog/?q=%D0%BC%D0%BE%D1%82%D0%BE%D1%80%D0%BD%D0%BE%D0%B5%20%D0%BC%D0%B0%D1%81%D0%BB%D0%BE%204%D0%BB"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Extract the data you need by inspecting the HTML structure of the page
    # For example, you can find and print product titles
    print(response.text)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
