                        Employee Leave Request System

Endpoint 1: <url> /leaverequest/ Only employee is allowed to create his/her leave
Method POST
Headers:[
‘Authorizaition’:’Token <Token from admin panel>’
]
Data body:
{
  "leave_type":"",
  "leave_description":"",
  "leave_from":"",Format<YYYY-MM-D>
  "leave_to":"" Format<YYYY-MM-D>
}

Endpoint 2: <url> /leaverequest/ Only employee is allowed to fetch his/her all leave requests with their status
Method GET
Headers:[
‘Authorizaition’:’Token <Token from admin panel>’
]

Endpoint 3: <url> / leaverequestsview/ Only admin is allowed to fetch all leave requests with their status
Method GET
Headers:[
‘Authorizaition’:’Token <Token from admin panel>’
]

Endpoint 4: <url> / leaverequestapproval/<leaveid>/  Only admin is allowed approv the leave request
Method PATCH
Headers:[
‘Authorizaition’:’Token <Token from admin panel>’
]

Endpoint 4: <url> / leaverequestrejection/<leaveid>/  Only admin is allowed reject  the leave request
Method PATCH
Headers:[
‘Authorizaition’:’Token <Token from admin panel>’
]



