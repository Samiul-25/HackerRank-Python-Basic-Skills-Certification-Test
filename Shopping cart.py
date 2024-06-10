import os


class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, item: Item):
        self.items.append(item)

    def total(self) -> int:
        return sum(item.price for item in self.items)

    def __len__(self):
        return len(self.items)


if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    index = 0
    n = int(data[index])
    index += 1
    items = []
    for _ in range(n):
        name, price = data[index].split()
        item = Item(name, int(price))
        items.append(item)
        index += 1

    cart = ShoppingCart()

    q = int(data[index])
    index += 1
    output = []
    for _ in range(q):
        line = data[index].split()
        command, params = line[0], line[1:]
        if command == "len":
            output.append(str(len(cart)))
        elif command == "total":
            output.append(str(cart.total()))
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)
        index += 1

    for line in output:
        print(line)
