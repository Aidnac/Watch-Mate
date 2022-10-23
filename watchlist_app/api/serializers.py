from rest_framework import serializers

from watchlist_app.models import WatchList, StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()

    class Meta:
        model = WatchList
        fields = "__all__"

        # fields = ['id', 'name', 'description']
        # exclude = ['name']

        # Object level validation
    #
    # def get_len_name(self, object):
    #     length = len(object.name)
    #     return length
    #
    # def validate(self, attrs):
    #     if attrs['name'] == attrs['description']:
    #         raise serializers.ValidationError("Title and Description cannot be the same")
    #     else:
    #         return attrs
    #
    # # Field level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     return value


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    # if you want to return only one field
    # watchlist = serializers.StringRelatedField(many=True)
    # if you want to return only links
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='movie-detail'
    # )
    class Meta:
        model = StreamPlatform
        fields = "__all__"

# # Field level validation
# def name_lenth(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")
#     return value
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_lenth])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     # Object level validation
#     def validate(self, attrs):
#         if attrs['name'] == attrs['description']:
#             raise serializers.ValidationError("Title and Description cannot be the same")
#         else:
#             return attrs
#
#     # Field level validation
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     return value
