from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from sisapp.models import Guardian, MyUser
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required(login_url='accounts:loginform')
def changepassword(request):
    if request.method == 'POST':
        password = request.POST.get('cpassword')
        print(password)
        user = MyUser.objects.get(username=request.user)
        user.set_password(password)
        user.save()
        return redirect('accounts:changepassword')
    return render(request, 'accounts/changepassword.html')

@login_required(login_url='accounts:loginform')
def editprofile(request):
    if request.method == 'POST':
        email = request.POST.get('emailAddress')
        phone = request.POST.get('mobilephone')
        profession = request.POST.get('profession')
        address = request.POST.get('address')
        gps = request.POST.get('gps')
        print(email, phone,profession,address,gps)
        # Guardian.objects.filter()
    return render(request, 'accounts/editprofile.html')

def forgetpassword(request):
    return render(request, 'accounts/forgetpassword.html')

def loginform(request):
    if request.method == 'POST':
        email = request.POST.get('emailaddress')
        password = request.POST.get('password')
        print(email)
        print(password)
        # user = MyUser.objects.filter(email=email, password=password)
        
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            # login(request, find)
            # return redirect('/')
            if user.is_active:
                login(request, user)
                return redirect('/')
            elif user.is_active == False:
                return render(request, 'accounts/loginform.html', {'error':'your account is curently unavailable'})
        else:
            return render(request, 'accounts/loginform.html', {'error':'invalid email or password'})
    return render(request, 'accounts/loginform.html')


@login_required(login_url='loginform')
def signout(request):
    logout(request, )
    return redirect('/')


@login_required(login_url='accounts:loginform')
def successfullysent(request):
    return render(request, 'successfullysent.html')


@login_required(login_url='loginform')
def signupform(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        # lastname = request.POST.get('lastname')
        # othernames = request.POST.get('othernames')
        email = request.POST.get('emailaddress')
        dob = request.POST.get('date_of_birth')
        phone = request.POST.get('phone')
        yoa = request.POST.get('yearOfadmission')
        clad = request.POST.get('classAdmitted')
        level = request.POST.get('level')
        group = request.POST.get('group')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        fullname = firstname
        print(fullname)
        user = MyUser.objects.create_user(email=email, username=fullname, password=password)
        user.save()
        # print(user)
        MyUser.objects.filter(username=fullname).update(date_of_birth=dob, yearOfadmission=yoa, classAdmitted=clad, 
        level=level, group=group, gender=gender, is_teacher=False, firstname=firstname,
        is_student=True, is_admin=False, phone=phone)
        saveduser = MyUser.objects.filter(username=fullname)
        message = ""
        if saveduser:
            message = 'Profile details saved.'
        else:
            message = 'An error occurred try some other time' 
        return render(request, 'accounts/signupform.html', {'message':message})
        # return redirect('signupform')
    else:
        return render(request, 'accounts/signupform.html')

# def guardian_ajax(request):
#     name = request.POST.get('name')
#     data = {
#         # 'is_taken': Site.objects.filter(site_id__iexact=username).exists()
#         'message':'ok'
#     }
#     return JsonResponse(data)

# ajaxes
@login_required(login_url='login')
def guardian_ajax(request):
    if request.is_ajax:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        othernames = request.POST.get('othernames')
        fullname = f"{firstname} {othernames} {lastname}"
        emailaddress = request.POST.get('emailaddress')
        phone = request.POST.get('phone')
        profession = request.POST.get('profession')
        address = request.POST.get('address')
        gps = request.POST.get('gps')
        print(firstname, othernames, lastname)
        print(emailaddress, phone, profession, gps)
        x = Guardian(firstname=firstname, lastname=lastname, fullname=fullname, othername=othernames, email=emailaddress,profession=profession, address=address, gps=gps)
        x.save()
        data = {
            # 'is_taken': Site.objects.filter(site_id__iexact=username).exists()
            'message':'saved'
        }
        return JsonResponse(data)


@login_required(login_url='login')
def student_ajax(request):
    if request.is_ajax:
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        othernames = request.POST.get('othernames')
        username = request.POST.get('username')
        emailaddress = request.POST.get('emailaddress')
        gender = request.POST.get('gender')
        group = request.POST.get('group')
        level = request.POST.get('level')
        classAdmitted = request.POST.get('classAdmitted')
        yearOfadmission = request.POST.get('yearOfadmission')
        guardian = request.POST.get('guardian')
        # profession: $('#student #profession').val(),
        print(firstname, othernames, lastname, gender,group, username)
        print(emailaddress, level, classAdmitted, yearOfadmission, guardian)
        guardiandb = Guardian.objects.get(fullname=guardian)
        x = MyUser(firstname=firstname, lastname=lastname, othername=othernames, email=emailaddress, 
            username=username, gender=gender, group=group, level=level,classAdmitted=classAdmitted,yearOfadmission=yearOfadmission,
            guardian=guardiandb)
        data = {
            # 'is_taken': Site.objects.filter(site_id__iexact=username).exists()
            'message':'student ok'
        }
        return JsonResponse(data)


def doesuserexists(request):
    user = request.POST.get('user')
    # print(MyUser.objects.filter(username__iexact=user))
    u = MyUser.objects.filter(username__iexact=user)
    res = ""
    if u:
        res = "user already exists" 
    data = {
        'message': res
    }
    return JsonResponse(data)


def doesemailexists(request):
    email = request.POST.get('email')
    u = MyUser.objects.filter(email__iexact=email)
    res = ""
    if u:
        res = "email already exists" 
    data = {
        'message': res
    }
    return JsonResponse(data)
