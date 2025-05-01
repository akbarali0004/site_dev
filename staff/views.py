from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff
from .forms import StaffForm



def staff_form(request):
    if request.method == "POST":
        form = StaffForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("staff_list")
    else:
        form = StaffForm()

    return render(request, 'staff_form.html', {"form": form})


def staff_view(request, pk):
    item = Staff.objects.get(id=pk)
    return render(request, 'staff_view.html', {'item':item})


def update_staff(request, pk):
    item = Staff.objects.get(id=pk)
    form = StaffForm(instance=item)

    if request.method == "POST":
        form = StaffForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('staff_list')
    return render(request, "update_staff.html", {'form':form})


def delete_staff(request, pk):
    Staff.objects.get(id=pk).delete()
    return redirect('staff_list')


def staff_list(request):
    staffs = Staff.objects.all().order_by('-id')
    return render(request, 'staff_list.html', {'staffs': staffs})













#domla
# def staff_form(request):
#     form = StaffForm(request.POST)
#     if request.POST and form.is_valid():
#         form.save()
#         return redirect("staff_list.html")
#     context = {
#         "form" : form
#     }

#     return render(request, 'staff_form.html', context)
















# def staff_view(request):
    # if request.POST:
    #     model = Staff()
    #     model.name = request.POST.get('name', '')
    #     model.surname = request.POST.get('surname', '')
    #     model.email = request.POST.get('email')
    #     model.age = request.POST.get('age', '')
    #     model.phone = request.POST.get('phone', '')
    #     model.save()

    #     print(request.POST)
        
    # return render(request, 'staff.html')