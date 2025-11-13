from library_books import library_books
from datetime import datetime, timedelta
# -------- Level 1 -------- completed
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author


## print the list of library books
## assign ids, titles, and authors to the book ID
## if statement: if book_not_available > dont print
def printavailablebooks():
    #print for every book in and only IF AVAILABLE books only with the 'available': true class
    ### reference: " How to filter a list of dictionaries in Python? by 32secondsofcode "
    for book in  library_books:
        if book['available'] == True:
            # keys are the "titles, author, ids" of each book, similar to genres or categories in a way, not to be confused w values.
            # fstrings can call items in the dictionary like this VVV
            # {} item
            # [] accessing values for the item
            print(f'{book["id"]} Title: {book["title"]}, Author: {book["author"]} ')

printavailablebooks()
print("\n")
# CONTINUE OPTION IS BELOW ITEM TRON FUNC


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books


def itemtron():
    #makes sure theres no duplicate options // a lot of iteration of set, but mainly for removing dupes and
    #                                      // identifying differences -pydoc
    genres = set()
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

    search = input("Please search for a genre OR an author!")
    if search: # only run if typed something
        search = search.lower() # hints and tips
        book_found = []
        for book in library_books:
            if book["available"] == True and (search in book["author"].lower() or search in book["genre"].lower()):
                    book_found.append(book)
        if book_found:
            for book in book_found:
                print(f'"{book["title"]}" by {book["author"]} ({book["genre"]})')
        else:
            print("Sorry, we couldn't find what you were looking for... ")


#would you like to continue?
cont_itemtron = input("Would you like to search for an item? (yes/no)")
if cont_itemtron == "yes":
    print("\n")
    print("***********************")
    print("\n")
    itemtron()

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
