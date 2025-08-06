import requests
from bs4 import BeautifulSoup

def decode_secret_message(doc_url):
    # Fetch the Google Doc content
    response = requests.get(doc_url)
    if response.status_code != 200:
        print("Failed to fetch the document.")
        return
    
    # Parse the HTML content to extract the data
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract all text from the document
    text = soup.get_text()
    
    # Split the text into lines and process each line
    data = []
    for line in text.split('\n'):
        # Split the line into parts, assuming they are separated by whitespace
        parts = line.strip().split()
        if len(parts) >= 3:
            try:
                x = int(parts[0])
                char = parts[1]
                y = int(parts[2])
                data.append((x, char, y))
            except ValueError:
                continue
    
    if not data:
        print("No valid data found in the document.")
        return
    
    # Determine grid dimensions
    max_x = max(item[0] for item in data)
    max_y = max(item[2] for item in data)
    
    # Initialize the grid with spaces
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Fill the grid with characters
    for x, char, y in data:
        if y <= max_y and x <= max_x:
            grid[y][x] = char
    
    # Print the grid row by row
    for row in grid:
        print(''.join(row))

# Example usage (replace with actual Google Doc URL)
doc_url = "https://docs.google.com/document/d/e/2PACX-1vRPzbNQcx5UriHSbZ-9vmsTow_R6RRe7eyAU60xIF9Dlz-vaHiHNO2TKgDi7jy4ZpTpNqM7EvEcfr_p/pub"
decode_secret_message(doc_url)