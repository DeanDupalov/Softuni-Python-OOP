from project.song import Song
from project.album import Album


class Band:
    name: str

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name not in map(lambda a: a.name, self.albums):
            return f"Album {album_name} is not found."

        current_album = [a for a in self.albums if a.name == album_name][0]
        if current_album.published:
            return "Album has been published. It cannot be removed."

        self.albums.remove(current_album)
        return f"Album {album_name} has been removed."

    def details(self):
        result = f"Band {self.name}\n"
        for al in self.albums:
            result += al.details() + "\n"

        return result


# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())
# print(album.publish())
# band = Band("Manuel")
# print(band.add_album(album))
# print(band.remove_album("Initial D"))
# print(band.details())
