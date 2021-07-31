from django.http import request, JsonResponse
from django.shortcuts import redirect, render
from .models import Final, Guardian, LEVEL, MyUser, Payment, Results, Subject
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginform')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='loginform')
def personalinfo(request):
    return render(request, 'personalinfo.html')

@login_required(login_url='loginform')
def publishedres(request):
    result = Results.objects.filter(student=request.user)
    level = Results.objects.values('level').distinct()
    str = "Basic 1 term 1"
    print(str[:7])
    context = {'results':result, 'levels':level}
    return render(request, 'publishedres.html', context)

@login_required(login_url='loginform')
def personalacc(request):
    return render(request, 'personalacc.html')

@login_required(login_url='loginform')
def success(request):
    return render(request, 'success.html')

@login_required(login_url='loginform')
def payments(request):
    return render(request, 'payment.html')

@login_required(login_url='loginform')
def message(request):
    users = MyUser.objects.filter(is_student = True)
    staffs = MyUser.objects.filter(is_teacher = True)
    print(users)
    context = {'users':users, 'staffs':staffs}
    return render(request, 'message.html', context)

@login_required(login_url='loginform')
def uploadresults(request):
    if request.method == 'POST':
        level = request.POST.get('levelselect')
        print(level)
        classlevel = level[:-7]
        print(classlevel)
        students = MyUser.objects.filter(is_student=True, level=classlevel)
        subjects = Subject.objects.all()
        context = {'students':students, 'level':level, 'subjects':subjects}
        return render(request, 'uploadresults.html', context)
    else:
        subjects = Subject.objects.all()
        return render(request, 'uploadresults.html', {'subjects':subjects})


@login_required(login_url='loginform')
def stdterm(request):
    
    if request.method == 'POST':
        level = request.POST.get('levelselect')
        results = Results.objects.raw(f'SELECT * FROM sisapp_myuser WHERE level="{level}" and is_student=1')
        res = Final.objects.all()
        context = {
            'results':results, 'res':res
        }
        return render(request, 'stdterm.html', context)
    else:
        return render(request, 'stdterm.html')


@login_required(login_url='loginform')
def submitresult(request):
    if request.method == 'POST':
        return redirect('sisapp:stdterm')


@login_required(login_url='loginform')
def saveresults(request):
    if request.method == 'POST':
        student = request.POST.get('student')
        classSore = request.POST.get('classSore')
        examscore = request.POST.get('examscore')
        totalScore = request.POST.get('totalScore')
        position = request.POST.get('position')
        subject = request.POST.get('subject')
        level = request.POST.get('level')
        # print(student," ", classSore," ", examscore," ", totalScore," ", position,
        # level," ", subject) 
        student = MyUser.objects.get(username=student)
        subject = Subject.objects.get(code=int(subject))
        res = Results.objects.filter(level=level, subject=subject, student=student)
        fin = Final.objects.filter(student=student, year=level[:-7])
        if fin:
            final = fin[0]
        else:
            final = Final(student=student, year=level[:-7], aggregate=0, average=0)
            final.save()
        if res:
            print(res)
            data = {'message': f"{student}'s result is already entered"}
            return JsonResponse(data)
        else:
            results = Results(student=student,subject=subject, classScore=classSore,
            examscore=examscore,totalscore=totalScore,position=position, level=level)
            results.save()
            agg1 = Final.objects.filter(student=student)[0]
            print(agg1)
            ag = agg1.aggregate
            print(ag)
            agg = float(ag) + float(totalScore)
            avg = (float(ag) + float(totalScore))/3
            Final.objects.filter(student=student).update(aggregate=agg, average=avg)
            data = {
                'message':'successfully saved',
                'student': f"{student}"
            }
            return JsonResponse(data)


@login_required(login_url='loginform')
def promote(request):
    if request.method == 'POST':
        student = request.POST.get('student')
        status = request.POST.get('status')
        if status == 'Promoted':
            level = MyUser.objects.get(firstname=student).level
            levelcls = level[6:]
            # print(levelcls)
            levelname = level[:-1] 
            # print(levelname)
            levelclsadd = int(levelcls) + 1
            # print(levelclsadd)
            newlevel = f"{levelname}{levelclsadd}"
            # print(newlevel)
            MyUser.objects.filter(firstname=student).update(level=newlevel)
            data = {
                'message':f'{student}'
            }
            return JsonResponse(data)
        else:
            data = {
                'message':f'{student}'
            }
            return JsonResponse(data)


def savepayments(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        currency = request.POST.get('currency')
        student = request.POST.get('student')
        mobile = request.POST.get('mobile')
        flw_ref = request.POST.get('flw_ref')
        transaction_id = request.POST.get('transaction_id')
        student = MyUser.objects.get(firstname=student)
        pay = Payment(amount=amount, currency=currency, student=student,mobile=mobile, flw_ref=flw_ref, transaction_id=transaction_id)
        pay.save()
        print('successfully done')
        return redirect('sisapp:success')
