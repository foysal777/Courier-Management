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
      
 - 
 - https://courier-management-eight.vercel.app/api/orders/1/update_status/
 - https://courier-management-eight.vercel.app/api/all_orders/
 - https://courier-management-eight.vercel.app/api/ad/1/assign_order/
 - https://courier-management-eight.vercel.app/api/stripe-payment/
 - https://courier-management-eight.vercel.app/api/success/
 - https://courier-management-eight.vercel.app/api/cancel/      
 - 
 
  

