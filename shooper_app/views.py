
from django.shortcuts import render,HttpResponse,redirect
from .models import*
from django.core.mail import send_mail
import random
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
import razorpay
from django.utils import timezone
# Create your views here.



"""================================================"""
"""----------Home page--------"""
def index(request):
    if 'email' in request.session:
        uid=User.objects.get(email=request.session['email'])
        mc=Main_category.objects.all()
        sc=Sub_category.objects.all()
        count=Add_to_cart.objects.filter(user_id=uid).count()
        countt=Add_to_whishlist.objects.filter(user_id=uid).count()
        
        # count1=Order.objects.filter(user_id=uid).count()
        
        mc2=request.GET.get("mc2")
        
        context={"uid":uid,'mc':mc,'sc':sc,'mc2':mc2,"count":count,"countt":countt}
        return render(request,"index.html",context)
    else:
        return render(request,"login.html")


"""================================================"""
"""----------Login Page--------"""

def login(request):
    if 'email'in request.session:
        return render(request,"index.html")
    try:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']
            
            uid=User.objects.get(email=email)
            if uid.email==email:
                request.session['email']=uid.email
                if uid.password==password:
                    return redirect("index")
                else:   
                    return render(request,"login.html")
            else:
                return render(request,"login.html")
        else:
            return render(request,"login.html")
    except:
        return render(request,"login.html")


"""================================================"""
"""----------Register Page--------"""


def register(request):

    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['c_password']
        
        try:
            uid=User.objects.get(email=email)
            if uid.email==email:
                con={"e_msg":"This Email ID is Already Login Add Another Email"}
                return render(request,"register.html",con)
        except:
            if password==c_password:
                User.objects.create(name=name,email=email,password=password)
                
                return render(request,"login.html")
            else:
                con={'e_msg': "Passwords do not match",}
                return render(request,"register.html",con)
            
    else:
        return render(request,"register.html")


"""================================================"""
"""----------Forgot Page OTP--------"""

def forget(request):
    if request.POST:
        email=request.POST['email']
        otp=random.randint(1000,9999)
        try:
            uid=User.objects.get(email=email)
        
            uid.otp=otp
            uid.save()
            send_mail("django",f"your otp is - {otp}",'gohiljayb10@gmail.com',[email])
            contaxt={
                "email":email
            }
            return render(request,"confirm_password.html",contaxt)
        except:
            print("Invalid Email")       
            return render(request,"forget.html") 
    else:
        return render(request,"forget.html")


"""================================================"""
"""---------- After OTP Confirm Password Page --------"""

def confirm_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        print(email, otp)
                                
        try:
            uid = User.objects.get(email=email)

            if str(uid.otp) == otp:
                print(otp)
                
                if new_password == confirm_password:
                    uid.password = new_password
                    uid.save()
                    print("Password Successfully Changed")
                    
                    context = {
                        'email': email,
                        'uid': uid,
                        'emsg': 'Login Password Changed Successfully'
                    }
                    return render(request, "login.html", context)
                else:
                    print("Passwords do not match")
                    context = {
                        "email": email,
                        'emsg': "Passwords do not match",
                    }
                    return render(request, "confirm_password.html", context)
            else:
                print("Invalid OTP")
                context = {
                    "email": email,
                    'emsg': "Invalid OTP" 
                }
                return render(request, "confirm_password.html", context)
        
        except:
            print("User not found")
            context = {
                "email": email,
                'emsg': "User not found",
            }
            return render(request, "confirm_password.html", context)
    
    return render(request, "confirm_password.html")

      

"""================================================"""
"""----------Logout Page--------"""



def logout(request):
    
    if 'email' in request.session:
        del request.session['email']
        return render(request,'login.html')
    else:
        return render(request,'login.html')



"""================================================"""
"""----------Contact Page--------"""

