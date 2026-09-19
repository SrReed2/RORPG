class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def show_description(self):
        print(f"{self.name}: {self.description}")

