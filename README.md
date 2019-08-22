# Lambda Task To Copy S3 Object From One AWS Account To Another

This lambda task is designed to copy objects from one AWS account (source S3 bucket) to another 
AWS account (destination S3 bucket). The advantage is that it can be used to automate certain tasks, such 
as automatically backing up files in one S3 bucket to another on a schedule.

# Instructions

1. Add the following Bucket Policy to the Source S3 Bucket, replacing the necessary
names in brackets.

`{
    "Version": "2012-10-17",
    "Id": "Policy1546558291129",
    "Statement": [
        {
            "Sid": "Stmt1546558287955",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::<account-id>:user/<username>"
            },
            "Action": [
		"s3:ListBucket",
		"s3:GetObject"
	    ],
            "Resource": [
                "arn:aws:s3:::<source-bucket-name>",
                "arn:aws:s3:::<source-bucket-name>/*"
            ]
        }
    ]
}`

2. Add the following Bucket Policy to the Destination S3 Bucket, replacing the necessary
names in brackets.

`{
    "Version": "2012-10-17",
    "Id": "Policy22222222222",
    "Statement": [
        {
            "Sid": "Stmt22222222222",
            "Effect": "Allow",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::<account-id>:user/<user>",
                    "arn:aws:iam::<account-id>:role/<lambda-role>"
                ]
            },
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::<destination-bucket-name>",
                "arn:aws:s3:::<destination-bucket-name>/*"
            ]
        }
    ]
}`


3. Create a Lambda task with the code given. Uses a Python 3.7 Runtime. Choose a Lambda role with the required permissions.
Input all required options. 

4. (Optional) To run on a schedule, create a CloudWatch Rule and select the Lambda task.
