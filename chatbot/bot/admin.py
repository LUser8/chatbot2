from django.contrib import admin
from .models import ChatAssistant

# register the model with admin app
admin.site.register([ChatAssistant])