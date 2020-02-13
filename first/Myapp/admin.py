from django.contrib import admin
from .models import Grades, Student

# Register your models here.


class StudentInline(admin.TabularInline):#字段横向显示
    model = Student
    extra = 2

# class StudentInline(admin.StackedInline):#字段纵向显示
#     model = Student
#     extra = 5

@admin.register(Grades)
class GradesAdmin(admin.ModelAdmin):
    # # bool值显示:
    # def delete(self):
    #     if self.isDelete:
    #         return '是'
    #     else:
    #         return '否'
    # 列表显示项
    inlines = [StudentInline] 
    list_display = [
        'id',
        'gname',
        'gdate',
        'ggirlnum',
        'gboynum',
        'isDelete',
    ]
    # 过滤器,过滤字段:
    list_filter = ['gname',]
    #查找搜索框:
    search_filter = ['gname']
    # 分页
    list_per_page = 10

    #修改添加、修改页的字段顺序
    # fields = ['ggirlnum','gboynum','name','gdate','isDelete']
    #给属性分组,不能和field同时使用
    fieldsets = (
        (None, {
            "fields": (
                'ggirlnum', 'gboynum'
            ),
        }),
        (None, {
            "fields": (
                'gname', 'gdate', 'isDelete'
            ),
        }),
    )

    # delete.shot_description =  '是否'
        
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    # 列表显示项

    list_display = [
        'id',
        'sname',
        'sgender',
        'sage',
        'scontent',
        'isDelete',
        'sgrade',
    ]
    # 过滤器,过滤字段:
    list_filter = ['sgender', 'sgrade']
    #查找搜索框:
    search_filter = ['sname']
    # 分页
    list_per_page = 10

# admin.site.register(Student, StudentAdmin)#已经有装饰器替代完成注册
# admin.AdminSite.site_header = '班级管理后台'
# admin.AdminSite.site_title = '数据运维'
