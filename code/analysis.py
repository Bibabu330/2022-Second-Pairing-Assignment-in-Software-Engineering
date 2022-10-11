from random import randint

# 初始化参数
count = 5
student_num = 300
class_num = 90
student_message = [] # 全体学生信息 300*(学号 绩点 职务)
total_student_absent = {} #  index对应student_message的学生名单
nA = randint(5,8)
nB = randint(5,8)
nC = randint(5,8)
nD = randint(5,8)
nE = randint(5,8)
sum_absentA = 0
sum_absentB = 0
sum_absentC = 0
sum_absentD = 0
sum_absentE = 0
sum_roll_callA = 0
sum_roll_callB = 0
sum_roll_callC = 0
sum_roll_callD = 0
sum_roll_callE = 0

# 读取学生信息
def ReadTotalStudent():
    with open("total_student_message", "r") as f:  # 打开文件
        data = f.readlines()  # 读取文件

    for i1 in range(student_num):
        student_message.append([])
        student_message[i1].append(int(data[i1][0:3]))
        student_message[i1].append(int(data[i1][4]))
        student_message[i1].append(int(data[i1][6]))

    return student_message

# 读单门课学生名单: 学号 成绩 职务
def ReadClassStudent(Cla):
    with open("../data/" + str(count) + "/Class_student{}".format(Cla), "r") as f:
        data = f.readlines()
    
    i1 = 0
    while data[i1] != '\n': # 80%缺课名单
        i1 += 1
    i1 += 1

    class_student = [] # 课程学生名单
    for j1 in range(class_num):
        class_student.append([])
        class_student[j1].append(int(data[i1][0:3]))
        class_student[j1].append(int(data[i1][4]))
        class_student[j1].append(int(data[i1][6]))
        i1 += 1

    return class_student

# 读出勤名单: 学号 20次出勤信息 (0为缺课,1为到位)
def ReadStudentAttendance(Cla):
    with open("../data/" + str(count) + "/student_attendance{}".format(Cla), "r") as f:
        data = f.readlines()

    class_attendance = [] # 课程学生名单
    for i1 in range(class_num):
        class_attendance.append([])
        for j1 in range(4, 43, 2):
            class_attendance[i1].append(int(data[i1][j1]))

    return class_attendance

# 第一次点名抽点成绩和职务为0的学生
def RollCallBeforeFindAll(class_student, class_attendance, absent_student, j2):
    absent = 0
    total_absent = 0
    roll_call_list = []
    for i1 in range(class_num):
        if class_student[i1][1] == 0 and class_student[i1][2] == 0:
            roll_call_list.append(i1) # 第一次点名名单

            if class_attendance[i1][j2] == 0: # 没到
                # 如果缺过课
                flag = 0

                for k in range(len(absent_student)):
                    if i1 == absent_student[k][0]:
                        flag = 1
                        absent_student[k][1] += 1
                        break

                # 未缺过课
                if flag == 0:
                    lst = [i1, 1]
                    absent_student.append(lst)

                # 缺课总表
                if str(class_student[i1][0]) not in total_student_absent:
                    total_student_absent[str(class_student[i1][0])] = 1
                else:
                    total_student_absent[str(class_student[i1][0])] += 1
                
                absent += 1

    for i1 in range(len(absent_student)):
        if absent_student[i1][1] >= 2:
            total_absent += 1

    result = [roll_call_list, absent_student, total_absent, absent]
    return result

def reCheck(absent_student, class_student):
    add_absent = 0
    for i1 in range(len(absent_student)):
        if str(class_student[absent_student[i1][0]][0]) in total_student_absent and total_student_absent[str(class_student[absent_student[i1][0]][0])] == 2:
            if absent_student[i1][1] < 2 :
                absent_student[i1][1] += 1
                if absent_student[i1][1] == 2:
                    add_absent += 1

    result = [absent_student, add_absent]
    return result

