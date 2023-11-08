# HTTP pieprasijums uz NASA API
import requests
# JASON datu formata apstrāde
import json
#NTP
import datetime
#Laiks
import time
import yaml
#Bibliotēka
from datetime import datetime
print('Asteroid processing service')
#Virsraksts


# Initiating and reading config values
#Lasa konfigurāciju no faila
print('Loading configuration from file')

# Divi mainīgie no kuriem viens ir NASA atslega un otrs API URL
nasa_api_key = "3Zx9XNftU3QuvP4kvUSjxhwEgZ9yoIJqfrhhsAb7"
nasa_api_url = "https://api.nasa.gov/neo/"

# Getting todays date
# Iegūst šodienas datumu
dt = datetime.now()
request_date = str(dt.year) + "-" + str(dt.month).zfill(2) + "-" + str(dt.day).zfill(2)  
print("Generated today's date: " + str(request_date))

# Izveido pieprasījuma URL, veic HTTP GET pieprasījumu uz NASA API
print("Request url: " + str(nasa_api_url + "rest/v1/feed?start_date=" + request_date + "&end_date=" + request_date + "&api_key=" + nasa_api_key))
r = requests.get(nasa_api_url + "rest/v1/feed?start_date=" + request_date + "&end_date=" + request_date + "&api_key=" + nasa_api_key)

#Izvada pieprasijuma statusu
print("Response status code: " + str(r.status_code))
print("Response headers: " + str(r.headers))
print("Response content: " + str(r.text))

# pārbauda vai pieprasijums bija veiksmīgs
if r.status_code == 200:


#izveido tukšus sarakstus lai uzskaitītu drošos un nedrošos akmeņus kosmosā :D 
	json_data = json.loads(r.text)

	ast_safe = []
	ast_hazardous = []


#Pārbauda vai atbildē ir dati par lidojošajiem akmeņiem kosmosa dzīlēs, to kopējo skaitu šajā datumā.
	if 'element_count' in json_data:
		ast_count = int(json_data['element_count'])
		print("Asteroid count today: " + str(ast_count))
#Iegūst informācijupar kopējiem bīstamajiem asteriodiem ja tādi ir, vismaz viens.
		if ast_count > 0:
#ejam cauri visiem akmeņiem šajā datumā.
			for val in json_data['near_earth_objects'][request_date]:

#pārbauda vai kosmosa akmeņi satur vajadzīgo info par nosaukumu, NASA JPL URL, izmēru un potenciālo bīstamību.
				if 'name' and 'nasa_jpl_url' and 'estimated_diameter' and 'is_potentially_hazardous_asteroid' and 'close_approach_data' in val:
#iegūstam akmeņa nosaukumu un URL
					tmp_ast_name = val['name']
					tmp_ast_nasa_jpl_url = val['nasa_jpl_url']
#Izmēri min , max un čeko vai dati ir pieejami. ja nav piešķir negatīvās vērtības.
					if 'kilometers' in val['estimated_diameter']:
						if 'estimated_diameter_min' and 'estimated_diameter_max' in val['estimated_diameter']['kilometers']:
							tmp_ast_diam_min = round(val['estimated_diameter']['kilometers']['estimated_diameter_min'], 3)
							tmp_ast_diam_max = round(val['estimated_diameter']['kilometers']['estimated_diameter_max'], 3)
						else:
							tmp_ast_diam_min = -2
							tmp_ast_diam_max = -2
					else:
						tmp_ast_diam_min = -1
						tmp_ast_diam_max = -1
#Fun daļa :D, Vai lidonis kosmosā ir potenciāli bīstams
					tmp_ast_hazardous = val['is_potentially_hazardous_asteroid']
#parbauda "Close approach" datus
					if len(val['close_approach_data']) > 0:
#Pārbauda vai satur vajadzīgos datus kā laiku, ātrumu un attālumu.
						if 'epoch_date_close_approach' and 'relative_velocity' and 'miss_distance' in val['close_approach_data'][0]:
