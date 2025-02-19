from rest_framework import serializers
from testapp.models import Employee
def multiple_of_1000(value):
    if value%1000!=0:
        raise serializers.ValidationError('employee salary should be multiple of thousand only..')


class EmployeeSerializer(serializers.ModelSerializer):
    esal=serializers.FloatField(validators=[multiple_of_1000])

    class Meta:
        model=Employee
        fields='__all__'

# class EmployeeSerializer(serializers.Serializer):
#     eno=serializers.IntegerField()
#     ename=serializers.CharField(max_length=64)
#     esal=serializers.FloatField(validators=[multiple_of_1000])
#     eaddr=serializers.CharField(max_length=50)
        
#     def validate(self,data):
#         print('object level validator')
#         ename=data.get('ename')
#         esal=data.get('esal')
#         if ename.lower()=='sunny':
#             if esal<50000:
#                 raise serializers.ValidationError('sunny salary should be min 50k')
#         return data

#     def create(self,validated_data):
#         return Employee.objects.create(**validated_data)
    
#     def update(self,instance,validated_data):
#         instance.eno=validated_data.get('eno',instance.eno)
#         instance.ename=validated_data.get('ename',instance.ename)
#         instance.esal=validated_data.get('esal',instance.esal)
#         instance.eaddr=validated_data.get('eaddr',instance.eaddr)
#         instance.save()
#         return instance 