if __name__ == "__main__":
    ReadTotalStudent()

    # 初始化
    # Class A
    roll_call_listA = []
    absent_studentA = []
    class_studentA = ReadClassStudent('A')
    class_attendanceA = ReadStudentAttendance('A')
    real_absentA = 0

     # Class B
    roll_call_listB = []
    absent_studentB = []
    real_absentB = 0
    class_studentB = ReadClassStudent('B')
    class_attendanceB = ReadStudentAttendance('B')

     # Class C
    roll_call_listC = []
    absent_studentC = []
    real_absentC = 0
    class_studentC = ReadClassStudent('C')
    class_attendanceC = ReadStudentAttendance('C')

     # Class D
    roll_call_listD = []
    real_absentD = 0
    absent_studentD = []
    class_studentD = ReadClassStudent('D')
    class_attendanceD = ReadStudentAttendance('D')

     # Class E
    roll_call_listE = []
    real_absentE = 0
    absent_studentE = []
    class_studentE = ReadClassStudent('E')
    class_attendanceE = ReadStudentAttendance('E')

    # Roll Out : find absent_student
    for i in range(0,20):
        if real_absentA < nA:
            resultA = RollCallBeforeFindAll(class_studentA, class_attendanceA, absent_studentA, i)
            roll_call_listA.append(resultA[0])
            absent_studentA = resultA[1]
            real_absentA = resultA[2]
            sum_absentA += resultA[3]


        if real_absentB < nB:
            resultB = RollCallBeforeFindAll(class_studentB, class_attendanceB, absent_studentB, i) # 第一次结果
            roll_call_listB.append(resultB[0])
            absent_studentB = resultB[1]
            real_absentB = resultB[2]
            sum_absentB += resultB[3]

        if real_absentC < nC:
            resultC = RollCallBeforeFindAll(class_studentC, class_attendanceC, absent_studentC, i) # 第一次结果
            roll_call_listC.append(resultC[0])
            absent_studentC = resultC[1]
            real_absentC = resultC[2]
            sum_absentC += resultC[3]

        if real_absentD < nD:
            resultD = RollCallBeforeFindAll(class_studentD, class_attendanceD, absent_studentD, i) # 第一次结果
            roll_call_listD.append(resultD[0])
            absent_studentD = resultD[1]
            real_absentD = resultD[2]
            sum_absentD += resultD[3]
        
        if real_absentE < nE:
            resultE = RollCallBeforeFindAll(class_studentE, class_attendanceE, absent_studentE, i) # 第一次结果
            roll_call_listE.append(resultE[0])
            absent_studentE = resultE[1]
            real_absentE = resultE[2]
            sum_absentE += resultE[3]

        # recheck
        tempA = reCheck(absent_studentA, class_studentA)
        absent_studentA = tempA[0]
        real_absentA += tempA[1]
        tempB = reCheck(absent_studentB, class_studentB)
        absent_studentB = tempB[0]
        real_absentB += tempB[1]
        tempC = reCheck(absent_studentC, class_studentC)
        absent_studentC = tempC[0]
        real_absentC += tempC[1]
        tempD = reCheck(absent_studentD, class_studentD)
        absent_studentD = tempD[0]
        real_absentD += tempD[1]
        tempE = reCheck(absent_studentE, class_studentE)
        absent_studentE = tempE[0]
        real_absentE += tempE[1]

        if real_absentA >= nA and \
            real_absentB >= nB and \
            real_absentC >= nC and \
            real_absentD >= nD and \
            real_absentE >= nE:
            break

    real_absent_studentA = []
    for i in range(len(absent_studentA)):
        if absent_studentA[i][1] >= 2 and len(real_absent_studentA) < nA:
            real_absent_studentA.append(absent_studentA[i])

    real_absent_studentB = []
    for i in range(len(absent_studentB)):
        if absent_studentB[i][1] >= 2 and len(real_absent_studentB) < nB:
            real_absent_studentB.append(absent_studentB[i])

    real_absent_studentC = []
    for i in range(len(absent_studentC)) :
        if absent_studentC[i][1] >= 2 and len(real_absent_studentC) < nC:
            real_absent_studentC.append(absent_studentC[i])

    real_absent_studentD = []
    for i in range(len(absent_studentD)):
        if absent_studentD[i][1] >= 2 and len(real_absent_studentD) < nD:
            real_absent_studentD.append(absent_studentD[i])

    real_absent_studentE = []
    for i in range(len(absent_studentE)):
        if absent_studentE[i][1] >= 2 and len(real_absent_studentE) < nE:
            real_absent_studentE.append(absent_studentE[i])

    # roll out absent_student
    print("rollA = {}".format(len(roll_call_listA)))
    print("rollB = {}".format(len(roll_call_listB)))
    print("rollC = {}".format(len(roll_call_listC)))
    print("rollD = {}".format(len(roll_call_listD)))
    print("rollE = {}".format(len(roll_call_listE)))

    # 生成完整点名名单
    for i in range(len(roll_call_listA),20):
        roll_call_listA.append([])
        sum_absentA += len(real_absent_studentA)
        for j in range(len(real_absent_studentA)):
            roll_call_listA[i].append(real_absent_studentA[j][0])

    for i in range(len(roll_call_listB),20):
        roll_call_listB.append([])
        sum_absentB += len(real_absent_studentB)
        for j in range(len(real_absent_studentB)):
            roll_call_listB[i].append(real_absent_studentB[j][0])

    for i in range(len(roll_call_listC),20):
        roll_call_listC.append([])
        sum_absentC += len(real_absent_studentC)
        for j in range(len(real_absent_studentC)):
            roll_call_listC[i].append(real_absent_studentC[j][0])

    for i in range(len(roll_call_listD),20):
        roll_call_listD.append([])
        sum_absentD += len(real_absent_studentD)
        for j in range(len(real_absent_studentD)):
            roll_call_listD[i].append(real_absent_studentD[j][0])

    for i in range(len(roll_call_listE),20):
        roll_call_listE.append([])
        sum_absentE += len(real_absent_studentE)
        for j in range(len(real_absent_studentE)):
            roll_call_listE[i].append(real_absent_studentE[j][0])

    sum_absent = sum_absentA + sum_absentB + sum_absentC + sum_absentD + sum_absentE

    for i in range(len(roll_call_listA)):
        sum_roll_callA += len(roll_call_listA[i])

    for i in range(len(roll_call_listB)):
        sum_roll_callB += len(roll_call_listB[i])

    for i in range(len(roll_call_listC)):
        sum_roll_callC += len(roll_call_listC[i])
    
    for i in range(len(roll_call_listD)):
        sum_roll_callD += len(roll_call_listD[i])
    
    for i in range(len(roll_call_listE)):
        sum_roll_callE += len(roll_call_listE[i])

    sum_roll_call = sum_roll_callA + sum_roll_callB + sum_roll_callC + sum_roll_callD + sum_roll_callE

    # 输出五门课20次点名名单
    fp = open("../data/" + str(count) + "/student_roll_callA", "w")
    for i in range(len(roll_call_listA)):
        fp.write("courseA No.{} roll call list".format(i) + "\n")
        for j in range(len(roll_call_listA[i])):
            fp.write(str(class_studentA[roll_call_listA[i][j]][0]) + ' ')
        fp.write("\n\n\n")
    fp.close()

    print("courseA roll call list build successfully")

    fp = open("../data/" + str(count) + "/student_roll_callB", "w")
    for i in range(len(roll_call_listA)):
        fp.write("courseA No.{} roll call list".format(i) + "\n")
        for j in range(len(roll_call_listA[i])):
            fp.write(str(class_studentA[roll_call_listA[i][j]][0]) + ' ')
        fp.write("\n\n\n")
    fp.close()

    print("courseB roll call list build successfully")

    fp = open("../data/" + str(count) + "/student_roll_callC", "w")
    for i in range(len(roll_call_listA)):
        fp.write("courseA No.{} roll call list".format(i) + "\n")
        for j in range(len(roll_call_listA[i])):
            fp.write(str(class_studentA[roll_call_listA[i][j]][0]) + ' ')
        fp.write("\n\n\n")
    fp.close()

    print("courseC roll call list build successfully")

    fp = open("../data/" + str(count) + "/student_roll_callD", "w")
    for i in range(len(roll_call_listA)):
        fp.write("courseA No.{} roll call list".format(i) + "\n")
        for j in range(len(roll_call_listA[i])):
            fp.write(str(class_studentA[roll_call_listA[i][j]][0]) + ' ')
        fp.write("\n\n\n")
    fp.close()

    print("courseD roll call list build successfully")

    fp = open("../data/" + str(count) + "/student_roll_callE", "w")
    for i in range(len(roll_call_listA)):
        fp.write("courseA No.{} roll call list".format(i) + "\n")
        for j in range(len(roll_call_listA[i])):
            fp.write(str(class_studentA[roll_call_listA[i][j]][0]) + ' ')
        fp.write("\n\n\n")
    fp.close()

    print("courseE roll call list build successfully")

    print("----------------------------result----------------------------")
    print("sum_of_absent = {}".format(sum_absent))
    print("sum_of_roll_call = {}".format(sum_roll_call))
    print("E = {}".format(sum_absent/sum_roll_call))