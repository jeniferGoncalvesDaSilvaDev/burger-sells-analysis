

from itertools import combinations, accumulate
#from collections import defaultdict

burgers_sells={
  "burger_joint": {
    "name": "Burger Haven",
    "location": "123 Main St, Foodville",
    "date": "2024-08-24",
    "sales": [
      {
        "order_id": 1001,
        "time": "12:30",
        "items": [
          {
            "item_name": "Classic Burger",
            "quantity": 2,
            "price_per_unit": 8.99
          },
          {
            "item_name": "Fries",
            "quantity": 1,
            "price_per_unit": 2.99
          },
          {
            "item_name": "Soda",
            "quantity": 2,
            "price_per_unit": 1.99
          }
        ],
        "total_price": 24.95,
        "payment_method": "Credit Card"
      },
      {
        "order_id": 1002,
        "time": "13:15",
        "items": [
          {
            "item_name": "Veggie Burger",
            "quantity": 1,
            "price_per_unit": 9.49
          },
          {
            "item_name": "Sweet Potato Fries",
            "quantity": 1,
            "price_per_unit": 3.49
          },
          {
            "item_name": "Iced Tea",
            "quantity": 1,
            "price_per_unit": 2.49
          }
        ],
        "total_price": 15.47,
        "payment_method": "Cash"
      },
      {
        "order_id": 1003,
        "time": "14:00",
        "items": [
          {
            "item_name": "Bacon Cheeseburger",
            "quantity": 3,
            "price_per_unit": 10.49
          },
          {
            "item_name": "Onion Rings",
            "quantity": 2,
            "price_per_unit": 3.99
          },
          {
            "item_name": "Milkshake",
            "quantity": 3,
            "price_per_unit": 4.99
          }
        ],
        "total_price": 52.42,
        "payment_method": "Debit Card"
      }
    ]
  }
}




#combinacões de itens 


def combinations_items(burgers_sells):
  items = list(burgers_sells["burger_joint"]["sales"][0]["items"])
  combinations_items = list(combinations(items, 2))
  return combinations_items
  
print("possíveis combinações de a cada 2 items")
print(combinations_items(burgers_sells))

#acumulo de vendas 
def sum_accumulate_sales(burgers_sells):
  sales = burgers_sells["burger_joint"]["sales"]
  total_sales = 0 # Initialize total sales
  for sale in sales:
    for item in sale["items"]:
      price = item["price_per_unit"] * item["quantity"]  # Calculate price for each item
      total_sales += price # Add to total sales
  return total_sales
print(sum_accumulate_sales(burgers_sells)) 
#print(burgers_sells["burger_joint"]["sales"][0]["items"][1]

def sells_accumulate():
  #with function accumulate in itertools
  sales = burgers_sells["burger_joint"]["sales"]
  total_sales=list(accumulate(sale["total_price"] for sale in sales))
  print(total_sales)

sells_accumulate()

#total de vendas
def total_sells():
  sales = burgers_sells["burger_joint"]["sales"]
  total_sales =sum(sale["total_price"] for sale in sales)
  print(total_sales)

total_sells()
