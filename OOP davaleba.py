class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        if pages > 0:
            self.__pages = pages
        else:
            print("გვერდების რაოდენობა არ არის დადებითი!")
            self.__pages = 1
        self.__is_read = False

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def pages(self):
        return self.__pages

    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @pages.setter
    def pages(self, new_pages):
        if new_pages > 0:
            self.__pages = new_pages
        else:
            print("გვერდების რაოდენობა არ არის დადებითი!")

    def mark_as_read(self):
        self.__is_read = True

    def get_info(self):
        status = "წაკითხულია" if self.__is_read else "არ არის წაკითხული"
        print(f"სათაური: {self.__title}")
        print(f"ავტორი: {self.__author}")
        print(f"გვერდები: {self.__pages}")
        print(f"სტატუსი: {status}")


book1 = Book("კვაჭი კვაჭანტირაძე", "მიხეილ ჯავახიშვილი", 512)

book1.get_info()
print()

book1.pages = -10
print()

book1.mark_as_read()
book1.get_info()
