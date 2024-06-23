import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['bodies']
    else:
        print("Failed to retrieve data")
        return []

def display_planet_data(planets):
    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'N/A')
            mass = planet.get('mass', {}).get('massValue', 'N/A')
            orbit_period = planet.get('sideralOrbit', 'N/A')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

def find_heaviest_planet(planets):
    heaviest_planet = max(
        (planet for planet in planets if planet['isPlanet']),
        key=lambda p: p.get('mass', {}).get('massValue', 0)
    )
    return heaviest_planet.get('englishName', 'N/A'), heaviest_planet.get('mass', {}).get('massValue', 'N/A')

# Fetch and display planet data
planets = fetch_planet_data()
display_planet_data(planets)

# Find and display the heaviest planet
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")

