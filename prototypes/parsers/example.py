from datetime import datetime

class BaseFeedItem(object):
    """
    Base class for each 'feed item' that we parse
    """

    def __init__(self):
        self.timestamp = None
        self.title = None
        self.link = None

    def get_data(self):
        """ Return the timestamp, title, and link """
        return self.timestamp, self.title, self.link

class RedditFeedItem(BaseFeedItem):
    def __init__(self):
        self.timestamp = datetime.now()
        self.title = 'A reddit story'
        self.link = 'reddit.com/coolstuff'

class TwitterFeedItem(BaseFeedItem):
    def __init__(self):
        self.timestamp = datetime.now()
        self.title = 'A tweet'
        self.link = 'twitter.com/coolstuff'

class RedditParser(object):
    def run(self):
        reddit_data = GetDataFromReddit('some username')
        reddit_list = []
        for item in reddit_data:
            r = RedditFeedItem()
            r.timestamp = item.date_posted
            r.title = item.title
            r.link = item.permalink
            reddit_list.append(r)

        return reddit_list


