class books():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "The title is {},the author is {} and the number of pages are {}".format(self.title,self.author,self.pages)


    def __len__(self):
        return self.pages

b=books('2_states','Chetan_Bhagat',400)

