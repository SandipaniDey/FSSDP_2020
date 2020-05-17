class book():
    def __init__(self,last,first,title,place,publisher,year):
        self.authorlast = last
        self.authorfirst = first
        self.authortitle = title
        self.authorplace = place
        self.authorpublisher = publisher
        self.year = year
        
    def write_bib_entry(self):
        print(self.authorlast,self.authorfirst,self.authortitle,self.authorplace,self.authorpublisher,self.year)
        return self.makeup(),self.book_of_your_choice()
    
    def beauty(self):
        print("The Evidential Power of Beauty. ")
    
    def pynut(self):
        print("Python in a Nutshell. ")
    
    def rev_year(self,year):
        self.year = year
    
    def makeup(self):
        pass
    
    def book_of_your_choice(self):
        pass
    
    def make_authoryear(self,authoryear):
        self.authoryear = str(authoryear)
        print(self.authoryear,'(',self.authoryear,')')
    
class Article(book):
    def __init__(self,article_title,volume_number,pages):
        self.article_title = article_title
        self.volume_number = volume_number
        self.pages = pages
        
    def write_bib_entry(self):
        print(self.article_title,self.volume_number,self.pages)
        
    def make_authoryear(self,authoryear):
        self.authoryear = str(authoryear)
        print('(',self.authoryear,')')
        
book = book("Bhagat","Chetan","Five Point Someone","India","Raju & Co.",2004)
book.write_bib_entry()
book.rev_year(2010)
book.beauty()
book.pynut()
book.makeup()
book.book_of_your_choice()
book.make_authoryear(1987)
article = Article("Article 1",4,500)
article.write_bib_entry()
article.make_authoryear(1998)
