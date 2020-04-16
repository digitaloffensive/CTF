#used for a ctf to decrypt the hex in the debug

import struct

h1 = struct.pack("<Q", 0x594234427b425448)
h2 = struct.pack("<Q",0x3448545f5633525f)
h3 = struct.pack("<Q",0x455f5354)
h4 = struct.pack("<Q",0x7d5a)
print (h1+h2+h3+h4)

FLag will print
