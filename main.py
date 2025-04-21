import json
import requests
import os

access_key = "bo71TiQUDKY5TrgwJCnovuRu-ciSbleijnHTmxuWxCo"

search_term = input("Enter a topic to download images from Unsplash: ").strip()

#original:-
per_page = 10
url = "https://api.unsplash.com/search/photos"
params = {
    "query": search_term,
    "per_page": per_page,
    "client_id": access_key
}

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200:
    data = response.json()

    # Create a folder based on search term
    dest_folder = f'unsplash_{search_term.replace(" ", "_")}'  # adds '_'(underscore) instead of " "(spaces) in the file name
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for i, img in enumerate(data['results']):
        img_url = img['urls']['full']
        img_data = requests.get(img_url).content

        file_path = os.path.join(dest_folder, f"{search_term}_{i+1}.jpg")
        with open(file_path, 'wb') as f:  # wb here refers to write binary
            f.write(img_data)
            print(f"Downloaded: {file_path}")

else:
    print(f"Error {response.status_code}: {response.text}")
