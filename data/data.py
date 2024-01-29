import requests
from PIL import Image
import urllib.request
from io import BytesIO
import base64
from io import BytesIO
from pydub import AudioSegment
import os

bird_info_data = {
    "Common Moorhen" : {
        "Scientific Name" : "Gallinula chloropus",
        "length" : "30-38 cm",
        "width" : "50-62 cm",
        "mass" : "192-500 g",
        "Description" : "The moorhen is a distinctive species, with predominantly black and brown plumage, with the exception of a white under-tail, white streaks on the flanks, yellow legs and a red frontal shield. The bill is red with a yellow tip. The young are browner and lack the red shield. The frontal shield of the adult has a rounded top and fairly parallel sides; the tailward margin of the red unfeathered area is a smooth waving line. In the related common gallinule (Gallinula galeata) of the Americas, the frontal shield has a fairly straight top and is less wide towards the bill, giving a marked indentation to the back margin of the red area.",
        "Location" : "This is a common breeding and resident bird in marsh environments, rivers, well-vegetated lakes and even in city parks. Populations in areas where the waters freeze, such as eastern Europe, will migrate to more temperate climates. In China, common moorhen populations are largely resident south of the Yangtze River, whilst northern populations migrate in the winter, therefore these populations show high genetic diversity.",
        
        "Image" : "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Common_moorhen_%28Gallinula_chloropus%29_France.jpg/1280px-Common_moorhen_%28Gallinula_chloropus%29_France.jpg",
        "Video" : "https://www.youtube.com/watch?v=FMp2P9GqGfk"
    },

    "Pied Avocet" : {
        "Scientific Name" : "Recurvirostra avosetta",
        "length" : "41.9-45.1 cm",
        "width" : "76-80 cm",
        "mass" : "240-315 g",
        "Description" : "The pied avocet is a striking white wader with bold black markings. Adults have white plumage except for a black cap and black patches in the wings and on the back. They have long, upturned bills and long, bluish legs. It is approximately 16.5-17.75 in (41.9-45.1 cm) in length of which the bill is approximately 2.95-3.35 in (7.5-8.5 cm) and the legs are approximately 3-4 in (7.6-10.2 cm). Its wingspan is approximately 30-31.5 in (76-80 cm). Males and females look alike. The juvenile resembles the adult but with more greyish and sepia tones.The call of the avocet is a far-carrying, liquid, melodious kluit kluit.",
        "Location" : "They breed in temperate Europe and across the Palearctic to Central Asia then on to the Russian Far East. It is a migratory species and most winter in Africa or southern Asia. Some remain to winter in the mildest parts of their range, for example in southern Spain and southern England.",
        
        "Image" : "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Pied_Avocet_Recurvirostra_avosetta.jpg/1280px-Pied_Avocet_Recurvirostra_avosetta.jpg",
        "Video" : "https://www.youtube.com/watch?v=0lKQVqV8dQg"
    },


    "Little Ringed Plover" : {
        "Scientific Name" : "Charadrius dubius",
        "length" : "15-18 cm",
        "width" : "42-48 cm",
        "mass" : "39 g",
        "Description" : "Adult little ringed plovers have a grey-brown back and wings, a white belly and a white breast with one black neckband. They have a brown cap, a white forehead, a black mask around the eyes with white above and a short dark bill. The legs are flesh-coloured and the toes are all webbed.This species differs from the larger ringed plover in leg colour, the head pattern, and the presence of a clear yellow eye-ring.",
        "Location" : "Their breeding habitat is open gravel areas near freshwater, including gravel pits, islands and river edges across the Palearctic including northwestern Africa. They nest on the ground on stones with little or no plant growth. Both males and females take turns incubating the eggs.They are migratory and winter in Africa. These birds forage for food on muddy areas, usually by sight. They eat insects and worms.",
        
        "Image" : "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Flussregenpfeifer_im_flachen_Wasser_01.jpg/1024px-Flussregenpfeifer_im_flachen_Wasser_01.jpg",
        "Video" : "https://www.youtube.com/watch?v=qU9Y2rMdVIc"
    },


    "Water Rail" : {
        "Scientific Name" : "Rallus aquaticus",
        "length" : "23-28 cm",
        "width" : "38-45 cm",
        "mass" : "114-164 g",

        "Description" : "The upper parts from the forehead to tail are olive-brown with black streaks, especially on the shoulders. The sides of the head and the underparts down to the upper belly are dark slate-blue, except for a blackish area between bill and eye, and brownish sides to the upper breast. The flanks are barred black and white, and the undertail is white with some darker streaks. The long bill and the iris are red, and the legs are flesh-brown. The sexes are similar; although the female averages slightly smaller than the male, with a more slender bill, determining sex through measurements alone is unreliable. The juvenile has a blackish crown and a white chin and throat. The underparts are buff or white with darker bars, and the flank markings are brown and buff, rather than black and white. The undertail is buff, and the eye, bill and leg colours are duller than the adult. The downy chick is all black apart from a mainly white bill. After breeding, the rail has an extensive moult, and is flightless for about three weeks. Individual adults can be identified by the markings on the undertail, which are unique to each bird. Adult males have the strongest black undertail streaks. It has been suggested that the dark barring on the undertail of this species is a compromise between the signalling function of a pure white undertail, as found in open water or gregarious species like the common moorhen, and the need to avoid being too conspicuous.The water rail can readily be distinguished from most other reed bed rails by its white undertail and red bill; the latter is a little longer than the rest of the rail's head (55-58 percent of the total) and slightly down-curved. The somewhat similar slaty-breasted rail of tropical Asia has a stouter bill, a chestnut crown and white-spotted upperparts. Juvenile and freshly moulted water rails may show a buff undertail like spotted crake, but that species' plumage is spotted with white, and it has a much shorter, mainly yellowish bill. The range of the water rail does not overlap with that of any other Rallus species, but vagrants could be distinguished from their American relatives by the lack of rufous or chestnut on the closed wing. The larger African rail has unstreaked darker brown upperparts and brighter red legs and feet.",

        "Location" : "The water rail is a bird species that breeds across temperate Eurasia, from Iceland and Ireland to North Africa, Saudi Arabia, and western China. The distribution in Asia is not well-studied. The Icelandic population became extinct in 1965 due to habitat loss and predation by introduced American minks. The species exhibits partial migration, with some populations wintering in specific areas.Breeding habitats include permanent wetlands with still or slow-moving fresh or brackish water, dense vegetation like reeds, rushes, and sedges. Nest construction depends on the availability of nearby plants. The water rail may also use unconventional locations such as roadside nests or nest boxes.The preferred breeding habitat is Phragmites reedbed standing in water with a depth of 5-30 cm. The presence of nearby willows or shrubs is favored over large uniform habitats. The distribution is influenced by vegetation cover, with the highest densities in the most vegetated areas.Unusual nesting locations have been observed, including roadside nests and nesting under the wooden floors of nest boxes. While primarily a lowland species, the water rail has been found breeding at higher altitudes, up to 1,240 m in the Alps and 2,000 m in Armenia.During migration and winter, the water rail utilizes a variety of wet habitats, including flooded thickets, bracken, and sometimes more open locations due to freezing conditions. Wintering birds in Iceland rely on warm geothermal streams, sheltering in holes and crevices in solidified lava when not feeding.The species occasionally ventures outside its normal range, with vagrants reported in locations such as the Azores, Madeira, Mauritania, the Arctic, Greenland, Malaysia, and Vietnam.",
        
        "Image" : "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/253662431/1800",
        "Video" : "https://www.youtube.com/watch?v=ibtG6IcH2Yc"
    },

    "Dunlin" : {
        "Scientific Name" : "Calidris alpina",
        "length" : "16-22 cm",
        "width" : "36-38 cm",
        "mass" : "48-76 g",

        "Description": "An adult dunlin in breeding plumage shows the distinctive black belly which no other similar-sized wader possesses. The winter dunlin is basically grey above and white below. Juveniles are brown above with two whitish 'V' shapes on the back. They usually have black marks on the flanks or belly and show a strong white wingbar in flight. The legs and slightly decurved bill are black. There are a number of subspecies differing mainly in the extent of rufous colouration in the breeding plumage and the bill length. Bill length varies between sexes, the females having longer bills than the males. On the tip of the Dunlin's bill is a soft covering that fills with blood and with many nerve endings, forming a sensitive probe that is used to locate invertebrate prey in mud and sand. Although the bill can look sharp-pointed in dead specimens, in life it is blunt.The call is a typical sandpiper 'peep', and the display song a harsh trill.",

        "Location": "Dunlin are small migratory waders, however they show strong philopatry with individuals of the Southern Dunlin (Calidris alpina schinzii) in Sweden and Finland returning to, or very close to, their natal patches. Habitat fragmentation has reduced the availability of habitat patches to these birds through reducing patch size and increasing patch isolation. This reduced connectivity between patches has reduced the movements of Dunlin leaving them more susceptible to inbreeding in these locations.",
        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/DunlinEastPoint.png/1280px-DunlinEastPoint.png",
        "Video" : "https://www.youtube.com/watch?v=eTivR71Nqo0"
    },


    "Grey Plover" : {
        "Scientific Name" : "Pluvialis squatarola",
        "length" : "27-30 cm",
        "width" : "71-83 cm",
        "mass" : "190-280 g",

        "Description": "In spring and summer (late April or May to August), adults are spotted black and white on the back and wings. The face and neck are black with a white border; they have a black breast and belly and a white rump. The tail is white with black barring. The bill and legs are black. They moult to winter plumage in mid August to early September and retain this until April; this being a fairly plain grey above, with a grey-speckled breast and white belly. The juvenile and first-winter plumages, held by young birds from fledging until about one year old, are similar to the adult winter plumage but with the back feathers blacker with creamy white edging. In all plumages, the inner flanks and axillary feathers at the base of the underwing are black, a feature which readily distinguishes it from the other three Pluvialis species in flight. On the ground, it can also be told from the other Pluvialis species by its larger (24-34 mm, 0.94-1.34 in), heavier bill.",

        "Location": "Their breeding habitat is Arctic islands and coastal areas across the northern coasts of Alaska, Canada, and Russia. They nest on the ground in a dry open tundra with good visibility; the nest is a shallow gravel scrape. Four eggs (sometimes only three) are laid in early June, with an incubation period of 26-27 days; the chicks fledge when 35-45 days old.They migrate to winter in coastal areas throughout the world. In the New World they winter from southwest British Columbia and Massachusetts south to Argentina and Chile, in the western Old World from Ireland and southwestern Norway south throughout coastal Africa to South Africa, and in the eastern Old World, from southern Japan south throughout coastal southern Asia and Australia, with a few reaching New Zealand. Most of the migrants to Australia are female. It makes regular non-stop transcontinental flights over Asia, Europe, and North America, but is mostly a rare vagrant on the ground in the interior of continents, only landing occasionally if forced down by severe weather, or to feed on the coast-like shores of very large lakes such as the Great Lakes, where it is a common passage migrant.",

        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/a/aa/Pluvialis_squatarola_%28summer_plumage%29.jpg",
        "Video" : "https://www.youtube.com/watch?v=MOaSTvDFLG0"
    },

     "Wood Sandpiper": {
        "Scientific Name": "Tringa glareola",
        "length" : "39-46 cm",
        "width" : "",
        "mass" : "190-327 g",

        "Description": "It resembles a longer-legged and more delicate green (T. ochropus) or solitary sandpiper (T. solitaria) with a short fine bill, brown back and longer yellowish legs. It differs from the first of those species in a smaller and less contrasting white rump patch, while the solitary sandpiper has no white rump patch at all.However, it is not very closely related to these two species. Rather, its closest relative is the common redshank (T. totanus), and these two share a sister relationship with the marsh sandpiper (T. stagnatilis). These three species are a group of smallish shanks with red or yellowish legs, a breeding plumage that is generally subdued light brown above with some darker mottling and with a pattern of somewhat diffuse small brownish spots on the breast and neck.",

        "Location": "The wood sandpiper breeds in subarctic wetlands from the Scottish Highlands across Europe and then east across the Palearctic. They migrate to Africa, Southern Asia, particularly India, and Australia. Vagrant birds have been seen as far into the Pacific as the Hawaiian Islands. In Micronesia it is a regular visitor to the Mariana Islands (where flocks of up to 32 birds are reported) and Palau; it is recorded on Kwajalein in the Marshall Islands about once per decade. This species is encountered in the western Pacific region between mid-October and mid-May. A slight westward expansion saw the establishment of a small but permanent breeding population in Scotland since the 1950s",

        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Wood_Sandpiper_Safari_Park.jpg/800px-Wood_Sandpiper_Safari_Park.jpg",
        "Video" : "https://www.youtube.com/watch?v=vvDhGy-coxU"
    },

     "Common Snipe": {
        "Scientific Name": "Gallinago gallinago",
        "length" : "25-27 cm ",
        "width" : "44-47 cm",
        "mass" : "80-140 g",

        "Description": "They have short greenish-grey legs and a very long (5.5-7 cm (2.2-2.8 in)) straight dark bill. The body is mottled brown with straw-yellow stripes on top and pale underneath. They have a dark stripe through the eye, with light stripes above and below it. The wings are pointed.The common snipe is the most widespread of several similar snipes. It most closely resembles the Wilson's snipe (G. delicata) of North America, which was until recently considered to be a subspecies - G. g. delicata - of the common snipe. They differ in the number of tail feathers, with seven pairs in G. gallinago and eight pairs in G. delicata; the North American species also has a slightly thinner white trailing edge to the wings (the white is mostly on the tips of the secondaries).[8][9] Both species breed in the Aleutian Islands.[6] It is also very similar to the pin-tailed snipe (G. stenura) and Swinhoe's snipe (G. megala) of eastern Asia; identification of these species there is complex.The subspecies faeroeensis is normally more richly toned on the breast, its upperparts and the head than the nominate gallinago.",

        "Location": "The common snipe breeds from Alaska to Newfoundland south to the mid-United States. It winters north from northern South America to British Columbia, the northern Gulf states and Virginia. It is also found in Europe, Northern Africa and Asia.",
        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Gallinago_gallinago_a1.JPG/1024px-Gallinago_gallinago_a1.JPG",
        "Video" : "https://www.youtube.com/watch?v=7U9gtsFCN8s"
    },

     "Common Redshank": {
        "Scientific Name": "Gallinago gallinago",
        "length" : "27-29 cm",
        "width" : "48-55 cm",
        "mass" : "120 g",

        "Description": "Common redshanks in breeding plumage are a marbled brown color, slightly lighter below. In winter plumage they become somewhat lighter-toned and less patterned, being rather plain greyish-brown above and whitish below. They have red legs and a black-tipped red bill, and show white up the back and on the wings in flight.The spotted redshank (T. erythropus), which breeds in the Arctic, has a longer bill and legs; it is almost entirely black in breeding plumage and very pale in winter. It is not a particularly close relative of the common redshank, but rather belongs to a high-latitude lineage of largish shanks. T. totanus on the other hand is closely related to the marsh sandpiper (T. stagnatilis), and closer still to the small wood sandpiper (T. glareola). The ancestors of the latter and the common redshank seem to have diverged around the Miocene-Pliocene boundary, about 5-6 million years ago. These three subarctic- to temperate-region species form a group of smallish shanks with have red or yellowish legs, and in breeding plumage are generally a subdued light brown above with some darker mottling, and have somewhat diffuse small brownish spots on the breast and neck.",

        "Location": "The common redshank is a widespread breeding bird across temperate Eurasia. It is a migratory species, wintering on coasts around the Mediterranean, on the Atlantic coast of Europe from Ireland and Great Britain southwards, and in South Asia. They are uncommon vagrants outside these areas; on Palau in Micronesia for example, the species was recorded in the mid-1970s and in 2000.[11] A tagged redshank was spotted at Manakudi Bird Sanctuary, Kanniyakumari District of Tamil Nadu, India in the month of April 2021.",

        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Common_Redshank_Tringa_totanus.jpg/1280px-Common_Redshank_Tringa_totanus.jpg",
        "Video" : "https://www.youtube.com/watch?v=HUqyWehh-Uw"
    },

     "White-breasted Waterhen": {
        "Scientific Name": "Amaurornis phoenicurus",
        "length" : "28-33 cm",
        "width" : "49 cm",
        "mass" : "165-328 g",

        "Description": "Adult white-breasted waterhens have mainly dark grey upperparts and flanks, and a white face, neck and breast. The lower belly and undertail are cinnamon or white coloured. The body is flattened laterally to allow easier passage through the reeds or undergrowth. They have long toes, a short tail and a yellow bill and legs. Sexes are similar but females measure slightly smaller. Immature birds are much duller versions of the adults. The downy chicks are black, as with all rails. Several subspecies are named for the populations that are widely distributed. The nominate subspecies is described from Sri Lanka but is often widened to include chinensis of mainland India and adjoining regions in Asia, west to Arabia and east nearly to Japan. The remaining subspecies are those from islands and include insularis of the Andaman and Nicobar Islands, midnicobaricus of the central Nicobars, leucocephala of Car Nicobar, maldivus of the Maldives, javanicus of Java and leucomelanus of Sulawesi and the Lesser Sundas.",

        "Location": "Their breeding habitat is marshes across tropical Asia from Pakistan east to Indonesia. They are mainly seen in the plains but have been known from the higher hills such as in Nainital (1300m) and the High Range (1500m) in Kerala. These large 32 cm (13 in) long rails are permanent residents throughout their range. They make short distance movements and are known to colonize new areas. They have been noted as some of the early colonizers on the volcanic island of Rakata.[7][8] Although most often found near freshwater, they are also found near brackish water and even the seashore when there is no freshwater as on the volcanic Barren Island in the Andamans.",

        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Amaurornis_phoenicurus_-_Singapore_Botanic_Gardens.jpg/1280px-Amaurornis_phoenicurus_-_Singapore_Botanic_Gardens.jpg",
        "Video" : "https://www.youtube.com/watch?v=QJaTRq7d3E4"
    },


     "Eurasian Oystercatcher": {
        "Scientific Name": "Haematopus ostralegus",
        "length" : " 40-45 cm",
        "width" : "80-85 cm",
        "mass" : "480 g",

        "Description": "The oystercatcher is one of the largest waders in the region, measuring 40-45 cm in length, with a wingspan of 80-85 cm and a distinctive appearance. It has black and white plumage, pink legs, and a robust red bill (8-9 cm) used for breaking open mollusks like mussels or for finding earthworms. Despite its name, oysters are not a major part of its diet, but it is adept at opening them.In flight, the oystercatcher is easily recognizable with white patches on its wings and tail, black upperparts, and white underparts. Young birds have a brown hue, a white neck collar, and a less vibrant bill. The call of the oystercatcher is a loud and distinctive piping sound.The bill shape varies among individuals, with some having broad bill tips for prising mollusks open, while others have pointed bills for digging up worms. This variation is learned from parents, and birds tend to specialize in one technique. The subspecies longipes has brownish upperparts and a nasal groove extending more than halfway along the bill. In contrast, the subspecies ostralegus has a nasal groove that stops short of the halfway mark, and the osculans subspecies lacks white on certain primaries. The American oystercatcher (Haematopus palliatus) differs from the Eurasian oystercatcher in having a yellow eye and blackish-brown dorsal plumage instead of black.",

        "Location": "The oystercatcher is a migratory species over most of its range. The European population breeds mainly in northern Europe, but in winter the birds can be found in north Africa and southern parts of Europe. Although the species is present all year in Ireland, Great Britain and the adjacent European coasts, there is still migratory movement: the large flocks that are found in the estuaries of south-west England in winter mainly breed in northern England or Scotland. Similar movements are shown by the Asian populations. The birds are highly gregarious outside the breeding season.",

        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Haematopus_ostralegus_Norway.jpg/1024px-Haematopus_ostralegus_Norway.jpg",
        "Video" : "https://www.youtube.com/watch?v=wd2JCWosT4s"
    },

     "Common Wood Pigeon": {
        "Scientific Name": "Columba palumbus",
        "length" : "38-44.5 cm",
        "width" : "68-80 cm",
        "mass" : "300-615 g",

        "Description": "The three Western European Columba pigeons—common wood pigeon, stock dove, and rock dove—may appear similar at first glance but exhibit distinctive characteristics. The common wood pigeon stands out with its larger size, measuring 38-44.5 cm and weighing 300-615 g. It has white markings on its neck and wings, setting it apart from the others. The bird is primarily grey with a pinkish breast, and adult individuals have green and white patches on their necks, along with a pink patch on the chest. The wingspan ranges from 68 to 80 cm, the tail measures 13.8 to 15 cm, the bill is 1.9 to 2.2 cm, and the tarsus is 2.5 to 2.8 cm. The eye color is a pale yellow.Juvenile common wood pigeons lack the white patches on the sides of the neck. Around six months of age, they develop small white patches on both sides of the neck, gradually enlarging until fully formed when the bird is about 6-8 months old. Juveniles also have a greyer beak and an overall lighter grey appearance compared to adult birds. This distinguishes them from the rock dove, which has orange-red eyes, and the stock dove, which has black eyes.",

        "Location": "In the colder northern and eastern parts of Europe and western Asia the common wood pigeon is a migrant, but in southern and western Europe it is a well distributed and often abundant resident. In Great Britain wood pigeons are commonly seen in parks and gardens[10] and are seen with increasing numbers in towns and cities.",
        
        "Image":"https://i.pinimg.com/564x/10/43/be/1043becd0ba8230abaf02ee90eb35709.jpg",
        "Video" : "https://www.youtube.com/watch?v=poeYBbpR9z4"
    },


     "Barn Swallow": {
        "Scientific Name": "Chirundo rustica",
        "length" : "17-19 cm",
        "width" : "32-34.5 cm",
        "mass" : "16-22 g",

        "Description": "The adult male barn swallow of the nominate subspecies H. r. rustica is 17-19 cm long, including 2-7 cm of elongated outer tail feathers, with a wingspan of 32-34.5 cm and a weight of 16-22 g. It features steel blue upperparts and a rufous forehead, chin, and throat, separated from the off-white underparts by a broad dark blue breast band. The distinctive deeply forked 'swallow tail' is created by elongated outer tail feathers, and there is a line of white spots across the outer end of the upper tail. The female is similar but has shorter tail streamers, less glossy upperparts, and paler underparts. Juveniles are browner with a paler rufous face and lack the long tail streamers of adults.Both male and female barn swallows sing, and recent descriptions include female song. Calls include witt or witt-witt, and a loud splee-plink is emitted when excited or warding off intruders. Alarm calls vary, with a sharp siflitt for predators like cats and a flitt-flitt for birds of prey. The species is relatively quiet during the wintering period. The distinctive red face and blue breast band make the adult barn swallow easily distinguishable from African Hirundo species and the welcome swallow (Hirundo neoxena) in Australasia. In Africa, the short tail streamers of juvenile barn swallows may be confused with juvenile red-chested swallows (Hirundo lucida), but differences in breast band width and tail coloration help in differentiation.",

        "Location": "The barn swallow prefers open country with low vegetation, including pasture, meadows, and farmland, especially near water. It avoids heavily wooded or precipitous areas and densely built-up locations. The presence of open structures like barns, stables, and culverts for nesting sites, along with exposed locations such as wires, roof ridges, or bare branches for perching, is crucial for selecting breeding sites. Barn swallows are semi-colonial, settling in groups ranging from a single pair to a few dozen pairs, particularly in larger wooden structures housing animals. They often return to the same breeding site year after year, with old nests being highly valued. The species breeds across the Northern Hemisphere from sea level to 2,700 m but up to 3,000 m in the Caucasus and North America, excluding deserts and the cold northernmost regions. In winter, barn swallows are cosmopolitan in their habitat choices, avoiding dense forests and deserts. They are common in open, low vegetation habitats such as savanna and ranch land. During winter, barn swallows exhibit a cosmopolitan distribution, avoiding only dense forests and deserts. They are most common in open, low vegetation habitats like savannas and ranch lands. In Venezuela, South Africa, and Trinidad and Tobago, they are attracted to burnt or harvested sugarcane fields and their waste. Roosting can occur on wires in the absence of suitable roost sites, and birds tend to return to the same wintering locality each year, congregating in large roosts in reed beds, some of which can be extremely large. Migration patterns of barn swallows have been documented, with records of birds traveling long distances as vagrants to areas such as Hawaii, Bermuda, Greenland, Tristan da Cunha, the Falkland Islands, and even Antarctica. Migration routes have been established, including movements between Britain and South Africa, providing insights into the species' impressive migratory capabilities.",

        
        "Image":"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTfG1JqKwZXucNy7E4d2zqiyxrW0We7NgjbZlbo29-G_2msbmxe",
        "Video" : "https://www.youtube.com/watch?v=f8dWDgjqSuM"
    },


     "Asian Koel": {
        "Scientific Name": "Eudynamys scolopaceus",
        "length" : "39-46 cm",
        "width" : "",
        "mass" : "190-327 g",

        "Description": "The Asian koel is a large and long-tailed cuckoo. The male of the nominate race is glossy bluish-black, with a pale greenish grey bill, the iris is crimson, and it has grey legs and feet. The female of the nominate race is brownish on the crown and has rufous streaks on the head. The back, rump and wing coverts are dark brown with white and buff spots. The underparts are whitish, but is heavily striped. The other subspecies differ in colouration and size.[16] The upper plumage of young birds is more like that of the male and they have a black beak.[20] They are very vocal during the breeding season (March to August in the Indian Subcontinent), with a range of different calls. The familiar song of the male is a repeated koo-Ooo. The female makes a shrill kik-kik-kik... call. Calls vary across populations.",

        "Location": "The Asian koel is a bird of light woodland and cultivation. It is a mainly resident breeder in tropical southern Asia from Iran, Pakistan, India, Bangladesh and Sri Lanka to southern China and the Greater Sundas. They have great potential in colonizing new areas, and were among the pioneer birds to colonize the volcanic island of Krakatau. They first arrived in Singapore in the 1980s and became very common birds.",
        
        "Image":"https://i.pinimg.com/564x/dc/34/e9/dc34e904e0ee0c10f1f42e2e5a9b84b9.jpg",
        "Video" : "https://www.youtube.com/watch?v=VvQaVyjXP1M"
    },

     "Black-tailed Godwit": {
        "Scientific Name": "Limosa limosa",
        "length" : "42 cm",
        "width" : "70-82 cm",
        "mass" : "280 g",

        "Description": "The black-tailed godwit is a large wader distinguished by its long bill (7.5 to 12 cm), neck, and legs. During the breeding season, the bill has a yellowish or orange-pink base with a dark tip; in winter, the base becomes pink. The legs can be dark grey, brown, or black. Both sexes are similar, but in breeding plumage, males have a brighter, more extensive orange breast, neck, and head. In winter, adults display a uniform brown-grey breast and upperparts, and juveniles have a pale orange wash to the neck and breast. In flight, the black-tailed godwit reveals bold black and white wings and a white rump. On the ground, it can be challenging to differentiate from the bar-tailed godwit, but the black-tailed godwit's longer, straighter bill and longer legs serve as diagnostic features. While similar in body size and shape to bar-tailed godwits, black-tailed godwits stand taller. The bird measures 42 cm from bill to tail with a wingspan of 70-82 cm. Males weigh around 280 g, and females weigh 340 g, with females being approximately 5 percent larger than males, possessing a bill that is 12-15 percent longer. The most common call of the black-tailed godwit is a strident 'weeka weeka weeka.' A study in the Netherlands found mortality rates of 37.6 percent in the first year of life, 32 percent in the second year, and 36.9% thereafter for black-tailed godwits.",

        "Location": "Black-tailed godwits have a breeding range extending from Iceland to the far east of Russia, with a habitat that includes river valley fens, lake edges, steppes, bogs, moorlands, and secondary habitats like wet grasslands and coastal marshes. Breeding can even occur in agricultural fields such as sugar beet, potato, and rye fields. During spring, these godwits primarily feed in grasslands, later moving to muddy estuaries for breeding and wintering. Wintering grounds include African swamps, floods, paddy fields, and various wet areas, while migration routes vary based on populations. Icelandic godwits winter mainly in the UK, Ireland, France, and the Netherlands, with some reaching Spain, Portugal, and Morocco. Western European godwits migrate to Morocco, Senegal, and Guinea-Bissau, while eastern European populations travel to Tunisia, Algeria, Mali, or Chad. Young European birds remain in Africa for their first winter, returning to Europe at the age of two. Asian godwits winter in locations like Australia, Taiwan, the Philippines, Indonesia, and Papua New Guinea. Black-tailed godwits are more commonly found in inland wetlands than coastal areas, migrating in flocks to Western Europe, Africa, South Asia, and Australia. In Ireland and Great Britain, they are present year-round, but breeding birds leave in autumn, replaced by the larger Icelandic race during winter. Some individuals may appear in the Aleutian Islands and, rarely, on the Atlantic coast of North America.",

        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/thumb/4/40/Black-tailed_Godwit_Uferschnepfe.jpg/1024px-Black-tailed_Godwit_Uferschnepfe.jpg",
        "Video" : "https://www.youtube.com/watch?v=TnXXqHaoWgs"
    },

     "Green Sandpiper": {
        "Scientific Name": "Tringa ochropus",
        "length" : "21-24 cm",
        "width" : "59 cm",
        "mass" : "75 g",

        "Description": "This species is a somewhat plump wader with a dark greenish-brown back and wings, greyish head and breast and otherwise white underparts. The back is spotted white to varying extents, being maximal in the breeding adult, and less in winter and young birds. The legs and short bill are both dark green. It is conspicuous and characteristically patterned in flight, with the wings dark above and below and a brilliant white rump. The latter feature reliably distinguishes it from the slightly smaller but otherwise very similar solitary sandpiper (T. solitaria) of North America. In flight it has a characteristic three-note whistle.",

        "Location": "The green sandpiper breeds across subarctic Europe and east across the Palearctic and is a migratory bird, wintering in southern Europe, the Indian Subcontinent, Southeast Asia, and tropical Africa. Food is small invertebrate items picked off the mud as this species works steadily around the edges of its chosen pond. This is not a gregarious species, although sometimes small numbers congregate in suitable feeding areas. Green sandpiper is very much a bird of freshwater, and is often found in sites too restricted for other waders, which tend to like a clear all-round view.",

        
        "Image":"https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcTuaTWs1oJCT2s7DqM8MSqrRvYhWoFR6mZDHNFkdi4dX6E9Ci89GJeLRniDtQMZhGHpvIHsZCxCGn0U8x4",
        "Video" : "https://www.youtube.com/watch?v=JNmc3bLEpek"
    },



    "Common Myna": {
        "Scientific Name": "Acridotheres tristis",
        "length" : "23-26 cm",
        "width" : "12-14.2 cm",
        "mass" : "82-143 g",

        "Description": "The common myna is readily identified by the brown body, black hooded head and the bare yellow patch behind the eye. The bill and legs are bright yellow. There is a white patch on the outer primaries and the wing lining on the underside is white. The sexes are similar and birds are usually seen in pairs. The common myna obeys Gloger's rule in that the birds from northwestern India tend to be paler than their darker counterparts in southern India.",

        "Location": "The common myna is native to Asia, with its original range covering countries such as Iran, Pakistan, India, Nepal, Bhutan, Bangladesh, Sri Lanka, Afghanistan, Uzbekistan, Tajikistan, Turkmenistan, Myanmar, Malaysia, Singapore, peninsular Thailand, Indochina, Japan, and China. It has been introduced to various parts of the world, including Canada, Australia, Israel, New Zealand, New Caledonia, Fiji, the United States (specifically South Florida), South Africa, Kazakhstan, Kyrgyzstan, Uzbekistan, the Cayman Islands, islands in the Indian Ocean, islands in the Atlantic and Pacific Oceans, and Cyprus. The common myna is adaptable and found in open woodlands, cultivated areas, and around human habitation. Despite its adaptability, it is considered a pest in certain regions, such as Singapore, where it competes with the introduced Javan myna. The species thrives in urban and suburban environments, and in places like Canberra, Australia, its population density increased significantly after its introduction, reaching 75 birds per square kilometer in some areas. The success of the common myna in urban settings, particularly in Sydney and Canberra, can be attributed to its evolutionary origins in the open woodlands of India. The bird is pre-adapted to habitats with tall structures and minimal ground cover, which are common features in city streets and urban nature preserves. The common myna's population expansion has led to its classification as one of the world's worst invasive species by the IUCN Species Survival Commission.",

        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/3/3c/Acridotheres_tristis00.jpg",
        "Video" : "https://www.youtube.com/watch?v=6fIkn50uNqw"
    },


    "Common Swift": {
        "Scientific Name": "Apus apus",
        "length" : "16-17 cm ",
        "width" : "38-40 cm",
        "mass" : "38 g",

        "Description": "Common swifts are small birds, 16-17 cm in length, with a wingspan of 38-40 cm. They are entirely blackish-brown, except for a small, not easily visible, white or pale grey patch on their chins. The short forked tail and long swept-back wings give them a crescent or boomerang-like appearance. Known for their loud screams, especially during 'screaming parties' in the evening, common swifts form groups of 10-20 birds around nesting areas. These gatherings, observed more at higher altitudes late in the breeding season, have unclear purposes, possibly related to ascending for sleep on the wing. Radar tracking reveals that flocking benefits swifts through cue acquisition, information exchange, or extended social behavior, particularly during evening ascent and dawn descent.",

        "Location": "Common swifts are migratory birds breeding across a vast range from Portugal and Ireland to China and Siberia. Breeding occurs in regions including Northern Africa, the Middle East, and Europe, up to Norway, Finland, and sub-Arctic Russia. Geolocator tracking indicates swifts breeding in Sweden winter in the Congo region of Africa. Migration involves spending about three to three-and-a-half months in Africa, followed by a similar period for breeding. Departure order includes unsuccessful breeders, fledglings, and sexually immature year-olds, breeding males, and finally, breeding females. Departure is influenced by light duration, starting when there is less than 17 hours of daylight. Migration routes through Central Europe involve south-by-southwest travel, with the Alps not acting as a barrier. In bad weather, swifts follow rivers for a better food supply. Two migration groups likely meet, with the western group following the Atlantic coastline of Africa and the eastern group taking a longer route over the eastern Mediterranean. In Africa, swifts turn southeast to reach winter feeding grounds in the humid savanna, benefiting from abundant insects in the Intertropical Convergence Zone. Some sexually immature swifts stay in Africa, while most fly northwards through Africa and turn east toward their destinations, utilizing low-pressure fronts during spring migrations and northeastern winds on the return trip. Central European return occurs in late April and early May, with swifts favoring lowlands and water-rich areas. Arrival dates vary based on weather conditions, impacting migration patterns from year to year.",

        
        "Image":"https://cdn.download.ams.birds.cornell.edu/api/v1/asset/44951031/1800",
        "Video" : "https://www.youtube.com/watch?v=pEmtXsW2bD8"
    },



    "Common Crane": {
        "Scientific Name": "Grus grus",
        "length" : "100-130 cm",
        "width" : "180-240 cm",
        "mass" : "3 to 6.1 kg",

        "Description": "The common crane displays sexual size dimorphism, with males being slightly larger and heavier than females. It has a slate-grey overall color, blackish forehead and lores, a bare red crown, and a white streak extending from behind the eyes to the upper back. The darkest coloration is on the back and rump, while the breast and wings are paler. Notable black markings are present on various parts, distinguishing it from similar Asian crane species. Juveniles have yellowish-brown tips on body feathers, lack the drooping wing feathers and bright neck pattern of adults, and have a fully feathered crown. Adult common cranes undergo a complete moult every two years before migration, rendering them flightless for six weeks until new feathers grow. The common crane is known for its loud trumpeting call, particularly during flight and display. The call is piercing and can be heard from a considerable distance. The species engages in a dancing display, involving leaping with uplifted wings.",

        "Location": "The common crane breeds across the Palearctic, with large populations in Russia, Finland, and Sweden. It's a rare breeder in parts of Europe, reappearing in some areas. Migration occurs from August to October in breeding areas and from late October to early December at wintering sites. Spring migration is from February to March at wintering sites and from March to May at breeding areas. Cranes winter in Portugal, Spain, northern Africa, and other locations. Some stay near breeding areas in mild winters. Migration involves staging areas from Sweden to China. The easternmost breeders winter in eastern China. Rarely seen in Japan, Korea, and western North America.",

        
        "Image":"https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Common_crane_grus_grus.jpg/1024px-Common_crane_grus_grus.jpg",
        "Video" : "https://www.youtube.com/watch?v=Yxryodcgr8s"
    },




    "Large-billed Crow": {
        "Scientific Name": "Corvus macrorhynchos",
        "length" : "46-59 cm",
        "width" : "100-130 cm",
        "mass" : "450-1000 g",

        "Description": "The overall size (length: 46-59 cm; 18-23 in). Wingspan is (100-130 cm; 39-51 in). Body proportions vary regionally. In the far northeast in Japan, the Kuriles and the Sakhalin peninsula, it is somewhat larger than the carrion crow. All taxa have a relatively long bill with the upper one quite thick and arched, making it look heavy and almost raven-like. Generally, all taxa have dark greyish plumage from the back of the head, neck, shoulders and lower body. Their wings, tail, face, and throat are glossy black. The depth of the grey shading varies across its range.",

        "Location": "The range of this species is extensive and stretches from the northeastern Asian seaboard to Afghanistan and eastern Iran in the west, through South and Southeast Asia, to the Lesser Sundas and Cambodia in the southeast. It occurs in woodland, parks and gardens, cultivated regions with at least some trees, but is a bird of more open country in the south of its range where it is not in competition with the common raven and carrion crow of the north.",

        
        "Image":"https://cdn.download.ams.birds.cornell.edu/api/v1/asset/85864191/1800",
        "Video" : "https://www.youtube.com/watch?v=276erlcjTDM"
    },




    "Common Quail": {
        "Scientific Name": "Coturnix coturnix",
        "length" : "16-18 cm",
        "width" : "32-35 cm",
        "mass" : "70-140 g",

        "Description": "The common quail is a small gallinaceous bird, measuring 16-18 cm (6½-7 in) in length, with a wingspan of 32-35 cm (12½-14 in). Its weight ranges from 70 to 140 g (2½ to 5 oz), with the highest weight occurring before migration at the end of the breeding season. The female is generally slightly heavier than the male. It has a streaked brown plumage with a white eyestripe and, in males, a white chin. The species has long wings, distinguishing it from typically short-winged gamebirds. The name 'quail' is thought to originate from Old French 'quaille' or possibly from Medieval Latin 'quaccula,' both imitative of the bird's cry. Alternatively, it may have indigenous roots in Proto-Germanic languages.",

        "Location": "This is a terrestrial species, feeding on seeds and insects on the ground. It is notoriously difficult to see, keeping hidden in crops, and reluctant to fly, preferring to creep away instead. Even when flushed, it keeps low and soon drops back into cover. Often the only indication of its presence is the distinctive 'wet-my-lips' repetitive song of the male. The call is uttered mostly in the mornings, evenings and sometimes at night. It is a strongly migratory bird, unlike most game birds. The common quail has been introduced onto the island of Mauritius on several occasions but has failed to establish itself and is now probably extinct.",

        
        "Image":"https://cdn.download.ams.birds.cornell.edu/api/v1/asset/241998281/1800",
        "Video" : "https://www.youtube.com/watch?v=lMapd0s1zt8"
    },


    "Spotted Crake": {
        "Scientific Name": "Porzana porzana",
        "length" : "19-22.5 cm",
        "width" : "37-42 cm",
        "mass" : "57-147 g",

        "Description": "At 19-22.5 cm (7.5-8.9 in) length, spotted crakes are slightly smaller than water rails, from which they are readily distinguished by the short straight bill, yellow with a red base. Adults have mainly brown upperparts and blue-grey breast, with dark barring and white spots on the flanks. They have green legs with long toes, and a short tail which is buff underneath.",

        "Location": "The spotted crake's breeding habitat is marshes and sedge beds across temperate Europe into western Asia. They nest in a dry location in marsh vegetation, laying 6-15 eggs. This species is migratory, wintering in Africa and Pakistan.",

        
        "Image":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmym_OC5NguL3jHOF7vyTltKCxA27dIx-VFj6XNbbD5YHH6ijJ",
        "Video" : "https://www.youtube.com/watch?v=_giaiLUCRe4"
    },


    "Rose-ringed Parakeet": {
        "Scientific Name": "Psittacula krameri",
        "length" : "38-42 cm",
        "width" : "15-17.5 cm",
        "mass" : "110-182 g",

        "Description": "The rose-ringed parakeet is sexually dimorphic. The adult male sports a pink and black neck ring, and the hen and immature birds of both sexes either show no neck rings, or display shadow-like pale to dark grey neck rings. Both sexes have a distinctive green colour in the wild with a red beak and blue tail,[9] and captive bred ringnecks have multiple colour mutations which include turquoise, cinnamon, olive, white, blue, violet, grey and yellow. Rose-ringed parakeets measure on average 40 cm (16 in) in length, including the tail feathers, a large portion of their total length. Their average single-wing length is about 15 to 17.5 cm (5.9 to 6.9 in). In the wild, this is a noisy species with an unmistakable squawking call. Captive individuals can be taught to speak. They are a herbivorous and non-migratory species.",

        "Location": "Since the 19th century, the rose-ringed parakeet has successfully colonised many other countries. It breeds further north than any other parrot species. It has established itself on a large scale in Germany, France, Belgium, the Netherlands, Italy, and especially the UK. See Feral Birds section below. The analyses show that the risk of parakeet establishment may rise further as a result of decreasing frost days due to global warming, rising urbanization, and rising human populations. Because of the significant separate parakeet imports in Europe, researchers are capable of investigating the widely held hypothesis of climate matching and human activity at the species level.",

        
        "Image":"https://cdn.download.ams.birds.cornell.edu/api/v1/asset/256173651/1800",
        "Video" : "https://www.youtube.com/watch?v=XeNkI16zlZc"
    },

    'Eurasian Woodcock': {
        "Scientific Name": "Scolopax rusticola",
        "length" : "33-38 cm",
        "width" : "55-65 cm",
        "mass" : "26.5 g",

        "Description": "Adults are 33-38 cm (13-15 in) in length, including the 6-8 cm (2.4-3.1 in) long straight bill, and have a 55-65 cm (22-26 in) wingspan. The Eurasian woodcock has cryptic camouflage to suit its woodland habitat, with intricately patterned reddish-brown upperparts and buff underparts. The head is barred with black, not striped like that of its close relatives, the snipe. It has large eyes located high on the sides of its head, giving it 360-degree monocular vision. The wings are rounded and the base of the bill is flesh-coloured with a dark tip. The legs vary from grey to pinkish.[7] The species is sexually dimorphic, with the male much larger than the female,[9] although the sexes cannot be separated in the field.",

        "Location": "About one-third of the Eurasian woodcock's global population breeds in Europe, with over 90 percent of Europe's population breeding in Russia and Fennoscandia. Its breeding range spans from Fennoscandia to the Mediterranean, western Europe to Russia, and includes the Canary Islands. The Azores population is genetically distinct. While northern and Asian populations migrate south, those in milder western European regions and Atlantic islands are resident. Spring migration starts in February, reaching breeding territories between March and May, influenced by weather conditions. The species has a large range, a stable population trend, and is evaluated as Least Concern. Fragmentation of woodland habitat poses a threat, along with reduced permanent grassland and intensified farming. The Eurasian woodcock prefers large, unfragmented areas of broadleaved or mixed forest with dense undergrowth. It requires varied habitats for resting, feeding, and flight within breeding territories. Winter habitats include scrubland and, in freezing conditions, intertidal mud.",

        
        "Image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQ2OZ1gqLwfaYzqjAc4HkDd3AhJbTFaFLUr0NU-NDckvUD6Qb1V",
        "Video": "https://www.youtube.com/watch?v=HvWiVaCSTCw"
    },


    'Black-winged Stilt': {
        "Scientific Name": "Himantopus himantopus",
        "length" : "33-36 cm ",
        "width" : "71-83 cm",
        "mass" : "about 160 g",

        "Description": "Adults are 33-36 cm (13-14 in) long, with long, pink legs, and a long, rather thin black bill. The birds are generally black above and white below, with a white head and neck (with a varying amount of black, species-dependent). Males have a black back, often with a greenish gloss or sheen. Females' backs have a brownish hue, contrasting with the black remiges. In populations where the top of the head is normally white (at least in winter), females tend to have less black on the head and neck the entire year-round, while males often have much more black, particularly in summer. This difference is not clear-cut, however, and males usually grow all-white head feathers in winter. Immature birds are grey, instead of black, and have a markedly sandy hue on their wings, with light feather fringes appearing as a whitish line in flight",

        "Location": "The breeding habitat of all these stilts is marshes, shallow lakes and ponds. Some populations are migratory and move to the ocean coasts in winter; those in warmer regions are generally resident or short-range vagrants. In Europe, the black-winged stilt is a regular spring overshoot vagrant north of its normal range, occasionally remaining to breed in northern European countries. ",

        
        "Image": "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/45038811/1800",
        "Video": "https://www.youtube.com/watch?v=B69b8tAzniA"
    },

    "Baillon's Crake": {
        "Scientific Name": "Zapornia pusilla",
        "length" : "16-18 cm",
        "width" : "33-37 cm",
        "mass" : "35-50 cm",

        "Description": "They are 16-18 cm (6.3-7.1 in) in length, and are similar to the only slightly larger little crake. Baillon's crake has a short straight bill, yellow or green without a red base. Adults have mainly brown upperparts with some white markings, and a blue-grey face and underparts. The rear flanks are barred black and white. They have green legs with long toes, and a short tail which is barred underneath. Immature Baillon's crakes are similar to the adults, but have extensively barred underparts. The downy chicks are black, as with all rails.",

        "Location": "Their breeding habitat is sedge beds in Europe, mainly in the east, and across the Palearctic. They used to breed in Great Britain up to the mid-19th century, but the western European population declined through drainage. There has been a recovery in north-western Europe in recent years, with the recolonisation of Germany and the Netherlands, and breeding suspected in Britain; an Irish record in 2012 was the first there since the 1850s.[2] They nest in a dry location in wet sedge bogs, laying 4-8 eggs. This species is migratory, wintering in east Africa and south Asia. It is also a resident breeder in Africa and Australasia. There is a single North American record of this species on Attu Island in September 2000.",

        
        "Image": "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/54349901/1800",
        "Video": "https://www.youtube.com/watch?v=ISVJzPi0-Ko"
    },

    'Ruddy Turnstone': {
        "Scientific Name": "Arenaria interpres",
        "length" : "22-24 cm",
        "width" : "50-57 cm",
        "mass" : "85-150 g",

        "Description": "It is a fairly small and stocky bird, 22-24 cm (8.7-9.4 in) long with a wingspan of 50-57 cm (20-22 in) and a weight of 85-150 g (3.0-5.3 oz). The dark, wedge-shaped bill is 2-2.5 cm (0.79-0.98 in) long and slightly upturned. The legs are fairly short at 3.5 cm (1.4 in) and are bright orange. In all seasons, the plumage is dominated by a harlequin-like pattern of black and white. Breeding birds have reddish-brown upper parts with black markings. The head is mainly white with black streaks on the crown and a black pattern on the face. The breast is mainly black apart from a white patch on the sides. The rest of the underparts are white. In flight it reveals a white wingbar, white patch near the base of the wing and white lower back, rump and tail with dark bands on the uppertail-coverts and near the tip of the tail. The female is slightly duller than the male and has a browner head with more streaking. Non-breeding adults are duller than breeding birds and have dark grey-brown upperparts with black mottling and a dark head with little white. Juvenile birds have a pale brown head and pale fringes to the upperpart feathers creating a scaly impression. Birds of the subspecies morinella are smaller with darker upperparts and less streaking on the crown. The ruddy turnstone has a staccato, rattling call and also a chattering alarm-call which is mainly given during the breeding season.",

        "Location": "The ruddy turnstone breeds in northern latitudes, usually no more than a few kilometres from the sea. The subspecies A. i. morinella occurs in northern Alaska and in Arctic Canada as far east as Baffin Island. A. i. interpres breeds in western Alaska, Ellesmere Island, Greenland, Norway, Denmark, Sweden, Finland, Estonia and northern Russia. It formerly bred on the Baltic coast of Germany and has possibly bred in Scotland and the Faroe Islands. In the Americas, the species winters on coastlines from Washington and Massachusetts southwards to the southern tip of South America although it is scarce in southern parts of Chile and Argentina and is only an unconfirmed vagrant in the Falkland Islands. In Europe, it winters in western regions from Iceland, Norway and Denmark southwards. Only small numbers are found on Mediterranean coasts. In Africa, it is common all the way down to South Africa with good numbers on many offshore islands. In Asia, it is widespread in the south with birds wintering as far north as southern China and Japan (mainly in the Ryukyu Islands). It occurs south to Tasmania and New Zealand and is present on many Pacific islands.[1] Some non-breeding birds remain year round in many parts of the wintering range, with some of those birds still taking on breeding plumage in the spring and summer.",

        
        "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3ZdCONla45VvyQB8S2MbPm5QE5rqpK9qduWr_cr5O_3Rn0kiJ",
        "Video": "https://www.youtube.com/watch?v=Ovv30db4mYk"
    },

    'Little Grebe': {
        "Scientific Name": "Tachybaptus ruficollis",

        "length" : "23-29 cm",
        "width" : "42 cm",
        "mass" : "140 g",

        "Description": "The little grebe is a small water bird with a pointed bill. The adult is unmistakable in summer, predominantly dark above with its rich, rufous colour neck, cheeks and flanks, and bright yellow gape. The rufous is replaced by a dirty brownish grey in non-breeding and juvenile birds. Juvenile birds have a yellow bill with a small black tip, and black and white streaks on the cheeks and sides of the neck as seen below. This yellow bill darkens as the juveniles age, eventually turning black in adulthood.In winter, its size, buff plumage, with a darker back and cap, and “powder puff” rear end enable easy identification of this species. The little grebe's breeding call, given singly or in duet, is a trilled repeated weet-weet-weet or wee-wee-wee which sounds like a horse whinnying.",

        "Location": "This bird breeds in small colonies in heavily vegetated areas of freshwater lakes across Europe, much of Asia down to New Guinea, and most of Africa. Most birds move to more open or coastal waters in winter, but it is only migratory in those parts of its range where the waters freeze. Outside of breeding season, it moves into more open water, occasionally even appearing on the coast in small bays.",

        
        "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1nJpfnlW8Vg511UscG0Eswi3VIFWY6kuJdCEvWRjwiFIeXLY-",
        "Video": "https://www.youtube.com/watch?v=wCcYq1NUnbM"
    },


     'Common Ringed Plover': {
        "Scientific Name": "Charadrius hiaticula",

        "length" : "17-19.5 cm",
        "width" : "35-41 cm",
        "mass" : "64 g",

        "Description": "Adults are 17-19.5 cm (6.7-7.7 in) in length with a 35-41 cm (14-16 in) wingspan. They have a grey-brown back and wings, a white belly, and a white breast with one black neckband. They have a brown cap, a white forehead, a black mask around the eyes and a short orange and black bill. The legs are orange and only the outer two toes are slightly webbed, unlike the slightly smaller but otherwise very similar semipalmated plover, which has all three toes slightly webbed, and also a marginally narrower breast band; it was in former times included in the present species. Juvenile ringed plovers are duller than the adults in colour, with an often incomplete grey-brown breast band, a dark bill and dull yellowish-grey legs. This species differs from the smaller little ringed plover in leg colour, the head pattern, and the lack of an obvious yellow eye-ring.",

        "Location": "The common ringed plover's breeding habitat is open ground on beaches or flats across northern Eurosiberia and in Arctic northeast Canada. Some birds breed inland, and in western Europe they nest as far south as northern France. They nest on the ground in an open area with little or no plant growth. If a potential predator approaches the nest, the adult will walk away from the scrape, calling to attract the intruder and feigning a broken wing. Once the intruder is far enough from the nest, the plover flies off. Common ringed plovers are migratory and winter in coastal areas south to Africa. In Norway, geolocators have revealed that adult breeding birds migrate to West Africa. Many birds in Great Britain and northern France are resident throughout the year.",

        
        "Image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTSFw5DttDwO1Ku31nJcR26umgiQpHuARz9ZdTWBpj2-X6DyCfh",
        "Video": "https://www.youtube.com/watch?v=PhTBiNsLKcw"
    },


    'Eurasian Coot': {
        
        "Scientific Name": "Fulica atra",

        "length" : "36-38 cm",
        "width" : "70-80 cm",
        "mass" : "750-890 g",


        "Description": "The Eurasian coot is 36-38 cm (14-15 in) in length with a wing-span of 70-80 cm (28-31 in); males weigh around 890 g (31 oz) and females 750 g (26 oz).[9] It is largely black except for the white bill and frontal shield (which gives rise to the phrase 'as bald as a coot', in use as early as 1430).[10] As a swimming species, the coot has partial webbing on its long strong toes. The sexes are similar in appearance. The juvenile is paler than the adult, has a whitish breast, and lacks the facial shield; the adult black plumage develops when about 3-4 months old, but the white shield is only fully developed at about one year old. The Eurasian coot is a noisy bird with a wide repertoire of crackling, explosive, or trumpeting calls, often given at night.",

        "Location": "The coot breeds across much of the Old World on freshwater lakes and ponds, and like its relative the common moorhen, has adapted well to living in urban environments, often being found in parks and gardens with access to water. It occurs and breeds in Europe, Asia, Australia, and Africa. The species has recently expanded its range into New Zealand. It is resident in the milder parts of its range, but migrates further south and west from much of Asia in winter as the waters freeze. It is known to occur as a vagrant in North America.",

        
        "Image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSRz91NRvrsfp0ib36OujnwjvgFK3sB7IJRkdrN7G8qIYlbUG0_",
        "Video": "https://www.youtube.com/watch?v=rm3k6Hkhzgc"
    },


     'Large-tailed Nightjar': {
        "Scientific Name": "Caprimulgus macrurus",

        "length" : "25-33 cm",
        "width" : "70-80 cm",
        "mass" : "52-59 g",

        "Description": "With pointed wings and long tails, their shape is similar to a Kestrel or Cuckoo. Their grey-brown, mottled, streaked and stripey plumage provides ideal camouflage in the daytime. They have an almost supernatural reputation thanks to their silent flight and their mythical ability to steal milk from goats.",

        "Location": "The Large-tailed Nightjar frequents open forests, second growth, woodlands, scrub and plantations, open and humid areas such as mangroves, forest edges and cultivated fields. This species can be seen from sea-level up to 2700 metres in the northern parts of the range. The elevation varies according to the location, from 460-900 metres to 1200 and 2000 or more. The Large-tailed Nightjar occurs from Asia, throughout Asia and Papua New Guinea, and N/NE Australia.",

        
        "Image": "https://singaporebirds.com/wp-content/uploads/2016/01/large-tailed-nightjar-fy7d0875-102eos7d-150315.jpg",
        "Video": "https://www.youtube.com/watch?v=rSZQVcJGh2k"
    }, 


    'Eurasian Curlew': {
        "Scientific Name": "Numenius arquata",

        "length" : "50-60 cm",
        "width" : "89-106 cm",
        "mass" : "410-1,360 g",

        "Description": "The Eurasian curlew is the largest wader in its range, at 50-60 cm (20-24 in) in length, with an 89-106 cm (35-42 in) wingspan and a body weight of 410-1,360 g (0.90-3.00 lb).[7] It is mainly greyish brown, with a white back, greyish-blue legs and a very long curved bill. Males and females look identical, but the bill is longest in the adult female. It is generally not possible to recognize the sex of a single Eurasian curlew, or even several ones, as there is much variation; telling male and female of a mated pair apart is usually possible however. The familiar call is a loud curloo-oo. The only similar species over most of the curlew's range is the Eurasian whimbrel (Numenius phaeopus). The whimbrel is smaller and has a shorter bill with a kink rather than a smooth curve. Flying curlews may also resemble bar-tailed godwits (Limosa lapponica) in their winter plumages; however, the latter have a smaller body, a slightly upturned beak, and legs that do not reach far beyond their tail tips. The Eurasian curlew's feet are longer, forming a conspicuous 'point'.",

        "Location": "The curlew exists as a migratory species over most of its range, wintering in Africa, southern Europe and south Asia. Occasionally a vagrant individual reaches places far from its normal range, such as Nova Scotia[8] and the Marianas.[9][10] It is present all year in the milder climates of Ireland and the United Kingdom and its adjacent European coasts. Reclamation and drainage of marshy fields and moorland, and afforestation of the latter, have led to local decreases, while conversion of forest to grassland in some parts of Scandinavia has led to increases there.",

        
        "Image": "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/255217891/1800",
        "Video": "https://www.youtube.com/watch?v=Fl4ybB7MEZ8"
    },


    'Common Tailorbird': {
        "Scientific Name": "Orthotomus sutorius",

        "length" : "10-14 cm",
        "width" : "5-5.5 cm",
        "mass" : "6-10 g",

        "Description": "The common tailorbird is a brightly coloured bird, with bright green upperparts and creamy underparts. They range in size from 10 to 14 centimetres (3.9 to 5.5 in) and weigh 6 to 10 grams (0.21 to 0.35 oz). They have short rounded wings, a long tail, strong legs and a sharp bill with curved tip to the upper mandible. They are wren-like with a long upright tail that is often moved around. The crown is rufous and the upperparts are predominantly olive green. The underside is creamy white. The sexes are identical, except that the male has long central tail feathers in the breeding season, although the reliability of sexing data accompanying museum specimens used in determining this sexual dimorphism has been questioned. Young birds are duller. When calling, the dark patches on the sides of the neck become visible. These are due to the dark pigmented and bare skin that are present in both sexes and sometimes give the appearance of a dark gorget.",

        "Location": "Like most warblers, the common tailorbird is insectivorous. The song is a loud cheeup-cheeup-cheeup with variations across the populations. The disyllabic calls are repeated often.[7] Tailorbirds are found singly or in pairs, usually low in the undergrowth or trees, sometimes hopping on the ground. They forage for insects and have been known to feed on a range of beetles and bugs. They are attracted to insects at flowers and are known to favour the inflorescences of mango. They also visit flowers such as those of Bombax, Salmalia for nectar and are sometimes covered in pollen, giving them a golden-headed appearance. The birds roost alone during the non-breeding season but may roost side-by-side during the breeding season, sometimes with the newly fledged juvenile sandwiched between the adults. The roost sites chosen are thin twigs on trees with cover above them and were often close to human habitation and lights.",

        
        "Image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTiM0eGOdA0wF9kjMR5eDxMb-A8d5O6jCvgWIXo-_bA1BTQ3XFm",
        "Video": "https://www.youtube.com/watch?v=130PnybCnIM"
    },


    'Great Crested Grebe': {
        "Scientific Name": "Podiceps cristatus",

        "length" : "46-51 cm",
        "width" : "59-73 cm",
        "mass" : "0.9-1.5 kg",

        "Description": "The great crested grebe is the largest member of the grebe family found in the Old World, with some larger species residing in the Americas. They measure 46-51 cm (18-20 in) long with a 59-73 cm (23-29 in) wingspan and weigh 0.9 to 1.5 kg (2.0 to 3.3 lb). It is an excellent swimmer and diver, and pursues its fish prey underwater. The adults are unmistakable in summer with head and neck decorations. In winter, this is whiter than most grebes, with white above the eye, and a pink bill.The call is a loud barking rah-rah-rah. They can also produce a clicking kek call, and deep growls.[10]Juveniles are recognisable by their plumage, with their heads featuring alternating black and white stripes. They lose these markings when they become adults.",

        "Location": "The great crested grebe breeds in vegetated areas of freshwater lakes. The subspecies P. c. cristatus is found across Europe and east across the Palearctic. It is resident in the milder west of its range, but migrates from the colder regions. It winters on freshwater lakes and reservoirs or the coast. The African subspecies P. c. infuscatus and the Australasian subspecies P. c. australis are mainly sedentary.",

        
        "Image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQM9JOIIFmIORmihcuHGyM8Nm2zYLcrrQiGHo0tGIL2s4V3TnDL",
        "Video": "https://www.youtube.com/watch?v=ZbRrxw-H6xA"
    },


    'Common Cuckoo': {
        "Scientific Name": "Cuculus canorus",

        "length" : "32-34 cm",
        "width" : "55-60 cm",
        "mass" : "110-130 g",


        "Description": "The common cuckoo is a slender bird measuring 32-34 cm in length, with a tail of 13-15 cm and a wingspan of 55-60 cm. Adult males are slate-grey, while adult females can be grey or rufous-brown. Juveniles and those in their first autumn exhibit variable plumage, with some having barred chestnut-brown upperparts. Identification features include a white nape patch and white feather fringes. During the breeding season, males have a distinct appearance with grey throat extending down to barred underparts. Common cuckoos undergo two molts a year, and males weigh around 130 grams, while females weigh about 110 grams. They resemble the Oriental cuckoo, but the latter is slightly shorter-winged on average.",

        "Location": "Essentially a bird of open land, the common cuckoo is a widespread summer migrant to Europe and Asia, and winters in Africa. Birds arrive in Europe in April and leave in September. The common cuckoo has also occurred as a vagrant in countries including Barbados, the United States, Greenland, the Faroe Islands, Iceland, Indonesia, Palau, Seychelles, Taiwan and China. Between 1995 and 2015, the distribution of cuckoos within the UK has shifted towards the north, with a decline by 69 percent in England but an increase by 33 percent in Scotland.",

        
        "Image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTdklBezemVQ4ADsWtpKY-3jE125kHtkC8ZKuT3yRvWOixZ0Jut",
        "Video": "https://www.youtube.com/watch?v=ZXdZZAf0AU0"
    },


    'Eurasian Whimbrel': {
        "Scientific Name": "Numenius phaeopus",

        "length" : "37-47 cm",
        "width" : "75-90 cm",
        "mass" : "270-493 g",


        "Description": "The Eurasian whimbrel is a fairly large wader, though mid-sized as a member of the curlew genus. It is 37-47 cm (15-19 in) in length, 75-90 cm (30-35 in) in wingspan, and 270-493 g (9.5-17.4 oz; 0.595-1.087 lb) in weight.[14] It is mainly greyish brown, with a white back and rump (subspecies N. p. phaeopus and N. p. alboaxillaris only), and a long curved beak with a kink rather than a smooth curve. The usual call is a rippling whistle, prolonged into a trill for the song. The only similar common species over most of this bird's range are larger curlews. The whimbrel is smaller, has a shorter, decurved bill and has a central crown stripe and strong supercilia.",

        "Location": "The whimbrel is a migratory bird wintering on coasts in Africa, and South Asia into Australasia. It is also a coastal bird during migration.[15] It is fairly gregarious outside the breeding season. It is found in Ireland and the United Kingdom, and it breeds in Scotland, particularly around Shetland, Orkney, the Outer Hebrides as well as the mainland at Sutherland and Caithness.",

        

        "Image": "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSFYVq_bO5LMZ4xuqtIqNioaZzF9BXgJm8mGBs25JgZ7W8dD9qO",
        "Video": "https://www.youtube.com/watch?v=z1JAP1Y-StQ"
    },


    'Common Sandpiper': {
        "Scientific Name": "Actitis hypoleucos",

        "length" : "18-20 cm",
        "width" : "32-35 cm",
        "mass" : "40 g",


        "Description": "The adult is 18-20 cm (7.1-7.9 in) long with a 32-35 cm (13-14 in) wingspan. It has greyish-brown upperparts, white underparts, short dark-yellowish legs and feet, and a bill with a pale base and dark tip. In winter plumage, they are duller and have more conspicuous barring on the wings, though this is still only visible at close range. Juveniles are more heavily barred above and have buff edges to the wing feathers. This species is very similar to the slightly larger spotted sandpiper (A. macularia) in non-breeding plumage. But its darker legs and feet and the crisper wing pattern (visible in flight) tend to give it away, and of course they are only rarely found in the same location.",

        "Location": "The common sandpiper breeds across most of temperate and subtropical Europe and Asia, and migrates to Africa, southern Asia and Australia in winter. The eastern edge of its migration route passes by Palau in Micronesia, where hundreds of birds may gather for a stop-over. They depart the Palau region for their breeding quarters around the last week of April to the first week of May.",

        
        "Image": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Actitis_hypoleucos_-_Laem_Pak_Bia.jpg",
        "Video": "https://www.youtube.com/watch?v=cRC0JjJit08"
    },



   

}

