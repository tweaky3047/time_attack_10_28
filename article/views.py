from django.shortcuts import render
from rest_framework.views import APIView

from article.serializers import ArticleSerializer, ArticleCreateSerializer
from .models import Article
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = ArticleCreateSerializer(data = request.data)
        if serializer.is_valid():
            
            serializer.save(author=request.user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
