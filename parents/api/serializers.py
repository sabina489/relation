from rest_framework import serializers
from parents.models import Parents, Children, GrandParent, Siblings

class GrandParentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parents
        fields = (
            "name",
            "age",
        )

class ParentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parents
        fields = (
            "name",
            "age",
            "parent",
        )

class ChildrenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Children
        fields = (
            "name", 
        )

class SiblingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Parents
        fields = (
            "name",
            "age",
        )