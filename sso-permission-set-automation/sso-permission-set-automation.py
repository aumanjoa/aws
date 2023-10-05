import boto3

def get_all_accounts_for_ou(ou_id):
  """Gets all accounts for an AWS organization unit.

  Args:
    ou_id: The ID of the organization unit.

  Returns:
    A list of account IDs.
  """

  client = boto3.client('organizations')

  paginator = client.get_paginator('list_accounts_for_parent')

  accounts = []
  for page in paginator.paginate(ParentId=ou_id):
    for account in page['Accounts']:
      accounts.append(account['Id'])

  return accounts


def add_all_accounts_from_ou_to_permission_set(ou_id, permission_set_arn, sso_instance_arn, sso_principle_id):
  """Adds all accounts in an AWS organization unit to a specific permission set.

  Args:
    ou_id (str): The ID of the organization unit.
    permission_set_arn (str): The ARN of the permission set. 
    sso_instance_arn (str): The ARN of the SSO instance.
    sso_principle_id (str): The principal ID (user or group) to assign the permission set to.
  """

  client = boto3.client('sso-admin')

  # Get all accounts in the specified OU.
  accounts = get_all_accounts_for_ou(ou_id)

#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin/client/create_account_assignment.html

  # Assign the permission set to each account.
  for account in accounts:
    client.create_account_assignment(
      InstanceArn=sso_instance_arn,
      PermissionSetArn=permission_set_arn,
      PrincipalId=sso_principle_id,
      PrincipalType='GROUP',
      TargetId=account,
      TargetType='AWS_ACCOUNT'
    )


def remove_accounts_from_permission_set(account, permission_set_arn, sso_instance_arn, sso_principle_id):
  """removes specific account from a sso permission set.

  Args:
    account (str): Amazon Web Services account identifier, (For example, 123456789012).
    permission_set_arn (str): The ARN of the permission set. 
    sso_instance_arn (str): The ARN of the SSO instance.
    sso_principle_id (str): The principal ID (user or group) to assign the permission set to.
  """

  client = boto3.client('sso-admin')

  #https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sso-admin/client/delete_account_assignment.html

  # Assign the permission set to each account.
  client.delete_account_assignment(
      InstanceArn=sso_instance_arn,
      PermissionSetArn=permission_set_arn,
      PrincipalId=sso_principle_id,
      PrincipalType='GROUP',
      TargetId=account,
      TargetType='AWS_ACCOUNT'
    )    

# Example usage:

ou_id = 'ou-ID'
permission_set_arn = 'arn:aws:sso:::permissionSet/ARN'
sso_instance_arn = 'arn:aws:sso:::instance/ARN'
sso_group_id = 'GROUP-ID'


add_all_accounts_from_ou_to_permission_set(ou_id, permission_set_arn, sso_instance_arn, sso_group_id)

remove_accounts_from_permission_set('123456789012', permission_set_arn, sso_instance_arn, sso_group_id)
