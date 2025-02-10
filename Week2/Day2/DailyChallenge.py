""" Daily Challenge : Pagination

Instructions:

    Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages. """

""" The Pagination class will accept 2 parameters:

    items (default: None): It will contain a list of contents to paginate.
    pageSize (default: 10): The amount of items to show in each page.

So for example we could initialize our pagination like this:

alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)
 """
import math
class Pagination:
    def __init__(self, items = None, pageSize = 10):
        self.items = items
        self.pageSize = int(pageSize)
        self.totalpages = math.ceil(len(self.items)/self.pageSize)
        self.currentPage =1


    def firstPage(self):
         return self.items[:self.pageSize]
    
    def nextPage(self):
        self.currentPage +=1
        beg_item = (self.currentPage-1)*self.pageSize
        end_item =  beg_item +self.pageSize
        return( self.items[beg_item:end_item])     
       
    def prevPage(self):
        self.currentPage -=1
            
    def goToPage(self,pageNum):
        self.currentPage = pageNum

    def getVisibleItems(self):
        if self.currentPage == self.totalpages:
            print (self.items[(self.totalpages-1)*self.pageSize:])
        else:
            beg_item = (self.currentPage-1)*self.pageSize
            end_item =  beg_item +self.pageSize
            print( self.items[beg_item:end_item])

    def lastPage(self):
        self.currentPage = self.totalpages
alphabetList = list("abcdefghijklmnopqrstuvwxyz")

p = Pagination(alphabetList, 4)

p.getVisibleItems() 
# ["a", "b", "c", "d"]

p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]
       
p.goToPage(3)

p.getVisibleItems()

p.prevPage()

p.getVisibleItems()

p.lastPage()

p.getVisibleItems()


p.firstPage()
p.getVisibleItems()

p.nextPage().nextPage()
p.getVisibleItems()