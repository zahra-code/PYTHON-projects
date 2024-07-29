"""This is a python project using OOPS.this coffee machine like calculating the remaining product quantity,calculating money entered in machine etc .
in last when coffee machine turns off it writes the data to a csv file"""
import datetime
import  csv

data={'order_id':[],'product_name':[],'money':[],'order_date':[]} #dictionary for storing the order data
order_id=0
class CoffeeMachine:
    def __init__(self,water,milk,coffee,money):
        self._Water=water
        self._Milk=milk
        self._coffee=coffee
        self._money=money
    @staticmethod
    def off():
        '''This function offs the coffeee machine'''
        print("coffee machine is turned off")
        exit()
    def start(self):
        '''This function starts the coffee machine and take orders'''
        self.choice =input("""
        WELCOME TO ZAHRA'S COFFEE MACHINE
                   hello USER!
                   what would you like?
                   1.espresso( $1.5)
                   2.latte( $2.5)
                   3.cappuccino( $3.5)
              """)

        if self.choice=="off":
            CoffeeMachine.off()
        else:
            self.choice=int(self.choice)
            if self.choice not in [1, 2, 3]:
                print("\tinvalid choice\n\tTRY AGAIN")
                self.start()
    @property
    def water(self):
        '''This function updates the remaining water in the coffee machine'''
        return self._Water

    @property
    def coffee(self):
        '''This function updates the remaining coffee in the coffee machine'''
        return self._coffee

    @property
    def milk(self):
        '''This function updates the remaining milk in the coffee machine'''
        return self._Milk
    @property
    def money(self):
        '''This function updates the added money in the coffee machine'''
        return self._money
    @property
    def report(self):
        '''This function displays the remaining quantities on screen.'''
        print(f"""
                         available resources
                       Water: {self._Water}ml
                       Milk: {self._Milk}ml
                       Coffee: {self._coffee}g
                       Money: ${self._money}""")
    @report.setter
    def report(self, value):
        pass

    def sufficient_resources(self):
        '''This function checks if the remaining product quantites are enough to take the new order.'''
        if self.choice==1:
          """for espresso 
          coffee =20g
          water=60 ml"""
          if self._Water>=60 and self._coffee>=20:
              print("you order can be taken")
              self._Water-=60
              self._coffee-=20
          else:
              print(f"sorry! your order cannot be placed because of lack of ingredients")
              self.off()
        elif self.choice==2:
            """for latte
            coffee=20g
            water=120ml
            milk=200ml"""
            if self._Water >= 120 and self._coffee >= 20 and self._Milk >=200:
                print("you order can be taken")
                self._Water -= 120
                self._coffee -= 20
                self._Milk-=200
            else:
                print(f"sorry! your order cannot be placed because of lack of ingredients")
                self.off()
        elif self.choice==3:
            """for capiccino
            coffee=20g
            water=120ml
            milk=150ml"""
            if self._Water >= 120 and self._coffee >= 20 and self._Milk >=150:
                print("you order can be taken!! enter coin to proceed")
                self._Water -=120
                self._coffee -= 20
                self._Milk-=150
            else:
                print(f"sorry! your order cannot be placed because of lack of ingredients")
                self.off()
    def make_coffe(self):
        pass
    def add_coin(self):
        '''This function takes different varity of coins as quarters,pennies etc and then calculate the total added amount'''
        self.coin = 0
        print("""enter money(when you have entered press done)=
                     1 for quarters($ 0.25)
                     2 for dimes($ 0.10)
                     3 for nickles($ 0.05)
                     4 for pennies($ 0.01)""")
        for _ in range(100):
            a = input("--")
            if a=="done":
                break
            elif a=="1":
                self.coin+=0.25
            elif a == "2":
                self.coin +=0.10
            elif a == "3":
                self.coin += 0.05
            elif a == "4":
                self.coin += 0.01
            else:
                print("invalid choice")
        print("\n" * 100)
        print(f"you entered $ {self.coin}")
    def transaction_successful(self):
        global order_id
        time = datetime.datetime.now().date()
        '''This function checks if the added money is enough for the order or not...if it is less then it withdraws the money without taking the order and if it is more it returns the remaining money'''
        if self.choice==1:                      #espressp
            if self.coin<1.5:
                print("sorry that's not enough money.MONEY REFUNDED...")
            elif self.coin==1.5:
                print("yeppy!enjoy your COFFEE")
                self._money += 1.5
                order_id+=1
                data['order_id'].append(order_id)
                data['product_name'].append('Espresso')
                data['money'].append(1.5)
                data['order_date'].append(time)
            elif self.coin>1.5:
                extra=self.coin-1.5
                print(f"here is your change {extra}\n enjoy your COFFEE!")
                self._money += 1.5
                order_id += 1
                data['order_id'].append(order_id)
                data['product_name'].append('Espresso')
                data['money'].append(1.5)
                data['order_date'].append(time)
        if self.choice==2:                      #latte
            if self.coin<2.5:
                print("sorry that's not enough money.MONEY REFUNDED...")
            elif self.coin==2.5:
                print("yeppy!enjoy your COFFEE")
                self._money += 2.5
                order_id += 1
                data['order_id'].append(order_id)
                data['product_name'].append('Latte')
                data['money'].append(2.5)
                data['order_date'].append(time)
            elif self.coin>2.5:
                extra=self.coin-2.5
                print(f"here is your change {extra}\n enjoy your COFFEE!")
                self._money += 2.5
                order_id += 1
                data['order_id'].append(order_id)
                data['product_name'].append('Latte')
                data['money'].append(2.5)
                data['order_date'].append(time)
        if self.choice==3:                     #capiccino
            if self.coin<3.0:
                print("sorry that's not enough money.MONEY REFUNDED...")
            elif self.coin==3.0:
                print("yeppy!enjoy your COFFEE")
                self._money += 3.0
                order_id += 1
                data['order_id'].append(order_id)
                data['product_name'].append('Capiccino')
                data['money'].append(3.5)
                data['order_date'].append(time)
            elif self.coin>3.0:
                extra=self.coin-3.0
                print(f"here is your change {extra}\n enjoy your COFFEE!")
                self._money += 1.5
                order_id += 1
                data['order_id'].append(order_id)
                data['product_name'].append('Capiccino')
                data['money'].append(3.5)
                data['order_date'].append(time)

c1=CoffeeMachine(2000,2000,100,2.5)
while True:
    c1.start()
    c1.report
    c1.sufficient_resources()
    c1.add_coin()
    c1.transaction_successful()
    print("Do want to take another order?('no' to exit)")
    choice=input().lower()
    if "no" in choice:
        print("\tThanks for using our coffe machine!Bye")

        # Convert datetime.date objects to strings in YYYY-MM-DD format
        formatted_data = {
            'order_date': [date.strftime('%Y-%m-%d') for date in data['order_date']]
        }

        # Writing to the CSV file
        with open('coffee_machine_order_data.csv', 'w', newline="") as f:
            fieldnames = ['order_id', 'product_name', 'price', 'order_date']
            writer = csv.DictWriter(f, fieldnames)
            writer.writeheader()

            for i in range(len(data['product_name'])):
                writer.writerow({
                    'order_id': data['order_id'][i],
                    'product_name': data['product_name'][i],
                    'price': data['money'][i],
                    'order_date': formatted_data['order_date'][i]
                })

        c1.off()
    else:
        continue