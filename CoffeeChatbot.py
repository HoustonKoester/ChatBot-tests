# Define your functions
def coffee_bot():
  print("Welcome to the cafe!")
  size = get_size()
  drink_type = get_drink_type()
  name = input("Can I get a name for that order?\n")

  print("Alright {2}! That's a {0} {1} coming right up!".format(size, drink_type,name))

def print_error():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")
def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large\n> ")
  if res == 'a' or res == "Small":
    res = "Small"
  elif res == 'b' or res == "Medium":
    res = "Medium"
  elif res == 'c' or res == "Large":
    res = "Large"
  else:
    print_error()
    res = get_size()
  return res
def get_drink_type():
  res = input("What type of drink can I get for you? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte\n> ")
  if res == 'a' or res == "Brewed Coffee":
    res = "Brewed Coffee"
  elif res == 'b' or res == "Mocha":
    res = "Mocha"
  elif res == 'c' or res == "Latte":
    res = "Latte"
    if res == "Latte":
      milk = order_latte()
    res = "Latte made with " + milk
  else:
    print_error()
    res = get_drink_type()
  return res
def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n> ")
  if res == 'a' or res == "2% milk":
    res = "2% milk"
  elif res == 'b' or res == "Non-fat milk":
    res = "Non-fat milk"
  elif res == 'c' or res == "Soy milk":
    res = "Soy milk"
  else:
    print_error()
    res = order_latte()
  return res
# Call coffee_bot()!
coffee_bot()
