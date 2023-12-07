#defining a class named "Book"
my_title = "matrix"
my_author = "immy"
my_pages = 200
#intance to of the class to display the information
class Book:
    def __init__ (my,title,author,pages):
        my.title = "matrix"
        my.author = "immy"
        my.pages = 200
x = Book("matrix", "immy", 200)
print(x.title)
print(x.author)
print(x.pages)


# class EBook inherits from the Book class
class EBook(Book):
    def __init__ (my,title,author,pages,format):
        my.title = "matrix"
        my.author = "immy"
        my.pages = 200
        my.format = "shans"
x = EBook({"matrix"}, {"immy"}, {200},{"shans"})
print(x.title)
print(x.author)
print(x.pages)
print(x.format)

# a function that return the book title and its author
def __str__(my):
        return f"{my.title}({my.author})"
x = Book("matrix", 200,"immy")
print(x)

# Definition
#class is used to create an object.
#object is a variable that contains functions used to manipulate data.