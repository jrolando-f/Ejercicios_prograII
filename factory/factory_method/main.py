from .store import NYPizzaStore, ChicagoPizzaStore

def main():
    ny = NYPizzaStore(); chi = ChicagoPizzaStore()
    p1 = ny.order_pizza("cheese"); print("Ethan ordered:", p1)
    p2 = chi.order_pizza("cheese"); print("Joel ordered:", p2)
    p3 = ny.order_pizza("veggie"); print("Oli orderer:", p3)
    p4 = ny.order_pizza("pepperoni"); print("More ordered:", p4)
    p5 = chi.order_pizza("veggie"); print("Belu ordered:", p5)
    p6 = chi.order_pizza("pepperoni"); print("Julian ordered:", p6)
    

if __name__ == "__main__":
    main()
