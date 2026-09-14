from coffee_tea import Coffee, Tea

if __name__=='__main__':
    coffee=Coffee()
    tea=Tea()

    print("Preparing Coffee")
    coffee.prepareBeverage()
    print('-'*50)

    print("Preparing Tea")
    tea.prepareBeverage()
    print('-'*50)
