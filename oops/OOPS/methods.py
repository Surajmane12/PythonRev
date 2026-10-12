class PlayList:

    def __init__(self,name):
        self.name=name
        self.songs=[]
    
    def addSong(self,song):
        self.songs.append(song)
    
    def delSong(self,song):
        if song in self.songs:
            self.songs.remove(song)
        else:
            print("No Song Found!!")
    
    def showSongs(self):
        for ind,song in enumerate(self.songs):
            print(f"{ind} : {song}")

myplayList = PlayList("Favorites")
myplayList.addSong("Pretty Littile Baby!!")
myplayList.addSong("Broken Angel")
myplayList.addSong("Cherry Cherry Lady")

myplayList.delSong("Broken Angel")
myplayList.showSongs()