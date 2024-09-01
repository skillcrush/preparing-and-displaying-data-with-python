import requests
from bs4 import BeautifulSoup

def get_soup(url):
  r = requests.get(url)
  r.raise_for_status()
  html = r.text.encode("utf-8")
  soup = BeautifulSoup(html, "html.parser")
  return soup

def get_categories(url):
  soup = get_soup(url)
  data = {}
  #ADD CODE - select and extract category animals here

  # Return the data here
  return data

category_data = get_categories("https://skillcrush.github.io/web-scraping-endangered-species/")