import os
import django
import pandas as pd

# 设置 Django 环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject1.settings")  # 改成你的 settings.py 路径
django.setup()

from FEIF_DB.models import Skill, Job  # 改成你的 app 名

def import_skills_from_excel(file_path):
    df = pd.read_excel(file_path)

    for _, row in df.iterrows():
        try:
            # 找到对应的 Job
            job = Job.objects.get(id=row["source_job"])  # 如果 Excel 里存的是 Job 的 id
            # job = Job.objects.get(name=row["source_job"])  # 如果存的是名字就用这句

            # 创建 Skill
            skill = Skill.objects.create(
                source_job=job,
                icon=f"skill_icons/{row['icon']}",  # 确保图片已经放到 media/skill_icons/
                name=row["name"],
                description=row.get("description", ""),
                learn_condition=row.get("learn_condition", "")
            )
            print(f"✅ 已导入技能: {skill.name}")
        except Job.DoesNotExist:
            print(f"❌ 找不到 Job: {row['source_job']}")
        except Exception as e:
            print(f"⚠️ 导入出错: {e}, 行数据: {row}")

if __name__ == "__main__":
    excel_file = r"E:\DjangoProject1\skill_eng.xlsx"  # 你的 Excel 文件名
    import_skills_from_excel(excel_file)
