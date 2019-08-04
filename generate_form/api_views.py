from rest_framework.generics import ListAPIView

from generate_form.serializers import FormSerializer
from generate_form.models import Form_Model


class FormList(ListAPIView):
	queryset = Form_Model.objects.all()
	serializer_class = FormSerializer