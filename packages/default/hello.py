import signalfx_lambda

@signalfx_lambda.emits_metrics
def lambda_handler(event):
    return {
        'statusCode': 200,
        'body': 'Hello from Nimbella!'
    }
