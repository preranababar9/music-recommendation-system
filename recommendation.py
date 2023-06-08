from similarity import *
from flet import *

###function for recommendation###
def recommend(song_title, page):
    # page.scroll = "always"
    
    song_index = data[data['track_name'] == song_title].index[0]

    ###printing song name and singer name from the input data###
    ###print(data.iloc[song_index].track_artist ," - ",  data.iloc[song_index].track_name)


    if song_index >= 1 and song_index <= 15978:
        distances = similarity[song_index]

        songs_list = sorted(list(enumerate(distances)), reverse=True, key=(lambda x:x[1]))[1:7]
        print(len(songs_list))
        print(songs_list)
        print("Recommended Songs are : ")
        
        for i in songs_list :
            # yellow = '#FFFF00'
            blue = '#F0F8FF',
            a = {
                    "track_artist" : data.iloc[i[0]].track_artist,  
                    "track_name" :  data.iloc[i[0]].track_name,
                    "similarity_score" : i[1]
                }
            aa = a.get("track_artist")
            ab = a.get("track_name")
            # similar = a.get("similarity_score")
            #print("similarity score : ", i[1])
            print(a)
            song_container = Container(
                #Text(value = a.get('track_artist'), color=colors.WHITE),
                Text(value="Artist = " + aa+"\nSong = "+ab , color=colors.WHITE),
                width=400,
                height=60,
                bgcolor=colors.BLUE_GREY,
                #padding=15 
            )
            song_container.border_radius = border_radius.all(5)
            #song_container.alignment = alignment.left
            song_container.margin = margin.all(5)
            
            page.add(song_container)
            page.scroll = "always"
            page.update()
            #page.update()
            #print(song_container)
    else:
        print("er1")
        #txt_name.error_text = "Sorry, Song not in my database!"
