def android_low(size, aspect):
    return {
        'nommer': 'media_nommer.ec2nommerd.nommers.ffmpeg.FFmpegNommer',
        'options': [
            {
                'outfile_options': [
                    ('threads', 0),
                    ('vcodec', 'libx264'),
                    ('vpre', 'slow_firstpass'),
                    ('vpre', 'baseline'),
                    ('b', '300k'),
                    ('r', '30'),
                    ('acodec', 'libfaac'),
                    ('strict', 'experimental'),
                    ('ab', '64k'),
                    ('ar', '44100'),
                    ('s', size),
                    ('aspect', aspect),
                    ('ac', '2'),
                    ('pass', '1'),
                    ('f', 'rawvideo'),
                    ('an', None),
                ],
            },
            {
                'outfile_options': [
                    ('threads', 0),
                    ('vcodec', 'libx264'),
                    ('vpre', 'slow'),
                    ('vpre', 'baseline'),
                    ('b', '300k'),
                    ('r', '30'),
                    ('acodec', 'libfaac'),
                    ('strict', 'experimental'),
                    ('ab', '64k'),
                    ('ar', '44100'),
                    ('s', size),
                    ('aspect', aspect),
                    ('ac', '2'),
                    ('pass', '2'),
                    ('deinterlace', None),
                    ('f', 'mp4'),
                ],
            },
        ],
    }