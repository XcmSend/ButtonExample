# HTML + JS only button example

This is an example repo on how you can create a button that posts data to a bagpipes scenario and returns the response. In this example the user is querying a pallet on polkadot with an address as input. 

## Bagpipes scenario:
![Bagpipes scenario](/images/bps.png)

### Steps:  
 -  Create a webhook our application can send data to
 -  Query the chain, based on the input the application has sent to the webhook
 -  Send the response from the Query node to an http endpoint 

#### Webhook:  
![](/images/webhook.png)

#### Query node:   
![](/images/query.png)

#### HTTP Node:   
![](/images/http_node.png)         
Set the HTTP url, in this example we will use the example python app that can be found in the `src/` directory.  

![](/images/http_node2.png)     
Drag and drop the eventdata from the query result in the side toolbar.  

Now we want to copy the webhook and http endpoint where we want our response to be sent and copy and paste it in our html file. 

## Button: 
Display the html file:  
![](/images/1.png)

Input an address:  
![](/images/2.png)

View the result:   
![](/images/3.png)


### Bagpipes template link:
https://alpha.bagpipes.io/#/create/?diagramData=eQ2ZKuS-u 



#### Python app:   
Simple PoC app: 

Post data:

POST `/mempool/<uuid>`:
```shell
curl -X POST \
   https://flipchan.pythonanywhere.com/mempool/blue123 \
  -H 'Content-Type: application/json' \
  -d '{
        "requestContent": "{\"nonce\":\"10\",\"consumers\":\"0\",\"providers\":\"1\",\"sufficients\":\"0\",\"data\":{\"free\":\"10,033,245,663\",\"reserved\":\"0\",\"frozen\":\"0\",\"flags\":\"170,141,183,460,469,231,731,687,303,715,884,105,728\"},\"chainKey\":\"polkadot\",\"palletName\":\"System\",\"methodName\":\"Account\",\"params\":\"setme\",\"atBlock\":null}"
      }'
```




GET `/loot/<uuid>`:   
```shell 
curl -X GET \
  https://flipchan.pythonanywhere.com/loot/blue123
```

Download the data that was previously posted. 



### With threadbag: 
You can: 
  - 1: Create a scenario with the main UI. 
  - 2: Copy the link and save the scenario id (the unique identifier at the end of the link)   
  - 3: Start the scenario with threadbag: 
`curl -X POST -H "Content-Type: application/json" -d '{"id": "LSm-41cJY"}' http://th-0.bagpipes.io/job/start -v`
   - 4: Send the accoundid32 public key with the threadbag_result.html file. 
   - 5: Query threadbag for the result: 
```shell
curl -X POST -H "Content-Type: application/json" -d '{"id": "LSm-41cJY", "log_type": "query"}' https://th-0.bagpipes.io/scenario/get_filter_logs
```
   - 6: Display result to user 






