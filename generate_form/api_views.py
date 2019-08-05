from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.exceptions import ValidationError
from generate_form.serializers import FormSerializer
from generate_form.models import Form_Model, Form_Model2


class FormList(ListAPIView):
	queryset = Form_Model2.objects.all()
	serializer_class = FormSerializer



class FormCreate(CreateAPIView):
	serializer_class = FormSerializer

	def create(self, request, *args, **kwargs):
		return super().create(request, *args, **kwargs)



# Form_Model.objects.create(student_org="SASE",date="2019-08-04",account_num=23412,sub_account_num=34234,dollar_amount=69)