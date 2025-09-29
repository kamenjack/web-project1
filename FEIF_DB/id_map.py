import pandas as pd

# 读取原始角色表
characters_df = pd.read_excel(r"E:\DjangoProject1\character_classid.xlsx",engine='openpyxl')  # 包含 'job_name' 列




# 建立名字到 id 的映射
job_dict = dict(zip(characters_df['job_source'], characters_df['id']))

def map_multi_class(cell):
    if pd.isna(cell) or cell == '':
        return []
    # 按换行拆分
    names = cell.split('\n')
    # 映射成 id，忽略不在 job_dict 的名字
    return [job_dict[name] for name in names if name in job_dict]
# 添加新列 job_id
characters_df['starting_class_ids'] = characters_df['starting_class'].apply(map_multi_class)
characters_df['buddy_class_ids']    = characters_df['buddy_class'].apply(map_multi_class)
characters_df['marriage_class_ids'] = characters_df['marriage_class'].apply(map_multi_class)

# 如果找不到的职业，可以设置默认值或保留空
characters_df['class_id'] = characters_df['class_id'].fillna('')

# 保存为新 Excel
characters_df.to_excel('characters_with_job_id1.xlsx', index=False)
