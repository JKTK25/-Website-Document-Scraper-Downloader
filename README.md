# 📄 Website Document Scraper & Downloader

This Python script allows you to **scrape PDF and Word documents** (`.pdf`, `.doc`, `.docx`) from any specified website and automatically **download** them into a folder. It then **zips the files** and offers a download option — perfect for collecting learning materials, curriculum files, or documents from educational sites 📚.

---

## 🚀 Features

- 🔗 Prompts for any website URL at runtime
- 🧠 Detects and extracts links to PDF and Word documents
- 🔍 Optionally checks linked subpages for more files
- 💾 Downloads all documents to a local folder
- 📦 Compresses all downloaded files into a ZIP archive
- 💻 Enables easy ZIP download if using Google Colab

---

## 🛠️ Requirements

### ✅ Python Version

- Python **3.6 or higher** is recommended.

### 📦 Required Python Modules

- `requests`
- `beautifulsoup4`

You can install them using pip:

```bash
pip install requests beautifulsoup4
```

### 🧪 Google Colab Setup (Optional)

If you're using Google Colab, you can install dependencies like this at the top of your notebook:

```python
!pip install requests beautifulsoup4
```

---

## 🧑‍💻 How to Use

### 1. Run the Script

You can copy the Python script into your local Python environment or Google Colab.

### 2. Enter the URL

When prompted, paste the full website URL that contains downloadable documents:

```
Enter the URL of the website you want to scrape for files:
```

Example:

```
https://teacher.co.ke/download-2024-schemes-of-work-for-free/
```

### 3. Let the Script Work

- It scans the page for `.pdf`, `.doc`, and `.docx` links.
- Downloads them into a local folder called `downloaded_files`.
- Compresses them into a `downloaded_files.zip`.
- If on **Google Colab**, the ZIP is auto-downloaded via browser.

---

## 📁 File Structure

Once the script runs, your project folder will look like this:

```
project/
│
├── downloaded_files/        # Folder containing downloaded files
├── downloaded_files.zip     # ZIP file with all documents
└── scraper_script.py        # The Python script itself
```

---

## 📎 Example Use Cases

- ✅ Download **schemes of work**, **lesson plans**, or **past papers**.
- ✅ Collect **free eBooks**, **forms**, or **syllabi**.
- ✅ Batch download and organize content for offline use.

---

## ⚠️ Notes

- This script avoids deep crawling to respect web server limits and prevent timeouts.
- 📌 Please ensure you **have permission** to download content from the site.
- ⚖️ Always respect `robots.txt`, copyright laws, and terms of use.

---

## 💬 Feedback & Support

Feel free to fork the repository or suggest improvements.  
If you face any issues, open an issue or reach out via GitHub or email.

---

## 🎉 Happy Scraping!
