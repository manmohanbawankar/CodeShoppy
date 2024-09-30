from django.shortcuts import render, redirect
from skillapp.forms import ContactForm, CustomerForm, AdminForm, SellForm,  AddFeedbackForm, CommentForm,BuyForm
from skillapp.models import Contacts, Customer, Admin, Sell, AddFeedback, Comment,Buy

# Create your views here.

def index(request):
    return render(request,"index.html",{})

def about(request):
    return render(request,"about.html",{})

def contact(request):
    if request.method == "POST":
        print("hii")
        form = ContactForm(request.POST)
        print("hii")
        if form.is_valid():
            form.save()
        return render(request, "contact.html", {})
    return render(request, "contact.html", {})

#Customer Views
def customer(request):
    return render(request, "customer.html", {})

def customer_loginpage(request):
    return render(request, "customer_login.html", {"msg": ""})

def regpage(request):
    return render(request, "customer_reg.html", {})

def customer_reg(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except Exception as e:
                print(e)
    return render(request, "customer_login.html", {"msg": ""})

def customer_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        customer = Customer.objects.filter(email=email, password=password)
        if customer.exists():
            request.session["email"] = email
            return render(request, "customer.html", {"msg": email})
        else:
            return render(request, "customer_login.html", {"msg": "email or password not exist"})
    return render(request, "customer_login.html", {})

def unknown(request):
    return render(request,"customer.html",{})

def is_customer_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False
def customer_change(request):
    if is_customer_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]

            try:
                customer = Customer.objects.get(email=email, password=password)
                customer.password = newpassword
                customer.save()
                msg = "password updated successfully"
                return render(request, "customer_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "customer_change.html", {"msg": msg})
        return render(request, "customer_change.html", {})
    else:
        return render(request, "customer_change.html", {})

def display(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    print("hello")
    return render(request,"customer_display.html",{"customer":customer})

def delete(request, email):
    customer = Customer.objects.get(email=email)
    customer.delete()
    return redirect("/customer_reg")

def edit(request, email):
    customer = Customer.objects.get(email=email)
    return render(request, "edit.html", {"customer": customer})

def update(request):
    if request.method == "POST":
        customeremail = request.POST["email"]
        customer = Customer.objects.get(email=customeremail)
        customer = CustomerForm(request.POST, instance=customer)
        if customer.is_valid():
            customer.save()
        return redirect("/display")
    return redirect("/display")

def logout(request):
    if request.session.has_key("email"):
        email = request.session["email"]
    return render(request, "customer_login.html", {"email": email})

#Admin Views
def administration(request):
    return render(request, "administration.html", {})

def admin_login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        print(email, " ", password)
        admin = Admin.objects.all()
        if admin.exists():
            print("hello")
            request.session["email"] = email
            return render(request, "administration.html", {"msg": email})
        else:
            return render(request, "admin_login.html", {"msg": "email or password not exist"})
    return render(request, "admin_login.html", {"msg": ""})

def adminbro(request):
    return render(request,"administration.html",{})

def is_admini_login(request):
    if request.session.__contains__("email"):
        return True
    else:
        return False

def admini_change(request):
    if is_admini_login(request):
        if request.method == "POST":
            email = request.session["email"]
            password = request.POST["password"]
            newpassword = request.POST["newpassword"]

            try:
                admin = Admin.objects.get(email=email, password=password)
                admin.password = newpassword
                admin.save()
                msg = "password updated successfully"
                return render(request, "admin_login.html", {"msg": msg})
            except:
                msg = "inavlid data"
                return render(request, "admini_change.html", {"msg": msg})
        return render(request, "admini_change.html", {})
    else:
        return render(request, "admini_change.html", {})

def admini_display(request):
    customer = Customer.objects.all()
    # sell = Sell.objects.all()
    print("hello")
    return render(request, "admini_display.html", {"customer": customer})

def admini_mypurchase(request):
    # customer = Customer.objects.all()
    sell = Sell.objects.all()
    print("hello")
    return render(request, "admini_mypurchase.html", {"sell": sell})

def addfeedback(request):
    if request.method == "POST":
        addfeedback = AddFeedbackForm(request.POST)
        if addfeedback.is_valid():
            addfeedback.save()
        return render(request, "addfeedback.html", {"msg": "succes"})
    return render(request, "addfeedback.html", {})

def viewfeedback(request):
    addfeedback = Contacts.objects.all()
    return render(request, "viewfeedback.html", {"addfeedbacks": addfeedback})

def viewfeedback_delete(request, id):
    addfeedback = Contacts.objects.get(id=id)
    addfeedback.delete()
    addfeedback = Contacts.objects.all()
    return redirect("/viewfeedback",{"addfeedbacks":addfeedback})


def sell(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    if request.method == "POST":
        print("hii")
        print(customer.email)
        sell = SellForm(request.POST)
        print("hii", sell.errors)
        if sell.is_valid():
            sell.save()
            sell = Sell.objects.filter(customer_id=customer.id)
        return render(request, "sellview_my.html", {"msg": "success", "id": customer.id,"sells":sell})
    return render(request, "sell.html", { "email": customer.id})

def sellview_my(request):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    sell = Sell.objects.filter(customer_id=customer.id)
    print("hii")
    return render(request, "sellview_my.html", {"sells": sell})

def sell_edit(request, id):
    sell = Sell.objects.get(id=id)
    return render(request, "sell_edit.html", {"sell": sell})

def sell_update(request):
    global id
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    if request.method == "POST":
        sellid = request.POST["id"]
        sell = Sell.objects.get(id=sellid)
        sell = SellForm(request.POST, instance=sell)
        print("erroes",sell.errors)
        if sell.is_valid():
            sell.save()
            sell = Sell.objects.filter(customer_id=customer.id)
        return redirect("/sellview_my",{"sells":sell})
    return redirect("/sellview_my")


def sell_delete(request, id):
    sell = Sell.objects.get(id=id)
    sell.delete()
    sell = Sell.objects.filter(customer_id=customer.id)
    return redirect("/sell",{"sells":sell})

def sellview_all(request):
    email=request.session['email']
    customer=Customer.objects.get(email=email)
    sell = Sell.objects.exclude(customer_id=customer.id)
    return render(request, "sellview_all.html", {"sells": sell})


def sell_buy(request,id):
    email = request.session['email']
    customer= Customer.objects.get(email=email)
    project=Sell.objects.get(id=id)
    if request.method == "POST":
        buy= BuyForm(request.POST)
        if buy.is_valid():
            buy.save()
            bookings = Buy.objects.filter(customer_id=customer.id)
            return render(request,"mypurchase.html",{"msg":"success","id":project.id,"cost":project.cost,"description":project.description,"customer":customer.id,"buys":bookings})
    return render(request, "sell_buy.html", {"id": project.id, "cost": project.cost, "description":project.description,"customer":customer.id})


def sell_likes(request,id):
    sell = Sell.objects.get(id=id)
    sell.likes = sell.likes+1
    sell.save()
    sell = Sell.objects.all()
    return render(request, "sellview_all.html", {"sell": sell})


def sell_dislikes(request,id):
    sell = Sell.objects.get(id=id)
    sell.dislikes = sell.dislikes+1
    sell.save()
    sell = Sell.objects.all()
    return render(request, "sellview_all.html", {"sell": sell})


def my_purchase(request):
    email = request.session['email']
    customer=Customer.objects.get(email=email)
    print("hello1")
    bookings = Buy.objects.filter(customer_id=customer.id)
    print("hello")
    return render(request,"mypurchase.html",{"buys":bookings})


def comment(request,id):
    email = request.session['email']
    customer = Customer.objects.get(email=email)
    seller = Sell.objects.get(id=id)
    if request.method == "POST":
        print("hii")
        print(customer.email)
        comment = CommentForm(request.POST)
        print("hii", comment.errors)
        if comment.is_valid():
            comment.save()
        return render(request, "comment.html", {"msg": "success","id":seller.id,  "customer": customer.id})
    return render(request, "comment.html", {"id": seller.id,"email": customer.id})


def comment_update(request):
    if request.method == "POST":
        commentid = request.POST["id"]
        comment = Customer.objects.get(id=commentid)
        comment = CustomerForm(request.POST, instance=comment)
        if comment.is_valid():
            comment.save()
        return redirect("/viewcomment")
    return redirect("/viewcomment")

def viewcomment(request):
    comment = Comment.objects.all()
    return render(request, "viewcomment.html", {"comments": comment})

def admini_logout(request):
     if request.session.has_key("email"):
        email = request.session["email"]
        return render(request,"admin_login.html",{"email":email})


def view_reviews(request,id):
    place=Sell.objects.get(id=id)
    comment=Comment.objects.filter(sell_id=place.id)
    return render(request,"customer_view_comment.html",{"comments":comment})


def admin_view_projects(request):
    comment = Sell.objects.all()
    return render(request, "admin_view_projects.html", {"sells": comment})


def customer_del(request,id):
    customer=Customer.objects.get(id=id)
    customer.delete()
    customer=Customer.objects.all()
    return render(request,"admini_display.html",{"customers":customer})



def project_del(request,id):
    sells=Sell.objects.get(id=id)
    sells.delete()
    sell=Sell.objects.all()
    return render(request,"admin_view_projects.html",{"sells":sell})



def comment_del(request,id):
    sells=Comment.objects.get(id=id)
    sells.delete()
    sell=Comment.objects.all()
    return render(request,"viewcomment.html",{"comments":sell})



def customer_comment_del(request,id):
    sells=Comment.objects.get(id=id)
    sells.delete()
    comment=Comment.objects.filter(sell_id=sells.id)
    return render(request,"customer_view_comment.html",{"comments":comment})