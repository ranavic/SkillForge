from django.contrib import admin
from .models import Category, Difficulty, Course, Module, Lesson, Tag, CourseReview, Enrollment, LessonProgress, CourseResource

admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Tag)
admin.site.register(CourseReview)
admin.site.register(Enrollment)
admin.site.register(LessonProgress)
admin.site.register(CourseResource)
