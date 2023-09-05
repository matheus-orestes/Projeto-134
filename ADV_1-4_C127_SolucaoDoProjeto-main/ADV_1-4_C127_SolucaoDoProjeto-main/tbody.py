import bs4
import time
import pandas as pd

webdriver.start()

scraped_data = []

def scrap():
    bright_star_table = soup.find("table", attrs = ("class", 'wikitable'))

    table_bobody = bright_star_table("tbody")

    table_rows = table_bobody_find_all('tr')

    for row in table_rows:
        table_cows = row.find_all("td")
        print(table_cows)

        temp_list = []

        for col_data in table_cows:
            print(col_data.text)

            data = col_data.text.strip()
            print(data)

            temp_list.append(data)


scraped_data.append(temp_list)



for i in range(0,len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum =scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum] 
    stars_data.append(required_data)


    headers = ['Star_name', 'Distance', 'Mass', 'Radius', Luminosity]

    # Defina o cabeçalho

    star_df_1 = pd.DataFrame(stars_data, columns-headers)


required_data.request("brown_dwarf")
required_data.find_all("brown_dwarf")
list = []
required_data.tags("tr_tags")

final_data.csv
planet_masses = []
planet_radiuses = []

for planet_data in low_gravity_planets:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])

fig = px.scatter(x=planet_radiuses, y=planet_masses)
fig.show()
dataframe.csv("star_with_gravity.csv")

temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
    if planet_data[1].lower() == "hd 100546 b":
        planet_data_rows.remove(planet_data)

planet_masses = []
planet_radiuses = []
planet_names = []

for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])

planet_gravity = []

for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()

planet_speeds = []
for planet_data in suitable_planets:
    distance = 2 * 3.14 *( planet_data[0] * 1.496e+8)
    time = planet_data[9] + 86400
    speed = distance / time
    planet_speeds.append(speed)

    speed_suporting_planets = list(suitable_planets)
    for index, planet_data in enumerate(temp_speed_suporting_planets):
        if planet_speeds[index] > 200:
            speed_suporting_planets.remove(planet_data)

print(len(speed_suporting_planets))
temp_planet_data_rows = list(planet_data_rows)

for planet_data in temp_planet_data_rows:
  if planet_data[1].lower() == "hd 100546 b":
    planet_data_rows.remove(planet_data)

planet_masses = []
planet_radiuses = []
planet_names = []

for planet_data in planet_data_rows:
  planet_masses.append(planet_data[3])
  planet_radiuses.append(planet_data[7])
  planet_names.append(planet_data[1])

planet_gravity = []

for index, name in enumerate(planet_names):
  gravity = (float(planet_masses[index])*5.972e+24) / (float(planet_radiuses[index])*float(planet_radiuses[index])*6371000*6371000) * 6.674e-11
  planet_gravity.append(gravity)

fig = px.scatter(x=planet_radiuses, y=planet_masses, size=planet_gravity, hover_data=[planet_names])
fig.show()


