eshop_X = {
    "name": "e-shop X",
    "product_A": {
        "cost": 30098,
        "rating": 4.7,
        "delivery_cost": 200,
        "mode": "Pay after delivery"
    },
    "product_B": {
        "cost": 5800,
        "rating": 4.8,
        "delivery_cost": 200,
        "mode": "Pay after delivery"
    }
}

eshop_Y = {
    "name": "e-shop Y",
    "product_A": {
        "cost": 29999,
        "rating": 4.0,
        "delivery_cost": 150,
        "mode": "Pay before delivery"
    },
    "product_B": {
        "cost": 5589,
        "rating": 5.0,
        "delivery_cost": 150,
        "mode": "Pay before delivery"
    }
}

def calculate_marginBenefit(product):
    return product["rating"]

def calculate_costBenefit(product):
    return product["rating"] / product["cost"]

def rank_products(eshop):
    ranked_products = {}  

    for pr_name, pr_data in eshop.items():
        mb = calculate_marginBenefit(pr_data)
        cb = calculate_costBenefit(pr_data)
        ranked_products[pr_name] = {"MB": mb, "CB": cb}  

    sorted_products = dict(sorted(ranked_products.items(), key=lambda item: (item[1]["MB"], item[1]["CB"]), reverse=True))
    return sorted_products

sorted_products_X = rank_products(eshop_X)
print("Sort Product:")
print(sorted_products_X)


