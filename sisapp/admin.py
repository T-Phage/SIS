from django.contrib import admin
from . models import *

# Register your models here.
class GuardianAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname', 'othername', 'fullname','email', 'profession', 'address','gps','phone')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'transaction_id','amount','currency','flw_ref','tx_ref','date')

class MyUserAdmin(admin.ModelAdmin):
    list_display = ('username','email','firstname','gender','date_of_birth','yearOfadmission','is_student','level','is_teacher', 'guardian','classAdmitted','is_admin','date_joined', 'password')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'period')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('subject','student','classScore','examscore','totalscore','position', 'level')

class FinalAdmin(admin.ModelAdmin):
    list_display = ('student', 'year', 'aggregate', 'average')

admin.site.register(Guardian, GuardianAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Results, ResultAdmin)
admin.site.register(Final, FinalAdmin)
