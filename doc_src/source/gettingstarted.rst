.. gettingstarted:

.. include:: global.txt

Getting Started
===============

The first thing you'll need to do is import the API module and specify
connection details for your ``feederd`` daemon. You will obviously need to
change the hostname, and possibly the port if you overrode the default of 8001.
After this call is made, you're ready to start submitting encoding jobs.

.. code-block:: python

    import media_nommer_api
    from media_nommer_api.presets.video_basic import web_medium
    
    api = media_nommer_api.connect('http://localhost:8001')
    
    response = api.job_submit(
        # Source file to encode.
        's3://YOUR_AWS_ID:YOUR_AWS_SECRET@SOME_BUCKET/infilename.mp4',
        # Destination for the encoding.
        's3://YOUR_AWS_ID:YOUR_AWS_SECRET@SOME_BUCKET2/outfilename.mp4',
        # The encoding preset to use.
        web_medium(),
    )

Encoding Presets
----------------

You'll notice in the example above that we use the
:py:func:`media_nommer_api.presets.video_basic.web_medium` encoding preset.
Presets determine the options that get passed to the encoder, ffmpeg in this
case. While this package comes with a number of :doc:`presets`, you are
encouraged to create your own that are specialized to your usage case.
                              
API Call Documentation
----------------------

You'll now want to review the :doc:`apiref` to see what calls are available.