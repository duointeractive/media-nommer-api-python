"""
[16:51] <gtaylor> let's say I don't know the dimensions or aspect ratio of a video, but we know a width we'd like to get down to, while preserving whatever aspect ratio was in the source file. Would it be -vf yadif:scale=640?
[16:52] <pasteeater> generally you could use '640:-1', but libx264 won't accept values not divisible by two, IIRC
[16:52] <pasteeater> so then you can use scale="640:trunc(ow/a/2)*2" instead
[16:53] <pasteeater> or scale="trunc(oh*a*2)/2:320" if you always want a specific height

ffmpeg -y -i roving_web.wmv -threads 0 -vcodec libx264 -preset medium -profile baseline -b 400k -vf yadif,scale=640:-1 -pass 1 -f mp4 -an /dev/null

ffmpeg -y -i roving_web.wmv -threads 0 -vcodec libx264 -preset medium -profile baseline -b 400k -vf yadif,scale=640:-1 -pass 2 -acodec libfaac -ab 128k -ar 48000 -ac 2 roving_enc.mp4
"""

def web_medium():
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
