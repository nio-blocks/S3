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
    file_name = StringProperty(title="S3 File Name", default="")
    key = StringProperty(title="S3 File Key", default="")
    bucket_name = StringProperty(title="Bucket Name", default="bucket")

    def process_signals(self, signals):
        for signal in signals:
            try:
                self.logger.debug("Uploading {} to the {} bucket".format(
                    self.file_name(signal), self.bucket_name(signal)))
                self.client.upload_file(
                    self.bucket_name(signal),
                    self.key(signal),
                    self.file_name(signal))
            except:
                self.logger.exception("File upload failed")
                # self.notify_signals