def audio_to_base64(file_path):
    with open(file_path, 'rb') as audio_file:
        audio_content = audio_file.read()
        encoded_audio = base64.b64encode(audio_content).decode('utf-8')
        return encoded_audio




def encode_image(url):
    response = urllib.request.urlopen(url)
    image_bytes = BytesIO(response.read())
    encoded_image = base64.b64encode(image_bytes.getvalue()).decode('utf-8')

    return encoded_image


# Assuming your FastAPI server is running at http://localhost:8000
selected_audio_folder = "selected_audios"

url = "http://localhost:8000/add_bird"

for bird_name, bird_info in bird_info_data.items():
    
    response = requests.get(f"http://localhost:8000/get_bird/{bird_name}")

    if response.status_code == 404:
        image_url = bird_info["Image"]
        image_encode = encode_image(image_url)

        response = requests.post(url, json={
                "name": bird_name,
                "length": bird_info["length"],
                "wingspan": bird_info["width"],
                "mass": bird_info["mass"],
                "scientificName": bird_info["Scientific Name"],
                "description": bird_info["Description"],
                "location": bird_info["Location"],
                # "audio": audio_encode,
                "imageUri": image_encode,
                "video": bird_info["Video"]
            })

        
    elif response.status_code == 200:
        print(f"Data for {bird_name} already exists in the database.")
    else:
        print(f"Unexpected response status code for {bird_name}: {response.status_code}")