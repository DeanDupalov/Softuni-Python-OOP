def play_instrument(cls):
    return cls.play()


class Guitar:
    def play(self):
        print("playing the guitar")


guitar = Guitar()
play_instrument(guitar)


class Piano:
    def play(self):
        print("playing the piano")


piano = Piano()
play_instrument(piano)