def contact(request):
    uid=User.objects.get(email=request.session['email'])
    
    mc=Main_category.objects.all()
    sc=Sub_category.objects.all()
    countt=Add_to_whishlist.objects.filter(user_id=uid).count()
    count=Add_to_cart.objects.filter(user_id=uid).count()
    
    mc2=request.GET.get("mc2")
    
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
            
        Contact.objects.create(name=name,email=email,subject=subject,message=message)
    context={"uid":uid,'mc':mc,'sc':sc,'mc2':mc2,"countt":countt,"count":count}
    return render(request,"contact.html",context)


"""================================================"""
"""----------Shop page--------"""
def shop(request):
    uid=User.objects.get(email=request.session['email'])
    count=Add_to_cart.objects.filter(user_id=uid).count()
    mc=Main_category.objects.all()
    wishlist_products = Add_to_whishlist.objects.filter(user_id=uid)
    countt=Add_to_whishlist.objects.filter(user_id=uid).count()
    
    l1=[]
    for i in wishlist_products:
        l1.append(i.product_id.id)
    mc2=request.GET.get("mc2")
    
    sc=Sub_category.objects.all()
    sc2=request.GET.get("sc2")
    
    pid=product.objects.all().order_by("-id")
    
    # piz=price.objects.all()
    # piz2=request.GET.get("piz2")
    
    sid=size.objects.all()
    sid2=request.GET.get("sid2")
    
    
    cid=color.objects.all()
    cid2=request.GET.get("cid2")
    
    s=request.GET.get("sort")
    
    
    
    pfid=price.objects.all()
        # print(pfid)
    pfidg=request.GET.get("pfid")
    
    
    
    # if piz2:
    #     pid=product.objects.filter(price1=piz2)
    
    
    if pfidg=="all":
        pid=product.objects.order_by("-id") 
    elif pfidg:
        pid=product.objects.filter(price1=pfidg)
    elif sid2:
        pid=product.objects.filter(size1=sid2)
    elif cid2:
        pid=product.objects.filter(color=cid2)
    elif mc2:
        pid=product.objects.filter(sub_category=mc2)
    elif sc2:
        pid=product.objects.filter(name=sc2)
    elif s=="lth":
        pid=product.objects.all().order_by("price")
    elif s=="htl":
        pid=product.objects.all().order_by("-price")
    elif s=="atz":
        pid=product.objects.all().order_by("name")
    elif s=="zta":
        pid=product.objects.all().order_by("-name")
        
    
    else:
        pid=product.objects.all().order_by("-id")
    

    paginator=Paginator(pid,1) 
    page_number=request.GET.get("page",1) 
    if page_number == "...":
        print("okokokokk")
    pid=paginator.get_page(page_number)
    # show_page = paginator.get_elided_page_range(page_number, on_each_side=1, on_ends=2)
    show_page=paginator.get_elided_page_range(page_number,on_each_side=1,on_ends=2)
    
    context={'mc':mc,'sc':sc,'mc2':mc2,'pid':pid,"uid":uid,'sid':sid,'cid':cid,"count":count,"pfid":pfid,"wishlist_products":wishlist_products,"l1":l1,"countt":countt,"show_page":show_page}
    return render(request,"shop.html",context)



#========================================================


def pagi(request):
    data_list = range(1, 101)  # A list of 100 items
    paginator1 = Paginator(data_list, 3)  # Show 10 items per page
    
    # Get the current page number from the query parameters
    page_number = request.GET.get('page', 1)
    page_number = int(page_number)  # Convert to integer
    
    # Get the elided page range for the current page
    elided_page_range = paginator1.get_elided_page_range(number=page_number, on_each_side=2, on_ends=2)
    
    context = {
        'elided_page_range': elided_page_range,
        'current_page': page_number,  # Pass current page number to context
        'paginator': paginator1,
        'page_obj': paginator1.page(page_number),
    }
    return render(request, 'pagi.html', context)



"""================================================"""
"""----------Color Filter--------"""

