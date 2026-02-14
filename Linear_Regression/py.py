from pytube import Playlist

url = "YOUR_PLAYLIST_URL"
pl = Playlist(url)

for video in pl.videos:
    print("Title:", video.title)
    print("URL:", video.watch_url)
    print("Length (s):", video.length)
    print("---")
