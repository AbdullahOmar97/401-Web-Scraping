# 401-Web-Scraping

This project scrapes data from the "Books to Scrape" website and generates an API based on selected categories.

## Project Structure

├── scrape.py
├── book_api.json
├── .env
├── .gitignore
└── README.md


- `scrape.py`: Python script for web scraping and API generation.
- `book_api.json`: JSON file where API data is stored.
- `.env`: Environment variables file (not included in the repository).
- `.gitignore`: File to ignore sensitive and unnecessary files in Git.
- `README.md`: This file providing project overview, setup instructions, and usage details.

## API Structure

The generated API (`book_api.json`) contains data structured as follows:

```json
[
  {
    "data": [
      {
        "title": "The title of the book",
        "rating": "The rating of the book",
        "price": "The price of the book",
        "availability": "The availability status of the book"
      },
      ...
    ],
    "type": "The category type"
  },
  ...
]
