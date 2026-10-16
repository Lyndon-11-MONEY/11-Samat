'''
Lyndon John F Nicolas
9-Samat
‎Oct. 16, 2026
‎'''
‎
‎class Publication:
‎    def __init__(self, title, author):
‎        self.title = title
‎        self.author = author
‎
‎    def get_title(self):
‎        return self.title
‎
‎    def get_author(self):
‎        return self.author
‎
‎    def set_title(self, title):
‎        self.title = title
‎
‎    def set_author(self, author):
‎        self.author = author
‎
‎    def display_info(self):
‎        print("Publication Information:")
‎        print(f"Title: {self.title}")
‎        print(f"Author: {self.author}")
‎
‎
‎class Book(Publication):
‎    def __init__(self, title, author, number_pages):
‎        super().__init__(title, author)
‎        self.number_pages = number_pages
‎
‎    def get_title(self):
‎        return self.title
‎
‎    def get_author(self):
‎        return self.author
‎
‎    def set_title(self, title):
‎        self.title = title
‎
‎    def set_author(self, author):
‎        self.author = author
‎
‎    def get_number_of_pages(self):
‎        return self.number_pages
‎
‎    def set_number_of_pages(self, number_pages):
‎        self.number_pages = number_pages
‎
‎    def display_info(self):
‎        print("Book Information:")
‎        print(f"Title: {self.title}")
‎        print(f"Author: {self.author}")
‎
‎
‎class Magazine(Publication):
‎    def __init__(self, title, author, issue_number):
‎        super().__init__(title, author)
‎        self.issue_number = issue_number
‎
‎    def get_title(self):
‎        return self.title
‎
‎    def get_author(self):
‎        return self.author
‎
‎    def set_title(self, title):
‎        self.title = title
‎
‎    def set_author(self, author):
‎        self.author = author
‎
‎    def get_issue_number(self):
‎        return self.issue_number
‎
‎    def set_issue_number(self, issue_number):
‎        self.issue_number = issue_number
‎
‎    def display_info(self):
‎        print("Magazine Information:")
‎        print(f"Title: {self.title}")
‎        print(f"Author: {self.author}")
‎
‎
‎pub1 = Publication(
‎    "Journal of Experimental Psychology",
‎    "Ratchiff, R. & Van Dongen, H.")
‎
‎book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
‎
‎mag1 = Magazine("National Geographic", "Various Authors", 202)
‎
‎pub1.display_info()
‎
‎book1.display_info()
‎book1.set_number_of_pages(-310)
‎print(book1.get_number_of_pages())
‎
‎mag1.display_info()
‎print(mag1.get_issue_number())
