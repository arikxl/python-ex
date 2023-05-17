import random

class Coin:
    def __init__(self, rare=False, clean = True, is_heads = True, **kwargs):

        for key, value in kwargs.items():
            setattr(self,key,value)

        self.is_rare = rare
        self.is_clean = clean

        if self.is_rare:
            self.value = self.original_value *1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color

    def __del__(self):
        print('Coin Spent!')

    def flip(self):
        head_options= [True, False]
        choice = random.choice(head_options)
        self.is_heads =choice


class Pound(Coin):
    def __init__(self):
        data = {
            'original_value':1.00,
            'clean_color': 'gold',
            'rusty_color':'greenish',
            'num_edges': 1,
            'diameter': 22.5,
            'thickness': 3.15,
            'mass': 9.5 
        }
        super().__init__(**data)

class Pence(Coin):
    def __init__(self):
        data = {
            'original_value':0.01,
            'clean_color': 'bronze',
            'rusty_color':'brownish',
            'num_edges': 1,
            'diameter': 20.3,
            'thickness': 1.52,
            'mass': 3.56 
        }
        super().__init__(**data)

class Five_Pence(Coin):
    def __init__(self):
        data = {
            'original_value':0.05,
            'clean_color': 'silver',
            'rusty_color':None,
            'num_edges': 1,
            'diameter': 18.0,
            'thickness': 1.77,
            'mass': 3.25 
        }
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color 

class Fifty_Pence(Coin):
    def __init__(self):
        data = {
            'original_value':0.50,
            'clean_color': 'silver',
            'rusty_color':None,
            'num_edges': 7,
            'diameter': 27.3,
            'thickness': 1.78,
            'mass': 8.00 
        }
        super().__init__(**data)

        def rust(self):
            self.color = self.clean_color 

class Two_Pound(Coin):
    def __init__(self):
        data = {
            'original_value':2.00,
            'clean_color': 'gold & silver',
            'rusty_color':'greenish',
            'num_edges': 1,
            'diameter': 28.3,
            'thickness': 2.50,
            'mass': 12.00 
        }
        super().__init__(**data)


coins =[Pound(),Pence(), Five_Pence(), Fifty_Pence(), Two_Pound()]

for coin in coins:
    arguments = [ coin.color, coin.value,]
    print(coin.value)        