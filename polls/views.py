from django.contrib.auth.models import User
from rest_framework import generics

from .models import Choice, Question
from polls.serializers import QuestionSerializer, ChoiceSerializer,\
    VoteSerializer,UserSerializer

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


