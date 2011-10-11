def android_low():
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
                    ('ac', '2'),
                    ('f', 'mp4'),
                ],
                'move_atom_to_front': True,
                },
        ],
        }