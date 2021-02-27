class Album:

    def __init__(self, name, *args) -> None:
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if self.published:
            return "Cannot add songs. Album is published."
        elif song in self.songs:
            return "Song is already in the album."
        elif song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot add songs. Album is published."
        elif song_name not in map(lambda s: s.name, self.songs):
            return "Song is not in the album."

        current_song = [s for s in self.songs if s.name == song_name][0]
        self.songs.remove(current_song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        for s in self.songs:
            result += f"== {s.get_info()}\n"

        return result


