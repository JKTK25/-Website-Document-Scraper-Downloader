import requests
from bs4 import BeautifulSoup
import os
import urllib.parse
import zipfile
from google.colab import files

# Install required libraries (only in Colab, comment out if not needed)
# !pip install requests beautifulsoup4

# Prompt user for the website link
BASE_URL = input("Enter the URL of the website you want to scrape for files: ").strip()

# Directory to save downloaded files
SAVE_DIR = "downloaded_files"
# Name of the ZIP file
ZIP_FILE = "downloaded_files.zip"

# Create directory if it doesn't exist
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def is_downloadable_file(url):
    """Check if the URL points to a PDF or Word document."""
    return url.lower().endswith(('.pdf', '.doc', '.docx'))

def get_absolute_url(base_url, link):
    """Convert relative URL to absolute URL."""
    return urllib.parse.urljoin(base_url, link)

def download_file(url, save_path):
    """Download a file from the given URL and save it to the specified path."""
    try:
        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"Downloaded: {save_path}")
        else:
            print(f"Failed to download {url}: Status code {response.status_code}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def zip_files(directory, zip_name):
    """Zip all PDF and Word files in the specified directory."""
    try:
        with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.lower().endswith(('.pdf', '.doc', '.docx')):
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.join("downloaded_files", file))
        print(f"Created ZIP file: {zip_name}")
        return True
    except Exception as e:
        print(f"Error creating ZIP file: {e}")
        return False

def main():
    try:
        # Fetch the main page
        response = requests.get(BASE_URL, headers=headers)
        if response.status_code != 200:
            print(f"Failed to access {BASE_URL}: Status code {response.status_code}")
            return

        # Parse the page
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)

        # Collect file links
        file_urls = set()
        for link in links:
            href = link['href']
            if is_downloadable_file(href):
                absolute_url = get_absolute_url(BASE_URL, href)
                file_urls.add(absolute_url)
            elif href.startswith('/') or BASE_URL in href:
                subpage_url = get_absolute_url(BASE_URL, href)
                try:
                    sub_response = requests.get(subpage_url, headers=headers)
                    if sub_response.status_code == 200:
                        sub_soup = BeautifulSoup(sub_response.text, 'html.parser')
                        sub_links = sub_soup.find_all('a', href=True)
                        for sub_link in sub_links:
                            if is_downloadable_file(sub_link['href']):
                                absolute_url = get_absolute_url(BASE_URL, sub_link['href'])
                                file_urls.add(absolute_url)
                except Exception as e:
                    print(f"Error accessing subpage {subpage_url}: {e}")

        # Download each file
        for url in file_urls:
            filename = os.path.basename(url)
            if not filename.lower().endswith(('.pdf', '.doc', '.docx')):
                filename += '.pdf'  # fallback
            save_path = os.path.join(SAVE_DIR, filename)
            download_file(url, save_path)

        if not file_urls:
            print("No PDF or Word files found on the website.")
        else:
            print(f"Total files downloaded: {len(file_urls)}")
            if zip_files(SAVE_DIR, ZIP_FILE):
                files.download(ZIP_FILE)
            else:
                print("Failed to create or download the ZIP file.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
