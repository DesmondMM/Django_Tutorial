from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator

from .models import Question, Choice


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice


    def create(self, validated_data):
        poll = validated_data["question"]
        choice = validated_data["choice"]
        if not choice in poll.choices.all():
            raise serializers.ValidationError('Choice must be valid.')
        vote = super(VoteSerializer, self).create(validated_data)
        return vote

class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Question

    def create(self, validated_data):
        choice_strings = self.context.get("request").data.get("choice_strings")
        if not choice_strings:
            raise serializers.ValidationError('choice_strings needed.')
        poll = super(QuestionSerializer, self).create(validated_data)
        for choice in choice_strings:
            Choice.objects.create(poll=poll, choice_text=choice)
        return poll



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user