# def color_filter(request):
#     c1=request.GET.get("color-1")
#     c2=request.GET.get("color-2")
#     c3=request.GET.get("color-3")
#     c4=request.GET.get("color-4")
#     c5=request.GET.get("color-5")
#     pid=[]
#     if c1:
#         print("Black")
#         p=product.objects.filter(color="Black")
#         pid.extend(p)
#     if c2:
#         print("White")
#         p=product.objects.filter(color="White")
#         pid.extend(p)
#     if c3:
#         print("Red")
#         p=product.objects.filter(color="Red")
#         pid.extend(p) 
#     if c4:
#         print("Blue")  
#         p=product.objects.filter(color="Blue")
#         pid.extend(p) 
#     if c5:
#         print("Green")  
#         p=product.objects.filter(color="Green")
#         pid.extend(p)
#     if len(pid) == 0:
#         print("ok")      
#     contaxt={
#         "pid":pid,
#         "p_count":len(pid)
#     }
#     return render(request, 'shop.html',contaxt)






# def color_filter(request):
#     a1=request.GET.getlist("color-1")
#     pid=product.objects.all()
#     cid=color.objects.all()
#     pid=[]
    
#     for i in a1:
#         a=product.objects.get(name=i)
#         m=color.objects.filter(name=a)
#         pid.extend(m)
        
#     con={"cid":cid,"pid":pid}    
#     return render(request, 'shop.html',con)

def color_filter(request):
    a1 = request.GET.getlist("color-1")
    pid = product.objects.all()

    if a1:
        pid = product.objects.filter(color__name__in=a1)
    color_count = len(pid)
    cid = color.objects.all()
    con = {"cid": cid, "pid": pid,"color_count":color_count}
    return render(request, 'shop.html', con)


# def course_instroctor_cate(request):
#     cat=Course_category.objects.all()
#     iid1=Instructor.objects.all()
#     l1=request.GET.getlist("option-instructor")

#     iid1=[]
#     for i in l1:
#         a=Instructor.objects.get(name=i)
#         p=Instructor.objects.filter(name=a)
#         iid1.extend(p)
    
    
#     print(iid1)
#     print(l1)
#     con={"cat":cat,"iid1":iid1} 
#     return render(request,"instructor.html",con)

"""================================================"""
"""----------Price page--------"""
def price_filter(request):
    p1=request.GET.get("price-1")
    p2=request.GET.get("price-2")
    p3=request.GET.get("price-3")
    p4=request.GET.get("price-4")
    p5=request.GET.get("price-5")
    pid=[]
    if p1:
        p=product.objects.filter(price1="0 - 500")
        pid.extend(p)
    if p2:
        p=product.objects.filter(price1="500 - 3000")
        pid.extend(p)
    if p3:
        p=product.objects.filter(price1="3000 - 10000")
        pid.extend(p)
        
    if p4:
        p=product.objects.filter(price1="10000 - 40000")
        pid.extend(p)
    if p5:
        p=product.objects.filter(price1="40000 - 60000")
        pid.extend(p)
    if len(pid) == 0:
        print("OK") 
    con={"pid":pid,"p_count":len(pid)}
    return render(request,"shop.html",con)





"""================================================"""
"""---------- Search Item--------"""
def search(request):
    srh=request.GET.get("srh")
    print(srh)
    if srh:
        pid=product.objects.filter(name__contains=srh)
        print(pid)
    con={"pid":pid}
    return render(request,"index.html",con)


"""================================================"""
"""----------Product Details--------"""
import math

def detail1(request,id):
    uid=User.objects.get(email=request.session['email'])
    pid=product.objects.get(id=id)
    rate_id=Rating.objects.filter(product_id=pid)
    count=Add_to_cart.objects.filter(user_id=uid).count()
    r_count=Rating.objects.filter(product_id=pid).count()
    countt=Add_to_whishlist.objects.filter(user_id=uid).count()
    sid=size.objects.all()
    cid=color.objects.all()
    # l1=[]
    # for i in rate_id:
    #     l1.append(i.rating) 
    # print(l1)
    # a=sum(l1)/rate_id.count()   #start count and sum:- total stars/total reviews
    # print(a)
    # a1=math.ceil(a)     #  for half star
    # print(a1)
    l1 = []
    for i in rate_id:
        l1.append(i.rating)

    print(l1)

    if rate_id.count() > 0:
        a = sum(l1)/rate_id.count()#start count and sum: total stars/total reviews
        print(a)
        a1 = math.ceil(a)  # for half star
        print(a1)
    else:
        a = 0
        a1 = 0
        print("No ratings available")
        
    
    con={'pid':pid,"count":count,"rate_id":rate_id,"countt":countt,"r_count":r_count,"sid":sid,"cid":cid,"a":a,"a1":a1}
    return render(request,"detail.html",con)

