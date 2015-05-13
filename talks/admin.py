from django.contrib import admin

# Register your models here.
from .models import TalkList
from .models import Talk


admin.site.register(TalkList)
admin.site.register(Talk)