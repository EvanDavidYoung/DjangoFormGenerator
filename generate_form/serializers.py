from rest_framework import serializers
from generate_form.models import Form_Model
import io 
from rest_framework.parsers import JSONParser
import json
import generate_form.fillableform as generate
    # Probably need to put this code in another file 
    # def serialize_hook(self, hook):
    #     # optional, there are serialization defaults
    #     # we recommend always sending the Hook
    #     # metadata along for the ride as well
    #     return {
    #         'hook': hook.dict(),
    #         'data': {
    #             'answers': self.answers
    #         }
    #     }
class FormSerializer(serializers.ModelSerializer):

	class Meta: 
		model = Form_Model
		fields = '__all__' 

	def getDataFromJSON(jsonDict):
		answers = jsonDict['form_response']['answers']						
		datas = dict()
		datas['Account Number'] = answers[2]['number']
		datas['SubAccount']		= answers[3]['number']
		datas['Amount'] 		= answers[5]['number']
		datas['Date'] 			= answers[1]['date'].replace('-','')
		datas['Org Name'] 		= answers[0]['choice']['label'] 
		datas['Reason'] 		= answers[4]['choice']['label']
		datas['Email']			= answers[6]['text']
	def create(self, validated_data):
		
		datas	= this.getDataFromJSON(validated_data)		
		generate.generate_form(datas)

		return Form_Model.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
	   #  instance.created = validated_data.get()
	   #  instance.student_org = 
	   #  instance.date = 
	   #  instance.account_num = 
	   #  instance.sub_account_num = 
	   #  instance.dollar_amount = 
	   #  instance.save()
	   #  return instance 
	def deserialize(json_string):
		stream = io.BytesIO(json_string)
		# print(stream)
		data = json.load(stream)
		print(data)
		data_dict = data['form_response']['answers']
		
		# form_response
		# new_form = FormSerializer.create(data)
		# return new_formw



















    # created = models.DateTimeField(auto_now_add=True)
    # student_org = models.CharField(blank=True, default='', max_length=100)
    # date = models.DateField()
    # account_num = models.BigIntegerField()
    # sub_account_num = models.BigIntegerField()
    # dollar_amount = models.BigIntegerField()

# from form_generator.models import Form_Model
# from form_generator.serializers import FormSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# jason = open("formjson.json")
# jasonastxt = jason.read()
# jasonastxt = jasonastxt.encode() 
# FormSerializer.deserialize(jasonastxt)
