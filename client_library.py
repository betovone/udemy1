from argparse import ArgumentParser
from library_xmlrpc import LibraryAPI

#from library_odoorpc import LibraryAPI

class Cliente:
    
    def __init__(self, host, port, db, user, pwd):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.pwd = pwd
        self.api = None

    def connect(self, obj):
        self.api = obj(self.host, self.port, self.db, self.user, self.pwd)
        return 
    
    def listar(self, title=[]):
        return self.api.search_read(title)
    
    def crear(self, title=None):
        return self.api.create(title)

    def write(self, id, title):
        return self.api.write(id, title)

    def unlink(self, id):
        return self.api.unlink(id)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
                "command",
                choices=["list", "add", "set", "del"]
            )
    parser.add_argument("params", nargs="*") # optional args
    args = parser.parse_args()
    
    c = Cliente("localhost", 8069, "odoo_docker", "odoo", "odoo")
    c.connect(LibraryAPI)
    
    if args.command == "list":
        title = args.params[:1]
        books = c.listar(''.join(title))
        for book in books:
            print("%(id)d %(name)s" % book)

    if args.command == "add":
        if len(args.params) > 0:
            title = args.params[0]
            book_id = c.crear(title)
            print("Book added with ID %d for title %s." % (book_id, title))
        else:
            print("debe ir el parametro del titulo")


    if args.command == "set":
        if len(args.params) != 2:
            print("set command requires a Title and ID.")
        else:
            book_id, title = int(args.params[0]), args.params[1]
            c.write(book_id, title)
            print("Title of Book ID %d set to %s." % (book_id, title))

    if args.command == "del":
        book_id = int(args.params[0])
        c.unlink(book_id)
        print("Book with ID %s was deleted." % book_id)

