Amazon S3
===========

Blocks to upload/download files from Amazon S3.  You will need an AWS account
and credentials for the block to function.

Properties
--------------
**AWS Access Key**(string): Amazon credential

**AWS Secret Access Key**(string): Amazon credential

**Bucket Name**(string): S3 Bucket to interact with

**File Key**(string): Name of file inside S3

**File Name**(string): Path and file on local machine to either upload or download
into


Dependencies
----------------
boto3

Commands
----------------
None

Input
-------
Any list of signals with a file name, key, and bucket name.

Output
---------
The downloaded file, placed in the specified path.