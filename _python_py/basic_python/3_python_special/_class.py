class Book:
    def __init__(self,title):
        self.title = title

    def price(self,price):
        self.price = price

    def publisher(self,publisher):
        self.publisher = publisher

    def year(self,year):
        self.year = year

    def get_book(self):
        bookinfo = f"책 제목: {self.title}\n출판사:{self.publisher}\n출판년도:{self.year}\n가격:{self.price}"
        return bookinfo
a = Book("운명이다")
a.publisher("사람사는 세상")
a.year("2010")
a.price("13500")
ainfo = a.get_book()

print(ainfo)
