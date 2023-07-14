from dataclasses import field
from rest_framework import serializers

from training.models import Course, CourseImage, Student, StudentImage, CourseClass


class CourseImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        course_id = self.context['course_id']
        return CourseImage.objects.create(course_id=course_id, **validated_data)

    class Meta:
        model = CourseImage
        fields = ['id', 'image']



class CourseClassSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        course_id = self.context['course_id']
        return CourseClass.objects.create(course_id=course_id, **validated_data)

    class Meta:
        model = CourseClass
        fields = ['id', 'session', 'location', 'start_date', 'end_date']

class CreateCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price']

class CourseSerializer(serializers.ModelSerializer):
    course_image = CourseImageSerializer(many=True)
    course_class = CourseClassSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'created_at', 'last_update', 'course_image', 'course_class']



class StudentImageSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        student_id = self.context['student_id']
        return StudentImage.objects.create(student_id=student_id, **validated_data)

    class Meta:
        model = StudentImage
        fields = ['id', 'image']


class CreateStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'contact_address', 'dob', 'gender', 'state', 'lga', 'qualification', 'occupation']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'contact_address', 'dob', 'gender', 'state', 'lga', 'qualification', 'occupation', 'student_image', 'created_at', 'last_update']