# --------------------
# Details Page Through Quantity Increment Decrement 

def single_add_to_cart(request,id):
    if 'email' in request.session:
        if request.POST:
            qty=request.POST['qty']
            print(qty,type(qty))
            uid=User.objects.get(email=request.session['email'])
            pid=product.objects.get(id=id)
            pcid=Add_to_cart.objects.filter(product_id=pid,user_id=uid).first()
            
            if pcid:
                pcid.quantity=pcid.quantity+int(qty)
                pcid.total_price=pcid.quantity*pcid.price
                pcid.save()
            else:
                Add_to_cart.objects.create(product_id=pid,user_id=uid,
                                           name=pid.name,
                                           image=pid.image,
                                           price=pid.price,
                                           quantity=int(qty),
                                           total_price=int(qty)*pid.price)
            return redirect("cart")
    else:
        return redirect("cart")
    

 
def detail(request):
    mc=Main_category.objects.all()
    sc=Sub_category.objects.all()
    rate_id=Rating.objects.all()
    mc2=request.GET.get("mc2")
    context={'mc':mc,'sc':sc,'mc2':mc2,"rate_id":rate_id}
    return render(request,"detail.html",context)


"""================================================"""
"""----------CART--------"""
def add_to_cart(request, id):
    if 'email' in request.session:
        uid = User.objects.get(email=request.session['email'])
        pid = product.objects.get(id=id)
        pcid = Add_to_cart.objects.filter(product_id=pid, user_id=uid).first()
                      
        if pcid:
            pcid.quantity = pcid.quantity + 1
            pcid.total_price = pcid.quantity * pcid.price
            pcid.save()
        else:
            Add_to_cart.objects.create(
                product_id=pid,
                user_id=uid,
                name=pid.name,
                image=pid.image,
                price=pid.price,
                total_price=pid.quantity * pid.price
            )

        return redirect("cart")
    else:
        return redirect("cart")

"""================================================"""

     
def cart(request):
    if "email" in request.session:
        uid=User.objects.get(email=request.session['email'])
        cid=Add_to_cart.objects.filter(user_id=uid)
        prod=Add_to_cart.objects.filter(user_id=uid)
        count=Add_to_cart.objects.filter(user_id=uid).count()
        countt=Add_to_whishlist.objects.filter(user_id=uid).count()
        pid=product.objects.all().order_by("-id")
        
        l1=[]
        sub_total=0
        charge=50
        total=0
        discount=0
        for i in prod:
            a=i.quantity*i.price
            l1.append(a)
            sub_total=sum(l1)

        con={"user_id":uid,"product_id":pid,
                "cid":cid,"total":total,"sub_total":sub_total,"charge":charge,"count":count,"countt":countt,"discount":discount}
        return render(request,"cart.html",con)
    else:
        return render(request,"cart.html")
                
        
            
    

"""================================================"""
"""----------Coupon CODE--------"""


