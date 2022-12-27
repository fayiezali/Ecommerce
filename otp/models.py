from django.db import models

from django.contrib.auth.models import User # إستيراد اسم المستخدم

from django.db.models.signals import post_save , post_delete # كلاس فكرته: انه بمجرد تنفيذ عملية الحفظ يقوم مباشرة بتنفيذ عملية اخرى بعده

import random
#
#
#
class otp_MODEL(models.Model):
    otp_user              = models.OneToOneField(User              , on_delete = models.CASCADE)
    otp_one_time_password  = models.IntegerField(db_index=True        , blank=True  , null=True )
    otp_created_at         = models.DateTimeField(auto_now_add=True)
    #
    def __str__(self):
        # this will make data labelled using username in table in django admin
        dataLabel = self.otp_user.username + " __ " + str(self.otp_one_time_password) + " ___ " + str(self.otp_created_at)
        return dataLabel
    # 
    # 'Z-A' ترتيب تنازلي
    class Meta:
        ordering =  ['otp_created_at'] 
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
    def create_otp(sender, **kwargs):
        if kwargs['created']: #'created' إذا كان هناك بيانات تم إستقبالها اطبع هذه الكلمة
            otp_MODEL.objects.create(otp_user=kwargs['instance']) #التي أستقبلتها "'instance'"جديد بناء على  معلومات المستخدم "PersonalData_MODEL" قم بإنشاء ملف
    # "" "user"والمستخدم  "post_save" الربط بين الفانكشن
    post_save.connect(create_otp , sender=User)
    #

