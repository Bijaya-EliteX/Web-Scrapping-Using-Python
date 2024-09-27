import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = "https://www.wscubetech.com/"
x = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(x.text, "lxml")

# Print the HTML in an indented, properly formatted manner
print(soup.prettify())
