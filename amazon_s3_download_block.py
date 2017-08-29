from nio.properties import FileProperty, VersionProperty
from nio.util.discovery import discoverable

from .amazon_s3_base_block import S3Base


@discoverable
class S3Download(S3Base):
    """Download files stored in S3
        User needs to specify bucket, file key in S3, and the path to where the
        file should be downloaded."""

    # Path to place file on local machine
    file_name = FileProperty(
        title="Path to Download Into", default="etc/download.txt")
    version = VersionProperty('0.0.1')

    def process_signals(self, signals):
        for signal in signals:
            try:
                self.logger.debug("Downloading {} from the {} bucket".format(
                    self.key(signal), self.bucket_name(signal)))
                self.client.download_file(
                    self.bucket_name(signal),
                    self.key(signal),
                    self.file_name(signal).value)
            except:
                self.logger.exception("File download failed")
