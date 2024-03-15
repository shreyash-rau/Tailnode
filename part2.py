import requests 
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Books to Scrape website
URL = 'http://books.toscrape.com/index.html'

# Send a GET request to the website
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all book elements
bookshelf = soup.findAll("li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"})

# Create a CSV file
filename = "Books.csv"
f = open(filename, "w")
headers = "Book title, Price\n"
f.write(headers)

# Extract book titles and prices
for book in bookshelf:
    book_title = book.h3.a["title"]
    book_price = book.findAll("p", {"class": "price_color"})[0].text.strip()
    print(f"Title of the book: {book_title}")
    print(f"Price of the book: {book_price}")
    f.write(f"{book_title},{book_price}\n")

f.close()
