import logging

import boto3
from botocore.exceptions import NoCredentialsError, ClientError

from bzt import TaurusConfigError
from bzt.engine import Service

import os

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
            raise TaurusConfigError("bucket not found in settings")
        self.file_name = self.settings.get("file", "")
        if not self.file_name:
            raise TaurusConfigError("file not found in settings")
        s3 = boto3.resource('s3')
        try:
            _, file_name = os.path.split(self.file_name) # Decoupling file itself from subkeys
            s3.meta.client.download_file(self.bucket_name, self.file_name, file_name) # Downloading the file without subkeys
        except (NoCredentialsError, ClientError) as err:
            raise TaurusConfigError(f'Error while downloading file {self.file_name} from {self.bucket_name}: {err}, check https://github.com/cezkuj/bzt-s3-reader#aws-authentication')

        self.log.info(f'File {self.file_name} downloaded from {self.bucket_name}')
