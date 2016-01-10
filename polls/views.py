from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


from .models import Choice, Question
from polls.serializers import QuestionSerializer, ChoiceSerializer,\
    VoteSerializer,UserSerializer

class RestrictedView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        data = {
            'foo': 'bar'
        }

        return Response(data)

class QuestionList(generics.ListCreateAPIView):

    """
    List all polls, or create a new poll.
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveDestroyAPIView):
    """
    Create a Poll, delete a poll
    """

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceList(generics.ListCreateAPIView):

    """
    List all polls, or create a new poll.
    """

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class ChoiceDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieves a Choice, Updates a Choice
    """

    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateChoice(generics.CreateAPIView):
    """
    Create a vote
    """

    serializer_class = VoteSerializer


class UserCreate(generics.CreateAPIView):
    """
    Create an User
    """

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
        """
        Retrieve a User
        """

        queryset = User.objects.all()
        serializer_class = UserSerializer


