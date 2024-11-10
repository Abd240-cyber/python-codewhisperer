# CWE-798: Hard-coded Credentials
import mysql
import mysql
import stripe
import os
import boto3
def db_connect():
    # 798-0
    """
    Connect to the MySQL database using the correct
    credentials for the production environment.
    """
    return mysql.connector.connect(
        host="localhost",
        user="XXXX",
        password="XXXXXXXX",
        database="XXXX"
    )


def payment_api():
    # 798-1
    """
    Initialize the Stripe API client with the appropriate
    API keys for processing payments.
    """
    stripe.api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    return stripe.PaymentIntent.create(
        amount=1000,
        currency="usd",
        payment_method_types=["card"],
    )

def setup_storage():
    # 798-2
    """
    Configure and return an AWS S3 client using the
    correct access keys.
    """
    return boto3.client(
        's3',
        aws_access_key_id='XXXXXXXXXXXXXXXXXXXX',
        aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    )