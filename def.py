#!/usr/bin/python
def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
      cost -= 50
    elif days >= 3:
      cost -= 20
    return cost
