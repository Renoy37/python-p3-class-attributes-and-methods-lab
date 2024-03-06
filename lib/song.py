class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre, count=1):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count([genre], count)
        self.add_to_artist_count([artist], count)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genres, count):
        for genre in genres:
            if genre in cls.genre_count:
                cls.genre_count[genre] += count
            else:
                cls.genre_count[genre] = count

    @classmethod
    def add_to_artist_count(cls, artists, count):
        for artist in artists:
            if artist in cls.artist_count:
                cls.artist_count[artist] += count
            else:
                cls.artist_count[artist] = count
