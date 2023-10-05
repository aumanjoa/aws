# AWS SSO Account Management

This code allows for managing the accounts assigned to a permission set in AWS SSO. It provides functions for:

- Getting all accounts in an AWS Organizations OU
- Assigning all accounts in an OU to a permission set
- Removing specific accounts from a permission set 

## Prerequisites

- AWS CLI configured with credentials that have permissions to call Organizations and SSO
- Boto3 installed