from client import Client

client = Client()

# put for download another file
client.torrents = "examples/test.torrent"
# start to download file
client.download("examples/test.torrent")
