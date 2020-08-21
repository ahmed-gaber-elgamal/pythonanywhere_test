from django.contrib import admin
from .models import AccessRecord, Topic, Webpage, User, UserProfile

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
admin.site.register(UserProfile)