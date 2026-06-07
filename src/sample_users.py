from src.user import User


def create_users():

    users = {}

    user1 = User(1, "Sujal")
    user1.add_purchase(101)
    user1.add_purchase(102)
    user1.add_search(105)
    user1.add_search(112)
    user1.add_to_cart(104)

    users[1] = user1

    user2 = User(2, "Rahul")
    user2.add_purchase(106)
    user2.add_purchase(107)
    user2.add_search(108)
    user2.add_to_cart(110)

    users[2] = user2

    user3 = User(3, "Priya")
    user3.add_purchase(110)
    user3.add_purchase(111)
    user3.add_search(109)

    users[3] = user3

    return users