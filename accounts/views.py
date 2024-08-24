from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SignupSerializer,LoginSerializer
from rest_framework import status

class SignupView(APIView):
    def post(self,request):
        try:
            data=request.data 
            serializer = SignupSerializer(data=data)
            
            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':'error has occured'
                },status=status.HTTP_400_BAD_REQUEST)
                
            serializer.save()
        
            return Response({
                'data':{},
                'message' : 'your account is created'
            },status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response({
                    'data':{},
                    'message':'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)
            

class LoginView(APIView):
    def post(self,request):
        try:
            data=request.data 
            serializer =LoginSerializer(data=data)
            
            if not serializer.is_valid():
                return Response({
                    'data':serializer.errors,
                    'message':'error has occured'
                },status=status.HTTP_400_BAD_REQUEST)
                
         
            return Response({   
                                'data':"Login Successfull"
                                                },status.HTTP_200_OK)
        
        except Exception as e:
            return Response({
                    'data':{},
                    'message':'something went wrong'
                },status=status.HTTP_400_BAD_REQUEST)       
                