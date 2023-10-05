# AWS IAM Identity Center Account Management

This code allows for managing the accounts assigned to a permission set in AWS IAM Identity Center. It provides functions for:

- Getting all accounts in an AWS Organizations OU
- Assigning all accounts in an OU to a permission set
- Removing a specific account from a permission set 

## Prerequisites

- AWS CLI configured with credentials that have permissions to call AWS Organizations and AWS IAM Identity Center
- Python 3.7+
- boto3 Python library


## Installation

```
pip install boto3
``` 

## Usage

```
python3 sso-permission-set-automation.py
``` 

## To use this in AWS Lambda:

1. Create a AWS Lambda function using Runtime Python 3.10
2. Add the required permissions and environment variables ( small code changes requered)
3. Test invoking the AWS Lambda function
