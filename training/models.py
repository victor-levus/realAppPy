from django.db import models

from training.validators import validate_file_size

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=510, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class CourseImage(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_image')
    image = models.ImageField(upload_to='courses/images', validators=[validate_file_size])

class CourseClass(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_class')
    session = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Instructor(models.Model):
        
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    contact_address = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=255)
    state = models.CharField(max_length=255, null=True, blank=True)
    lga = models.CharField(max_length=255, null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name


class StudentImage(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_image')
    image = models.ImageField(upload_to='students/images', validators=[validate_file_size])