def apply_coupon(request):
    uid=User.objects.get(email=request.session['email'])
    aid=Add_to_cart.objects.filter(user_id=uid)
    
    
    l1=[]
    sub_total=0
    charge=50
    for i in aid:
        l1.append(i.total_price)
    print(l1)
    sub_total=sum(l1)
    print(sub_total)
    total=sub_total+charge
    discount=0
    if request.POST:
        coupon=request.POST['code']
        print(coupon)
        caid=coupon_code.objects.filter(code=coupon).exists()
        print(caid)
        if caid:
            cid=coupon_code.objects.get(code=coupon)
            total-=cid.discount
            discount=cid.discount
            request.session['discount']=discount
            contaxt={"uid":uid,
                "aid":aid,
                "sub_total":sub_total,
                "total":total,
                "charge":charge,
                "discount":discount,}
            # return render(request,"cart.html",contaxt)
            return redirect("cart")
        else:
            contaxt={"uid":uid,
                "aid":aid,
                "sub_total":sub_total,
                "total":total,
                "charge":charge,
                "discount":0,
                }
            return render(request,"cart.html",contaxt)

    else:
        return render(request,"cart.html")
                                                  

"""================================================"""
"""----------CART Increment Decrement--------"""
def cart_plus(request,id):
    c=Add_to_cart.objects.get(id=id)
    if c:
        c.quantity=c.quantity+1
        c.total_price=c.quantity*c.price
        c.save()
        return redirect("cart")
    


def cart_mines(request,id):
    c=Add_to_cart.objects.get(id=id)
    if c.quantity==1:
        c.delete()
        return redirect("cart")
    else:
        if c:
            c.quantity=c.quantity-1
            c.total_price=c.quantity*c.price
            c.save()
            
            return redirect("cart")
 
def cart_remove(request,id):
    remove=Add_to_cart.objects.get(id=id)
    remove.delete()   
    return redirect("cart")        
 

  
"""================================================"""
"""----------Checkout Payment--------"""
# def checkout(request):
#     uid=User.objects.get(email=request.session['email'])
#     count=Add_to_cart.objects.filter(user_id=uid).count()
#     countt=Add_to_whishlist.objects.filter(user_id=uid).count()
    
#     mc=Main_category.objects.all()
#     cid=Add_to_cart.objects.filter(user_id=uid)
#     sc=Sub_category.objects.all()



#     list1=[]
#     sub_total=0
#     total_price=1
#     charge=0
#    
#     for i in cid:
#         m=i.price*i.quantity
#         list1.append(m)
#         sub_total=sum(list1)
#         charge=50
#         total_price=sub_total+charge

    
#     if request.POST:
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         email=request.POST['email']
#         phone=request.POST['phone']
#         address=request.POST['address']
#         country=request.POST['country']
#         city=request.POST['city']
#         state=request.POST['state']
#         zip_code=request.POST['zip_code']
#         phone = int(phone)
#         zip_code = int(zip_code)

#         Address.objects.create(first_name=first_name,last_name=last_name,email=email,
#                                        phone=phone,address=address,country=country,
#                                        city=city,state=state,zip_code=zip_code)
        
                                                                
#     amount = total_price*100 #100 here means 1 dollar,1 rupree if currency INR
#     client = razorpay.Client(auth=('rzp_test_uqhoYnBzHjbvGF','jEhBs6Qp9hMeGfq5FyU45cVi'))
#     response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
#     print(response,"*******")



#     con={"ch":ch,
#         'uid':uid,
#         'count':count,
#         'mc':mc,
#         'cid':cid,

#         'response':response,
#         'sub_total':sub_total,
#         'charge':charge,
#         'total_price':total_price,
#         'sc':sc,
#         "countt":countt}
#     return render(request,"checkout.html",con)



