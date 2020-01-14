planet_list = ["Mercury", "Mars"]

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")


# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Uranus", "Neptune"])


# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Venus")
planet_list.insert(2, "Earth")


# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")


# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets = planet_list[:4]


# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[-1]

print(planet_list)

# Challenge: Iterating over planets

# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on.

# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.

# Example spacecraft list
spacecraft = [
   ("Cassini", "Saturn"),
   ("EltonJohn", "Mars"),
   ("Thor", "Earth"),
   ("Metallica", "Mercury"),
   ("Madonna", "Venus"),
   ("Train", "Jupiter"),
   ("Beevis", "Uranus"),
   ("Netflix", "Neptune"),
   ("Disney", "Earth"),
]
print()
# for planet in planet_list:
#     for ship_tuple in spacecraft:
#         if planet == ship_tuple[1]:
#             print(f"{ship_tuple[0]} has visited {planet}")

for planet in planet_list:
    ships_visited = []
    for ship_tuple in spacecraft:
        if planet == ship_tuple[1]:
            ships_visited.append(ship_tuple[0])
    ships = ", ".join(ships_visited)
    print(f"{planet} has been visited by {ships}")