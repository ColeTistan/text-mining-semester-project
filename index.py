from bs4 import BeautifulSoup

import requests


def scrape_data(url):
    """
    Request and scrape data from url entered

    Args:
        url (String): URL link entered by user
    """
    web_page = requests.get(url)
    soup = BeautifulSoup(web_page.text, "html.parser")
    product_name = soup.h1.string
    print(f"{soup.title}\n{product_name}")
    

if __name__ == "__main__":
    user_input = input("Enter a url: ")
    scrape_data(user_input)
    
