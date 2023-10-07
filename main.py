import os
import pdfkit
import requests
from bs4 import BeautifulSoup

def generate_pdf(limit):
    count = 1

    # Create the "articles" directory if it doesn't exist
    if not os.path.exists("Articles"):
        os.makedirs("Articles")

    while count <= limit:
        URL = "https://en.wikipedia.org/wiki/Special:Random"
        reqs = requests.get(URL)
        soup = BeautifulSoup(reqs.text, 'html.parser')

        for title in soup.find_all("title"):
            pdf_title = title.get_text()

        pdfkit.from_url(URL, f"Articles/{pdf_title.replace('- Wikipedia','')}.pdf")

        print(f"Generated {count} articles.")
        count += 1

def main():
    limit = int(input("Number of articles to generate: "))
    generate_pdf(limit)

if __name__ == '__main__':
    main()

