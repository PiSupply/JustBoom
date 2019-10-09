# JustBoom Rest API

## Playback commands

JustBoom Player has the ability to make REST API calls. All API calls will look like the following:

```
justboom.local/api/v1/commands?cmd=
```

example:
```
justboom.local/api/v1/commands/?cmd=play
```
Available commands:

**Play**
```
justboom.local/api/v1/commands/?cmd=play&N=2
```
Where `N` is optional and is the ordinal number of the track in the queue you wish to start to play from. The above call will play the third track in the queue.

**Toggle between play and pause**
```
justboom.local/api/v1/commands/?cmd=toggle
```
**Stop**
```
justboom.local/api/v1/commands/?cmd=stop
```
**Pause**
```
justboom.local/api/v1/commands/?cmd=pause
```
**Previous**
```
justboom.local/api/v1/commands/?cmd=prev
```
**Next**
```
justboom.local/api/v1/commands/?cmd=next
```
**Volume**
```
justboom.local/api/v1/commands/?cmd=volume&volume=80
```
Where `volume=` can be: 0-100, mute, unmute, plus, minus (plus and minus will increase/decrease as per parameter one click volume steps)

## Music Library
Get the current state of the player
```
justboom.local/api/v1/getstate
```
**Response**
```
{"status":"play","position":0,"title":"La guerra è finita","artist":"Baustelle","album":"La malavita","albumart":"/albumart?web=Baustelle/La%20malavita/extralarge&path=%2FNAS%2FMusic%2FBaustelle%20-%20La%20Malavita","uri":"mnt/NAS/Music/Baustelle - La Malavita/02 la guerra è finita.mp3","trackType":"mp3","seek":4224,"duration":262,"samplerate":"44.1 KHz","bitdepth":"24 bit","channels":2,"random":null,"repeat":null,"repeatSingle":false,"consume":false,"volume":41,"mute":false,"stream":"mp3","updatedb":false,"volatile":false,"service":"mpd"}
```
**Clear the queue**
```
justboom.local/api/v1/commands/?cmd=clearQueue
```
**List Playlists**
```
justboom.local/api/v1/listplaylists
```
**Play a Playlist**
```
justboom.local/api/v1/commands/?cmd=playplaylist&name=Rock
```
Where `name` is the name of the playlist to play

**Repeat a track**
```
justboom.local/api/v1/commands/?cmd=repeat&key
```
Where `key` is true or false

**Random** Makes the order in which tracks are played random
```
justboom.local/api/v1/commands/?cmd=random&key
```
Where `key` is true or false
