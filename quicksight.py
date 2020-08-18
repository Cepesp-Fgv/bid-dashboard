import boto3

from config import AWS_ACCOUNT_ID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY


class QuickSightClient:

    def __init__(self):
        self.quicksight = boto3.client('quicksight', region_name='us-east-1', aws_access_key_id=AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

    def describe_user(self, email):
        return self.quicksight.describe_user(
            UserName=email,
            AwsAccountId=str(AWS_ACCOUNT_ID),
            Namespace='default'
        )

    def get_dashboard_embed_url(self, user_arn, dashboard_id):
        embed_response = self.quicksight.get_dashboard_embed_url(
            AwsAccountId=AWS_ACCOUNT_ID,
            DashboardId=dashboard_id,
            IdentityType='QUICKSIGHT',
            SessionLifetimeInMinutes=300,
            UndoRedoDisabled=True,
            ResetDisabled=True,
            UserArn=user_arn
        )

        return embed_response['EmbedUrl']
