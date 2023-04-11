# Projects
Two people in a group, one is sender, another is receiver. To make the project easy, using symmetric key on both sides.

Sender: generator a random number, then encrypt the random number by a secret key with message digest together send to receiver.

Receiver: decrypt the received message and generate an new message digest, and compare with original one to make sure there was no issues.

You do need to send multiple times to make sure it works.

You can build the network structure by yourself or you can rely on open source.

Each group does need to present the project to me on Week14 class.
Notes: Please submit your project on LiveText as well.
