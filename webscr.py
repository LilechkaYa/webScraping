from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://quotes.toscrape.com/")
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for quote, author in zip(quotes, authors):
    print(quote.text + "-" + author.text)

print("Hello World!")

