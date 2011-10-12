.. gettingstarted:

.. include:: global.txt

Getting Started
===============

The first thing you'll need to do is import the API module and specify
connection details for your ``feederd`` daemon.

.. code-block:: python

    import media_nommer_api
    
    api = media_nommer_api.connect('http://localhost:8001')
    
You will obviously need to change the hostname, and possibly the port if
you overrode the default of 8001. After this call is made, you're ready to
start making queries.

.. code-block:: python

    preset = 'flash_hq'
    job_opts = {
        'outfile_options': {
            'sameq': None,
        }
    }
    response = api.job_submit('s3://YOUR_AWS_ID:YOUR_AWS_SECRET@SOME_BUCKET/infilename.mp4', 
                              's3://YOUR_AWS_ID:YOUR_AWS_SECRET@SOME_BUCKET2/outfilename.mp4', 
                              preset, job_options=job_opts)
                              
API Call Documentation
----------------------

You'll now want to review the :doc:`apiref` to see what calls are available.