import boto3
import os

rds_client = boto3.client("rds")

CLUSTER_ID = os.getenv("perf-group-el", "perf-group-el")

def lambda_handlers():
    response = rds_client.start_db_cluster(DBClusterIdentifier=CLUSTER_ID)
    print("Stopped cluster {CLUSTER_ID}", "response", response)

lambda_handlers()

