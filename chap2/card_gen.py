# 原始数据
raw_first_name = "  aLBERT  "
raw_last_name = "  eiNstEiN  "
job_title = 'Senior "Python" Developer' # 注意这里的双引号嵌套
base_salary = 12_500  # 基础薪资

#part 1
full_name = f"{(raw_first_name.strip()).title()} {(raw_last_name.strip()).title()}"
print(full_name,"\n")

#part 2
BONUS_RATE = 0.08
bonus = base_salary * BONUS_RATE
total_income = bonus + base_salary
print(total_income,"\n")

#part 3
print(f"{full_name},{job_title},{base_salary},{bonus},{total_income}\n")

#part 4
import this