def checkout(request):
    uid=User.objects.get(email=request.session['email'])
    count=Add_to_cart.objects.filter(user_id=uid).count()
    countt=Add_to_whishlist.objects.filter(user_id=uid).count()
    
    mc=Main_category.objects.all()
    cid=Add_to_cart.objects.filter(user_id=uid)
    sc=Sub_category.objects.all()

                                

    list1=[]
    sub_total=0
    total_price=1
    charge=0
    dis=0
    for i in cid:
        m=i.price*i.quantity
        list1.append(m)
        sub_total=sum(list1)
        charge=50
        discount=0
        dis=None
        total_price=sub_total+charge

        if sub_total==0:
            charge=0
            total_price=0
        else:
            charge=50
        if "discount" in request.session:
            dis=request.session.get("discount")
            total_price=sub_total+charge-dis
            print(dis)
        else:
            dis=0
            total_price=sub_total+charge
        if total_price==0:
            con={"ch":ch,
            'uid':uid,
            'count':count,
            'mc':mc,
            'cid':cid,
            'sub_total':sub_total,
            'charge':charge,
            'total_price':total_price,
            'sc':sc,
            "discount":dis,
            "countt":countt}
            return render(request,"checkout.html",con)
    else:


                                                                
        amount = total_price*100 #100 here means 1 dollar,1 rupree if currency INR
        client = razorpay.Client(auth=('rzp_test_uqhoYnBzHjbvGF','jEhBs6Qp9hMeGfq5FyU45cVi'))
        response = client.order.create({'amount':amount,'currency':'INR','payment_capture':1})
        print(response,"*******")



        con={"ch":ch,
            'uid':uid,
            'count':count,
            'mc':mc,
            'cid':cid,
            "discount":dis,
            'response':response,
            'sub_total':sub_total,
            'charge':charge,
            'total_price':total_price,
            'sc':sc,
            "countt":countt}
        return render(request,"checkout.html",con)




"""================================================"""
"""----------Order Confirm Page--------"""

def order(request):
    sc=Sub_category.objects.all()
    uid=User.objects.get(email=request.session['email'])
    countt=Order.objects.filter(user_id=uid).count()
    pro=Add_to_cart.objects.filter(user_id=uid)
    countt=Order.objects.filter(user_id=uid).count()
    ord=Order.objects.filter(user_id=uid)
    countt=Add_to_whishlist.objects.filter(user_id=uid).count()
    
    print(ord)
    
    
    if request.POST:
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        country=request.POST['country']
        city=request.POST['city']
        state=request.POST['state']
        zip_code=request.POST['zip_code']
        phone = int(phone)
        zip_code = int(zip_code)

        Address.objects.create(first_name=first_name,last_name=last_name,email=email,
                                       phone=phone,address=address,country=country,
    
                                       city=city,state=state,zip_code=zip_code)
    total_price=1    
    for i in pro:
        print(i.name)
        
        total_price = sum(product.price * product.quantity for product in pro) #100
    client = razorpay.Client(auth=('rzp_test_uqhoYnBzHjbvGF','jEhBs6Qp9hMeGfq5FyU45cVi'))
    response = client.order.create({'amount': total_price * 100, 'currency': 'INR', 'payment_capture': 1})
    print(response,"********")

    for i in pro:
        print(i.name)

        Order.objects.create(order_id=response['id'],user_id=uid,
                             image=i.image,
                             name=i.name,
                             price=i.price,
                             quantity=i.quantity,
                             total=i.price*i.quantity,
                             total_price=total_price,
                             )

        i.delete()


    con={'uid':uid,
             'ord':ord,
             'sc':sc,
             'countt':countt,
             'pro':pro,
             "countt":countt,
             }
    return render(request,"order.html",con)

def order_delete(request,id):
    dell=Order.objects.get(id=id)
    dell.delete()
    return redirect("order")


# def order_id(request):
#     uid=User.objects.get(email=request.session['email'])
#     otid=Order.objects.filter(order_id=uid)
#     if request.method == 'POST':
#         order_id = request.POST.get('order_id')
#         uid = User.objects.get(email=request.session['email'])
#     print(order_id)
#     for i in otid:
#         Order.objects.create(order_id=order_id,user_id=uid)
#     con={"otid":otid}
#     return render(request,"order_id.html",con)


def order_track(request):
    
    if request.method == 'POST':
        order_id = request.POST['order_id']
        uid = User.objects.get(email=request.session['email'])
        
        otid = Order.objects.filter(order_id=order_id, user_id=uid)
        print(otid)
        
        
        context = {"otid": otid,"chh":chh}
        return render(request, "order_track.html", context)
    else:
        return render(request, "order_id.html")


