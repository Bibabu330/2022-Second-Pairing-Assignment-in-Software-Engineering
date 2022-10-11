from random import randint

student_num = 90
student_attendance = []

def ReadClassStudent(Class):
    with open("../data/1/Class_student{}".format(Class), "r") as f:  # 打开文件
        data = f.readlines()  # 读取文件

    class_student = []
    absent_student = []
    i1 = 0
    while data[i1] != '\n': # 80%缺课名单
        absent_student.append([])
        absent_student[i1].append(int(data[i1][0:3]))
        absent_student[i1].append(int(data[i1][4]))
        absent_student[i1].append(int(data[i1][6]))
        i1 += 1
    i1 += 1

    for j1 in range(student_num):# 课程学生名单
        class_student.append([])
        class_student[j1].append(int(data[i1][0:3]))
        class_student[j1].append(int(data[i1][4]))
        class_student[j1].append(int(data[i1][6]))
        student_attendance.append([])
        if class_student[j1] in absent_student: # 标记固定缺课学生为1,初始化为0
            class_student[j1].append(1)
            # 80%缺课的学生到位情况
            student_attendance[j1] = [0] * 20
            h = 0
            while h < 4: # 0 为缺课,1为到位
                k = randint(0,19)
                if student_attendance[j1][k] == 0:
                    student_attendance[j1][k] = 1
                    h += 1
        else:# 不是固定缺课,初始化为1
            student_attendance[j1] = [1] * 20
            class_student[j1].append(0)
        i1 += 1

    return class_student,student_attendance

if __name__ == "__main__":

    for Cla in ['A','B','C','D','E']:
        class_student_copy,student_attendance_copy = ReadClassStudent(Cla)
        # 0-3个没到的学生
        for i in range(20):
            for j in range(3):
                ab = randint(0,student_num-1)
                if class_student_copy[ab][3] == 0 and class_student_copy[ab][1] == 0 and class_student_copy[ab][2] == 0:# 不是固定缺课的学生,也不是缺过课的学生
                    class_student_copy[ab][3] = 2 # 2为偶尔缺课学生
                    student_attendance_copy[ab][i] = 0

        # 输出到文件
        fp = open("../data/1/student_attendance{}".format(Cla), "w")
        for i in range(student_num):
            fp.write(str(class_student_copy[i][0]))
            for j in range(20):
                fp.write(" "+str(student_attendance_copy[i][j]))
            fp.write("\n")
        fp.close()