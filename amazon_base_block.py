import boto3
from nio.block.base import Block
from nio.properties import (VersionProperty, PropertyHolder, StringProperty,
                            ObjectProperty)
from nio.util.discovery import not_discoverable


# What is PropertyHolder?
class AWSCreds(PropertyHolder):
    aws_access_key_id = StringProperty(
        title="Access Key ID", default="", allow_none=False)
    aws_secret_access_key = StringProperty(
        title="Secret Access Key", default="", allow_none=False)
    aws_session_token = StringProperty(
        title="Session Token", default="", allow_none=False)


@not_discoverable
class AmazonBase(Block):
    """ This is the base block for integrating n.io with AWS"""
    version = VersionProperty('1.0.0')
    creds = ObjectProperty(
        AWSCreds, title="AWS Credentials", default=AWSCreds())

    def __init__(self):
        self.boto3 = boto3
        super().configure()
        super().__init__()

    def configure(self):
        self.client = self.boto3.client(
            's3',
            aws_access_key_id=self.creds().aws_access_key_id(),
            aws_secret_access_key=self.creds().aws_secret_access_key(),
            aws_session_token=self.creds().aws_secret_access_key())
