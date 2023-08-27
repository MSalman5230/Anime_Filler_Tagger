# Anime_Filler_Marker
Simple py Script to Automatically tag an anime episode as Filler or not.

* Uses www.animefillerlist.com for Episodes metadata.

* Change the .py to configure
```python
LastEp = 892 # from where the script will scan
loc = "//NAS/.Anime$/One Piece/Episodes/9.Yonko Saga" # location of your episodes
showname = "One Piece" # Anime Name
url = "https://www.animefillerlist.com/shows/one-piece" # animefillerlist url for that show
default_quality=" [720p]" # if quality is not in filename, this quality is tagged in the filename
```

* Example of Rename:
```bash
[Judas] One Piece - 782.mkv -> One Piece - 782 [720p] [Filler].mkv
[Anime Time] One Piece - 1073 [1080p][HEVC 10bit x265][AAC][Multi Sub].mkv -> One Piece - 1070 [1080p].mkv
 ```



