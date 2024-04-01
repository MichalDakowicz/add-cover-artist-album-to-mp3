import os
import eyed3

def get_mp3_files(directory):
    mp3_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.mp3'):
                mp3_files.append(os.path.join(root, file))
    return mp3_files

def set_album_info(mp3_file, album, cover_artist):
    audiofile = eyed3.load(mp3_file)
    if audiofile is not None:
        if audiofile.tag is None:
            audiofile.initTag()
        audiofile.tag.album = album
        audiofile.tag.artist = cover_artist
        audiofile.tag.save()
    else:
        print(f"Unable to load {mp3_file} as an audio file")

def add_album_cover(mp3_file, album_cover):
    audiofile = eyed3.load(mp3_file)
    if audiofile is not None:
        if audiofile.tag is None:
            audiofile.initTag()
        audiofile.tag.images.set(3, open(album_cover, 'rb').read(), 'image/png')
        audiofile.tag.save()
    else:
        print(f"Unable to load {mp3_file} as an audio file")

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