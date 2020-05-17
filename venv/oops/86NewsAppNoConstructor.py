class SportsNews:
    def sportsInfo(self):
        print('Sports Info - 1')
        print('Sports Info - 2')
        print('Sports Info - 3')
        print('Sports Info - 4')


class MovieNews:
    def moviesInfo(self):
        print('Movies Info - 1')
        print('Movies Info - 2')
        print('Movies Info - 3')


class PoliticsNews:
    def politicsInfo(self):
        print('Politics Info - 1')
        print('Politics Info - 2')
        print('Politics Info - 3')
        print('Politics Info - 4')
        print('Politics Info - 5')


class NewsApp:
    def __init__(self, sportsNews, movieNews, politicsNews):
        self.sportsNews = sportsNews
        self.movieNews = movieNews
        self.politicsNews = politicsNews

    def getNews(self):
        print('Welcome to News App')
        self.sportsNews.sportsInfo()
        self.movieNews.moviesInfo()
        self.politicsNews.politicsInfo()


newsApp = NewsApp(SportsNews(), MovieNews(), PoliticsNews())
newsApp.getNews()

# Welcome to News App
# Sports Info - 1
# Sports Info - 2
# Sports Info - 3
# Sports Info - 4
# Movies Info - 1
# Movies Info - 2
# Movies Info - 3
# Politics Info - 1
# Politics Info - 2
# Politics Info - 3
# Politics Info - 4
# Politics Info - 5
