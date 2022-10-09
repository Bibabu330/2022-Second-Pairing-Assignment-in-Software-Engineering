from random import randint
import copy

student_num = 300 # 五个课程人员总名单
absent_num = 40 # 缺课人员总名单
class_num = 90 # 每班90人
absent_80 = [] # 80%缺课的学生名单，共40人缺课
cnt_replication = [0] * student_num # 用来标记是否缺课
student_message = []

# 读学生信息
def read_student_message():
    with open("student_message", "r") as f:  # 打开文件
        data = f.readlines()  # 读取文件
    for i in range(student_num):
        student_message.append([])
        student_message[i].append(int(data[i][0:3]))
        student_message[i].append(int(data[i][4]))
        student_message[i].append(int(data[i][6]))
    return student_message

# 80%缺课总名单
def build_absent_list():
    cnt = 0
    while 1:
        i = randint(0, student_num-1)
        if student_message[i][1] == 0 and student_message[i][2] == 0 and cnt_replication[i] == 0:
            cnt_replication[i] = 1
            absent_80.append(student_message[i])
            cnt += 1
        if cnt >= 40:
            break

# 生成五门课学生名单，每门课90-8不固定缺课，8 80%缺课
def build_class_list(absent_be, absent_ed, Class):
    cnt_class = copy.deepcopy(cnt_replication)
    class_absent = copy.deepcopy(absent_80[absent_be:absent_ed])  # 单门课固定缺课学生A
    present_num = class_num - len(class_absent)
    class_present = []
    while 1:
        i = randint(0, student_num-1)
        if cnt_class[i] == 0:
            cnt_class[i] = 1
            class_present.append(student_message[i])
            present_num -= 1
            if present_num == 0:
                break
    class_student = class_absent + class_present
    sorted_class_student = sorted(class_student, key=lambda s: s[0])

    fp = open("./Class{}_student".format(Class), "w")
    for i in range(class_num):
        fp.write(str(sorted_class_student[i][0]) + " " + str(sorted_class_student[i][1]) + " " + str(sorted_class_student[i][2]) + "\n")
    fp.close()

    return class_student

if __name__ == "__main__":
    read_student_message()
    build_absent_list()

    # 生成五门课学生名单
    classA_student_list = build_class_list(0, 8, 'A')
    classB_student_list = build_class_list(5, 13, 'B')
    classC_student_list = build_class_list(10, 18, 'C')
    classD_student_list = build_class_list(20, 28, 'D')
    classE_student_list = build_class_list(30, 38, 'E')




