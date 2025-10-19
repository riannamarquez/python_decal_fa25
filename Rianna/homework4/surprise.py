# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

# 1
def print_star_names():
    for star in targets:
        print(star)
print_star_names()

# 2
def print_star_spectral_types():
    for star, info in targets.items():
        print(f"{star}: {info['Spectral Type']}")
print_star_spectral_types()

#3
def print_dim_stars():
    for star, info in targets.items():
        if info["Magnitude"] > 0.1:
            print(f"{star}: {info['Magnitude']}")
print_dim_stars()

#4
targets["Altair"] = {
    "RA": "19h 50m 47s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.77,
    "Spectral Type": "A7V"
}

print(targets["Altair"])

#5
def find_star_near_20():
    closest_star = None
    closest_diff = float("info")
    for star, info in targets.items():
        dec_str = info["Dec"]
        dec_val = float(dec_str.replace("°", "").replace("+", "").replace("−", "-").split()[0])
        diff = abs(dec_val - 20)
        if diff < closest_diff:
            closest_diff = diff
            closest_star = (star, info)
    print(f"The star closest to +20° Dec is {closest_star[0]} at {closest_star[1]['Dec']}")

#6
print("My favorite constellation is Cygnus!")
