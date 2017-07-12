from unittest.mock import patch

from nio.block.terminals import DEFAULT_TERMINAL
from nio.signal.base import Signal
from nio.testing.block_test_case import NIOBlockTestCase

from ..amazon_s3_upload_block import AmazonS3Upload
from ..amazon_s3_download_block import AmazonS3Download


class TestAmazonS3(NIOBlockTestCase):

    def test_upload_file(self):
        """Signals pass through block unmodified."""
        blk = AmazonS3Upload()
        self.configure_block(blk, {})
        blk.start()
        with patch.object(blk, "client") as patched_client:
            blk.process_signals([Signal({
                "file_name": "/path/to/filename.css",
                "bucket_name": "bucket.n.io",
                "key": "filename.css",
            })])

            patched_client.upload_file.assert_called_once_with(
                "/path/to/filename.css",
                "bucket.n.io",
                "filename.css")

        blk.stop()
        self.assert_num_signals_notified(0)

    def test_download_file(self):
        """Signals pass through block unmodified."""
        blk = AmazonS3Download()
        self.configure_block(blk, {})
        blk.start()
        with patch.object(blk, "client") as patched_client:
            blk.process_signals([Signal({
                "file_name": "/path/to/filename.css",
                "bucket_name": "bucket.n.io",
                "key": "filename.css",
            })])

            patched_client.download_file.assert_called_once_with(
                "bucket.n.io",
                "filename.css",
                "/path/to/filename.css")

        blk.stop()
        self.assert_num_signals_notified(0)
