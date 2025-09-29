import os
import django
import pandas as pd
from django.core.files import File

# 1️⃣ 初始化 Django 环境
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoProject1.settings")
django.setup()

# 2️⃣ 导入模型
from FEIF_DB.models import Item  # 替换成你的 App 名

# 3️⃣ Excel 文件路径
excel_path = r"E:\DjangoProject1\item_eng.xlsx"

# 4️⃣ 图片文件夹路径
img_folder = r"E:\DjangoProject1\media\item_icons"

# 5️⃣ 读取 Excel
try:
    df = pd.read_excel(excel_path)
    print(f"成功读取 Excel，记录总数: {len(df)}")
except Exception as e:
    print(f"读取 Excel 出错: {e}")
    exit(1)

# 6️⃣ 检查列名
print("Excel 列名:", list(df.columns))

# 7️⃣ 遍历每一行，创建 Item
for idx, row in df.iterrows():
    try:
        # 打印每行数据预览
        print(f"\n正在导入第 {idx+1} 行: {row.to_dict()}")

        item = Item(
            name=row['name'],
            durability=row.get('durability', 0),
            price=row.get('price', '--'),
            description=row.get('description', ''),
            obtain_method=row.get('obtain_method', '')
        )

        # 处理图片
        icon = row.get('icon')
        if icon:
            icon_path = os.path.join(img_folder, icon)
            if os.path.exists(icon_path):
                with open(icon_path, 'rb') as f:
                    item.icon.save(icon, File(f), save=False)
                print(f"图片已找到并关联: {icon}")
            else:
                print(f"图片未找到: {icon_path}")

        # 保存到数据库
        item.save()
        print(f"已导入: {item.name}")

    except Exception as e:
        print(f"导入第 {idx+1} 行 {row.get('name', '未知')} 出错: {e}")

print("\n所有数据导入完成！")

