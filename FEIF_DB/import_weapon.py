import os
import django
import pandas as pd
from django.core.files import File

# 设置 Django 环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject1.settings")
django.setup()

from FEIF_DB.models import Weapon, WeaponCategory

def import_weapons():
    # Excel 文件路径
    excel_path = r"E:\DjangoProject1\weapons_eng.xlsx"
    # 图片存放文件夹
    images_folder = r"E:\DjangoProject1\media\weapon_icons"

    df = pd.read_excel(excel_path)

    for _, row in df.iterrows():
        try:
            category = WeaponCategory.objects.get(name=row["category"])
        except WeaponCategory.DoesNotExist:
            print(f"❌ Category '{row['category']}' not found! Skipping row.")
            continue

        defaults = {
            "category": category,
            "description": row.get("description", ""),
            "level": row.get("level", ""),
            "might": row.get("might", 0),
            "hit": row.get("hit", 0),
            "crit": row.get("crit", 0),
            "avoid": row.get("avoid", 0),
            "dodge": row.get("dodge", 0),
            "range": row.get("range", ""),
            "effect": row.get("effect", ""),
            "price": row.get("price", 0),
            "obtain_method": row.get("obtain_method", ""),
        }

        # 处理 icon 图片
        icon_file_name = row.get("icon", None)
        if icon_file_name:
            icon_file_path = os.path.join(images_folder, icon_file_name)
            if os.path.exists(icon_file_path):
                f=open(icon_file_path, "rb")
                defaults["icon"] = File(f, name=icon_file_name)
            else:
                print(f"⚠️ Icon file '{icon_file_name}' not found. Skipping icon.")

        weapon, created = Weapon.objects.update_or_create(
            name=row["name"],
            defaults=defaults
        )

        if created:
            print(f"✅ Added weapon: {weapon.name}")
        else:
            print(f"♻️ Updated weapon: {weapon.name}")

if __name__ == "__main__":
    import_weapons()

