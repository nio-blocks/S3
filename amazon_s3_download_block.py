import boto3

from nio.block.base import Block
from nio.signal.base import Signal
from nio.properties import (VersionProperty, StringProperty, PropertyHolder,
                            ObjectProperty)


class AWSCreds(PropertyHolder):
    aws_access_key_id = StringProperty(
        title="Access Key ID", default="", allow_none=False)
    aws_secret_access_key = StringProperty(
        title="Secret Access Key", default="", allow_none=False)
    aws_session_token = StringProperty(
        title="Session Token", default="", allow_none=False)


class AmazonS3Download(Block):

    version = VersionProperty("1.0.0")
    creds = ObjectProperty(
        AWSCreds, title="AWS Credentials", default=AWSCreds())

    # Bucket in which file is stored
    bucket_name = StringProperty(title="Bucket Name", default="")
    # Name of file in bucket
    key = StringProperty(title="S3 File Key", default="")
    # File to write to on local machine
    file_name = StringProperty(title="Download Location for File", default="")

    def __init__(self):
        self.client = None
        super().__init__()

    def configure(self, context):
        super().configure(context)
        self.client = boto3.client(
            's3',
            aws_access_key_id=self.creds().aws_access_key_id(),
            aws_secret_access_key=self.creds().aws_secret_access_key(),
            aws_session_token=self.creds().aws_secret_access_key())

    def process_signals(self, signals):
        for signal in signals:
            try:
                self.logger.debug("Downloading {} from the {} bucket".format(
                    self.key(signal), self.bucket_name(signal)))
                self.client.download_file(
                    self.bucket_name(signal),
                    self.key(signal),
                    self.file_name(signal))
            except:
                self.logger.exception("File download failed")
        # self.notify_signals

    # Once file is downloaded, then what?
