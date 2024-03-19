import os
import eyed3
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC

def get_mp3_files(directory):
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

def set_album_info(mp3_file, album, cover_artist):
    audiofile = eyed3.load(mp3_file)
    if audiofile.tag is None:
        audiofile.initTag()
    audiofile.tag.album = album
    audiofile.tag.artist = cover_artist
    audiofile.tag.save()

def add_album_cover(mp3_file, album_cover):
    audio = MP3(mp3_file, ID3=ID3)
    audio.tags.add(
        APIC(
            encoding=3,
            mime="image/png",
            type=3,
            desc='Cover',
            data=open(album_cover, mode='rb').read()
        )
    )
    
def main(directory, album, cover_artist):
    mp3_files = get_mp3_files(directory)
    album_cover = os.path.join(directory, "cover.png")
    for mp3_file in mp3_files:
        set_album_info(mp3_file, album, cover_artist)
        add_album_cover(mp3_file, album_cover)
        print("Added album cover to " + mp3_file)
        
if __name__ == "__main__":
    directory = input("Enter the directory of the mp3 files (it will be the album name too): ")
    cover_artist = input("Enter the cover artist name: ")
    main(directory, directory, cover_artist)