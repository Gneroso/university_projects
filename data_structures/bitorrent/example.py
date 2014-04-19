from client import Client

client = Client()
client.torrents = "examples/test.torrent"
client.download("examples/test.torrent")
