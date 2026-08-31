from rest_framework import serializers
from .models import Product, Category,File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', 'avatar')


class FileSerializer(serializers.ModelSerializer):
    file_type=serializers.SerializerMethodField()
    
    class Meta:
        model = File
        fields = ('id','title', 'file','file_type')
        
    def get_file_type(self,obj):
        return obj.get_file_type_display()    
        
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    files=FileSerializer(many=True)
    # new_field=serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id",'title', 'description', 'avatar', 'categories','files','url')
        
    # def get_new_field(self,obj):
    #     return "You will see that" 


        
        
        
        
        
        
        