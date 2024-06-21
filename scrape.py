import requests
from bs4 import BeautifulSoup
import json

# URL for the base site
BASE_URL = "https://books.toscrape.com/catalogue/category/books/"

# Categories to scrape
categories = [
    "travel_2",
    "mystery_3",
    "historical-fiction_4"
]

# Function to scrape a category
def scrape_category(category):
    url = BASE_URL + category + "/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    books = []
    for article in soup.find_all('article', class_='product_pod'):
        title = article.h3.a.attrs['title']
        price = article.find('p', class_='price_color').text
        availability = article.find('p', class_='instock availability').text.strip()
        rating = article.p.attrs['class'][1]
        
        books.append({
            "title": title,
            "rating": rating,
            "price": price,
            "availability": availability
        })
    
    return books

# Main function to generate API
def generate_api():
    api_data = []
    for category in categories:
        books = scrape_category(category)
        api_data.append({
            "data": books,
            "type": category.split('_')[0].capitalize()  # Extract type from category name
        })
    
    return api_data

# Save API data to JSON file
def save_to_json(data):
    with open('book_api.json', 'w') as outfile:
        json.dump(data, outfile, indent=2)

if __name__ == "__main__":
    api_data = generate_api()
    save_to_json(api_data)
    print("API data generated and saved to book_api.json")
