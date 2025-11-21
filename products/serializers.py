from rest_framework import serializers
from .models import Product  # ✅ .models থেকে ইনপোর্ট করতে হবে


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'  # ✅ বানানে ভুল ছিল: fiels ❌ → fields ✅
