"""MIB.

Exercises the alien class members and uses the Location class.
"""


class MIB:
    """MIB class."""

    def main():
        """Run Main function."""
        import alien
        import location
        frank = alien.Alien("Frank", "Saturn", location.JMU, "Frank the Pug")
        bug = alien.Alien("Bug", "Romulus",
                          location.Location(38.89778, -77.0132), "Edgar")
        print("Aliens now 1: ", alien.Alien.get_number_aliens())
        print("Wanted now 1: ", alien.Alien.get_number_wanted())
        # next, let's move them around
        frank.move(location.ISAT)
        bug.gone_rogue()
        print("Aliens now 2: ", alien.Alien.get_number_aliens())
        print("Wanted now 2: ", alien.Alien.get_number_wanted())

        # Let's add a couple more
        et = alien.Alien("opm**", "Home",
                         location.Location(38.8619, -77.0647), "ET")
        superman = alien.Alien("Kai-el", "Krypton",
                               location.Location(40.7306, -73.9889),
                               "Clark Kent")
        print("Aliens now 3: ", alien.Alien.get_number_aliens())
        print("Wanted now 3: ", alien.Alien.get_number_wanted())

        et.deport()
        superman.gone_rogue()

        print("Aliens now 4: ", alien.Alien.get_number_aliens())
        print("Wanted now 4: ", alien.Alien.get_number_wanted())

        bug.deport()

        print("Aliens now 5: ", alien.Alien.get_number_aliens())
        print("Wanted now 5: ", alien.Alien.get_number_wanted())

        steve = alien.Alien("Beedle", "Jupiter",
                            location.Location(38.89778, -77.0132),
                            "Steven Spielberg")
        steve.captured_jmu()
        superman.captured_jmu()

        print("Aliens now 6: ", alien.Alien.get_number_aliens())
        print("Wanted now 6: ", alien.Alien.get_number_wanted())

        pete = steve  # will we have new Aliens now?

        # steve escapes
        steve.move(location.ISAT)
        steve.gone_rogue()

        print("Aliens now 7: ", alien.Alien.get_number_aliens())
        print("Wanted now 7: ", alien.Alien.get_number_wanted())

        print("\nThe final set of alien.Aliens: ")
        print(frank)
        print(bug)
        print(et)
        print(superman)
        print(steve)
        print(pete)
    main()

