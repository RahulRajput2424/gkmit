# gkmit

----------------------------------------------------
User SignUp - Post
----------------------------------------------------
SignUp: URL: http://127.0.0.1:8000/spiceApp/user_signup_view/ 

Param= {
    "email":"user@gmail.com", 
    "mobileNumber":7858588481, 
    "username":"user1", 
    "password":"user"
}

Response :-

{
    "status": 200,
    "message": "Successfully Created, Please Sign-In`",
    "data": {
        "email": "rahul1@gmail.com",
        "mobileNumber": "2233223300",
        "password": "pbkdf2_sha256$216000$ig2i25IxGE9a$ym97uoUKkpuISmDpsZbpTnsyYGb4ph/Jlc26O6jZa7I=",
        "username": "rahulrajput1"
    }
}
----------------------------------------------------
User Login - Post
----------------------------------------------------

2- Login: URL: http://127.0.0.1:8000/spiceApp/user_login_view/ 

{
    "email": "user@gmail.com", "password":"user"
}
Response : -

{
    "data": {
        "message": "You have logged in successfully.",
        "token": "(<Token: 7efe74277c786f291eb1fb8066622b32cc238a44>, True)"
    },
    "status": 200
}

----------------------------------------------------
Bank Account Opening - Post
----------------------------------------------------

3- URL: http://127.0.0.1:8000/gkmitApp/open-account/
{
    "user": "1", "account_balance":"500
}
Response : -
{
    "id": 9,
    "account_id": "9845e886-c49f-42de-b8cc-ff893b778104",
    "account_balance": "500.00",
    "created_at": "2020-12-20T11:52:11.500822Z",
    "user": 1
}
----------------------------------------------------
Deposit  Monet - Post
----------------------------------------------------

4- URL: http://127.0.0.1:8000/gkmitApp/deposit-money/
{
    "transaction_amount": "1000", "account_id":"263fdb63-9767-4801-a064-c6ae11e72b37"
}
Response :-
{
    "message": "Money Successfully Deposit",
    "status": true,
    "Current Balance": 1000.0,
    "data": {
        "id": 65,
        "transaction_id": "a1abd53b-0e48-4b74-bb9e-6ac13503ed70",
        "transaction_timestamp": "2020-12-20T11:47:00.412750Z",
        "transaction_amount": "1000.00",
        "account": 8
    }
}
----------------------------------------------------
Withdraw Money - Post
----------------------------------------------------

5- URL: http://127.0.0.1:8000/gkmitApp/withdraw-money/
{
     "transaction_amount": "1000", "account_id":"263fdb63-9767-4801-a064-c6ae11e72b37"
}
Response

{
    "message": "Money Successfully Debited",
    "status": true,
    "Current Balance": 980.0,
    "data": {
        "id": 66,
        "transaction_id": "80e56e05-a2f4-404f-9e95-681c01bfa5bc",
        "transaction_timestamp": "2020-12-20T11:48:50.492777Z",
        "transaction_amount": "20.00",
        "account": 8
    }
}
----------------------------------------------------
Bank Account Detail - Get
----------------------------------------------------

6 - URL: http://127.0.0.1:8000/gkmitApp/balance-detail/?account_id=263fdb63-9767-4801-a064-c6ae11e72b37

Response : 
{
    "Account Balance": 980.0,
    "Account Created": "2020-12-19T20:42:54.464310Z",
    "Username": "hima",
    "email": "hima@gmail.com",
    "mobile number": "4433443323",
    "status": true
}
----------------------------------------------------
Transaction History - Get
----------------------------------------------------

7- URL: http://127.0.0.1:8000/gkmitApp/transaction-history/?start_date=2020-12-10&end_date=2020-12-20

Note -- This request will also download the csv file with all the transaction detail 
Response : [
    {
        "Transaction Id": "cc8af749-b8ba-4215-871d-39ef442b359a",
        "Transaction Amount": 3000.0,
        "Account Id": "263fdb63-9767-4801-a064-c6ae11e72b37",
        "Account Balance": 980.0,
        "Username": "hima",
        "email": "hima@gmail.com",
        "mobile number": "4433443323",
        "transaction_timestamp": "2020-12-19T20:48:36.825159Z"
    },
    {
        "Transaction Id": "76905c0d-5f86-4441-80ef-616d4ef63e92",
        "Transaction Amount": 3000.0,
        "Account Id": "263fdb63-9767-4801-a064-c6ae11e72b37",
        "Account Balance": 980.0,
        "Username": "hima",
        "email": "hima@gmail.com",
        "mobile number": "4433443323",
        "transaction_timestamp": "2020-12-19T20:50:50.987644Z"
    },
    {
        "Transaction Id": "ae45fda4-cb6b-4a9d-90e0-096935956b36",
        "Transaction Amount": 3000.0,
        "Account Id": "263fdb63-9767-4801-a064-c6ae11e72b37",
        "Account Balance": 980.0,
        "Username": "hima",
        "email": "hima@gmail.com",
        "mobile number": "4433443323",
        "transaction_timestamp": "2020-12-19T20:56:47.780453Z"
    },
    {
        "Transaction Id": "da2fb92e-24a8-4d25-a64f-7c6a693244a7",
        "Transaction Amount": 3000.0,
        "Account Id": "263fdb63-9767-4801-a064-c6ae11e72b37",
        "Account Balance": 980.0,
        "Username": "hima",
        "email": "hima@gmail.com",
        "mobile number": "4433443323",
        "transaction_timestamp": "2020-12-19T21:25:44.193086Z"
    },
    {
        "Transaction Id": "b375b9a2-502d-46fc-9e65-49cb88f5f0fb",
        "Transaction Amount": 3000.0,
        "Account Id": "263fdb63-9767-4801-a064-c6ae11e72b37",
        "Account Balance": 980.0,
        "Username": "hima",
        "email": "hima@gmail.com",
        "mobile number": "4433443323",
        "transaction_timestamp": "2020-12-19T21:27:30.643345Z"
    },
    {
        "Transaction Id": "44d6be57-141f-4909-a334-479d80687748",
        "Transaction Amount": 3000.0,
        "Account Id": "263fdb63-9767-4801-a064-c6ae11e72b37",
        "Account Balance": 980.0,
        "Username": "hima",
        "email": "hima@gmail.com",
        "mobile number": "4433443323",
        "transaction_timestamp": "2020-12-19T21:28:17.183577Z"
    },
    {
        "Transaction Id": "65662bef-4440-4756-a398-2c05ebc96c1a",
        "Transaction Amount": 3000.0,
        "Account Id": "263fdb63-9767-4801-a064-c6ae11e72b37",
        "Account Balance": 980.0,
        "Username": "hima",
        "email": "hima@gmail.com",
        "mobile number": "4433443323",
        "transaction_timestamp": "2020-12-19T21:28:19.006032Z"
    },
    ]
