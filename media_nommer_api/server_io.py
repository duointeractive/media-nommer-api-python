"""
API request and response abstraction and helpers. This module and its contents 
should not be instantiated directly.
"""
import urllib
import urllib2
import simplejson

class APIRequest(object):
    """
    An abstraction class that all outbound API requests to ``feederd``
    are wrapped in. Handles some basic serialization and transport stuff.
    
    :ivar dict data: The dict to be urlencoded and sent to the API server.
    :ivar str api_hostname: The protocol, hostname, and port in URI format.
    :ivar str request_path: The URL path to the API method. 
    """
    def __init__(self, api_hostname, request_path, data):
        """
        :param str api_hostname: The protocol, hostname, and port of your feederd's
            REST API. There should be no trailing slash.
        :param str request_path: The URL to query. No leading or trailing slash.
        :param dict data: A dict object of key/value pairs to urlencode and send
                to feederd's REST API. If some of your POST keys require
                JSON values, you'll need to serialize in your API method.
        """
        self.data = data
        self.api_hostname = api_hostname
        self.request_path = request_path

    def _send(self):
        """
        Sends the query, returns an :py:class:`APIResponse` object with the 
        un-serialized response included.
        
        :returns: An :py:class:`APIResponse` object.
        :raisess: A :py:exc:`urllib2.URLError` when urllib2 runs into issues.
        """
        encoded_data = urllib.urlencode(self.data)
        full_request_path = '%s/%s' % (self.api_hostname, self.request_path)
        request = urllib2.Request(full_request_path, encoded_data)
        response = urllib2.urlopen(request)
        return APIResponse(self, response.read())

class APIResponse(object):
    """
    A basic API response. Performs some simple error handling and provides 
    helpers to check the response for success or failure.
    
    Your application will be interested in this class's :py:attr:`data` instance
    variable, which contains the server's response.
    
    :ivar dict data: The un-serialized response from ``feederd`` in dict form.
    :ivar APIRequest request: The :py:class:`APIRequest` object that this object 
        originated from.
    :ivar str raw_response: The raw, serialized string returned from ``feederd``. 
    """
    def __init__(self, request, raw_response):
        """
        :type request: :py:class:`APIRequest`
        :param request: The request object that instantiated this
            response object.
        :param str raw_response: The raw server response's body.
        """
        self.request = request
        self.raw_response = raw_response
        # The response JSON parsed by simplejson. This is what you mostly
        # will want to look at from within your application.
        self.data = simplejson.loads(self.raw_response)

    def __str__(self):
        """
        When str()'d, just show the underlying response data.
        """
        return repr(self.data)

    def is_success(self):
        """
        Indicates whether the call completed without errors.
        
        :returns: True if there were no errors, False otherwise.
        :rtype: bool
        """
        return True
