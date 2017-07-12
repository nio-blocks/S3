from nio.properties import (VersionProperty, StringProperty,
                            ObjectProperty)
from .amazon_base_block import AmazonBase, AWSCreds
from nio.util.discovery import discoverable


@discoverable
class AmazonS3(AmazonBase):

    version = VersionProperty("1.0.0")
    creds = ObjectProperty(
        AWSCreds, title="AWS Credentials", default=AWSCreds())

    # Should these properties be in the base block?
    # Path to file on local machine
    file_name = StringProperty(title="S3 File Name", default="")
    # S3 bucket to upload to
    bucket_name = StringProperty(title="Bucket Name", default="bucket")
    # What to name file in S3 bucket
    key = StringProperty(title="S3 File Key", default="")

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
