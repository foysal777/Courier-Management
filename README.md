# Courier Management System

Develop a scalable RESTful backend API for a Courier Management System.
 The system must support multiple roles and allow users to place and track orders, delivery men to manage assigned orders, and admins to manage the entire system.


# API EndPoint
- https://courier-management-eight.vercel.app/admin   ( username = admin , password = 123 )
- POST https://courier-management-eight.vercel.app/api/token/
  - Postman credentials
  - username : admin
  - password : 123

  
- POST https://courier-management-eight.vercel.app/api/token/refresh/
  -  postman credential
  -  refresh : your refesh token is here

   
- POST https://courier-management-eight.vercel.app/api/register/
  - postman credential
  - username , password , password2, email , first_name , last_name  , role

  
- POST https://courier-management-eight.vercel.app/api/profile-update/
   - postman credential
   - Authorization : token barer (N.B. token will be expired every 5 minutes) 
   - header : content-type : application/json
   
 - POST https://courier-management-eight.vercel.app/api/orders/
   -Postman Credential
   - Must be authenticated by access token authorisation & headers
   - pickup_address ,delivery_address ,price  use this form data or json  
   

   
 - GET https://courier-management-eight.vercel.app/api/my_orders/
    - postman credential
    - Must be authenticated by access token authorisation & headers (GET request )
   
 - https://courier-management-eight.vercel.app/api/my_assigned_orders/
     - Must be give token delivery man
     - get request
     - authorization & headers add 
      
   
 - https://courier-management-eight.vercel.app/api/orders/1/update_status/
    - must be use patch request
    - need admin token
    - give actual params
    - authorization & headers included
    
 - https://courier-management-eight.vercel.app/api/all_orders/
     - must to add admin access token
     - get request
     - authorisation & header add 

   
 - https://courier-management-eight.vercel.app/api/ad/1/assign_order/
     - Patch request
     - use admin token
     - add credential  delivery_id:2
        

   
 - https://courier-management-eight.vercel.app/api/stripe-payment/
    - Get request
    - authorisation & pass token must
    - see the checkout Url , click to see stripe payment gateway
  
      
 - https://courier-management-eight.vercel.app/api/success/

     - get request
     - see html successfull page
     - 
 - https://courier-management-eight.vercel.app/api/cancel/      
     -get request
     - see the html cancel page
 
  

