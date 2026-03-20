import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
    
    # Configuration
    SNS_TOPIC_ARN = 'PASTE-YOUR-SNS-ARN-HERE'
    COST_THRESHOLD = 5.00
    
    try:
        # Get billing metric from CloudWatch
        cw_client = boto3.client(
            'cloudwatch', 
            region_name='us-east-1'
        )
        
        # Get estimated charges
        response = cw_client.get_metric_statistics(
            Namespace='AWS/Billing',
            MetricName='EstimatedCharges',
            Dimensions=[
                {
                    'Name': 'Currency',
                    'Value': 'USD'
                }
            ],
            StartTime=datetime.now().replace(
                day=1, hour=0, minute=0
            ),
            EndTime=datetime.now(),
            Period=86400,
            Statistics=['Maximum']
        )
        
        # Get latest cost
        datapoints = response['Datapoints']
        
        if datapoints:
            latest = sorted(
                datapoints,
                key=lambda x: x['Timestamp']
            )[-1]
            total_cost = latest['Maximum']
        else:
            total_cost = 0.0
        
        # Build email message
        today = datetime.now().strftime('%Y-%m-%d')
        
        if total_cost > COST_THRESHOLD:
            subject = f"ALERT: AWS Cost ${total_cost:.2f} exceeded limit!"
            message = f"""
AWS Cost Monitor ALERT!
=======================
Date: {today}
Account: Mithun AWS Account

Total Estimated Cost: ${total_cost:.2f}

WARNING: Your cost has exceeded
the threshold of ${COST_THRESHOLD}!

Action Required:
1. Check unused EC2 instances
2. Check unused RDS databases
3. Review S3 storage
4. Delete unused resources

Stay within free tier limits!
"""
        else:
            subject = f"AWS Cost Report: ${total_cost:.2f} this month"
            message = f"""
AWS Cost Monitor Report
=======================
Date: {today}
Account: Mithun AWS Account

Total Estimated Cost: ${total_cost:.2f}
Cost Threshold: ${COST_THRESHOLD:.2f}

Status: Within Limit!

Your AWS costs are looking good!
Keep monitoring regularly!

Services to watch:
- EC2 instances
- RDS databases
- S3 storage
- Lambda functions
"""
        
        # Send email via SNS
        sns_client = boto3.client(
            'sns',
            region_name='eu-north-1'
        )
        
        sns_client.publish(
            TopicArn=SNS_TOPIC_ARN,
            Message=message,
            Subject=subject
        )
        
        print(f"Cost: ${total_cost:.2f}")
        print(f"Email sent successfully!")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'total_cost': total_cost,
                'threshold': COST_THRESHOLD,
                'alert_sent': total_cost > COST_THRESHOLD,
                'message': 'Cost report sent!'
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }
```

---

## Important! 

### Replace SNS ARN:
1. Go to **SNS → Topics**
2. Click **mithun-cost-alerts**
3. Copy **ARN** from top:
```
arn:aws:sns:eu-north-1:
691778448681:mithun-cost-alerts
