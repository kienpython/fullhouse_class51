class Playlist:
    def __init__(self, songs):
        self.songs = list(songs)

    def __len__(self):                 # len(p)
        return len(self.songs)

    def __getitem__(self, idx):            # p[idx]
        return self.songs[idx]

    def __setitem__(self, idx, val):       # p[idx] = val
        self.songs[idx] = val

    def __contains__(self, song):           # song in p
        return song in self.songs

    def __iter__(self):                 # for s in p
        for s in self.songs:
            yield s

p = Playlist(['A', 'B', 'C'])
print(len(p), p[1], 'C' in p)   # 3 B True
p[1] = 'X'
print(list(p)) 