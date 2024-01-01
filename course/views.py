from django.shortcuts import render
from datetime import datetime

# # Create your views here.
# def learn_django(request):
#     return render(request,'course/courseone.html',{'nm':'Django'})


# def learn_django(request):
#     cname ='Django'
#     duration = '4 months'
#     seats = 10

#     course_detail = {'nm':cname,'du':duration,'st':seats}
#     return render(request,'course/courseone.html',context=course_detail)

# def learn_django(request):
#    return render(request,'course/courseone.html',{'nm':'django is awesome'})


# def learn_django(request):
#    d = datetime.now()
#    return render(request,'course/courseone.html',{'dt':d})


# def learn_django(request):
#     return render(request,'course/courseone.html',{'nm':True})


def learn_django(request):
    students = {'names':['ali','azam','asim','tayyab','haseeb']}
    return render(request,'course/courseone.html',students)
