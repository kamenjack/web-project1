import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject1.settings")
django.setup()

from FEIF_DB.models import Personal_skill

# Excel 文件路径
excel_file = r"E:\DjangoProject1\personal_skill.xlsx"

df = pd.read_excel(excel_file)

for _, row in df.iterrows():
    skill_name = row['skill_name']
    if skill_name:  # 确保不为空
        skill = Personal_skill.objects.create(skill_name=skill_name)

