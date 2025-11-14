from library_books import library_books
import datetime
from datetime import timedelta
# -------- Level 1 -------- completed
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author


## print the list of library books
## assign ids, titles, and authors to the book ID
## if statement: if book_not_available > dont print
def printavailablebooks():
    #print for every book in and only IF AVAILABLE books only with the 'available': true value
    ### reference: " How to filter a list of dictionaries in Python? by 32secondsofcode "
    for book in  library_books:
        if book['available'] == True:
            # keys are the "titles, author, ids" of each book, similar to genres or categories in a way, not to be confused w values.
            # fstrings can call items in the dictionary like this VVV
            # {} item
            # [] accessing values for the item
            print(f'{book["id"]} Title: {book["title"]}, Author: {book["author"]} ')




# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books


def itemtron():
    #makes sure theres no duplicate options // a lot of iteration of set, but mainly for removing dupes and
    #                                      // identifying differences -pydoc
    genres = set() # does not allow any duplicate values inside of the variable. {dict}
    authors = set()
    ### len(s) :: Return the number of elements in set s (cardinality of s). from python documentation
    for book in library_books: # puts genres and authors inside of "genre set" and "author set" and prints it
        if book['available'] == True:
            genres.add(book["genre"])
            authors.add(book["author"])

    print("Available genres: ")
    for genre in genres:
        print(f'{genre}') #prints the available book genres from the genre set (w/o dupes)

    print("\n")
    print("Available authors:")
    for author in authors:
        print(f'{author}') #prints the available book authors from the author set (w/o dupes)

    # ok now i have all the options for genres and author, now the user can SEARCH FOR THE BOOK BASED ON AUTHOR OR GENRE!
    print("\n")
    search = input("Please search for a genre OR an author!: ")
    if search: # only run if typed something
        search = search.lower() # hints and tips
        book_found = []
        for book in library_books:
            if book["available"] == True and (search in book["author"].lower() or search in book["genre"].lower()):
                    book_found.append(book)
        if book_found:
            for book in book_found:
                print(f'"{book["title"]}" by {book["author"]} ({book["genre"]}) and the ID is {book["id"]}')
        else:
            print("Sorry, we couldn't find what you were looking for... ")


#would you like to continue?


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkoutbook():
    inp =input("Please enter the book ID you would like to check out: ")
    for book in library_books:
        if book["available"] and book["id"] == inp:
                book["available"] = False
                book["when_due"] = datetime.date.today() + datetime.timedelta(days=14) # this actually took forever
                print("Book is now unavailable!")
                print(f'Your book is due on {book["when_due"]}')
                print("\n")
                print("Please return out your book before the deadline! Have a nice day.")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def returningbook():
    inp =input("Please enter the book ID you would like to return: ")
    for book in library_books:
        if book["available"] == False and book["id"] == inp:
                today = datetime.date.today()
                if book["when_due"] < today:
                     print("This book was overdue on " + {book["when_due"]} + ".")
                book["available"] = True
                book["when_due"] = None
                print("Come back again sometime.")
                return
    if inp != book["id"]:
         print("Please print a valid book ID!")





# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

printavailablebooks()
print("\n")

cont_itemtron = input("Would you like to search for an item? (yes/no)")
if cont_itemtron == "yes":
    print("\n")
    print("***********************")
    print("\n")
    itemtron()

print("\n")
checkout = input("Would you like to check out a book?(yes/no): ")
checkout = checkout.lower()
if checkout == "yes":
    checkoutbook()
    print("\n")
    print("**********************")
    print("\n")

print("\n")
checkout = input("Would you like to return a book?(yes/no): ")
checkout = checkout.lower()
if checkout == "yes":
    returningbook()
    print("\n")
    print("**********************")
    print("\n")

if __name__ == "__main__":
    pass
