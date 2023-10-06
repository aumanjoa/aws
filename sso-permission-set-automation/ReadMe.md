# AWS IAM Identity Center Account Management

This code allows for managing the accounts assigned to a permission set in AWS IAM Identity Center. It provides functions for:

- Getting all accounts in an AWS Organizations OU
- Assigning all accounts in an OU to a permission set
- Removing a specific account from a permission set 

## Prerequisites

Prerequisites you need from your AWS account:

- ou_id (str): The ID of the organization unit that you want to add all accounts from to the permission set. (For exmaple ou-ID)
- permission_set_arn (str): The ARN of the permission set that you want to add the accounts to.
- sso_instance_arn (str): The ARN of the AWS SSO instance that the permission set belongs to.
- sso_principle_id (str): The principal ID (user or group) to assign the permission set to.
- accountId_to_remove_from_permission_set (str): The Amazon Web Services account identifier, (For example, 123456789012).

Technical Prerequisites:

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
