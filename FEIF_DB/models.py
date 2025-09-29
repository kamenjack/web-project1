from django.db import models

# Create your models here.
class Job(models.Model):
    id=models.AutoField(primary_key=True)
    Allegiance=models.CharField(max_length=100,choices=[('A','Neutral'),('B','Dark'),('C','Light')])
    title = models.CharField(max_length=100)
    level=models.CharField(max_length=10,choices=[('A','Base'),('B','Promoted'),('C','Special')])
    skills = models.ManyToManyField('Skill', blank=True)
    Weapon_Proficiency_Cap=models.CharField(max_length=100)
    movement=models.IntegerField()
    growth_hp = models.IntegerField(verbose_name="HP Growth Modifier (%)")
    growth_strength = models.IntegerField(verbose_name="Strength Growth Modifier (%)")
    growth_magic = models.IntegerField(verbose_name="Magic Growth Modifier (%)")
    growth_skill = models.IntegerField(verbose_name="Skill Growth Modifier (%)")
    growth_speed = models.IntegerField(verbose_name="Speed Growth Modifier (%)")
    growth_luck = models.IntegerField(verbose_name="Luck Growth Modifier (%)")
    growth_defense = models.IntegerField(verbose_name="Defense Growth Modifier (%)")
    growth_resistance = models.IntegerField(verbose_name="Resistance Growth Modifier (%)")
    cap_hp = models.IntegerField(verbose_name="HP Cap")
    cap_strength = models.IntegerField(verbose_name="Strength Cap")
    cap_magic = models.IntegerField(verbose_name="Magic Cap")
    cap_skill = models.IntegerField(verbose_name="Skill Cap")
    cap_speed = models.IntegerField(verbose_name="Speed Cap")
    cap_luck = models.IntegerField(verbose_name="Luck Cap")
    cap_defense = models.IntegerField(verbose_name="Defense Cap")
    cap_resistance = models.IntegerField(verbose_name="Resistance Cap")
    cap_total = models.IntegerField(verbose_name="Total Cap")
    Class_Traits=models.CharField(max_length=100)
    remarks=models.TextField()
    def __str__(self):
        return self.title
class Personal_skill(models.Model):
    id=models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=100)
    def __str__(self):
        return self.skill_name

class Character(models.Model):
    STORYLINES = [
        ('A', 'White'),
        ('B', 'Dark'),
        ('C', 'Tomo'),
    ]
    storyline = models.CharField(max_length=1, choices=STORYLINES, default="A")
    id = models.AutoField(primary_key=True)
    avatar=models.ImageField(upload_to='avatars/')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons/')
    personal_skills = models.ForeignKey(Personal_skill, on_delete=models.CASCADE)
    jobs= models.ForeignKey(Job,on_delete=models.CASCADE)
    joined_charpter=models.CharField(max_length=100)
    starting_weapon_level = models.CharField(max_length=50, blank=True)
    growth_hp = models.IntegerField()
    growth_strength = models.IntegerField()
    growth_magic = models.IntegerField()
    growth_skill = models.IntegerField()
    growth_speed = models.IntegerField()
    growth_luck = models.IntegerField()
    growth_defense = models.IntegerField()
    growth_resistance = models.IntegerField()
    growth_total = models.IntegerField()
    level = models.IntegerField()
    base_hp = models.IntegerField()
    base_strength = models.IntegerField()
    base_magic = models.IntegerField()
    base_skill = models.IntegerField()
    base_speed = models.IntegerField()
    base_luck = models.IntegerField()
    base_defense = models.IntegerField()
    base_resistance = models.IntegerField()
    base_movement = models.IntegerField()
    starting_class = models.ManyToManyField('Job',  blank=True,
                                       related_name='starting_characters')

    buddy_class = models.ManyToManyField('Job',  blank=True,
                                    related_name='buddy_characters')
    buddy_target = models.CharField(max_length=100, blank=True)  # 支援A+对象名

    marriage_class = models.ManyToManyField('Job',   blank=True,
                                       related_name='marriage_characters')
    marriage_target = models.CharField(max_length=100, blank=True)  # 支援S对象名
    def __str__(self):
        return self.name

class WeaponCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="WeaponCategory")

    def __str__(self):
        return self.name

# 具体的武器，例如“铁剑”、“银剑”……
class Weapon(models.Model):
    name = models.CharField(max_length=100, verbose_name="Weapon")
    category = models.ForeignKey(WeaponCategory, on_delete=models.CASCADE, related_name='weapons', verbose_name="WeaponsBelong")
    icon = models.ImageField(upload_to='weapon_icons/', blank=True, null=True, verbose_name="icon")
    description = models.TextField(blank=True, verbose_name="description")
    level = models.CharField(max_length=5, verbose_name="Level")
    might = models.CharField(verbose_name="Might")
    hit = models.CharField(default=0, verbose_name="Hit")
    crit = models.CharField(verbose_name="Crit")
    avoid = models.CharField(default=0, verbose_name="Avoid")
    dodge = models.CharField(default=0, verbose_name="Dodge")
    range = models.CharField(max_length=20, blank=True, verbose_name="Range")
    effect = models.CharField(max_length=200, blank=True, verbose_name="Effect")
    price = models.CharField(verbose_name="Price")
    obtain_method = models.CharField(max_length=1000, blank=True, verbose_name="Obtain Method")

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='item_icons/', blank=True, null=True)
    durability = models.IntegerField(default=0)
    price = models.CharField(max_length=20, default='--')  # 用CharField兼容“--”
    description = models.TextField(blank=True)
    obtain_method = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Skill(models.Model):
    id=models.AutoField(primary_key=True)
    source_job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='source_skills', verbose_name="Skill Source Job")
    icon = models.ImageField(upload_to='skill_icons/', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    learn_condition = models.TextField(blank=True, verbose_name="Normal Learn Condition")

    def __str__(self):
        return f"{self.name} ({self.source_job.title})"