"""
Encoding Presets
================

Encoding presets are simple functions that return dicts that are passed
to the selected Nommer. At the current time, this is almost always
FFmpegNommer, which uses EC2 instances + ffmpeg to get encodings done.

To use a preset, simply import it and pass it as the ``job_options`` argument
to :py:meth:`media_nommer_api.api.APIConnection.job_submit` method.

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
"""