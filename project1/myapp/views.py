from django.shortcuts import render, redirect
from .models import Company, Poster, Intern
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def home():
    return redirect('kaamkaj/')

def index(request):
    return render(request, 'Index.html')

@csrf_exempt
def companysignup(request):
    if request.method == "POST":
        c = Company(company_name=request.POST['companyname'], email=request.POST['companymail'], password=request.POST['companypass'], contact_number=request.POST['companynumber'])
        c.save()
        return redirect('/')

@csrf_exempt
def companylogin(request):
    cdetail = Company.objects.all()
    for i in cdetail:
        a = i.email
        b = i.password
        if request.method == "POST":
            cmail = request.POST['cmail']
            cpass = request.POST['cpass']
            if (cmail in a) and (cpass in b):
                cname = i.company_name
                return JsonResponse({'name': cname})

def company(request, cname):
    return render(request, 'CompanyInterface.html', {'cname': cname})

def companyprofile(request, cname):
    results = Company.objects.all().filter(company_name=cname)
    return render(request, 'Companyprofile.html', {'results': results})

@csrf_exempt
def poster(request):
    if request.method == "POST":
        poster = Poster(company_name=request.POST['company_name'],
                        company_description=request.POST['company_description'],
                        internship_description=request.POST['internship_description'],
                        responsibilities=request.POST['responsibilities'],
                        qualification=request.POST['qualification'],
                        benefits=request.POST['benefits'],
                        cost=request.POST['cost'],
                        start_date=request.POST['startdate'],
                        end_date=request.POST['lastdate'],
                        contact_info=request.POST['company_number'],
                        contact_info2=request.POST['employee_number'],
                        feedback=request.POST['feedback']
                        ).save()
        return redirect('/')

@csrf_exempt
def internsignup(request):
    if request.method == "POST":
        print("isme")
        c = Intern(name=request.POST['internname'], email=request.POST['internmail'], password=request.POST['internpass'], contact_number=request.POST['internnumber'])
        c.save()
        return JsonResponse({'show':'done'})

@csrf_exempt
def internlogin(request):
    idetail = Intern.objects.all()
    for i in idetail:
        a = i.email
        b = i.password
        if request.method == "POST":
            imail = request.POST['imail']
            ipass = request.POST['ipass']
            print(imail)
            print(ipass)
            if(imail in a) and (ipass in b):
                iname = i.name
                return JsonResponse({'name': iname})

@csrf_exempt
def intern(request, iname):
    post = Poster.objects.all()
    print(post)
    return render(request, 'StudentInterface.html', {'iname': iname, 'post':post})

def internprofile(request, iname):
    results = Intern.objects.all().filter(name=iname)
    return render(request, 'Internprofile.html', {'results': results})

