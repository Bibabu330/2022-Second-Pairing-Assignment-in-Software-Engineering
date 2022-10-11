import copy
import random

count = 5
student_num = 300
absent_num = 40
class_num = 90
cnt_replication = [0] * student_num
absent_80 = [] # 80%缺课的学生名单，共40人缺课
student_message = []
 
def ClassStudent(absent_begin, absent_end, Class):
    cnt_class = copy.deepcopy(cnt_replication)
    class_absent = copy.deepcopy(absent_80[absent_begin:absent_end]) # 单门课固定缺课学生A
    present_num = class_num - len(class_absent)
    class_present = []

    while 1:
        i1 = random.randint(0, student_num - 1)
        if cnt_class[i1] == 0:
            cnt_class[i1] = 1
            class_present.append(student_message[i1])
            present_num -= 1
            if present_num == 0:
                break

    class_student = class_absent+class_present

    # 输出双0人数
    cnt2 = 0
    for i1 in range(len(class_student)):
        if class_student[i1][1] == 0 and class_student[i1][2] == 0:
            cnt2 += 1
    class_student = sorted(class_student, key=lambda s:s[0])

    fp = open("../data/" + str(count) + "/Class_student{}".format(Class), "w")
    for i1 in range(len(class_absent)):
        fp.write(str(class_absent[i1][0]) + " " + str(class_absent[i1][1]) + " " + str(class_absent[i1][2]) + "\n")
    fp.write("\n")
    for i1 in range(class_num):
        fp.write(str(class_student[i1][0]) + " " + str(class_student[i1][1]) + " " + str(class_student[i1][2]) + "\n")
    fp.close()

    return class_student

if __name__ == "__main__":

    # 读学生信息
    with open("total_student_message", "r") as f:  # 打开文件
        data = f.readlines()  # 读取文件
        # print(data)

    for i in range(student_num): # 记录读取到的数据
        student_message.append([])
        student_message[i].append(int(data[i][0:3]))
        student_message[i].append(int(data[i][4]))
        student_message[i].append(int(data[i][6]))

    # 80%缺课总名单
    cnt = 0
    while 1:
        i = random.randint(0,student_num-1)
        if student_message[i][1] == 0 and student_message[i][2] == 0 and cnt_replication[i] == 0:
            cnt_replication[i] = 1
            absent_80.append(student_message[i])
            cnt += 1
            if cnt >= 40:
                break

    # 生成五门课学生名单，每门课90-8不固定缺课，8 80%缺课
    classA_student = ClassStudent(0,8,'A')
    classB_student = ClassStudent(5,13,'B')
    classC_student = ClassStudent(10,18,'C')
    classD_student = ClassStudent(15,23,'D')
    classE_student = ClassStudent(30,38,'E')