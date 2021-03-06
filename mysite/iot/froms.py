
# iot/forms.py

# 引入表单类
from django import forms
# 引入文章模型
from .models import RaspberryPi

# 写文章的表单类
class RaspberryPiForm(forms.ModelForm):
    class Meta:
        # 指明数据模型来源
        model = RaspberryPi
        # 定义表单包含的字段
        fields = ('Temperature', 'weight')



