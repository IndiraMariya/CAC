import requests
from bs4 import BeautifulSoup
import re  # Import the 're' module for regular expressions

def scrape_and_display_top_image(article_url):
    try:
        # Send a GET request to the article URL
        response = requests.get(article_url)
        response.raise_for_status()  # Raise an exception for any HTTP errors

        # Parse the HTML content of the article
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the image element by inspecting the HTML structure of the webpage
        img_element = soup.find('img', {'style': re.compile(r'background-image:.*url\([\'"](.*?)[\'"]\)')})

        if img_element:
            # Extract the image URL from the 'srcset' attribute
            srcset_attr = img_element.get('srcset')
            if srcset_attr:
                # Split the srcset attribute by commas to separate different URLs
                image_urls = [url.strip() for url in srcset_attr.split(',')]
                # Take the first URL as the top image (you can adjust this logic)
                top_image_url = image_urls[0].split()[0]

                # Display the top image URL
                print(f"Top Image URL: {top_image_url}")
            else:
                print("No 'srcset' attribute found for the image.")
        else:
            print("No image found on the webpage.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the article: {e}")

if __name__ == "__main__":
    article_url = "https://www.washingtonpost.com/politics/2023/09/02/sherrod-brown-ohio-reelection/"
    scrape_and_display_top_image(article_url)
