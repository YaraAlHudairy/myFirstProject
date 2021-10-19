from .models import Student

def students(request):
    return {'students': Student.objects.all()}