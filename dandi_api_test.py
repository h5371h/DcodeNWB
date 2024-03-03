import tkinter as tk
from tkinter import simpledialog
import requests

ROOT = tk.Tk()
ROOT.withdraw()  # Use to hide the main tkinter window

# Function to get user input for DANDIset ID
def get_user_input(prompt):
    return simpledialog.askstring(title="Input", prompt=prompt)

# Function to fetch Dandiset assets
def get_dandiset_assets(dandiset_id, version="draft"):
    url = f"https://api.dandiarchive.org/api/dandisets/{dandiset_id}/versions/{version}/assets/"
    response = requests.get(url)
    response.raise_for_status()
    assets = response.json()['results']
    return assets

# Main execution logic
if __name__ == "__main__":
    dandiset_id = get_user_input("Enter DANDIset ID:")
    if dandiset_id:
        assets = get_dandiset_assets(dandiset_id)
        for asset in assets:
            print(asset.get('path'), asset.get('asset_id'))
    else:
        print("No DANDIset ID provided.")

