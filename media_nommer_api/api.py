"""
This is the top-level API module. You should generally instantiate the
:py:class:`APIConnection` object in here by using 
:py:func:`media_nommer_api.connect` instead of direct initialization of 
:py:class:`APIConnection`.

The :py:class:`APIConnection` class is your link to ``feederd``, 
which runs a JSON API.
"""
from media_nommer_api.server_io import APIRequest
from media_nommer_api.exceptions import InvalidInputError

class APIConnection(object):
    """
    Your application's means of communicating with feederd's JSON API.
    The public methods on this class correspond to API calls.

    API calls return :py:class:`APIResponse <media_nommer.client.server_io.APIResponse>` 
    objects with the results of your queries. Check the APIResponse.data attrib 
    for your un-serialized results.

    .. tip:: Do not instantiate this class directly. Use
        the :py:func:`media_nommer_api.connect` function for that purpose.

    :ivar str api_hostname: The protocol, hostname, and port in URI format.
    """
    def __init__(self, api_hostname):
        """
        This should generally only be called by media_nommer.client.connect().
        
        Do any setup work to prepare this object for communication with
        feederd's API. This method constructor should be as lazy as possible.
        
        :param str api_hostname: A URL with protocol, hostname, and port.
            No trailing slash.
        """
        self.api_hostname = api_hostname

    def _send_request(self, request_path, job_data):
        """
        Helper method for sending an API request. Pulls some values off of
        this APIConnection object to avoid repetition.
        
        :returns:
            A media_nommer_api.server_io.APIResponse object with the result
            of sending the APIRequest object this method forms. Your application
            will be interested in the APIResponse.data attribute, which is the
            un-serialized response from the server. 
        """
        return APIRequest(self.api_hostname, request_path, job_data)._send()

    ##############################
    ### Begin API call methods ###
    ##############################

    def job_submit(self, source_path, dest_path, job_options,
                   notify_url=None):
        """
        Submits an encoding job to feederd. This is an async call, so you may
        want to specify a notify_url for job state notifications to be sent to.
        
        :param str source_path: The path string to the master file to encode.
        :param str dest_path: The path string to where you'd like the encoded 
            files to be saved to.
        :param str preset: A preset string that corresponds to key in the
            settings.PRESETS dict.
        :param dict job_options: A dictionary with additional job
            options like bitrates, target encoding formats, etc. These options 
            can vary based on the Nommer and the formats you're asking for.
        :keyword str notify_url: (Optional) A URL to send job state updates to.
        
        :returns: An :py:class:`APIResponse <media_nommer_api.server_io.APIResponse>`
            object containing ``feederd``'s response.
        """
        if not source_path:
            raise InvalidInputError()

        if not dest_path:
            raise InvalidInputError()

        if not job_options:
            raise InvalidInputError()

        job_data = {
            'source_path': source_path,
            'dest_path': dest_path,
            'notify_url': notify_url,
            'job_options': job_options,
        }

        return self._send_request('job/submit', job_data)
