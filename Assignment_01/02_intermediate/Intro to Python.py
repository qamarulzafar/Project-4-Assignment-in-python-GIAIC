


# 🔭 Milestone #1: Mars Weight Calculation



# earth_weight = float(input("Enter a weight on Earth: "))
# mars_weight = earth_weight * 0.378
# mars_weight_rounded = round(mars_weight, 2)

# print("The equivalent on Mars:", mars_weight_rounded)




# Milestone #2: All Planets Weight Calculation


earth_weight = float(input("Enter a weight on Earth: "))
planet = input("Enter a planet: ")

if planet == "Mercury":
    multiplier = 0.376
elif planet == "Venus":
    multiplier = 0.889
elif planet == "Mars":
    multiplier = 0.378
elif planet == "Jupiter":
    multiplier = 2.36
elif planet == "Saturn":
    multiplier = 1.081
elif planet == "Uranus":
    multiplier = 0.815
elif planet == "Neptune":
    multiplier = 1.14

planet_weight = round(earth_weight * multiplier, 2)

print(f"The equivalent weight on {planet}: {planet_weight}")