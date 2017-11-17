# 角色:学校、学员、课程、讲师
# 要求:
# 1. 创建北京、上海 2 所学校
# 2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
# 3. 课程包含，周期，价格，通过学校创建课程
# 4. 通过学校创建班级， 班级关联课程、讲师
# 5. 创建学员时，选择学校，关联班级
# 5. 创建讲师角色时要关联学校，


# 6. 提供两个角色接口
# 6.1 学员视图， 可以注册， 交学费， 选择班级，
# 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
# 6.3 管理视图，创建讲师， 创建班级，创建课程
#
# 7. 上面的操作产生的数据都通过pickle序列化保存到文件里

class School:
	def __init__(self,school_info_dict,courses,classroom,teacher,student):
		self.school_info = school_info_dict
		self.courses = courses
		self.classroom = classroom
		self.teacher = teacher
		self.student = student
class Student:
	def __init__(self,student_info_dict,obj):
		self.student_info = student_info_dict
		self.obj = obj
class Course:
	def __init__(self,course_info_dict,obj):
		self.course_info = course_info_dict
		self.obj = obj
class ClassRoom:
	def __init__(self,class_info_dict,obj):
		self.class_info = class_info_dict
		self.obj = obj
class Teacher:
	def __init__(self,teacher_info_dict,obj):
		self.teacher_info = teacher_info_dict
		self.obj = obj



sch_obj1 = School({'school_location':'北京'},Course,ClassRoom,Teacher,Student)
sch_obj2 = School({'school_location':'上海'},Course,ClassRoom,Teacher,Student)

course_obj1 = sch_obj1.courses({'course_name':'linux','course_price':1000,'course_week':30},sch_obj1) #调用创建课程方法,返回一个课程对象
course_obj2 = sch_obj1.courses({'course_name':'python','course_price':1200,'course_week':60},sch_obj1) #调用创建课程方法,返回一个课程对象
course_obj3 = sch_obj2.courses({'course_name':'go','course_price':1500,'course_week':10},sch_obj2) #调用创建课程方法,返回一个课程对象

teacher1 = sch_obj1.teacher({'teacher_name':'Lee'},course_obj1)
teacher2 = sch_obj1.teacher({'teacher_name':'Tom'},course_obj2)
teacher3 = sch_obj1.teacher({'teacher_name':'Jack'},course_obj3)


class1 = sch_obj1.classroom({'class_name':'one'},teacher1)
class2 = sch_obj1.classroom({'class_name':'two'},teacher2)
class3 = sch_obj2.classroom({'class_name':'three'},teacher3)

student1 = sch_obj1.student({'student_name':'lizi'},class1)
student2 = sch_obj1.student({'student_name':'wangqiang'},class2)
student3 = sch_obj2.student({'student_name':'kangkang'},class3)

print(student1.obj.obj.obj.obj.school_info)

exit()




