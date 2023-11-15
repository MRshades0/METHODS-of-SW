

from cart_class import Cart
import sys
import sqlite3

def main():
    
    try:
        connection = sqlite3.connect("methods.db")
        print('connection successful')
    except:
        print('connection failed')
        sys.exit()

    test = Cart("methods.db", "CART", connection)

    test.viewCart("0022","INVENTORY")
    test.addToCart("0022", "0001")
    test.addToCart("0022", "0001")
    test.viewCart("0022","INVENTORY")
    test.removeFromCart("0022", "0001")
    test.viewCart("0022","INVENTORY")
    
    
    
    
main()