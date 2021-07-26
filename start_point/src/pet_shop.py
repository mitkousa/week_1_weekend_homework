# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(total_cash, cash):
    total_cash["admin"]["total_cash"] += cash

# def add_or_remove_cash(cash_removed, cash):
#     cash = -10
#     cash_removed["admin"]["total_cash"] += cash
#     return cash_removed

def get_pets_sold(sold_pets):
    return sold_pets["admin"]["pets_sold"]

def increase_pets_sold(total_sold, increased_pets):
        total_sold["admin"]["pets_sold"] += increased_pets

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(pets, pet_breed):
    found = []
    for pet in pets["pets"]:
        if pet["breed"] == pet_breed:
            found.append(pet)
    return found

def find_pet_by_name(pets, name):
    for pet in pets["pets"]:
        if pet["name"] == name:
           return pet