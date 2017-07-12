from nio.properties import (VersionProperty, StringProperty,
                            ObjectProperty)
from .amazon_base_block import AmazonBase, AWSCreds
from nio.util.discovery import discoverable


@discoverable
class AmazonS3(AmazonBase):

    version = VersionProperty("1.0.0")
    creds = ObjectProperty(
        AWSCreds, title="AWS Credentials", default=AWSCreds())

    # Bucket in which file is stored
    bucket_name = StringProperty(title="Bucket Name", default="bucket")
    # Name of file in bucket
    key = StringProperty(title="S3 File Key", default="")
    # File to write to on local machine
    file_name = StringProperty(title="S3 File Name", default="")

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