#Te iegūst "close approach" datu info. Pārbauda vai dati ir pieejami un piešķir vērtības, ja dati nav pieejami.
							tmp_ast_close_appr_ts = int(val['close_approach_data'][0]['epoch_date_close_approach']/1000)
							tmp_ast_close_appr_dt_utc = datetime.utcfromtimestamp(tmp_ast_close_appr_ts).strftime('%Y-%m-%d %H:%M:%S')
							tmp_ast_close_appr_dt = datetime.fromtimestamp(tmp_ast_close_appr_ts).strftime('%Y-%m-%d %H:%M:%S')

							if 'kilometers_per_hour' in val['close_approach_data'][0]['relative_velocity']:
								tmp_ast_speed = int(float(val['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']))
							else:
								tmp_ast_speed = -1

							if 'kilometers' in val['close_approach_data'][0]['miss_distance']:
								tmp_ast_miss_dist = round(float(val['close_approach_data'][0]['miss_distance']['kilometers']), 3)
							else:
								tmp_ast_miss_dist = -1
						else:
							tmp_ast_close_appr_ts = -1
							tmp_ast_close_appr_dt_utc = "1969-12-31 23:59:59"
							tmp_ast_close_appr_dt = "1969-12-31 23:59:59"
					else:
						print("No close approach data in message")
						tmp_ast_close_appr_ts = 0
						tmp_ast_close_appr_dt_utc = "1970-01-01 00:00:00"
						tmp_ast_close_appr_dt = "1970-01-01 00:00:00"
						tmp_ast_speed = -1
						tmp_ast_miss_dist = -1



#Izvada info par nosaukumu, NASA URL, laiku un ātrumu ar ko tuvojas.
					print("------------------------------------------------------- >>")
					print("Asteroid name: " + str(tmp_ast_name) + " | INFO: " + str(tmp_ast_nasa_jpl_url) + " | Diameter: " + str(tmp_ast_diam_min) + " - " + str(tmp_ast_diam_max) + " km | Hazardous: " + str(tmp_ast_hazardous))
					print("Close approach TS: " + str(tmp_ast_close_appr_ts) + " | Date/time UTC TZ: " + str(tmp_ast_close_appr_dt_utc) + " | Local TZ: " + str(tmp_ast_close_appr_dt))
					print("Speed: " + str(tmp_ast_speed) + " km/h" + " | MISS distance: " + str(tmp_ast_miss_dist) + " km")
					
					# Adding asteroid data to the corresponding array
#pievieno datus masīvam (bīstams vai nē)
					if tmp_ast_hazardous == True:
						ast_hazardous.append([tmp_ast_name, tmp_ast_nasa_jpl_url, tmp_ast_diam_min, tmp_ast_diam_max, tmp_ast_close_appr_ts, tmp_ast_close_appr_dt_utc, tmp_ast_close_appr_dt, tmp_ast_speed, tmp_ast_miss_dist])
					else:
						ast_safe.append([tmp_ast_name, tmp_ast_nasa_jpl_url, tmp_ast_diam_min, tmp_ast_diam_max, tmp_ast_close_appr_ts, tmp_ast_close_appr_dt_utc, tmp_ast_close_appr_dt, tmp_ast_speed, tmp_ast_miss_dist])

#izvada ziņojumu ja nav bīstamu akmeņu šajā datumā.
		else:
			print("No asteroids are going to hit earth today")
#izvada kopējo skaitu gan bīstamo gan drošo,
	print("Hazardous asteorids: " + str(len(ast_hazardous)) + " | Safe asteroids: " + str(len(ast_safe)))
#Pārbauda vai ir vismaz viens bīstams
	if len(ast_hazardous) > 0:
#sakārto bīstamos akmeņus un izvada informāciju par tiem. Laiks, nosaukums
		ast_hazardous.sort(key = lambda x: x[4], reverse=False)

		print("Today's possible apocalypse (asteroid impact on earth) times:")
		for asteroid in ast_hazardous:
			print(str(asteroid[6]) + " " + str(asteroid[0]) + " " + " | more info: " + str(asteroid[1]))
#Sakarto bīstamos pēc attāluma un izvada info par attālumu un laiku
		ast_hazardous.sort(key = lambda x: x[8], reverse=False)
		print("Closest passing distance is for: " + str(ast_hazardous[0][0]) + " at: " + str(int(ast_hazardous[0][8])) + " km | more info: " + str(ast_hazardous[0][1]))
#izvada ziņojumu ja šajā datumā nav bīstamo akmeņu
	else:
		print("No asteroids close passing earth today")
#Ziņojums ja nav iespējams sakonektēties ar API
else:
	print("Unable to get response from API. Response code: " + str(r.status_code) + " | content: " + str(r.text))
