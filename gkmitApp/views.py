  
import datetime
from datetime import date
from .serializers import UserSignupSerializer, UserLoginSerializer, OpenAccountSerializer, DepositMoneySerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .models import User, Accounts, Transaction
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import status, authentication
from rest_framework.authtoken.models import Token
from django.db import IntegrityError, transaction
from django.db.models import Q
from .email  import send_email
from .permission import *
import csv
class UserSignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    authentication_classes = []
    permission_classes = []

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({
            'status': 200,
            'message': 'Successfully Created, Please Sign-In`',
            'data': response.data
        })

class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token= Token.objects.get_or_create(user=user)
            response = {"data": {"message":"You have logged in successfully.",
													  "token": str(token), 
										},
								"status": 200,}
            return Response(response, status=status.HTTP_200_OK)
        else:
            error_data = serializer.errors
            return Response(data=error_data)

class OpenAccount(CreateAPIView):
    queryset = Accounts.objects.all()
    serializer_class = OpenAccountSerializer
    permission_classes = (IsAuthenticated, )

class DepositMoney(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self,request):
        data = request.data
        account_id = data['account']
        transaction_amount = data['transaction_amount']
        try:
            with transaction.atomic():
                accounts = Accounts.objects.get(account_id=account_id)
                accounts.account_balance = accounts.account_balance + int(transaction_amount)
                accounts.save()
                serializer_data = {"account": accounts.id,"transaction_amount":transaction_amount}
                serializer = DepositMoneySerializer(data=serializer_data)
                if serializer.is_valid():
                    serializer.save()
                    data = serializer.data
                    response = {"message":"Money Successfully Deposit", "status":True,
                                "Current Balance": accounts.account_balance,"data":data}
                    
                    send_email("Money Deposit",response,amount="Credited")
                else:
                    return Response(serializer.errors)
        except IntegrityError:
            response = {"message":"Please try again after some time", "status":False,
                    "Current Balance": accounts.account_balance}
        return Response(response,status=200)        

class WithdrawAmount(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self,request):
        data = request.data
        account_id = data['account']
        transaction_amount = data['transaction_amount']
        try:
            with transaction.atomic():
                accounts = Accounts.objects.get(account_id=account_id)
                accounts.account_balance = accounts.account_balance - int(transaction_amount)
                accounts.save()
                serializer_data = {"account": accounts.id,"transaction_amount":transaction_amount}
                serializer = DepositMoneySerializer(data=serializer_data)
                if serializer.is_valid():
                    serializer.save()
                    data = serializer.data
                    response = {"message":"Money Successfully Debited", "status":True,
                                "Current Balance": accounts.account_balance,"data":data}
                
                    send_email("Money Deposit",response,amount="Debited")
                else:
                    return Response(serializer.errors)
        except IntegrityError:
            response = {"message":"Please try again after some time", "status":False,
                    "Current Balance": accounts.account_balance}
        return Response(response,status=200) 

class AccountDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        account_id = request.query_params.get("account_id")
        try:
            accounts = Accounts.objects.get(account_id=account_id)
            response = {"Account Balance": accounts.account_balance,
                        "Account Created":accounts.created_at,
                        "Username": accounts.user.username,
                        "email": accounts.user.email,
                        "mobile number":accounts.user.mobileNumber,
                        "status":True}
        except:
            response = {"message":"Account dose not exists.", "status":False, "data":{}}
        
        return Response(response, status=200)

class TransactionHistories(APIView):
    permission_classes = [AdminPermission]
    def get(self, request):
        start_date = request.query_params.get("start_date")
        end_date = request.query_params.get("end_date")
        start_dtime = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_dtime  = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        try:
            
            trans_history = Transaction.objects.filter(transaction_timestamp__gte=start_dtime,transaction_timestamp__lte=end_dtime)

            trans_lst = [] 
            file_lst = []
            for t in trans_history:
                response = {"Transaction Id": t.transaction_id,
                        "Transaction Amount":t.transaction_amount,
                        "Account Id" : t.account.account_id,
                        "Account Balance" : t.account.account_balance,
                        "Username": t.account.user.username,
                        "email": t.account.user.email,
                        "mobile number":t.account.user.mobileNumber,
                        "transaction_timestamp": t.transaction_timestamp,
                        }
                trans_lst.append(response)
                flst = [t.transaction_id,t.transaction_amount,t.account.account_id,t.account.account_balance,t.account.user.username,t.account.user.email,t.account.user.mobileNumber, t.transaction_timestamp]
                file_lst.append(flst)
        except Exception as e:
            print(e)
            trans_lst = {"message":"Data does not exist in the give date time range", "status":False, "data":{}}
        print(trans_lst)
        with open('GFG1', 'w') as f:
                write = csv.writer(f)
                write.writerow(['Transaction Id','Transaction Amount', 'Account Id', 'Account Balance','Username','email','mobile number','transaction_timestamp'])
                write.writerows(file_lst)
        return Response(trans_lst, status=200)


