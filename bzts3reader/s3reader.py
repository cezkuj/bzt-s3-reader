import logging

import boto3

from bzt.engine import EngineModule, Service


class S3Reader(Service):
    def __init__(self):
        super(S3Reader, self).__init__()
        self.log = logging.getLogger(self.__class__.__name__)
        self.bucket_name = ""
        self.file_name = ""

    def prepare(self):
        super(S3Reader, self).prepare()
        self.bucket_name = self.settings.get("bucket", "")
        if not self.bucket_name:
            raise Exception("bucket not found in settings")
        self.file_name = self.settings.get("file", "")
        if not self.file_name:
            raise Exception("file not found in settings")
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(self.bucket_name)
        bucket.download_file(self.file_name, f'./{self.file_name}')
        self.log.info(f'File {self.file_name} downloaded from {self.bucket_name}')
