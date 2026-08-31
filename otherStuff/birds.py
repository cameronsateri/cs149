class Birds:
    beaks = 1
    wings = 2

    def flyup(self, canfly):
        if canfly:
            print("Woohooo I’m in the clouds")
        else:
            print("I can walk though!")


if __name__ == '__main__':
    parrot = Birds()
    print(parrot.beaks)
    flight = True
    parrot.flyup(flight)
