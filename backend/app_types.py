class Item:
    def __init__(self, id, name, item_count):
        self.id = id
        self.name = name
        self.count = item_count


class Characteristic:
    def __init__(self, category, value):
        self.category = category
        self.value = value
