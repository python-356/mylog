from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import status  # 状态码
from rest_framework.response import Response # 响应

from log import models
from log import serializers

# Create your views here.

# viewsets
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# FBV api_view
@api_view(["get"])
def article_list(request):
    """
    获取所有文章
    :param request:
    :return: 所有文章信息
    """
    if request.method == "get":
        response_data =  serializers.UserSerializer(instance=models.Article.objects.all(),many=True)  # many=True 序列化多个对象
        return Response(response_data.data, status=status.HTTP_200_OK)


def article_detail(request):
    pass