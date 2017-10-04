S3Download
==========
Blocks to download files from an Amazon S3 bucket.  You will need an AWS account and credentials for the block to function.

Properties
----------
- **bucket_name**: S3 Bucket to interact with.
- **creds**: AWS credentials to sign into Amazon S3 service.
- **file_name**: Path and file on local machine to download into.
- **key**: Name of file inside S3.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
None

Commands
--------
None

S3Upload
========
Blocks to upload files to an Amazon S3 bucket.  You will need an AWS account and credentials for the block to function.

Properties
----------
- **bucket_name**: S3 Bucket to interact with.
- **creds**: AWS credentials to sign into Amazon S3 service.
- **file_name**: Path and file on local machine to upload.
- **key**: Name of file inside S3.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
None

Commands
--------
None

Dependencies
------------
boto3

