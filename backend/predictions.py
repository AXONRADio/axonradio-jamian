import os, shutil
import youtube_crawler as yc
import quick_test as qt
from time import gmtime, strftime
from flask_pymongo import PyMongo
from pymongo import MongoClient

client = MongoClient()
db = client.song_db

def jazz(post):
    jazz_songs = db.jazz
    return jazz_songs.insert_one(post).inserted_id
def rock(post):
    rock_songs = db.rock
    return rock_songs.insert_one(post).inserted_id
def blues(post):
    blues_songs = db.blues
    return blues_songs.insert_one(post).inserted_id
def pop(post):
    pop_songs = db.pop
    return pop_songs.insert_one(post).inserted_id
def reggae(post):
    reggae_songs = db.reggae
    return reggae_songs.insert_one(post).inserted_id
def hiphop(post):
    hiphop_songs = db.hiphop
    return hiphop_songs.insert_one(post).inserted_id
def disco(post):
    disco_songs = db.disco
    return disco_songs.insert_one(post).inserted_id
def country(post):
    country_songs = db.country
    return country_songs.insert_one(post).inserted_id
def classical(post):
    classical_songs = db.classical
    return classical_songs.insert_one(post).inserted_id
def metal(post):
    metal_songs = db.metal
    return metal_songs.insert_one(post).inserted_id


def putInDb(arg, post):
    switcher = {
        'jazz': jazz,
        'rock': rock,
        'blues': blues,
        'pop': pop,
        'reggae': reggae,
        'hiphop': hiphop,
        'disco': disco,
        'country': country,
        'classical': classical,
        'metal': metal
    }
    func = switcher.get(arg, lambda:'invalid genre')
    func(post)

#def classify_songs():
def get_genre(vid_id = None):
    #remove songs from the music directory
    path = './music'
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

    #download our random youtube song
    youtubeURL = 'https://www.youtube.com/watch'
    if(vid_id == None):
        vidID = yc.youtube_search()
    else:
        vidID = vid_id
    try:
        url = '?v='.join([youtubeURL, vidID])
    except TypeError as e:
        print(e)

    try:
        yc.download_song(url)
    except TypeError as e:
        print(e)

    #analyze our songs genre
    try:
        genre, song_name, mean = qt.run()
    except Exception as e:
        print(e)


    #put song data in database
    time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    post = {"name": song_name[:-4],
            "genre": genre,
            "url": url,
            "vidID": vidID,
            "date": time,
            "mean": mean,
            "score": 0}

    #print("url: {} \ngenre: {} \ntime entered: {} \n".format(url, genre, time))
    if(vid_id == None):
        putInDb(genre, post)
    else:
        return post

if __name__ == '__main__':
    #while(True):
    try:
        get_genre("BqnG_Ei35JE")
    except Exception as e:
        print(e)
        #continue
