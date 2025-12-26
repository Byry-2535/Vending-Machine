class Snacks:
    def __init__(self, name, price):
        self. name = name
        self.price = price
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
class Biscuits(Snacks):
    def __init__(self, name, price, flavor):
        super().__init__(name, price)
        self.flavor = flavor
        
class Softdrinks(Snacks):
    def __init__(self, name, price, isCarbonated):
        super().__init__(name, price)
        self.isCarbonated = isCarbonated

class Vending:
    def __init__(self, slots):
        self.slots = slots
        self.snacks = []
        
    def add_item(self, snack: Snacks):
        if self.slots > len(self.snacks):
            self.snacks.append(snack)
            return True
        print(f'Out of Slots. Max({self.slots})')
        return False
    
    def view_items(self):
        if self.snacks != []:
            for i in range(len(self.snacks)):
                print(f'Food: {self.snacks[i].get_name()}, Price: {self.snacks[i].get_price()}')
        else:
            print('No items')
            
def main():
    print('Welcome to Vending Machine')
    vending_machine = Vending(10)
    while True:
        snacks = input('(1) Add (2) View (3) Exit\n>> ')
        if snacks == '1':
            snack_type = input('(1) Biscuit (2) Softdrink (3) Back\n>> ')
            if snack_type == '1':
                name = input('Name   : ')
                price = input('Price  : ')
                if price.isdigit():
                    flavor = input('Flavor : ')
                    biscuit = Biscuits(name, price, flavor)
                    vending_machine.add_item(biscuit)
                else:
                    price('Price must be an Integer!')
                    continue
            elif snack_type == '2':
                name = input('Name              : ')
                price = input('Price             : ')
                if price.isdigit():
                    isCarbonated = input('Carbonated? (Y/n) : ').lower()
                    if isCarbonated == 'y':
                        isCarbonated = True
                    elif isCarbonated == 'n':
                        isCarbonated = False
                    else:
                        print('Invalid Choice!')
                        continue
                    softdrink = Softdrinks(name, price, isCarbonated)
                    vending_machine.add_item(softdrink)
                else:
                    price('Price must be an Integer!')
                    continue
            elif snack_type == '3':
                continue
            else:
                print('Invalid Choice!')
                continue
        elif snacks == '2':
            vending_machine.view_items()
        elif snacks == '3':
            print('Arigatou Gozaimasita!\n\nProgram Finished.')
            quit()
        else:
            print('Invalid Choice!')
            continue

if __name__ == '__main__':
    main()