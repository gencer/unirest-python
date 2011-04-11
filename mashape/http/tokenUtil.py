#
# Copyright (C) 2011 Mashape, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# The author of this software is Mashape, Inc.
# For any question or feedback please contact us at: support@mashape.com
#++

import urllib2
import urllib
import json
from mashape.exception.clientException import MashapeClientException

class TokenUtil:

	def requestToken(self, apiKey):
		TOKEN_URL="http://api.mashape.com/requestToken"
		data = {'apikey' : apiKey}
		jsonToken = urllib2.urlopen(TOKEN_URL, urllib.urlencode(data)).read()
		answer = json.loads(jsonToken)
		errors = answer["errors"]
		if len(errors) == 0:
			return answer['token']
		else:
			print errors
			raise MashapeClientException(errors[0]["message"], errors[0]["code"])
