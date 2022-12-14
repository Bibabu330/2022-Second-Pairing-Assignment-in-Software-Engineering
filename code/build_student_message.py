# 学生300人，6个班，每个班50人，其中100人成绩为0，每个班15人有职位1, 过去是否经常缺课 50
# 学号 绩点 职务
import random

if __name__ == "__main__":

    position_num = 15
    class_number = 6
    student_in_class = 50
    total_num = student_in_class * class_number
    grade_low = 100
    student = []
    grade = 0

    for c in range(class_number): # class
        position = 0
        for i in range(student_in_class): # every class
            student.append([])
            j=c*student_in_class+i
            # 学号
            s = (c+1)*100+i+1
            student[j].append(s)

            # 绩点
            ran_grade = random.randint(0,1)
            if grade < grade_low:
                student[j].append(ran_grade)
                if ran_grade == 0:
                    grade += 1
            else:
                student[j].append(1)

            # 职务
            ran_position = random.randint(0,1)
            if position < position_num: # 有职务
                student[j].append(ran_position)
                position += ran_position
            else:
                student[j].append(0)

    fp = open("total_student_message", "w")
    for i in range(total_num):
        fp.write(str(student[i][0])+' '+str(student[i][1])+' '+str(student[i][2])+'\n')
    fp.close()
