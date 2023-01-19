from django.db import models
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.core.validators import RegexValidator
from django.db.models.signals import post_save , post_delete # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده


#
class SendOtpToWhatsappMODEL(models.Model):
    # Table fields
    SOTW_user             = models.OneToOneField(User                   , on_delete = models.CASCADE , blank=False  , null=False )
    SOTW_mobile_regex      = RegexValidator(regex=(r"[\+\d]?(\d{2,3}[-\.\s]??\d{2,3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")        , message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    SOTW_mobile_number    = models.CharField(validators=[SOTW_mobile_regex] , max_length=13, blank=True , null=True) # Validators should be a list
    SOTW_Is_whatsApp_active = models.BooleanField(default=False , help_text="Choose to activate WhatsApp service")
    SOTW_created_at        = models.DateTimeField(auto_now_add=True)
    
	#
    def __str__(self):
        # this will make data labelled using username in table in django admin
        dataLabel = self.SOTW_user.username + " ____ " + str(self.SOTW_mobile_number) + " ____ " + str(self.SOTW_created_at) + "____" + str(self.SOTW_Is_whatsApp_active)
        return dataLabel
# 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering =  ['SOTW_created_at'] 
    #
    # class Meta: #'admin'عرض إسم المودل/الجدول في صفحة
    #     verbose_name_plural = 'otp_MODE'
    #
    # create_profile: للمستخدم الجديد "profile"دالة تقوم بإنشاء
    # sender: هي فانكش/دالة تقوم بمتابعة الملف الذي ترتبط به فبمجرد قيام الملف المرتبطة به بحدث ما تقوم بتفيذ الكود الموجود فيها
    # **kwargs: "Type" وﻻ نوعها "size" فانكش تقوم  بإستقبال المعلومات (المجهولة) التي لايعرف  حجمها
    # ['created']:الكلمة التي سوف يتم طباعتها إذا تم إستقبال بيانات
    # user:
    # ['instance']: هي البيانات التي تسم إستقبالها
    # post_save:  ""   ""  يتم تنفيذ  حدث اخر بعده  "Save" كلاس فكرته: ان بمجرد تنفيذ عملية الحفظ
    def create_send_otp_to_whatsapp(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            SendOtpToWhatsappMODEL.objects.create(SOTW_user=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
    post_save.connect(create_send_otp_to_whatsapp , sender=User)
    #
