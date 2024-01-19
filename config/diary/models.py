from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Diary(models.Model):

    class Meta:
        db_table = 'diary'


    title = models.CharField(max_length=100) # タイトル
    content = models.TextField(max_length=1000) # 内容
    create_at = models.DateField(auto_now_add=True, blank=True, null=True, default=None) # 作成日時
    create_at = models.DateField(blank=True, null=True, default=None) # 作成日時
 
    def __str__(self):
        return self.title


