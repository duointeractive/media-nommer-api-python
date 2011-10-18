"""
The following presets are basic video encoding presets. Right now, this is
just ffmpeg, but may be expanded in the future with the addition of Nommers.
"""

def web_medium():
    """
    This preset is suitable for medium-quality encodings for web consumption.
    The two-pass encoding yields a smaller size, and we use qtfaststart.py to
    move the meta-data to the front for faster buffering.
    """
    return {
        'nommer': 'media_nommer.ec2nommerd.nommers.ffmpeg.FFmpegNommer',
        'options': [
            {
                'outfile_options': [
                    ('vcodec', 'libx264'),
                    ('preset', 'medium'),
                    ('vprofile', 'baseline'),
                    ('b', '400k'),
                    ('vf', "yadif,scale='640:trunc(ow/a/2)*2'"),
                    ('pass', '1'),
                    ('f', 'mp4'),
                    ('an', None),
                ],
            },
            {
                'outfile_options': [
                    ('vcodec', 'libx264'),
                    ('preset', 'medium'),
                    ('vprofile', 'baseline'),
                    ('b', '400k'),
                    ('vf', "yadif,scale='640:trunc(ow/a/2)*2'"),
                    ('pass', '2'),
                    ('acodec', 'libfaac'),
                    ('ab', '128k'),
                    ('ar', '48000'),
                    ('async', '480'),
                    ('ac', '2'),
                    ('f', 'mp4'),
                ],
                'move_atom_to_front': True,
            },
        ],
    }
