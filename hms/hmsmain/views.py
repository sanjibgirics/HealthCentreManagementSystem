from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth import login, logout, authenticate
from .models import MyUser,Medicine,Order,orderDetail,Consumption,consumptionDetail
# Create your views here.


def index(request):
    #return HttpResponse("kjnii")
    return render(request,'hmsmain/index.html')

def about(request):
    return render(request,'hmsmain/about.html')

def facilities(request):
    return render(request,'hmsmain/facilities.html')


def people(request):
    return render(request, 'hmsmain/people.html')

def login1(request):
    #return HttpResponse("kjnii")

    return render(request, 'hmsmain/loginform.html')

def logout1(request):
    logout(request);
    return render(request,'hmsmain/index.html')

def loginHandle(req):
    if req.method == 'POST':
        try:
            data = req.POST.copy()
            print(data)
        except:
            return HttpResponse('<h2> Incorrect Request Body</h2>')
        try:
            username = data.get('username')
            password = data.get('pwd')
        except KeyError as missing_data:
            return HttpResponse('<h2> Missing key - {0} </h2>'.format(missing_data))
        user1 = authenticate(username=username, password=password)
        if user1 is not None:
            login(req, user1)
            try:
                user = MyUser.objects.get(user=user1)
            except Exception:
                return HttpResponse('<h2>Profile for this user does not exist!</h2>')
            utype = str(user.utype)
            print(utype)
            return render(req, 'hmsmain/index.html')
        else:
            return HttpResponse('<h2> Unable to Login</h2>')
    elif req.method == 'GET':
        return redirect('hmshome/userHome.html')

def addMedicine(request):
    #return HttpResponse("kjnii")

    return render(request, 'hmsmain/addMedicineForm.html')

def addMedicineHandle(req):
    if req.method == 'POST':
            mnamel = req.POST.getlist('mname[]')
            minfol = req.POST.getlist('minfo[]')
            mpricel = req.POST.getlist('mprice[]')
            mqtyl = req.POST.getlist('mqty[]')
            for i in range(len(mnamel)):
                med = Medicine(mname=mnamel[i],minfo = minfol[i],mprice = mpricel[i],mqty = mqtyl[i])
                med.save()
            return HttpResponse('Added')
    else:
            return HttpResponse('<h2> Unable to dat</h2>'
                                )
def raiseOrder(request):
    mnames = Medicine.objects.all()
    return render(request, 'hmsmain/raiseOrderForm.html', {'mnames': mnames})

def raiseOrderHandle(req):
    if req.method == 'POST':
        data = req.POST.getlist
        order = Order()
        order.save()
        omidl = req.POST.getlist('omid[]')
        omqty = req.POST.getlist('omqty[]')
        total = 0
        for i in range(len(omidl)):
            omid = Medicine.objects.get(pk=omidl[i])
            total += int(omid.mprice) * int(omqty[i])
            om = orderDetail(ooid=order,omid = omid,omqty = omqty[i])
            om.save()
        order.total = total;
        order.save()
        return HttpResponse('Order Added')
    else:
            return HttpResponse('<h2> Unable to dat</h2>')

def viewMedicine(request):
    mnames = Medicine.objects.all()
    return render(request, 'hmsmain/viewMedicine.html', {'mnames': mnames})

def viewPendingOrders(request):
    utype = request.GET.get('utype')
    orderl = list(Order.objects.filter(status=utype))
    orderdetaill = orderDetail.objects.all()
    medicinel = Medicine.objects.all()
    return render(request, 'hmsmain/viewPendingOrders.html', {'orderl': orderl,'orderdetaill':orderdetaill,
                                                              'medicinel':medicinel,'utype':utype})
def forwardOrder(request):
    order1 = request.POST.get('oid')
    comment = request.POST.get('comment')
    print(order1)
    order1 = Order.objects.get(pk=order1)
    status = order1.status
    order1.status = status+1;
    order1.lastComment = comment;
    order1.save()
    return render(request,'hmsmain/index.html')
def revertOrder(request):
    user1 = request.user
    user = MyUser.objects.get(user=user1)
    utype = user.utype
    order1 = request.POST.get('oid')
    comment = request.POST.get('comment')
    print(order1)
    order1 = Order.objects.get(pk=order1)
    if utype != 1:
        order1.status = 1;
    else:
        order1.status = 0;
    order1.lastComment = comment;
    order1.save()
    return render(request, 'hmsmain/index.html')

def userHome(request):
    #return HttpResponse("kjnii")
    user1 = request.user
    user = MyUser.objects.get(user=user1)
    utype = str(user.utype)
    return render(request, 'hmsmain/userHome.html',{'utype':utype})

def viewOrders(request):
    orderl = Order.objects.all()
    orderdetaill = orderDetail.objects.all()
    medicinel = Medicine.objects.all()
    return render(request, 'hmsmain/viewOrders.html', {'orderl': orderl,'orderdetaill':orderdetaill,
                                                              'medicinel':medicinel})

def issueMedicine(request):
    mnames = Medicine.objects.all()
    return render(request, 'hmsmain/issueMedicineForm.html', {'mnames': mnames})

def issueMedicineHandle(req):
    if req.method == 'POST':
        data = req.POST.getlist
        patientID = req.POST.get('patientID');
        desc = req.POST.get('desc');
        consumption = Consumption(patientID=patientID,desc=desc);
        consumption.save()
        omidl = req.POST.getlist('omid[]')
        omqty = req.POST.getlist('omqty[]')
        for i in range(len(omidl)):
            omid = Medicine.objects.get(pk=omidl[i])
            if int(omid.mqty) - int(omqty[i]) < 0:
                return HttpResponse('Medicine stocks not available')
            omid.mqty = int(omid.mqty) - int(omqty[i])
            omid.save()
            om = consumptionDetail(ccid=consumption,cmid = omid,cmqty = omqty[i])
            om.save()
        return HttpResponse('Record Added')
    else:
            return HttpResponse('<h2> Unable to Record</h2>')


def viewConsumption(request):
    consumptionl = Consumption.objects.all()
    consumptiondetaill = consumptionDetail.objects.all()
    medicinel = Medicine.objects.all()
    return render(request, 'hmsmain/viewConsumption.html', {'consumptionl': consumptionl,'consumptiondetaill':consumptiondetaill,
                                                              'medicinel':medicinel})

def editOrderPage(request):
    order1 = request.GET.get('oid')
    orderl = Order.objects.get(pk = order1)
    orderdetaill = orderDetail.objects.all()
    medicinel = Medicine.objects.all()
    return render(request, 'hmsmain/editOrder.html', {'m': orderl, 'orderdetaill': orderdetaill,
                                                       'medicinel': medicinel})

def editOrder(request):
    order1 = request.POST.get('oid')
    omid = request.POST.get('omid')
    nqty = request.POST.get('nqty')
    print(order1)
    print(omid)
    print(nqty)
    try:
        medicine1 = orderDetail.objects.get(ooid=order1,omid=omid)
    except orderDetail.DoesNotExist:
        return HttpResponse('<h2>No Record</h2>')
    print(medicine1)
    if int(nqty) != 0:
        medicine1.ooid.total = (medicine1.ooid.total -  (int(medicine1.omid.mprice) * int(medicine1.omqty))
        ) + (int(medicine1.omid.mprice) * int(nqty))
        medicine1.omqty = nqty
        medicine1.ooid.save()
        medicine1.save()
    else:
        medicine1.delete()
    return render(request, 'hmsmain/index.html')