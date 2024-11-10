# Lyric's Finder

**Lyric's Finder** is a Python-based GUI tool that allows users to search for and view song lyrics from **Genius.com**. The application uses **PySide6** for the graphical interface and **BeautifulSoup** for scraping web data. It fetches lyrics via the **Genius API** and displays them in a user-friendly interface.

## Features

- Search for song lyrics by entering the song name.
- Fetches lyrics from **Genius.com** using the Genius API.
- Simple, clean graphical user interface built with **PySide6**.
- Lyrics are displayed directly within the app.

## Requirements

- Python 3.x
- `PySide6` (for GUI)
- `requests` (for making HTTP requests)
- `BeautifulSoup4` (for scraping content from web pages)
- **Genius API Access Token** (required to fetch lyrics)

## Installation

### 1. Install Required Python Libraries

First, clone this repository and navigate into the project directory. Then install the required libraries:

```bash
pip install PySide6 BeautifulSoup4 requests
