import requests

API_URL = "https://api.escuelajs.co/api"
VERSION = "v1"

def get_categories():
  req = requests.get(f"{API_URL}/{VERSION}/categories/")
  # print(req.status_code)
  categories = req.json()
  return categories

def get_category(category_id):
  req = requests.get(f"{API_URL}/{VERSION}/categories/{category_id}")
  # print(req.status_code)
  category = req.json()
  return category


def get_products_by_category(category_id):
  req = requests.get(f"{API_URL}/{VERSION}/categories/{category_id}/products")
  # print(req.status_code)
  products = req.json()
  return products

