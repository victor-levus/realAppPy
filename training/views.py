from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from training.models import Course, CourseImage, Student, StudentImage, CourseClass
from training.serializers import CourseImageSerializer, CourseSerializer, CreateCourseSerializer, StudentSerializer, StudentImageSerializer, CreateStudentSerializer, CourseClassSerializer


# Create your views here.

class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all().prefetch_related('course_class', 'course_image')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCourseSerializer
        if self.request.method == 'PUT':
            return CreateCourseSerializer
        return CourseSerializer


class CourseImageViewSet(ModelViewSet):
    serializer_class = CourseImageSerializer

    def get_queryset(self):
        return CourseImage.objects.filter(course_id=self.kwargs['course_pk'])

    def get_serializer_context(self):
        return {"course_id": self.kwargs['course_pk']}


class CourseClassViewSet(ModelViewSet):
    serializer_class = CourseClassSerializer

    def get_queryset(self):
        return CourseClass.objects.filter(course_id=self.kwargs['course_pk'])

    def get_serializer_context(self):
        return {"course_id": self.kwargs['course_pk']}



################################################

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateStudentSerializer
        if self.request.method == 'PUT':
            return CreateStudentSerializer
        return StudentSerializer


class StudentImageViewSet(ModelViewSet):
    serializer_class = StudentImageSerializer

    def get_queryset(self):
        return StudentImage.objects.filter(student_id=self.kwargs['student_pk'])

    def get_serializer_context(self):
        return {"student_id": self.kwargs['student_pk']}

