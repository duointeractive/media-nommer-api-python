def cb_low():
    return {
        'nommer': 'media_nommer.ec2nommerd.nommers.ffmpeg.FFmpegNommer',
        'options': [
                {
                'outfile_options': [
                    ('vcodec', 'libx264'),
                    ('preset', 'medium'),
                    ('vprofile', 'baseline'),
                    ('b', '230k'),
                    ('bufsize', '230k'),
                    ('vf', "yadif,scale='400:trunc(ow/a/2)*2'"),
                    ('pass', '1'),
                    ('f', 'mp4'),
                    ('keyint_min', '60'),
                    ('g', '120'),
                    ('an', None),
                ],
                },
                {
                'outfile_options': [
                    ('vcodec', 'libx264'),
                    ('preset', 'medium'),
                    ('vprofile', 'baseline'),
                    ('b', '230k'),
                    ('bufsize', '230k'),
                    ('vf', "yadif,scale='400:trunc(ow/a/2)*2'"),
                    ('pass', '2'),
                    ('acodec', 'libfaac'),
                    ('ab', '96k'),
                    ('async', '480'),
                    ('keyint_min', '60'),
                    ('g', '120'),
                    ('f', 'mp4'),
                ],
                'move_atom_to_front': True,
                },
        ],
    }


def cb_medium():
    return {
        'nommer': 'media_nommer.ec2nommerd.nommers.ffmpeg.FFmpegNommer',
        'options': [
            {
                'outfile_options': [
                    ('vcodec', 'libx264'),
                    ('preset', 'medium'),
                    ('vprofile', 'baseline'),
                    ('b', '921k'),
                    ('bufsize', '921k'),
                    ('vf', "yadif,scale='640:trunc(ow/a/2)*2'"),
                    ('pass', '1'),
                    ('f', 'mp4'),
                    # Keyframe
                    ('keyint_min', '60'),
                    ('g', '120'),
                    ('an', None),
                ],
            },
            {
                'outfile_options': [
                    ('vcodec', 'libx264'),
                    ('preset', 'medium'),
                    ('vprofile', 'baseline'),
                    ('b', '921k'),
                    ('bufsize', '921k'),
                    ('vf', "yadif,scale='640:trunc(ow/a/2)*2'"),
                    ('pass', '2'),
                    ('acodec', 'libfaac'),
                    ('ab', '125k'),
                    ('async', '480'),
                    # Keyframe
                    ('keyint_min', '60'),
                    ('g', '120'),
                    ('f', 'mp4'),
                ],
            'move_atom_to_front': True,
            },
        ],
    }


def cb_high():
    return {
        'nommer': 'media_nommer.ec2nommerd.nommers.ffmpeg.FFmpegNommer',
        'options': [
                {
                'outfile_options': [
                    ('vcodec', 'libx264'),
                    ('preset', 'medium'),
                    ('vprofile', 'baseline'),
                    ('b', '2000k'),
                    ('bufsize', '2000k'),
                    ('vf', "yadif,scale='1280:trunc(ow/a/2)*2'"),
                    ('pass', '1'),
                    ('f', 'mp4'),
                    ('keyint_min', '60'),
                    ('g', '120'),
                    ('an', None),
                ],
                },
                {
                'outfile_options': [
                    ('vcodec', 'libx264'),
                    ('preset', 'medium'),
                    ('vprofile', 'baseline'),
                    ('b', '2000k'),
                    ('bufsize', '2000k'),
                    ('vf', "yadif,scale='1280:trunc(ow/a/2)*2'"),
                    ('pass', '2'),
                    ('acodec', 'libfaac'),
                    ('ab', '125k'),
                    ('async', '480'),
                    ('keyint_min', '60'),
                    ('g', '120'),
                    ('f', 'mp4'),
                ],
                'move_atom_to_front': True,
                },
        ],
    }