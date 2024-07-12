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

