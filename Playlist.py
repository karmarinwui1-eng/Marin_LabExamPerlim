class Song:
    def __init__(self, songId, songTitle, artist, duration):    #this where we store the attritudes which are empty
        self.songId = songId                                    #nererecevice ng parameter natin na init
        self.songTitle = songTitle                              #allows for us to pass value inside of them and reuse them many things.
        self.artist = artist
        self.duration = duration


class Node:                        #this class points to the next node
    def __init__(self, song):      #which is empty
        self.song = song
        self.next = None


class LinkedList:
    def __init__(self):            #by creating this class we, it will help keep track of the first node. and currently it is empty.
        self.head = None           
        self.count = 0


    def insertFirst(self, song):
        new_node = Node(song)      #this the part where we first do, an insert. by calling from the node

        new_node.next = self.head   #head---->node ito yung visual
        self.head = new_node        #now node is like pointing to the newly added node new node<---old node. we shift from right to left

        self.count += 1             #it will increase the number of items


    def insertLast(self, song):
        new_node = Node(song)       #same process sya ng first, only sa dulo sya magaadd

        if self.head is None:
            self.head = new_node    #saying that if wala laman head next na yun ang magiging head.

        else:
            current = self.head     #If the list already has nodes, start searching from the head.

            while current.next is not None: #While there is still another node after current, keep moving forward
                current = current.next

            current.next = new_node #Ngayon like the one insertfirt yung node is naka point na sa baging lastnode

        self.count += 1


    def insertAt(self, song, position): #this one check if tama yung position ng input.
        if position < 0 or position > self.count:       #travel to one before the position, put new node between the two nodes
            raise IndexError("Position out of range")

        if position == 0:
            self.insertFirst(song)
            return

        new_node = Node(song)   #same lang sa first one singluar flow, and until ma reach yung current 
        current = self.head

        for i in range(position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.count += 1


    def display(self):
        if self.head is None:
            print("\nPlaylist is empty.")
            return

        print("\nPLAYLIST")
        print("------------------------------")

        current = self.head

        while current is not None:
            print(f"Song ID: {current.song.songId}")
            print(f"Song Title: {current.song.songTitle}")
            print(f"Artist: {current.song.artist}")
            print(f"Duration: {current.song.duration}")
            print()

            current = current.next 

        print(f"Total Number of Songs: {self.count}")


    def search(self, songId):
        current = self.head

        while current is not None:
            if current.song.songId == songId:
                print("\nSong Found")
                print("------------------------------")
                print(f"Song ID: {current.song.songId}")
                print(f"Song Title: {current.song.songTitle}")
                print(f"Artist: {current.song.artist}")
                print(f"Duration: {current.song.duration}")
                return

            current = current.next

        print("\nSong not found.")


    def delete(self, songId):
        if self.head is None:
            print("\nPlaylist is empty.")
            return

        if self.head.song.songId == songId:
            self.head = self.head.next
            self.count -= 1
            print("\nSong removed successfully.")
            return

        current = self.head

        while current.next is not None:
            if current.next.song.songId == songId:
                current.next = current.next.next
                self.count -= 1
                print("\nSong removed successfully.")
                return

            current = current.next

        print("\nSong not found.")


    def size(self):
        return self.count


    def isEmpty(self):
        return self.count == 0


playlist = LinkedList()


while True:
    print("\n...............................")
    print("MUSIC PLAYLIST MANAGER")
    print("+++++++++++++++++++++++++++++++++")
    print("1. Add Song at Beginning")
    print("2. Add Song at End")
    print("3. Insert Song at Position")
    print("4. Display Playlist")
    print("5. Search Song")
    print("6. Remove Song")
    print("7. Display Playlist Size")
    print("8. Exit")

    choice = int(input("\nEnter your choice: "))


    if choice == 1:
        songId = input("Enter Song ID: ")
        songTitle = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = input("Enter Duration: ")

        song = Song(songId, songTitle, artist, duration)

        playlist.insertFirst(song)

        print("\nSong added at the beginning successfully.")


    elif choice == 2:
        songId = input("Enter Song ID: ")
        songTitle = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = input("Enter Duration: ")

        song = Song(songId, songTitle, artist, duration)

        playlist.insertLast(song)

        print("\nSong added at the end successfully.")


    elif choice == 3:
        songId = input("Enter Song ID: ")
        songTitle = input("Enter Song Title: ")
        artist = input("Enter Artist: ")
        duration = input("Enter Duration: ")

        position = int(input("Enter Position: "))

        song = Song(songId, songTitle, artist, duration)

        try:
            playlist.insertAt(song, position)
            print("\nSong inserted successfully.")

        except IndexError:
            print("\nInvalid position.")


    elif choice == 4:
        playlist.display()


    elif choice == 5:
        songId = input("Enter Song ID to search: ")

        playlist.search(songId)


    elif choice == 6:
        songId = input("Enter Song ID to remove: ")

        playlist.delete(songId)


    elif choice == 7:
        print(f"\nPlaylist Size: {playlist.size()}")


    elif choice == 8:
        print("\nClose Music Playlist.")
        break


    else:
        print("\nInvalid choice.")