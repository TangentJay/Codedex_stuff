# code_task/hiddenmsg.py
'''
* Author: TanB
* Created: 7/30/2025
* Company: Oosode
* GitHub: https://github.com/TangentJay/Codedex_stuff
'''
import requests
from bs4 import BeautifulSoup
import re

def print_grid_from_doc(url):
    """
    Given a URL to a published Google Doc, extracts character data in the form (x, A, y)
    and prints a grid displaying the correctly oriented message.
    """
    try:
        # Fetch the HTML content from the Google Doc
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all visible text from paragraph tags
        text = '\n'.join(''.join(p.stripped_strings) for p in soup.find_all('p'))

        # Find all tuples in the format (x, A, y)
        pattern = re.compile(r'\(\s*(\d+)\s*,\s*([A-Z])\s*,\s*(\d+)\s*\)')
        matches = pattern.findall(text)

        if not matches:
            print('No valid data found.')
            return

        # Convert matches into grid points
        points = [(int(x), char, int(y)) for x, char, y in matches]
        max_x = max(x for x, _, _ in points)
        max_y = max(y for _, _, y in points)

        # Create and fill the grid
        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
        for x, char, y in points:
            grid[y][x] = char

        # Print the final output
        for row in grid:
            print(''.join(row))

    except Exception as e:
        print(f'Error: {e}')


print_grid_from_doc('https://docs.google.com/document/d/e/2PACX-1vTER-wL5E8YC9pxDx43gk8eIds59GtUUk4nJo_ZWagbnrH0NFvMXIw6VWFLpf5tWTZIT9P9oLIoFJ6A/pub')