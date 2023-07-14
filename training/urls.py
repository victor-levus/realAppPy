
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register('courses', views.CourseViewSet, basename='courses')
router.register('students', views.StudentViewSet, basename='students')

courses_router = routers.NestedDefaultRouter(router, 'courses', lookup='course')
courses_router.register('images', views.CourseImageViewSet, basename='course-images')
courses_router.register('courseclasses', views.CourseClassViewSet, basename='course-classes')

students_router = routers.NestedDefaultRouter(router, 'students', lookup='student')
students_router.register('studentimages', views.StudentImageViewSet, basename='student-images')


urlpatterns = router.urls + courses_router.urls + students_router.urls