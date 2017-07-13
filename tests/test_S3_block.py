from unittest.mock import patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..amazon_s3_upload_block import S3Upload
from ..amazon_s3_download_block import S3Download


class TestS3(NIOBlockTestCase):

    def test_upload_file(self):
        """Signals pass through block unmodified."""
        blk = S3Upload()
        self.configure_block(blk, {"file_name": "{{ $file_name }}"})
        blk.start()
        with patch.object(blk, "client") as patched_client:
            blk.process_signals([Signal({
                "file_name": "etc/testupload.txt",
                "bucket_name": "bucket.n.io",
                "key": "filename.css",
            })])

            patched_client.upload_file.assert_called_once_with(
                "etc/testupload.txt",
                "bucket.n.io",
                "filename.css")

        blk.stop()
        self.assert_num_signals_notified(0)

    def test_download_file(self):
        """Signals pass through block unmodified."""
        blk = S3Download()
        self.configure_block(blk, {"file_name": "{{ $file_name }}"})
        blk.start()
        with patch.object(blk, "client") as patched_client:
            blk.process_signals([Signal({
                "file_name": "etc/testdownload.txt",
                "bucket_name": "bucket.n.io",
                "key": "filename.css",
            })])

            patched_client.download_file.assert_called_once_with(
                "bucket.n.io",
                "filename.css",
                "etc/testdownload.txt")

        blk.stop()
        self.assert_num_signals_notified(0)
