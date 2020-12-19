  
import datetime
from .serializers import UserSignupSerializer, UserLoginSerializer, OpenAccountSerializer, DepositMoneySerializer
from django.http import HttpResponse
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .models import User, Accounts, Transaction
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status, authentication
from rest_framework.authtoken.models import Token
from django.db import IntegrityError, transaction
from .email  import send_email
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


