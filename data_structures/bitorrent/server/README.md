Tracker
=======

In order to implement bittorent protocol from scratch, I want a fresh new
tracker (or two).

TCP
===
The tracker is an HTTP/HTTPS service which responds to HTTP GET requests. The
requests include metrics from clients that help the tracker keep overall
statistics about the torrent. The response includes a peer list that helps the
client participate in the torrent. The base URL consists of the "announce URL"
as defined in the metainfo (.torrent) file. The parameters are then added to
this URL, using standard CGI methods (i.e. a '?' after the announce URL,
followed by 'param=value' sequences separated by '&').
Note that all binary data in the URL (particularly info_hash and peer_id) must
be properly escaped. This means any byte not in the set 0-9, a-z, A-Z, '.', '-',
'_' and '~', must be encoded using the "%nn" format, where nn is the hexadecimal
value of the byte. (See RFC1738 for details.)
For a 20-byte hash of
\x12\x34\x56\x78\x9a\xbc\xde\xf1\x23\x45\x67\x89\xab\xcd\xef\x12\x34\x56\x78\x9a,
The right encoded form is %124Vx%9A%BC%DE%F1%23Eg%89%AB%CD%EF%124Vx%9A

### Tracker Request Parameters
The parameters used in the client->tracker GET request are as follows:
 * info_hash: urlencoded 20-byte SHA1 hash of the value of the info key from the
Metainfo file. Note that the value will be a bencoded dictionary, given the
definition of the info key above.
 * peer_id: urlencoded 20-byte string used as a unique ID for the client, generated
by the client at startup. This is allowed to be any value, and may be binary
data. There are currently no guidelines for generating this peer ID. However,
one may rightly presume that it must at least be unique for your local machine,
thus should probably incorporate things like process ID and perhaps a timestamp
recorded at startup. See peer_id below for common client encodings of this
field.
 * port: The port number that the client is listening on. Ports reserved for
BitTorrent are typically 6881-6889. Clients may choose to give up if it cannot
establish a port within this range.
 * uploaded: The total amount uploaded (since the client sent the 'started' event
to the tracker) in base ten ASCII. While not explicitly stated in the official
specification, the concensus is that this should be the total number of bytes
uploaded.
 * downloaded: The total amount downloaded (since the client sent the 'started'
event to the tracker) in base ten ASCII. While not explicitly stated in the
official specification, the consensus is that this should be the total number of
bytes downloaded.
 * left: The number of bytes this client still has to download in base ten ASCII.
Clarification: The number of bytes needed to download to be 100% complete and
get all the included files in the torrent.
 * compact: Setting this to 1 indicates that the client accepts a compact response.
The peers list is replaced by a peers string with 6 bytes per peer. The first
four bytes are the host (in network byte order), the last two bytes are the port
(again in network byte order). It should be noted that some trackers only
support compact responses (for saving bandwidth) and either refuse requests
without "compact=1" or simply send a compact response unless the request
contains "compact=0" (in which case they will refuse the request.)
 * no_peer_id: Indicates that the tracker can omit peer id field in peers
dictionary. This option is ignored if compact is enabled.
 * event: If specified, must be one of started, completed, stopped, (or empty which
is the same as not being specified). If not specified, then this request is one
performed at regular intervals.
   * started: The first request to the tracker must include the event key with this
value.
   * stopped: Must be sent to the tracker if the client is shutting down gracefully.
completed: Must be sent to the tracker when the download completes. However,
must not be sent if the download was already 100% complete when the client
   * started. Presumably, this is to allow the tracker to increment the "completed
downloads" metric based solely on this event.
 * ip: Optional. The true IP address of the client machine, in dotted quad format
or rfc3513 defined hexed IPv6 address. Notes: In general this parameter is not
necessary as the address of the client can be determined from the IP address
from which the HTTP request came. The parameter is only needed in the case where
the IP address that the request came in on is not the IP address of the client.
This happens if the client is communicating to the tracker through a proxy (or
a transparent web proxy/cache.) It also is necessary when both the client and
the tracker are on the same local side of a NAT gateway. The reason for this is
that otherwise the tracker would give out the internal (RFC1918) address of the
client, which is not routable. Therefore the client must explicitly state its
(external, routable) IP address to be given out to external peers. Various
trackers treat this parameter differently. Some only honor it only if the IP
address that the request came in on is in RFC1918 space. Others honor it
unconditionally, while others ignore it completely. In case of IPv6 address
(e.g.: 2001:db8:1:2::100) it indicates only that client can communicate via
IPv6.
 * numwant: Optional. Number of peers that the client would like to receive from
the tracker. This value is permitted to be zero. If omitted, typically defaults
to 50 peers.
 * key: Optional. An additional client identification mechanism that is not shared
with any peers. It is intended to allow a client to prove their identity should
their IP address change.
 * trackerid: Optional. If a previous announce contained a tracker id, it should be
set here.

###Tracker Response
The tracker responds with "text/plain" document consisting of a bencoded
dictionary with the following keys:
 * failure reason: If present, then no other keys may be present. The value is
a human-readable error message as to why the request failed (string).
 * warning message: (new, optional) Similar to failure reason, but the response
still gets processed normally. The warning message is shown just like an error.
 * interval: Interval in seconds that the client should wait between sending
regular requests to the tracker
 * min interval: (optional) Minimum announce interval. If present clients must not
