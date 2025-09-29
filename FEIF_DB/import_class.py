import os
import django
import pandas as pd

# ===================== 修改这里 =====================
PROJECT_NAME = "DjangoProject1"   # 你的 Django 项目名
APP_NAME = "FEIF_DB"             # 你的 app 名
EXCEL_FILE = r"E:\DjangoProject1\class_eng.xlsx"  # Excel 路径，记得用 r 前缀
# ===================================================

# 设置 Django 环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{PROJECT_NAME}.settings")
django.setup()

from FEIF_DB.models import Job   # 如果 APP_NAME 不一样，这里也要改

def import_jobs():
    df = pd.read_excel(EXCEL_FILE)

    for _, row in df.iterrows():
        job = Job(
            Allegiance=row["Allegiance"],   # A/B/C
            title=row["title"],
            level=row["level"],            # A/B
            Weapon_Proficiency_Cap=row["Weapon_Proficiency"],
            movement=row["movement"],
            growth_hp=row["growth_hp"],
            growth_strength=row["growth_strength"],
            growth_magic=row["growth_magic"],
            growth_skill=row["growth_skill"],
            growth_speed=row["growth_speed"],
            growth_luck=row["growth_luck"],
            growth_defense=row["growth_defense"],
            growth_resistance=row["growth_resistance"],
            cap_hp=row["cap_hp"],
            cap_strength=row["cap_strength"],
            cap_magic=row["cap_magic"],
            cap_skill=row["cap_skill"],
            cap_speed=row["cap_speed"],
            cap_luck=row["cap_luck"],
            cap_defense=row["cap_defense"],
            cap_resistance=row["cap_resistance"],
            cap_total=row["cap_total"],
            Class_Traits=row["Class_Traits"],
            remarks=row.get("remarks", "")
        )
        job.save()
        print(f"✅ 导入职业: {job.title}")

if __name__ == "__main__":
    import_jobs()
    print("🎉 所有职业导入完成！")
