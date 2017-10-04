from nio.properties import FileProperty, VersionProperty
from nio.util.discovery import discoverable

from .amazon_s3_base_block import S3Base


@discoverable
class S3Upload(S3Base):
    """Upload files into S3
        User needs to specify bucket, file key in S3, and the path to which
        file should be uploaded."""

    # Path to file on local machine
    file_name = FileProperty(
        title="File to Upload", default="etc/upload.txt")
    version = VersionProperty("0.1.1")

    def process_signals(self, signals):
        for signal in signals:
            try:
                self.logger.debug("Uploading {} to the {} bucket".format(
                    self.file_name(signal), self.bucket_name(signal)))
                self.client.upload_file(
                    self.file_name(signal).value,
                    self.bucket_name(signal),
                    self.key(signal))
            except:
                self.logger.exception("File upload failed")
