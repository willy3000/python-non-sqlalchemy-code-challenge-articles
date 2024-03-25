class Article:

    all=[]

    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    
    def __repr__(self):
        return f" Article ({self.author}, {self._magazine}, Title: {self._title})"

    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self, value):
        if (isinstance(value, str) and len(value) >= 5 and len(value) <= 50):
                    self._title = value
        else:
            return ('Article title must be between 5 and 50 characters long.')

    @property
    def author(self):
        return self._author if isinstance(self._author, Author) else ('Author must be an instance of class Author')
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            return('Author must be an instance of the "Author" class.')
        
    @property
    def magazine(self):
        return self._magazine if isinstance(self._magazine, Magazine) else ('Magazine must be an instanze of class "Magazine"')

    @magazine.setter
    def magazine(self, mag):
        if isinstance(mag, Magazine):
            self._magazine = mag
        else:
            return('Magazine must be an instance of the "Magazine" class.')


class Author:

    all=[]

    def __init__(self, name):
        self._name = name
        Author.all.append(self)

    def __repr__(self):
        return  f'Author ({self.name})'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value != self._name:
            return None
        elif value == self._name:
            self._name = value

    def articles(self):
        return [articles for articles in Article.all if  articles.author == self]

    def magazines(self):
        mag_list= []
        for article in Article.all:
            if article.magazine in mag_list and isinstance(article.magazine, Magazine):
                pass
            elif article.author==self:
                mag_list.append(article.magazine)

        return mag_list


    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        if isinstance(magazine, Magazine) and isinstance(title, str):
            return new_article
        else: 
            raise Exception('Invalid input')


    def topic_areas(self):
        category_tracker = []
        mag_list = Author.magazines(self)

        if mag_list == []:
            return None
        
        for magazine in mag_list:
            if magazine.category in category_tracker:
                pass
            else:
                category_tracker.append(magazine.category)
        return category_tracker
            


class Magazine:
    
    all=[]
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)

    def __repr__(self):
        return f"Magazine (Name: {self.name}, Category: {self.category})"

    @property
    def name(self):
            return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 2 and len(value) <= 16:
            self._name = value
        else:
            return ('Magazine name must be between 2 and 16 characters long')

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        contributors = []
        
        for article in Article.all:
            if article.author in contributors and isinstance(article.author, Author):
                pass
            elif article.magazine == self and isinstance(article.author, Author):
                contributors.append(article.author)
        return contributors

    def article_titles(self):
        article_list = self.articles()
        titles= [article.title for article in article_list if isinstance(article.title, str)]
        if article_list == []:
            return None
        else:
            return titles

    # this is the only method that I struggled to get working
    def contributing_authors(self):
        authors = self.contributors()
        contributing_count = {}
        met_criteria = []

        for author in authors:
            if author not in contributing_count:
                contributing_count[author] = 1
            else:
                contributing_count[author] += 1
        
        
        for author in contributing_count:
            if contributing_count[author] <= 1:
                return None
            elif contributing_count[author] > 1:
                met_criteria.append(author)
        return met_criteria


# author_1 = Author("Carry Bradshaw")
# author_2 = Author("Nathaniel Hawthorne")
# magazine_1 = Magazine("Vogue", "Fashion")
# magazine_2 = Magazine("AD", "Architecture")
# Article(author_1, magazine_1, "How to wear a tutu with style")
# Article(author_1, magazine_1, "How to be single and happy")
# Article(author_1, magazine_1, "Dating life in NYC")
# Article(author_1, magazine_2, "Carrara Marble is so 2020")
# Article(author_2, magazine_2, "2023 Eccentric Design Trends")

# # print(Article.all)
# print(magazine_1.contributing_authors())
# print(magazine_2.contributing_authors())