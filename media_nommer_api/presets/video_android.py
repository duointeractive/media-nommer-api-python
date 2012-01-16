"""
The following presets are geared towards compatibility with Android devices.
Some of the older handsets are very picky about certain settings like framerate,
audio channels, and etc.
"""

def android_low():
    """
    A lower-quality Android video encoding setting. This should be suitable for
    the vast majority of devices.
    """
    return {
        'nommer': 'media_nommer.ec2nommerd.nommers.ffmpeg.FFmpegNommer',
        'options': [
            {
            'outfile_options': [
                ('vcodec', 'libx264'),
                ('preset', 'medium'),
                ('vprofile', 'baseline'),
                ('b', '300k'),
                ('r', '30'),
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
                ('b', '300k'),
                ('r', '30'),
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