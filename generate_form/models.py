from django.db import models
# from django.utils import timezone

# from django_hstore import hstore



class Form_Model(models.Model):
	# user data 
    created = models.DateTimeField(auto_now_add=True)
    student_org = models.CharField(blank=True, default='', max_length=100)
    date = models.DateField()
    account_num = models.BigIntegerField()
    sub_account_num = models.BigIntegerField()
    dollar_amount = models.BigIntegerField()
    class Meta: 
        ordering = ('created', )
# class WebhookTransaction(models.Model):
#     UNPROCESSED = 1
#     PROCESSED = 2
#     ERROR = 3

#     STATUSES = (
#         (UNPROCESSED, 'Unprocessed'),
#         (PROCESSED, 'Processed'),
#         (ERROR, 'Error'),
#     )

#     date_generated = models.DateTimeField()
#     date_received = models.DateTimeField(default=timezone.now)
#     body = hstore.SerializedDictionaryField()
#     request_meta = hstore.SerializedDictionaryField()
#     status = models.CharField(max_length=250, choices=STATUSES, default=UNPROCESSED)

#     objects = hstore.HStoreManager()

#     def __unicode__(self):
#         return u'{0}'.format(self.date_event_generated)
# class Message(models.Model):
#     date_processed = models.DateTimeField(default=timezone.now)
#     webhook_transaction = models.OneToOneField(WebhookTransaction)

#     team_id = models.CharField(max_length=250)
#     team_domain = models.CharField(max_length=250)
#     channel_id = models.CharField(max_length=250)
#     channel_name = models.CharField(max_length=250)
#     user_id = models.CharField(max_length=250)
#     user_name = models.CharField(max_length=250)
#     text = models.TextField()
#     trigger_word = models.CharField(max_length=250)

#     def __unicode__(self):
#         return u'{}'.format(self.user_name)