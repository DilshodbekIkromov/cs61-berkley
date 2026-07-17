class Artist:
    def __init__(self, name: str):
        """
        >>> taylor = Artist('Taylor Swift')
        >>> taylor.name
        'Taylor Swift'
        >>> taylor.albums
        []
        >>> taylor.followers
        0
        """
        "YOUR CODE HERE"
        self.name = name
        self.albums = []
        self.followers = 0 

class User:
    def __init__(self, name: str):
        """
        >>> rebecca = User('Rebecca')
        >>> rebecca.name
        'Rebecca'
        >>> rebecca.liked_songs is rebecca.playlists[0]
        True
        >>> len(rebecca.playlists)
        1
        >>> rebecca.following
        []
        >>> taylor = Artist('Taylor Swift')
        >>> rebecca.follow(taylor)
        >>> len(rebecca.following)
        1
        >>> rebecca.following[0] is taylor
        True
        >>> taylor.followers
        1
        """
        "YOUR CODE HERE"
        self.name = name 
        self.following = []
        self.liked_songs = []
        self.playlists = [self.liked_songs]
        def following(self, artist:Artist ):
            self.following.append(artist)
            artist.followers +=1
             
            



taylor = Artist('Taylor Swift')

print(taylor.followers)

