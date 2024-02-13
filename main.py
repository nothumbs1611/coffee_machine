from art import logo
from dictionary import menu
from dictionary import resources
print(logo)
print("Welcome to the coffee machine")
profit = 0




# 2 turn off coffee machine by entering 'off'
    # ends execution

# 3 print report:  when user enters 'report' a report is generated showing the current resources
   # starting values
    # water 1300ml
    # milk:  200 ml
    # coffee 100g
    # money $

# 4.  check to see if resources is sufficient when
    # when user chooses dring, program checks to see if it has enough resources to make the drink
    # if not enough of a resource, alerts user
    # espresso = 50ml water, 18g coffee
    # latte = 200ml water, 24g coffee, 150ml milk
    # cappuccino = 250ml water, 24g cofffee, 100ml milk


def is_resource_sufficient(order_ingredients):
    """returns true if sufficient resources, false if not enough"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f" Sorry, there is not enough {item} for that drink.")
            return False
    return True


# 5 process coins:
    # espresso costs $1.50
    # latte costs $2.50
    # cappuccino costs $3.00
    # prompt user to insert coins
    # quarters = .25, dimes nickles and pennies
    # calculate the money inserted.
def process_coin():
    print(" Please insert coins ")
    total = int(input("How many quarters?: ")) *0.25
    total += int(input(" How many dimes?: ")) * 0.10
    total += int(input(" How many nickles?: ")) * 0.05
    total += int(input(" How many pennies?: ")) * 0.01
    return total


#6.  check transaction:
    # did user insert enough $$?  if not, alert user and refunds what was deposited
    # if true, this $$ gets added to the money resource
    # if user inserted too much money, issues refund.
def transaction_successful(money_received, drink_cost):
    """returns true when sufficient payment, false if insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that is not enough money, Transaction cancelled.  Money refunded.")
        return False


# 7: make coffee:
    # deducts resources that were consumed
    # alerts user their coffee is ready.
def make_coffee(drink_name, order_ingredients):
    """deducts the ingredients consumed"""
    for item in order_ingredients:
        resources[item] =+ order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy")
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino? ")
    #if choice == "latte":
     #   print(f"a {choice} costs {'menu'}{'latte}['cost']")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml remaining")
        print(f"Milk: {resources['milk']}ml remaining")
        print(f"Coffee: {resources['coffee']}g remaining")
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])