import store

def print_categories(categories):
  title = "Categories" if len(categories) > 1 else "Category"
  
  print("="*15, title, "="*15)
  print("[id] => Name")

  if(len(categories) > 1):
    for category in categories:
      print(f"[{category['id']}]  => {category['name']}")
  else:
    category =  categories[0] 
    print(f"[{category['id']}]  => {category['name']}")



def print_products(products):
  if(len(products) == 0):
    print("There aren'n any products for category you selected")
    return

  title = "Products by category"
  print("="*15, title, "="*15)
  print("[id] => $[price] => Name")
  for product in products:
    print(f"[{product['id']}] => ${product['price']} => {product['title']}")

def run():
  categories = store.get_categories()
  if len(categories) == 0:
    print("There aren't any category yet.")
    return

  all_category_ids = list(map(lambda cat: cat['id'], categories))
  print("Look at all those categories, which category do you want to explore?")
  print_categories(categories)

  while True:
    category_id = input("Please type a category id: ")
    if not category_id.isdigit():
      print(f"{category_id} is not an option, please try again")
    elif not int(category_id) in all_category_ids:
      print(f"{category_id} is not an option, please try again")
    else:
      category_id = int(category_id)
      break

  category = store.get_category(category_id)
  products = store.get_products_by_category(category_id)
  print_categories([category])
  print_products(products)

if __name__ == "__main__":
  run()