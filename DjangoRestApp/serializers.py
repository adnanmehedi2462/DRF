from DjangoRestApp.models import artical

from rest_framework import serializers

class articalSerializer(serializers.ModelSerializer):
	class Meta:
		model = artical
		fields = ['id','title', 'author', 'email', 'created_at']


	# title = serializers.CharField(max_length=200)
	# author=serializers.CharField(max_length=200)
	# email=serializers.EmailField()
	# created_at=serializers.DateTimeField()
	# def create(self,validated_data):
	# 	return artical.objects.create(validated_data)
	# def update(self,instance,validated_data):
	# 	instance.title=validated_data.get('title',instance.title)
	# 	instance.author=validated_data.get('author',instance.author)
	# 	instance.email=validated_data.get('email',instance.email)
	# 	instance.created_at=validated_data.get('created_at',instance.created_at)
	# 	instance.save()
	# 	return instance