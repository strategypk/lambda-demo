import json
def lambda_handler(event, context):
    print("Received Billing Amount ")
    json.dumps(event, indent=2)
    print(event["transactiontype"])
    if event['transactiontype']== 'BUY' :
        # buy indicator
        print("Transaction Type - BUY")
        result = event['stockprice'] + event['commission']
    elif event['transactiontype']== 'SELL':
        # sell indicator
        print("Transaction Type - SELL")
        result = event['stockprice'] - event['commission']
    else :
        result = event['stockprice'] + event['commission']*0.20
    print("Total Billable : ", result)
    return result
# test data 5
# lambda_handler({"stockprice":200,"commission":10, "transactiontype":"BUY"}, context=1)
# lambda_handler({"stockprice":200,"commission":10, "transactiontype":"SELL"}, context=1)
# lambda_handler({"stockprice":200,"commission":10, "transactiontype":"OTHERS"}, context=1)

print('Version 1.7')