reannounce more frequently than this.
 * tracker id: A string that the client should send back on its next announcements.
If absent and a previous announce sent a tracker id, do not discard the old
value; keep using it.
 * complete: number of peers with the entire file, i.e. seeders (integer)
 * incomplete: number of non-seeder peers, aka "leechers" (integer)
 * peers: (dictionary model) The value is a list of dictionaries, each with the
following keys:
   * peer id: peer's self-selected ID, as described above for the tracker request
(string)
   * ip: peer's IP address either IPv6 (hexed) or IPv4 (dotted quad) or DNS name
(string)
   * port: peer's port number (integer)
 * peers: (binary model) Instead of using the dictionary model described above, the
peers value may be a string consisting of multiples of 6 bytes. First 4 bytes
are the IP address and last 2 bytes are the port number. All in network (big
endian) notation.
As mentioned above, the list of peers is length 50 by default. If there are
fewer peers in the torrent, then the list will be smaller. Otherwise, the
tracker randomly selects peers to include in the response. The tracker may
choose to implement a more intelligent mechanism for peer selection when
responding to a request. For instance, reporting seeds to other seeders could be
avoided.
Clients may send a request to the tracker more often than the specified
interval, if an event occurs (i.e. stopped or completed) or if the client needs
to learn about more peers. However, it is considered bad practice to "hammer" on
a tracker to get multiple peers. If a client wants a large peer list in the
response, then it should specify the numwant parameter.
Implementer's Note: Even 30 peers is plenty, the official client version 3 in
fact only actively forms new connections if it has less than 30 peers and will
refuse connections if it has 55. This value is important to performance. When
a new piece has completed download, HAVE messages (see below) will need to be
sent to most active peers. As a result the cost of broadcast traffic grows in
direct proportion to the number of peers. Above 25, new peers are highly
unlikely to increase download speed. UI designers are strongly advised to make
this obscure and hard to change as it is very rare to be useful to do so.

UDP
===

All values are send in network byte order (big endian). Do not expect packets
to be exactly of a certain size. Future extensions could increase the size of
 packets.

Before announcing or scraping, you have to obtain a connection ID.

  1. Choose a random transaction ID.
  2. Fill the connect request structure.
  3. Send the packet.

connect request:
```
Offset  Size            Name            Value
0       64-bit integer  connection_id   0x41727101980
8       32-bit integer  action          0 // connect
12      32-bit integer  transaction_id
16
```
  1. Receive the packet.
  2. Check whether the packet is at least 16 bytes.
  3. Check whether the transaction ID is equal to the one you chose.
  4. Check whether the action is connect.
  5. Store the connection ID for future use.

connect response:
```
Offset  Size            Name            Value
0       32-bit integer  action          0 // connect
4       32-bit integer  transaction_id
8       64-bit integer  connection_id
16
```
  1. Choose a random transaction ID.
  2. Fill the announce request structure.
  3. Send the packet.

announce request:
```
Offset  Size    Name    Value
0       64-bit integer  connection_id
8       32-bit integer  action          1 // announce
12      32-bit integer  transaction_id
16      20-byte string  info_hash
36      20-byte string  peer_id
56      64-bit integer  downloaded
64      64-bit integer  left
72      64-bit integer  uploaded
80      32-bit integer  event           0 // 0: none; 1: completed; 2: started; 3: stopped
84      32-bit integer  IP address      0 // default
88      32-bit integer  key
92      32-bit integer  num_want        -1 // default
96      16-bit integer  port
98
```
  1. Receive the packet.
  2. Check whether the packet is at least 20 bytes.
  3. Check whether the transaction ID is equal to the one you chose.
  4. Check whether the action is announce.
  5. Do not announce again until interval seconds have passed or an event has occurred.

announce response:
```
Offset      Size            Name            Value
0           32-bit integer  action          1 // announce
4           32-bit integer  transaction_id
8           32-bit integer  interval
12          32-bit integer  leechers
16          32-bit integer  seeders
20 + 6 * n  32-bit integer  IP address
24 + 6 * n  16-bit integer  TCP port
20 + 6 * N
```

Up to about 74 torrents can be scraped at once. A full scrape can't be done with this protocol.

  1. Choose a random transaction ID.
  2. Fill the scrape request structure.
  3. Send the packet.

scrape request:
```
Offset          Size            Name            Value
0               64-bit integer  connection_id
8               32-bit integer  action          2 // scrape
12              32-bit integer  transaction_id
16 + 20 * n     20-byte string  info_hash
16 + 20 * N
```
  1. Receive the packet.
  2. Check whether the packet is at least 8 bytes.
  3. Check whether the transaction ID is equal to the one you chose.
  4. Check whether the action is scrape.

scrape response:
```
Offset      Size            Name            Value
0           32-bit integer  action          2 // scrape
4           32-bit integer  transaction_id
8 + 12 * n  32-bit integer  seeders
12 + 12 * n 32-bit integer  completed
16 + 12 * n 32-bit integer  leechers
8 + 12 * N
```
If the tracker encounters an error, it might send an error packet.

  1. Receive the packet.
  2. Check whether the packet is at least 8 bytes.
  3. Check whether the transaction ID is equal to the one you chose.
error response:
```
Offset  Size            Name            Value
0       32-bit integer  action          3 // error
4       32-bit integer  transaction_id
8       string  message
```
