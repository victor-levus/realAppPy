
from email.policy import default
from rest_framework import serializers

from betcodes.models import BetCode, FootballClub, BookCodeInfo, Likes, Post, Comment, Reply


class BetCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = BetCode
        fields = ['id', 'home_team', 'away_team', 'bet', 'odd', 'ht_home_score',
                  'ht_away_score', 'ft_home_score', 'ft_away_score', 'remark', 'match_time']


class BookCodeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookCodeInfo
        fields = ['book_code', 'total_odd', 'ticket_date']


class ReplySerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Reply
        fields = ['id', 'user', 'description', 'placed_at', 'updated_at']

    def create(self, validated_data):
        comment_id = self.context['comment_id']
        user_id = self.context['user_id']
        return Reply.objects.create(comment_id=comment_id, user_id=user_id.id, **validated_data)


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'description', 'placed_at']

    def create(self, validated_data):
        post_id = self.context['post_id']
        user_id = self.context['user_id']
        return Comment.objects.create(post_id=post_id, user_id=user_id.id, **validated_data)


class CreateCommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Comment
        fields = ['user', 'description']

    def create(self, validated_data):
        post_id = self.context['post_id']
        user_id = self.context['user_id']
        return Comment.objects.create(post_id=post_id, user_id=user_id.id, **validated_data)


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Likes
        fields = ['id', 'user', 'likes', 'placed_at']

    def create(self, validated_data):
        post_id = self.context['post_id']
        user_id = self.context['user_id']
        verify_like = Likes.objects.filter(user_id=user_id.id)

        if (verify_like):
            return NULL
        else:
            return Likes.objects.create(post_id=post_id, user_id=user_id.id, **validated_data)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes = LikeSerializer(many=True, read_only=True)
    user = serializers.CharField(read_only=True)

    def create(self, validated_data):
        user_id = self.context['user_id']
        return Post.objects.create(user_id=user_id.id, **validated_data)

    class Meta:
        model = Post
        fields = ['id', 'user', 'description',
                  'placed_at', 'comments', 'likes']


class FootballClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = FootballClub
        fields = ['club_name', 'country',
                  'continent', 'domestic_league', 'logo']
