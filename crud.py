from lib import *

#read and parse an XML file
ntree = ET.parse('programmingbooks.xml')
root = ntree.getroot()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#CRUD OPERATIONS (Create, Read, Update, Delete)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Show all books.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def showAllBooks():
    for book in root.findall('book'):
        bookid = book.find('bookid').text
        author = book.find('author').text
        title = book.find('title').text
        genre = book.find('genre').text
        price = book.find('price').text
        publish_date = book.find('publish_date').text
        isbn10 = book.find('isbn10').text
        description = book.find('description').text
        print("--------------------------------------------")
        print("ID: " + bookid)
        print("Author: " + author)
        print("Title: " + title)
        print("Genre: " + genre)
        print("Price: " + price)
        print("Publish Date: " + publish_date)
        print("ISBN-10: " + isbn10)
        print("Description: " + description)
    print("--------------------------------------------")
    print("End of books.")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Search for a book.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def searchForBook():
    isbn10 = input("Enter the ISBN-10 of the book you want to search for: ")
    for book in root.findall('book'):
        isbn10A = book.find('isbn10').text

        if isbn10A == isbn10:
            print("ISBN-10 Requested: " + isbn10 + " ISBN-10 Found: " + isbn10A)
            bookid = book.find('bookid').text
            author = book.find('author').text
            title = book.find('title').text
            genre = book.find('genre').text
            price = book.find('price').text
            publish_date = book.find('publish_date').text
            isbn10 = book.find('isbn10').text
            description = book.find('description').text
            print("--------------------------------------------")
            print("ID: " + bookid)
            print("Author: " + author)
            print("Title: " + title)
            print("Genre: " + genre)
            print("Price: " + price)
            print("Publish Date: " + publish_date)
            print("ISBN-10: " + isbn10)
            print("Description: " + description)
            print("--------------------------------------------")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Edit a book.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def editBook():
    isbn10 = input("Enter the ISBN-10 of the book you want to edit: ")

    for book in root.findall('book'):
        isbn10A = book.find('isbn10').text

        if isbn10A == isbn10:
            bookid = book.find('bookid').text
            author = book.find('author').text
            title = book.find('title').text
            genre = book.find('genre').text
            price = book.find('price').text
            publish_date = book.find('publish_date').text
            isbn10 = book.find('isbn10').text
            description = book.find('description').text

            # edit author
            author = input("Please enter author:(" + author + ")") or author
            book.find('author').text = author
            # edit title
            title = input("Please enter title:(" + title + ")") or title
            book.find('title').text = title
            # edit genre
            genre = input("Please enter genre:(" + genre + ")") or genre
            book.find('genre').text = genre
            # edit price
            price = input("Please enter price:(" + price + ")") or price
            book.find('price').text = price
            # edit publish_date
            publish_date = input("Please enter publish_date:(" + publish_date + ")") or publish_date
            book.find('publish_date').text = publish_date
            # edit isbn10
            isbn10 = input("Please enter isbn10:(" + isbn10 + ")") or isbn10
            book.find('isbn10').text = isbn10
            # edit age
            description = input("Please enter description:(" + description + ")") or description
            book.find('description').text = description

            ntree.write("programmingbooks.xml")

            print("--------------------------------------------")
            print("BOOK ID: " + bookid + " UPDATED")
            print("--------------------------------------------")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#New ID.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def newid1():
    max = 0
    for book in root.findall('book'):
        id = int(book.find('bookid').text)
        if id > max:
            max = id
    return max+1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Book Exists.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bookExists(isbn10):
    aValue = False

    for book in root.findall('book'):
        isbn10Tried = book.find('isbn10').text

        if isbn10Tried == isbn10:
            aValue = True

    return aValue

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Create a book.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def createBook():
    isbn10Input = input("Enter the ISBN-10 of the book you want to search for: ")
    exists = bookExists(isbn10Input)

    if exists == False:
        newID = newid1()
        print("Create a book record...")
        author = input("Author:")
        title = input("Title:")
        genre = input("Genre:")
        price = input("Price:")
        publish_date = input("Publish Date:")
        isbn10 = input("ISBN-10:")
        description = input("Description:")

        # create a contact element at root level
        newbookRec = ET.SubElement(root, "book", id=str(newID))

        # add the fields into out new record
        ET.SubElement(newbookRec, "bookid", name="bookid").text = str(newID)
        ET.SubElement(newbookRec, "author", name="author").text = author
        ET.SubElement(newbookRec, "title", name="title").text = title
        ET.SubElement(newbookRec, "genre", name="genre").text = genre
        ET.SubElement(newbookRec, "price", name="price").text = price
        ET.SubElement(newbookRec, "publish_date", name="publish_date").text = publish_date
        ET.SubElement(newbookRec, "isbn10", name="isbn10").text = isbn10
        ET.SubElement(newbookRec, "description", name="description").text = description

        ntree.write("programmingbooks.xml")

    else:
        print("--------------------------------------------")
        print("Book record already exists!")
        print("--------------------------------------------")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Delete a book.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def deleteBook():
    deleteBook = input("Enter the ISBN-10 of the book you want to delete: ")
    for book in root.findall('book'):
        bookISBN = book.find('isbn10').text
        if bookISBN == deleteBook:
            root.remove(book)
            ntree.write("programmingbooks.xml")
            print("--------------------------------------------")
            print("Book ISBN-10:", deleteBook, "deleted!")
            print("--------------------------------------------")

