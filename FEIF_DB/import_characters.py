import os
import django
import pandas as pd
import math

# ---------------------------
# 工具函数
# ---------------------------
def parse_ids(value):
    """解析 Excel 中的单个或多 ID 字段，支持 27 / [27] / [27,28] / nan"""
    if value is None:
        return []
    if isinstance(value, float) and math.isnan(value):
        return []
    cleaned = str(value).strip()
    if cleaned.lower() in ["", "nan", "none"]:
        return []
    cleaned = cleaned.replace("[", "").replace("]", "")
    result = []
    for x in cleaned.split(","):
        x = x.strip()
        if x.isdigit():
            result.append(int(x))
    return result

# ---------------------------
# 设置 Django 环境
# ---------------------------
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject1.settings")
django.setup()

from FEIF_DB.models import Character, Job, Personal_skill

# ---------------------------
# 导入函数
# ---------------------------
def import_characters_from_excel(excel_file, media_root="media"):
    df = pd.read_excel(excel_file)

    for _, row in df.iterrows():
        try:
            # ---------------------------
            # 外键解析
            # ---------------------------
            # personal_skills
            skill = None
            if not pd.isna(row.get("personal_skills")):
                try:
                    skill = Personal_skill.objects.get(id=int(row["personal_skills"]))
                except Personal_skill.DoesNotExist:
                    print(f"⚠️ personal_skill id={row['personal_skills']} 不存在，将留空")

            # jobs (主职)
            job = None
            ids = parse_ids(row.get("jobs"))
            if ids:
                try:
                    job = Job.objects.get(id=ids[0])
                except Job.DoesNotExist:
                    print(f"⚠️ job id={ids[0]} 不存在，将留空")

            # ---------------------------
            # 创建 Character
            # ---------------------------
            character = Character.objects.create(
                storyline=row.get("storyline", "A"),
                name=row["name"],
                joined_charpter=row.get("joined_charpter", ""),
                starting_weapon_level=row.get("starting_weapon_level", ""),
                growth_hp=row["growth_hp"],
                growth_strength=row["growth_strength"],
                growth_magic=row["growth_magic"],
                growth_skill=row["growth_skill"],
                growth_speed=row["growth_speed"],
                growth_luck=row["growth_luck"],
                growth_defense=row["growth_defense"],
                growth_resistance=row["growth_resistance"],
                growth_total=row["growth_total"],
                level=row["level"],
                base_hp=row["base_hp"],
                base_strength=row["base_strength"],
                base_magic=row["base_magic"],
                base_skill=row["base_skill"],
                base_speed=row["base_speed"],
                base_luck=row["base_luck"],
                base_defense=row["base_defense"],
                base_resistance=row["base_resistance"],
                base_movement=row["base_movement"],
                personal_skills=skill,
                jobs=job,
            )

            # ---------------------------
            # 图片路径赋值
            # ---------------------------
            if not pd.isna(row.get("avatar")):
                character.avatar = f"avatars/{row['avatar']}"
            if not pd.isna(row.get("icon")):
                character.icon = f"icons/{row['icon']}"

            # ---------------------------
            # 多对多字段处理
            # ---------------------------
            for field_name in ["starting_class", "buddy_class", "marriage_class"]:
                ids = parse_ids(row.get(field_name))
                if ids:
                    jobs_qs = Job.objects.filter(id__in=ids)
                    getattr(character, field_name).set(jobs_qs)

            # 普通可选字段
            character.buddy_target = row.get("buddy_target", "")
            character.marriage_target = row.get("marriage_target", "")

            # 保存
            character.save()
            print(f"✅ 导入角色成功: {character.name}")

        except Exception as e:
            print(f"❌ 导入失败: {row.get('name', '未知')} - {e}")


# ---------------------------
# 主入口
# ---------------------------
if __name__ == "__main__":
    excel_path = r"E:\DjangoProject1\character.xlsx"   # 替换为你的 Excel 路径
    media_root = "media"  # MEDIA_ROOT
    import_characters_from_excel(excel_path, media_root)

