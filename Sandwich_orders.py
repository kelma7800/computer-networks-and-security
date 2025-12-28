sandwich_orders =['grilled cheese', 'roasted beef', 'turkey', 'pastrami', 'vegetable']
print(sandwich_orders)
finished_sandwiches =[]
print("pastrami orders found in sandwich_orders:")
while 'pastrami' in sandwich_orders:
       print("pastrami")
       while 'pastrami' in sandwich_orders:
           sandwich_orders.remove('pastrami')
           print(sandwich_orders)
           while sandwich_orders:
               current_sandwich =sandwich_orders.pop()
               print(" m working on ur current sandwich")
               finished_sandwiches.append(current_sandwich) #print each finished sandwich
               print("sandwiches made:")
               for sandwich in finished_sandwiches:
                   print("i made a sandwitch")

