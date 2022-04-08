import requests
import json
video_game= "league-of-legends"
#token = "W9yhcC6-9fEyj3yb4q_vK_Lk_deM9lHr_kTnIpVwJe4q1LtqZqE"
#data = requests.get(f"https://api.pandascore.co/videogames/{video_game}?token={token}").json()

lfl_teams=f'https://api.pandascore.co/videogames/{video_game}/leagues?search\[name\]=lfl&sort=&page=1&per_page=50'



url = f"https://api.pandascore.co/lol/series/2374/teams?&league_id=4292&sort=&page=1&per_page=50"


#lmao = "https://api.pandascore.co/leagues/4292/tournaments?sort=&page=1&per_page=50"
lmao = "https://api.pandascore.co/leagues/4292/matches/past?sort=&page=1&per_page=50"


    #"https://api.pandascore.co/lol/matches?sort&tournament_id=4292&page=number=10000&size=50&per_page=50"



headers = {"Accept": "application/json",
           "Authorization": "Bearer W9yhcC6-9fEyj3yb4q_vK_Lk_deM9lHr_kTnIpVwJe4q1LtqZqE"
           }


cdkcdokc = requests.request("GET", lmao, headers=headers).json()
response = requests.request("GET", url, headers=headers)
hahah = cdkcdokc
print(cdkcdokc[0])
data= response.json()
lfl_data = requests.request("GET", lfl_teams, headers=headers).json()
split = lfl_data[3]["series"][0]

#print(split)
#print(response.text)
#print(datab)

#print(data)

