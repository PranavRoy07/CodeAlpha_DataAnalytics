import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Website URL
url = "https://books.toscrape.com/"

# Step 2: Send request to website
response = requests.get(url)

# Step 3: Parse HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 4: Find all book containers
books = soup.find_all("article", class_="product_pod")

# Step 5: Create empty lists
titles = []
prices = []
ratings = []
availability = []

# Step 6: Extract data from each book
for book in books:
    # Book title
    title = book.h3.a["title"]
    titles.append(title)

    # Book price
    price = book.find("p", class_="price_color").text
    prices.append(price)

    # Book rating
    rating = book.find("p", class_="star-rating")
    ratings.append(rating["class"][1])

    # Availability
    stock = book.find("p", class_="instock availability").text.strip()
    availability.append(stock)

# Step 7: Create DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Availability": availability
})

# Step 8: Save to CSV
df.to_csv("books_data.csv", index=False)

print("Web scraping completed. Data saved as books_data.csv")
