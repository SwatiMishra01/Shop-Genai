import random

def recommender_agent(category):
    sample_products = {
        "Sports Shoes": ["Nike Air Max", "Adidas Ultraboost", "Puma Running Pro"],
        "Laptops": ["MacBook Pro", "Dell XPS 13", "HP Spectre"],
        "Headphones": ["Sony WH-1000XM5", "Bose QuietComfort", "JBL Live 660NC"]
    }
    return random.sample(sample_products.get(category, []), k=3)
