# Random PDF Generator

This Python script utilizes Wikipedia's random article function to generate a specified number of PDF files with diverse content. Some websites such as StuDocu and ScribD require the user to upload their own PDFs in order to download content off of their website. This script can easily generate unique PDFs that will be accepted by these websites.

## Usage:
1. Ensure you have the required Python packages installed:
   - `pdfkit`
   - `requests`
   - `beautifulsoup4`

2. Run the following command to generate the PDFs:
   ```bash
   python main.py
   ```
The generated PDFs will be saved in a directory named 'Articles'. Feel free to modify the limit variable in main.py to control the number of articles to generate. Enjoy exploring a world of random knowledge!
