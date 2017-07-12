from nio.util.discovery import discoverable

from .amazon_s3_base_block import AmazonBase


@discoverable
class AmazonS3Download(AmazonBase):

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
