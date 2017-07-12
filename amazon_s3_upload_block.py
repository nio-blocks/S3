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


class AmazonS3Upload(Block):

    version = VersionProperty("1.0.0")
    creds = ObjectProperty(
        AWSCreds, title="AWS Credentials", default=AWSCreds())

    # Path to file on local machine
    file_name = StringProperty(title="File to Upload", default="")
    # S3 bucket to upload to
    bucket_name = StringProperty(title="Bucket Name", default="")
    # What to name file in S3 bucket
    key = StringProperty(title="S3 File Key", default="")

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
                self.logger.debug("Uploading {} to the {} bucket".format(
                    self.file_name(signal), self.bucket_name(signal)))
                self.client.upload_file(
                    self.file_name(signal),
                    self.bucket_name(signal),
                    self.key(signal))
            except:
                self.logger.exception("File upload failed")
        # self.notify_signals

    # How does the relative path stuff work?
        # How will nio access file to upload?
    # I have no idea what the key is
