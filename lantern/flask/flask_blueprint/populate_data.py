import csv


def get_users():
    with open("users.csv", "r") as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users


def get_goods():
    with open("goods.csv", "r") as g:
        reader = csv.DictReader(g)
        goods = [i for i in reader]
    return goods
