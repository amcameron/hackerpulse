""" A collection of parsers to grab items from web services. """

from datetime import datetime
from urllib2 import urlopen, HTTPError
from xml.etree.ElementTree import parse

class BaseFeedItem(object):
    """ Base class for each 'feed item' that we parse. """

    def __init__(self, timestamp=None, title=None, link=None):
        self.timestamp = timestamp
        self.title = title
        self.link = link

    def get_data(self):
        """ Return the timestamp, title, and link """
        return self.timestamp, self.title, self.link

class RedditFeedItem(BaseFeedItem):
    def __init__(self):
		raise NotImplementedError

class TwitterFeedItem(BaseFeedItem):
    def __init__(self):
		raise NotImplementedError

class BaseParser(object):
	""" Base class for parsers. """

	def __init__(self, username):
		self.username = username

	def run(self):
		raise NotImplementedError

class RedditParser(BaseParser):
    def run(self):
		raise NotImplementedError

class GitHubParser(BaseParser):
	"""A parser to find a user's recent GitHub activity.

	An existing username is sufficient to access this information.

	"""

	# As the public Atom feed is not part of the official API,
	# there are no documented limits for it. I (amcameron) submitted
	# a discussion for it in GitHub's support system, and it is currently
	# awaiting moderation.

	url_prefix = "http://github.com/"
	url_suffix = ".atom"
	xmlns = "{http://www.w3.org/2005/Atom}"
	event_tag = "entry"
	timestamp_tag = "published"
	title_tag = "title"
	link_tag = "link"

	def run(self):
		""" Parse recent events from the user's GitHub Atom feed. """

		github_list = []

		try:
			xml_activities = urlopen(self.url_prefix + self.username +
					self.url_suffix)
		except HTTPError as e:
			if e.code == 404:
				#TODO: re-raise as better error, e.g. "user does not exist"
				raise e
			else:
				#TODO: else what?
				raise e

		tree = parse(xml_activities)
		events = tree.getroot().findall(self.xmlns + self.event_tag)

		for event in events:
			#TODO: Write a GitHubFeedItem that parses the XML on its own.
			# Then, this for loop becomes:
			# github_list = [GitHubFeedItem(tostring(e)) for e in events]
			timestamp = event.find(self.xmlns + self.timestamp_tag).text
			title = event.find(self.xmlns + self.title_tag).text
			link = event.find(self.xmlns + self.link_tag).get('href')

			item = BaseFeedItem(timestamp, title, link)
			github_list.append(item)

		return github_list
