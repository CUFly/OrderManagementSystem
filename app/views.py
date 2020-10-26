from django.shortcuts import render, redirect
from .models import Customer,Product,Order
from .forms import CustomerForm, OrderForm
# Create your views here.


def indexpage(request):
    return render(request, 'app/index.html')

def homepage(request):
    # apt_list = ['APT1', 'APT2', 'APT3', 'APT4']
    # context = {
    #     'apt_list': apt_list
    # }
    customer = Customer.objects.all()
    c_count = customer.count()

    order_p_count = Order.objects.filter(status='Pending').count()
    order_d_count = Order.objects.filter(status='Delivered').count()
    order_o_count = Order.objects.filter(status='Out for delivering').count()



    order = Order.objects.all()
    o_count = order.count()
    c = 0
    last_five = []
    for i in reversed(order):
        if c >= 5:
            break
        last_five.append(i)
        c += 1



    context = {
        'customer': customer,
        'c_count': c_count,
        'o_count': o_count,
        'order': order,
        'last_five': last_five,
        'order_p_count': order_p_count,
        'order_d_count': order_d_count,
        'order_o_count': order_o_count,
    }

    return render(request, 'app/home.html', context)


def create(request):
    c_form = CustomerForm()
    o_form = OrderForm()

    if request.method == 'POST':
        if 'c-button' in request.POST:
            c_form = CustomerForm(request.POST)
            if c_form.is_valid():
                name_get = c_form.cleaned_data['name']
                phone_get = c_form.cleaned_data['phone']
                email_get = c_form.cleaned_data['email']
                customer = Customer.objects.create(name=name_get, phone=phone_get, email=email_get)
                customer.save()
                return redirect('homepage')

        if 'o-button' in request.POST:
            o_form = OrderForm(request.POST)
            if o_form.is_valid():
                customer_get = o_form.cleaned_data['custom']
                product_get = o_form.cleaned_data['product']
                status_get = o_form.cleaned_data['status']
                order = Order.objects.create(custom=customer_get, product=product_get, status=status_get)
                order.save()
                return redirect('homepage')

    context = {
        'c_form': c_form,
        'o_form': o_form
    }
    return render(request, 'app/create.html', context)


def updateorder(request, pk):
    order = Order.objects.get(id=pk)
    o_form = OrderForm(instance=order)

    if request.method == 'POST':
        o_form = OrderForm(request.POST)
        if o_form.is_valid():
            customer_get = o_form.cleaned_data['custom']
            product_get = o_form.cleaned_data['product']
            status_get = o_form.cleaned_data['status']
            order = Order.objects.filter(id=pk)
            order.update(custom=customer_get, product=product_get, status=status_get)
            return redirect('homepage')

    context = {
        'order': order,
        'o_form': o_form
    }
    return render(request, 'app/updateorder.html', context)

def deleteorder(request, pk):
    order = Order.objects.get(id=pk)
    # message = ''

    if request.method == 'POST':
        order.delete()
        # message = 'delete successfully!'
        return redirect('homepage')

    context = {
        'order': order
    }
    return render(request, 'app/deleteorder.html', context)
