import unittest
from media_nommer_api import connect
from media_nommer_api.presets import video_basic
from media_nommer_api.testing_utils import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

class JobSubmitTests(unittest.TestCase):
    def setUp(self):
        self.connection = connect('http://localhost:8001')
        self.source_path = 's3://%s:%s@%s/%s' % (
            AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY,
            'nommer_in',
            'asf_to_mpeg-1.mpeg'
        )
        self.dest_path = 's3://%s:%s@%s/%s' % (
            AWS_ACCESS_KEY_ID,
            AWS_SECRET_ACCESS_KEY,
            'nommer_out',
            'roving_web'
        )

    def test_job_submit(self):
        job_opts = video_basic.web_medium('640x480', '1.3333')
        print "COMEBACK", self.connection.job_submit(self.source_path,
                                                     self.dest_path,
                                                     job_opts)
