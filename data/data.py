import requests

bird_info_data = {
     "Asian Koel": {
        "Scientific Name": "Eudynamys scolopaceus",
        "Description": "The Asian Koel is a member of the cuckoo family known for its distinctive call. It is a brood parasite, laying its eggs in the nests of other birds.",
        "Location": "Asian Koels are found in various parts of Asia, including India, Southeast Asia, and parts of Australia.",
        "Image":"https://i.pinimg.com/564x/dc/34/e9/dc34e904e0ee0c10f1f42e2e5a9b84b9.jpg"
    },
    "Black Kite": {
        
        "Scientific Name": "Milvus migrans",
        "Description": "The Black Kite is a medium-sized bird of prey known for its forked tail and soaring flight. It primarily feeds on carrion.",
        "Location": "Black Kites are widespread and can be found in Europe, Asia, Africa, and Australia.",
        "Image": "https://i.pinimg.com/564x/3b/61/2c/3b612cfde066d944737392761ffc56ef.jpg"
    },
    "Black-breasted Parrotbill": {
        
        "Scientific Name": "Paradoxornis flavirostris",
        "Description": "The Black-breasted Parrotbill is a small bird known for its distinctive black breast and yellow bill. It is found in parts of Southeast Asia.",
        "Location": "Black-breasted Parrotbills inhabit regions in Southeast Asia, including Myanmar, Thailand, and Laos.",
        "Image": "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/409103751/"
    },
    "Black-necked crane": {
        
        "Scientific Name": "Grus nigricollis",
        "Description": "The Black-necked crane is a medium-sized crane species known for its striking black neck and white body. It is a high-altitude bird found in the Himalayas.",
        "Location": "Black-necked cranes are native to the Himalayan region, including countries like Bhutan and Tibet.",
        "Image": "https://i.pinimg.com/564x/12/d5/63/12d56346010eaad8b3b15a9012ecd73a.jpg"
    },
    "Bristled Grassbird": {
        
        "Scientific Name": "Chaetornis striata",
        "Description": "The Bristled Grassbird is a small, elusive bird known for its distinctive bristle-like feathers on its tail. It inhabits dense grasslands and reed beds.",
        "Location": "Bristled Grassbirds are typically found in parts of Southeast Asia, including Indonesia and the Philippines.",
        "Image": "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/150314681/1800"
    },
    "Cheer Pheasant": {
        
        "Scientific Name": "Catreus wallichii",
        "Description": "The Cheer Pheasant is a colorful and large pheasant species known for its striking plumage and distinctive calls. Males have a white face with black markings, and they are often seen in hilly and forested areas.",
        "Location": "Cheer Pheasants are native to the Himalayan region, including countries like India, Nepal, and Bhutan.",
        "Image": "https://i.pinimg.com/564x/77/45/d0/7745d0c97921be060147fb33c7933651.jpg"
    },
    "Common Cuckoo": {
        
        "Scientific Name": "Cuculus canorus",
        "Description": "The Common Cuckoo is a well-known brood parasite known for its distinctive call. It lays its eggs in the nests of other bird species. The cuckoo migrates between Europe and Africa.",
        "Location": "Common Cuckoos are found across Europe, Asia, and Africa during their breeding and migration periods.",
        "Image": "https://i.pinimg.com/564x/8a/47/3a/8a473a6774b53abda354aeae85379f54.jpg"
    },
    "Common Pochard": {
        
        "Scientific Name": "Aythya ferina",
        "Description": "The Common Pochard is a diving duck known for its distinctive red head in males. It is often found in freshwater lakes and ponds, where it dives to feed on aquatic plants and invertebrates.",
        "Location": "Common Pochards are distributed across Europe, Asia, and parts of North Africa during their breeding and wintering seasons.",
        "Image": "https://i.pinimg.com/564x/ab/be/d1/abbed16e19d4a63f407ea4d8a52ea342.jpg"
    },
    "Common Wood Pigeon": {
        
        "Scientific Name": "Columba palumbus",
        "Description": "The Common Wood Pigeon is a large pigeon species found in woodlands and urban areas. It is known for its gentle cooing calls and is a common sight in many European cities.",
        "Location": "Common Wood Pigeons are widespread throughout Europe, western Asia, and parts of North Africa.",
        "Image": "https://i.pinimg.com/564x/10/43/be/1043becd0ba8230abaf02ee90eb35709.jpg"
    },
    "Eastern Imperial Eagle": {
        
        "Scientific Name": "Aquila heliaca",
        "Description": "The Eastern Imperial Eagle is a large and powerful bird of prey known for its dark plumage and strong build. It is often seen soaring in open landscapes.",
        "Location": "Eastern Imperial Eagles are found in parts of Europe, Asia, and the Middle East, with a range extending from Eastern Europe to Central Asia.",
        "Image": "https://i.pinimg.com/564x/98/6b/51/986b51faeec7fae5b8a05d1a2f48158c.jpg"
    },
    
#     "Egyptian Vulture": {
        
#         "Scientific Name": "Neophron percnopterus",
#         "Description": "The Egyptian Vulture is a small, white scavenging bird of prey. It is known for its bald head and bright yellow face. It primarily feeds on carrion and is associated with ancient Egyptian symbolism.",
#         "Location": "Egyptian Vultures are found in various parts of Africa, the Middle East, and some regions of Europe and Asia."
#         "Image": " "
#     },
#     "Great Slaty Woodpecker": {
        
#         "Scientific Name": "Mulleripicus pulverulentus",
#         "Description": "The Great Slaty Woodpecker is one of the largest woodpecker species in the world. It has a black body with white markings and is known for its loud drumming calls. It inhabits dense forests and is often seen on large trees.",
#         "Location": "Great Slaty Woodpeckers are found in parts of Southeast Asia, including countries like India, Thailand, and Indonesia."
#         "Image": " "
#     },
#     "Greater Spotted Eagle": {
        
#         "Scientific Name": "Clanga clanga",
#         "Description": "The Greater Spotted Eagle is a large bird of prey known for its dark plumage and distinctive white spots on its wings. It primarily preys on small mammals and birds.",
#         "Location": "Greater Spotted Eagles have a wide distribution range, including Europe, Asia, and parts of the Middle East."
#         "Image": " "
#     },
#     "Grey Treepie": {
        
#         "Scientific Name": "Dendrocitta formosae",
#         "Description": "The Grey Treepie is a medium-sized bird with a grey body and a long, graduated tail. It is known for its vocalizations and is often found in wooded and urban areas.",
#         "Location": "Grey Treepies are native to parts of South and Southeast Asia, including India, Myanmar, and Taiwan."
#         "Image": " "
#     },
#     "Grey-crowned Prinia": {
        
#         "Scientific Name": "Prinia cinereocapilla",
#         "Description": "The Grey-crowned Prinia is a small, brownish bird with a distinctive grey crown on its head. It is known for its melodious song and is commonly found in grasslands and scrubby habitats.",
#         "Location": "Grey-crowned Prinias are distributed across various parts of South and Southeast Asia."
#         "Image": " "
#     },
#     "Grey-sided Thrush": {
        
#         "Scientific Name": "Turdus feae",
#         "Description": "The Grey-sided Thrush is a medium-sized thrush species with a greyish-brown plumage and distinctive white eye-rings. It is known for its beautiful song and is often seen in forested areas.",
#         "Location": "Grey-sided Thrushes are native to parts of East and Southeast Asia, including China, Vietnam, and Taiwan."
#         "Image": " "
#     },
#    "Himalayan Monal": {
        
#         "Scientific Name": "Lophophorus impejanus",
#         "Description": "The Himalayan Monal is a strikingly colorful pheasant species with a vibrant plumage of blues, greens, and reds. Males have a distinctive crest on their heads. They are often found in the mountainous regions of the Himalayas.",
#         "Location": "Himalayan Monals are native to the Himalayan region, including countries like India, Nepal, and Bhutan."
#         "Image": " "
#     },
#     "House Crow": {
        
#         "Scientific Name": "Corvus splendens",
#         "Description": "The House Crow is a small to medium-sized crow species known for its adaptability to urban environments. They are often found in cities and towns and are known for their distinctive cawing calls.",
#         "Location": "House Crows are commonly found in urban areas across South Asia and parts of Southeast Asia."
#         "Image": " "
#     },
#     "House Sparrow": {
        
#         "Scientific Name": "Passer domesticus",
#         "Description": "The House Sparrow is a small, brown bird with a characteristic black bib on its throat. It is a familiar sight in urban and suburban areas worldwide. House Sparrows are known for their cheerful chirping.",
#         "Location": "House Sparrows have a global distribution and are found in urban areas across North America, Europe, Asia, and other regions."
#         "Image": " "
#     },
#     "Indian Spotted Eagle": {
        
#         "Scientific Name": "Clanga hastata",
#         "Description": "The Indian Spotted Eagle is a medium-sized bird of prey with distinctive spots on its wings and body. It primarily preys on small mammals and birds and is often seen soaring in the sky.",
#         "Location": "Indian Spotted Eagles are native to the Indian subcontinent, including India, Nepal, and parts of Southeast Asia."
#         "Image": " "
#     },
#     "Jerdon's Babbler": {
        
#         "Scientific Name": "Chrysomma altirostre",
#         "Description": "Jerdon's Babbler is a small, brown bird with a distinctive white throat and chest. It is known for its secretive behavior in dense undergrowth and is often heard more than seen.",
#         "Location": "Jerdon's Babblers are found in parts of South and Southeast Asia, including India and Myanmar."
#         "Image": " "
#     },
#     "Kashmir Flycatcher": {
        
#         "Scientific Name": "Ficedula subrubra",
#         "Description": "The Kashmir Flycatcher is a small and colorful bird known for its striking plumage and habit of catching insects in mid-air. It is often found in wooded areas and gardens.",
#         "Location": "Kashmir Flycatchers are typically found in regions of South Asia, including India, Pakistan, and Nepal."
#         "Image": " "
#     },
#     "Large-billed Crow": {
        
#         "Scientific Name": "Corvus macrorhynchos",
#         "Description": "The Large-billed Crow is a large crow species known for its hefty bill. It is often found in a variety of habitats, including forests, urban areas, and agricultural fields.",
#         "Location": "Large-billed Crows have a wide distribution range and can be found in parts of Asia, including India, Southeast Asia, and East Asia."
#         "Image": " "
#     },
#     "Long-tailed Duck": {
        
#         "Scientific Name": "Clangula hyemalis",
#         "Description": "The Long-tailed Duck is a medium-sized diving duck known for its long, slender tail feathers. It is often found in cold-water habitats and is an excellent swimmer.",
#         "Location": "Long-tailed Ducks are native to the northern regions of North America, Europe, and Asia, often seen in Arctic and subarctic environments."
#         "Image": " "
#     },
#     "Pallas's Fish Eagle": {
        
#         "Scientific Name": "Haliaeetus leucoryphus",
#         "Description": "Pallas's Fish Eagle is a large bird of prey with distinctive white head and neck feathers. As the name suggests, it primarily feeds on fish and is often seen near water bodies.",
#         "Location": "Pallas's Fish Eagles are native to parts of Asia, including India, Southeast Asia, and parts of Russia."
#         "Image": " "
#     },
#     "Red-billed Blue Magpie": {
        
#         "Scientific Name": "Urocissa erythroryncha",
#         "Description": "The Red-billed Blue Magpie is a colorful member of the crow family known for its striking blue plumage and long tail. It is often found in forested and hilly areas.",
#         "Location": "Red-billed Blue Magpies are native to South and Southeast Asia, including countries like India, Nepal, and Thailand."
#         "Image": " "
#     },
#     "Rose-ringed Parakeet": {
        
#         "Scientific Name": "Psittacula krameri",
#         "Description": "The Rose-ringed Parakeet is a medium-sized parrot known for its bright green plumage and a distinctive rose-colored ring around its neck. It is a popular pet bird and is often seen in urban areas.",
#         "Location": "Rose-ringed Parakeets have a wide distribution and are found in parts of Africa and South Asia, including India."
#         "Image": " "
#     },
#     "Rufous Treepie": {
        
#         "Scientific Name": "Dendrocitta vagabunda",
#         "Description": "The Rufous Treepie is a medium-sized bird with a brown body and a distinctive long tail. It is known for its curious and noisy behavior and is often seen in open woodlands.",
#         "Location": "Rufous Treepies are native to parts of South Asia, including India, Sri Lanka, and Nepal."
#         "Image": " "
#     },
#     "Rufous-necked Hornbill": {
        
#         "Scientific Name": "Aceros nipalensis",
#         "Description": "The Rufous-necked Hornbill is a large and colorful hornbill species known for its distinctive casque and rufous neck. It is often found in the forests of the Himalayan region.",
#         "Location": "Rufous-necked Hornbills are native to the Himalayan region, including countries like India, Nepal, and Bhutan."
#         "Image": " "
#     },
#     "Rustic Bunting": {
        
#         "Scientific Name": "Emberiza rustica",
#         "Description": "The Rustic Bunting is a small songbird with a brownish plumage. It is known for its melodious song and is often seen in shrubby habitats and grasslands.",
#         "Location": "Rustic Buntings breed in parts of northern Asia, including Siberia, and migrate to parts of Southeast Asia during the winter."
#         "Image": " "
#     },
#     "Saker Falcon": {
        
#         "Scientific Name": "Falco cherrug",
#         "Description": "The Saker Falcon is a large bird of prey known for its powerful flight and hunting skills. It has a brownish plumage with distinctive facial markings. It primarily preys on birds and small mammals.",
#         "Location": "Saker Falcons have a wide distribution range and are found in parts of Europe, Asia, and the Middle East."
#         "Image": " "
#     },
#     "Sarus Crane": {
        
#         "Scientific Name": "Antigone antigone",
#         "Description": "The Sarus Crane is one of the tallest flying birds in the world. It has a predominantly white plumage and a red facial skin patch. Sarus Cranes are known for their graceful dance displays.",
#         "Location": "Sarus Cranes are native to South Asia and Southeast Asia, including countries like India and Cambodia."
#         "Image": " "
#     },
#     "Satyr Tragopan": {
        
#         "Scientific Name": "Tragopan satyra",
#         "Description": "The Satyr Tragopan is a colorful pheasant species known for its striking plumage and vivid colors. Males have distinctive horn-like projections on their heads.",
#         "Location": "Satyr Tragopans are found in the eastern Himalayan region, including countries like India, Bhutan, and Nepal."
#         "Image": " "
#     },
#     "Slender-billed Babbler": {
        
#         "Scientific Name": "Turdoides longirostris",
#         "Description": "The Slender-billed Babbler is a small bird known for its slender bill and brownish plumage. It is often found in dense undergrowth and is known for its cooperative breeding behavior.",
#         "Location": "Slender-billed Babblers are native to parts of South Asia, including India and Sri Lanka."
#         "Image": " "
#     },
#     "Spiny Babbler": {
        
#         "Scientific Name": "Turdoides nipalensis",
#         "Description": "The Spiny Babbler is a medium-sized bird known for its distinctive spiky plumage. It is endemic to the Himalayan region and is known for its unique calls.",
#         "Location": "Spiny Babblers are endemic to the Himalayan region, including countries like Nepal and Bhutan."
#         "Image": " "
#     },
#     "Spotted Dove": {
    
#         "Scientific Name": "Spilopelia chinensis",
#         "Description": "The Spotted Dove is a small and slender dove species known for its spotted plumage and gentle cooing calls. It is often seen in urban and rural areas.",
#         "Location": "Spotted Doves have a wide distribution range and can be found in parts of Asia, including India, Southeast Asia, and East Asia."
#         "Image": " "
#     },
#     "Steppe Eagle": {

#         "Scientific Name": "Aquila nipalensis",
#         "Description": "The Steppe Eagle is a large bird of prey known for its brown plumage and distinctive white patches on the wings. It is often seen soaring over open landscapes.",
#         "Location": "Steppe Eagles have a wide distribution range, including parts of Europe, Asia, and Africa, and are known for their long-distance migrations."
#         "Image": " "
#     },
    
#     "Swamp Francolin": {
        
#         "Scientific Name": "Francolinus gularis",
#         "Description": "The Swamp Francolin is a medium-sized bird known for its brown plumage and distinctive calls. It is often found in wetland habitats, especially in tall grasses and reeds.",
#         "Location": "Swamp Francolins are native to parts of South Asia, including India, Bangladesh, and Nepal."
#         "Image": " "
#     },
#     "Swamp Grass-babbler": {
        
#         "Scientific Name": "Graminicola bengalensis",
#         "Description": "The Swamp Grass-babbler is a small bird known for its cryptic plumage and habit of skulking in dense vegetation. It is often heard more than seen.",
#         "Location": "Swamp Grass-babblers are native to wetland habitats in South and Southeast Asia, including countries like India and Thailand."
#         "Image": " "
#     },
#     "White-throated Bushchat": {
        
#         "Scientific Name": "Saxicola insignis",
#         "Description": "The White-throated Bushchat is a small bird with a distinctive white throat and black plumage. It is often found in grassy and open habitats.",
#         "Location": "White-throated Bushchats are native to parts of South Asia, including India, Nepal, and Bhutan."
#         "Image": " "
#     },
#     "Wood Snipe": {
        
#         "Scientific Name": "Gallinago nemoricola",
#         "Description": "The Wood Snipe is a medium-sized wader bird known for its cryptic plumage and long bill. It is often found in wetlands and forested areas.",
#         "Location": "Wood Snipes are native to parts of South and Southeast Asia, including countries like India, Myanmar, and Indonesia."
#         "Image": " "
#     },
}




# Assuming your FastAPI server is running at http://localhost:8000
url = "http://localhost:8000/add_bird"

for bird_name, bird_info in bird_info_data.items():
    # Check if the bird data already exists in the MongoDB database
    response = requests.get(f"http://localhost:8000/get_bird/{bird_name}")

    if response.status_code == 404:
        # Bird data does not exist, so send the POST request to add it
        response = requests.post(url, json={
            "name": bird_name,
            "scientificName": bird_info["Scientific Name"],
            "description": bird_info["Description"],
            "location": bird_info["Location"],
            "imageUri" : bird_info["Image"]
        })

        print(f"Data for {bird_name} added to the database.")
        
    elif response.status_code == 200:
        print(f"Data for {bird_name} already exists in the database.")
    else:
        print(f"Unexpected response status code for {bird_name}: {response.status_code}")



