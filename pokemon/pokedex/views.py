from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    unknown = "unknown"
    if request.method == 'POST':
        pokemon_name = request.POST.get('pokemon_name', '').lower()
        if pokemon_name:
            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/')
            if response.status_code == 200:
                data = response.json()
                name = data['name'].capitalize()
                poke_id = data['id']
                types = ', '.join([t['type']['name'].capitalize() for t in data['types']])
                height = data['height']
                weight = data['weight']
                image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{poke_id}.png"
                response = requests.get(image_url)
                img_data = response.content
                return render(request, 'page.html', {'pokemon': data, 'img_data': img_data, 'name': name, 'poke_id': poke_id, 'types': types, 'height': height, 'weight': weight})
            else:
                return render(request, 'page.html', {'pokemon': unknown, 'img_data': unknown, 'name': unknown, 'poke_id': unknown, 'types': unknown, 'height': unknown, 'weight': unknown})
            
    return render(request, 'page.html', {'pokemon': unknown, 'img_data': unknown, 'name': unknown, 'poke_id': unknown, 'types': unknown, 'height': unknown, 'weight': unknown})
    