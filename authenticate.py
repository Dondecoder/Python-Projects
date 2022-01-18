from customer import Customer

customers = [
    Customer('John','shark')
]


name_mapping = {c.name: c for c in customers}


def authenticate(name, password):
    customer = name_mapping.get(name, None)
    if customer.password == password:
        return customer