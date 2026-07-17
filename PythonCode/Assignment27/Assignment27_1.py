class BookStore:
    NoteBook = 0
    def __init__(self,a,b):
        self.Name = a
        self.Author = b
        BookStore.NoteBook =  BookStore.NoteBook + 1
    def Display(self):
        print(f"{self.Name} by {self.Author}. No of Books : {BookStore.NoteBook}")

obj1 = BookStore("LSP","Robert Love")
obj1.Display()
obj2 = BookStore("C programming","Dennis Ritchie")
obj2.Display()
