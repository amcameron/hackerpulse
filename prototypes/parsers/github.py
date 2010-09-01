"""Classes to parse events from a GitHub user."""

from urllib2 import urlopen, HTTPError
from xml.etree.ElementTree import parse

from parsers import BaseParser

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
