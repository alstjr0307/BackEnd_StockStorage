from .models import AuthUser, BlogPostcomment, BlogPosts, BlogPostsLikes, DjangoAdminLog, DjangoContentType, DjangoMigrations, TaggitTaggeditem,TaggitTag
from rest_framework import serializers, viewsets



class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = '__all__'
class AuthUserViewSet(viewsets.ModelViewSet):
    queryset =AuthUser.objects.all()
    serializer_class = AuthUserSerializer



class BlogPostcommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPostcomment
        fields = '__all__'
class BlogPostcommentViewSet(viewsets.ModelViewSet):
    queryset = BlogPostcomment.objects.all()
    serializer_class = BlogPostcommentSerializer

class BlogPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPosts
        fields = '__all__'
class BlogPostsViewSet(viewsets.ModelViewSet):
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer

class BlogPostsLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPostsLikes
        fields = '__all__'
class BlogPostsLikesViewSet(viewsets.ModelViewSet):
    queryset = BlogPostsLikes.objects.all()
    serializer_class = BlogPostsLikesSerializer

class DjangoAdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoAdminLog
        fields = '__all__'
class DjangoAdminLogViewSet(viewsets.ModelViewSet):
    queryset = DjangoAdminLog.objects.all()
    serializer_class = DjangoAdminLogSerializer

class DjangoContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoContentType
        fields = '__all__'
class DjangoContentTypeViewSet(viewsets.ModelViewSet):
    queryset = DjangoContentType.objects.all()
    serializer_class = DjangoContentTypeSerializer

class DjangoMigrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoMigrations
        fields = '__all__'
class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    queryset = DjangoMigrations.objects.all()
    serializer_class = DjangoMigrationsSerializer

class TaggitTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggitTag
        fields = '__all__'
class TaggitTagViewSet(viewsets.ModelViewSet):
    queryset = TaggitTag.objects.all()
    serializer_class = TaggitTagSerializer

class TaggitTaggeditemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaggitTaggeditem
        fields = '__all__'
class TaggitTaggeditemViewSet(viewsets.ModelViewSet):
    queryset = TaggitTaggeditem.objects.all()
    serializer_class = TaggitTaggeditemSerializer