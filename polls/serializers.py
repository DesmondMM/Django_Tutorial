from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.response import Response
from .models import Question, Choice
from django.db.models import F


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('question', 'choice_text', 'votes', 'id')

    def create(self, validated_data):
        choice =  Choice(
            question=validated_data['question'],
            choice_text=validated_data['choice_text'],
            votes=validated_data['votes'],
            id=validated_data['id']
        )
        choice.save()
        return choice


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