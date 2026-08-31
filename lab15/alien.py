"""Alien.

This simulates an alien tracker.
Author: Cameron Sateri
Version: 11/29/22
I worked with Heikel
"""

import location


class Alien:
    """Alien class."""

    alien_count = 0
    rogue_count = 0

    def __init__(self, name="Unknown", home_planet="Unknown",
                 loc=location.ISAT, alias="Unknown"):
        """Alien Constructor.

        Creates an Alien with these specs:

        Args:
            name(str): this alien's original name
            home_planet(location):  the origination of this alien
            loc(location): the current location for this alien
            alias(str): the name this alien goes by on Earth
        """
        self.name = name
        self.home_planet = home_planet
        self.loc = loc
        self.alias = alias
        Alien.alien_count += 1
        # increasing alien count everytime a new Alien object is created
        self.wanted = False
        # setting the wanted status of the new alien to be false

    def captured_jmu(self):
        """captured_jmu.

        Indicates that an alien that has been captured and placed at
        the JMU detention facility. If the alien was a wanted criminal,
        then reset wanted to false and decrement the rogueCount.
        In either case, this alien should be placed at the JMU location.
        """
        if self.wanted:
            self.wanted = False
            Alien.rogue_count -= 1
        self.loc = location.JMU

    def deport(self):
        """deport.

        Indicates an alien has been deported. It is possible to deport an
        alien without a prior capture. If this alien is wanted, reset the
        the wanted attribute to false and decrement the rogue_count. In either
        case, set the location to None and decrement the alien_count.
        """
        if self.wanted:
            self.wanted = False
            Alien.rogue_count -= 1
        Alien.alien_count -= 1
        self.loc = None

    def gone_rogue(self):
        """gone_rogue.

        Identifies that an alien has violated the rules of alien immigration.
        If this is a new identification (wanted is false), set wanted to true
        and increment the rogue count. If this alien is already wanted, then
        do neither.
        """
        if not self.wanted:
            self.wanted = True
            Alien.rogue_count += 1

    def move(self, new_loc):
        """move.

        Places this alien into a new location.

        Args:
            new_loc (location):  new current location
        """
        self.loc = new_loc

    def get_current_location(self):
        """get_current_location.

        Returns the current location of this alien.

        Returns:
            location: current location
        """
        return self.loc

    def __str__(self):
        """toString.

        Returns basic information about this alien.

        Returns:
            str: a String of the form: "%s aka %s from %s is currently at %s"
            followed by the term "ROGUE" or the empty String,
            depending on whether isWanted is true or false.
            If location is null, output "Off Planet" in place of the location.
        """
        ret = self.name + " aka " + self.alias + " from " + self.home_planet
        if self.loc is None:
            ret = ret + " is currently at Off Planet "
        else:
            ret = ret + " is currently at " + str(self.loc) + " "
        if self.wanted:
            ret += "ROGUE"
        return ret

    def get_number_aliens():
        """get_number_aliens.

        Returns the total number of aliens on the planet.

        Returns:
            aliens(int): total number of aliens (including those wanted)
        """
        return Alien.alien_count

    def get_number_wanted():
        """get_number_wanted.

        Returns the total number of wanted aliens on the planet.

        Returns:
            wanted: number of wanted aliens
        """
        return Alien.rogue_count
