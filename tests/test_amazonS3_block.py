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
        # with patch.object(blk,
            self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal({"hello": "n.io"})])
        blk.stop()
        self.assert_num_signals_notified(1)
        self.assertDictEqual(
            self.last_notified[DEFAULT_TERMINAL][0].to_dict(),
            {"hello": "n.io"})
