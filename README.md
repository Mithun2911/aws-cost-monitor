# AWS Cloud Cost Monitor

## Overview
An automated AWS cost monitoring
system that sends daily email
reports and alerts when costs
exceed the defined threshold.

## Architecture

EventBridge (Daily 9 AM trigger)
runs Lambda Function (Python)
which reads CloudWatch Billing Metrics
then sends email via SNS:
- Cost Normal = Daily Report Email
- Cost High = ALERT Email!

## Technologies Used

| Service | Purpose |
|---|---|
| AWS Lambda | Runs monitoring code |
| CloudWatch | Billing metrics source |
| SNS | Email notifications |
| EventBridge | Daily scheduling |
| Python 3.12 | Lambda runtime |
| IAM | Permissions management |

## Features

- Runs automatically every day at 9 AM
- Checks AWS estimated charges
- Sends detailed cost breakdown
- Triggers alert when cost exceeds limit
- Zero manual intervention needed

## Project Structure

- lambda_function.py = Main code
- README.md = Documentation
- architecture.png = Architecture diagram

## How to Deploy

Step 1 - Create SNS Topic
- Go to AWS SNS Console
- Create Standard topic
- Subscribe your email
- Confirm subscription

Step 2 - Create Lambda Function
- Runtime: Python 3.12
- Add CloudWatchReadOnlyAccess policy
- Add AmazonSNSFullAccess policy

Step 3 - Add Code
- Copy lambda_function.py
- Replace SNS_TOPIC_ARN with your ARN
- Deploy function

Step 4 - Schedule with EventBridge
- Add EventBridge trigger
- Schedule: cron(0 9 * * ? *)
- Runs every day at 9 AM UTC

## Sample Email Report

AWS Cost Monitor Report

Date: 2026-03-20

Account: Mithun AWS Account

Total Estimated Cost: $0.00

Cost Threshold: $5.00

Status: Within Limit!

Your AWS costs are looking good!

## What I Learned

- AWS Lambda function development
- CloudWatch metrics API
- SNS email notifications
- EventBridge scheduling
- Python boto3 SDK
- IAM permissions management
- Cloud cost optimization

## Author

Mithundev M R

Portfolio: https://d1y331nvg2x1x9.cloudfront.net

LinkedIn: linkedin.com/in/mithundev-mr
