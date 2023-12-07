import json
import requests
import googletrans

trans = googletrans.Translator()

tag = ['사람이 많은', '분위기 좋은']
place = '송도'
place_type = '관광지'
query = ''
for i in tag:
    query = query + i + ", "
query = query + place +"에 있는, " + place_type
query = trans.translate(text = query, dest='en').text
url = 'https://places.googleapis.com/v1/places:searchText'
headers = {
    'Content-Type': 'application/json',
    'X-Goog-Api-Key': 'Google_map_API_Key', 
    'X-Goog-FieldMask': 'places.id,places.rating,places.displayName,places.formattedAddress,places.priceLevel'
}

data = {
    'textQuery': query
}

response = requests.post(url, json=data, headers=headers)

result_list = []
for key in response.json():{
    result_list.append([key, response.json()[key]])
}
    
places = result_list[0][1]

sorted_places = sorted([place for place in places if 'rating' in place], key=lambda x: x['rating'], reverse=True)