"""=============================================="""
"""----------⭐ Item Rating & Reviews ⭐--------"""

from django.urls import reverse
def create_rating(request):
    if request.method == 'POST':
        rate = request.POST['rate']
        comment = request.POST['comment']
        name = request.POST['name']
        email = request.POST['email']
        product_id = request.POST['product_id']

        date = timezone.localtime(timezone.now()).date()
        
         
        redirect_url = reverse('detail1', kwargs={'id': product_id})
        
        pid = product.objects.get(id=product_id)
        Rating.objects.create(product_id=pid, rating=rate, comment=comment, name=name, email=email, date=date)
        
        return redirect(redirect_url)

    return render(request, "detail.html")


"""================================================"""
"""----------Whishlist page--------"""
def add_whishlist(request, id):
    uid = User.objects.get(email=request.session['email'])
    pid = product.objects.get(id=id)
    wid = Add_to_whishlist.objects.filter(product_id=pid, user_id=uid).first()
    
    if wid:
        wid.delete()
        messages.info(request, "Item Removed From Your Wishlist")
    else:
        Add_to_whishlist.objects.create(
            user_id=uid,
            product_id=pid,
            price=pid.price,
            name=pid.name,
            image=pid.image,
        )
        messages.info(request, "Item Saved In Your Wishlist")

    return redirect('shop')
    
    

def remove_whishlist(request, id):
    c=Add_to_whishlist.objects.get(id=id)
    c.delete()
    return redirect('whishlist')



def whishlist(request):
    uid=User.objects.get(email=request.session['email'])
    wwid=Add_to_whishlist.objects.filter(user_id=uid) 
    countt=Add_to_whishlist.objects.filter(user_id=uid).count()
    
    con={"uid":uid,"wwid":wwid,"countt":countt}
    
    return render(request,"whishlist.html",con)



# ================================


"""================================================"""
"""----------User Profile Page--------"""
    
def user_profile(request,id):
    uid=User.objects.get(email=request.session['email'])
    user=User.objects.get(id=id)
    
    
    context = {
       "user":user,
        'uid':uid,
    }
    return render(request,"profile.html",context)  


#------Show Profile-----


def show_profile(request):
    uid=User.objects.get(email=request.session["email"])
    con={"uid":uid}
    return render(request,"profile.html",con)
        
         
#----Edit Profile Page----      


def edit_profile(request, id):
    uid = User.objects.get(email=request.session['email'])
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if "image" in request.FILES:
            image=request.FILES['image']
            uid.image=image
            uid.name = name
            uid.email = email
            uid.password = password
            uid.save()
            request.session['email']=email
            return redirect("user_profile", id=uid.id)
        else:
            uid.name = name
            uid.email = email
            uid.password = password
            uid.save()
            request.session['email']=email
            return redirect("user_profile", id=uid.id)
    context = {'uid': uid,}
    return render(request, "edit_profile.html", context)


"""================================================"""
"""----------User Profile Page--------"""

       
def invoice(request):
    uid=User.objects.get(email=request.session['email'])
    bid=Address.objects.filter(user_id=uid).order_by("-id")[:1]
    for i in bid:
        print(i.first_name,i.last_name)
    oid=Order.objects.order_by("-id")[:1]
    a=None
    datetime=None   
    for i in oid:
        a=i.order_id
        datetime=i.datetime
        print(i.order_id)
    print(a)    
    oid1=Order.objects.filter(order_id=a)
    print(oid1)
    l1=[]
    sub_total=0
    for i in oid1:
        l1.append(i.price)
    sub_total=sum(l1)
    charge=50
    discount=sub_total*10/100
    my_variable = request.session.get('my_variable', 0)
    total_price = sub_total + charge - my_variable

    print("ok",my_variable)
    contaxt={"oid":oid,
        "bid":bid,
        "oid1":oid1,
        "a":a,
        "sub_total":sub_total,
        "charge":charge,
        "discount":my_variable,
        "datetime":datetime,
        "total_price":total_price,}
    return render(request, 'invoice.html',contaxt)


