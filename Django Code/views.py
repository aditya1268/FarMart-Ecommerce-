from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import*
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import  login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def front_page(request):
        
        return render(request, "page_front.html")
def front_page1(request):
        
        return render(request, "page_front.html")


def register_page(request):
        
        if (request.method=="POST"):
                store1_name=request.POST['store_name']
                store_username=request.POST['store_username']
                store_password=request.POST['store_password']
                store_address=request.POST['store_address']
                
                print(store1_name)
                print(store_username)
                print(store_password)
                store1 = Store.objects.filter(store_username=store_username).exists()
                if(store1):
                        messages.info(request, "Username is Already taken")
                        return redirect('/second_page/')

                data=Store.objects.create(
                store1_name=store1_name , 
                store_username=store_username,
                store_password=store_password,
                store_address=store_address
                )   
                


                print(data.store_password)   
                return redirect('/second_page/')  
        
        return render(request,'secondpage.html')



# if (request.method=="POST"):
#           first_name=request.POST['first_name']
#           last_name=request.POST['last_name']
#           username=request.POST['user_name']
#           password=request.POST['password']
          
#           user=User.objects.filter(username=username)
#           if(user.exists()):
#                messages.info(request, "Username is Already taken")
#                return redirect('/register/')
              
#           data=User.objects.create_user(
#              first_name=first_name , 
#              last_name=last_name,
#              username=username
#           )
#           data.set_password(password)
#           data.save()
#           messages.info(request, "Account created sucessfully")

#           return redirect('/register/')
     
#      return render(request,'register.html')


def user_show1(request):
        queryset=Store.objects.all()
        context={"stores_all":queryset}
        
        return render(request, "total_user.html",context)

# def add_vege(request):
#         if(request.method=="POST"):
#             data=request.POST
#             recipi_imag=request.FILES.get("recipi_imag")
#             recipi_name=data.get("recipi_name")
#             recipi_descr=data.get("recipi_descr")
#             print(recipi_name)
#             print(recipi_descr)

#             print(recipi_imag)
#             Recipi.objects.create(recipi_name=recipi_name,
#                                   recipi_descr=recipi_descr,
#                                   recipi_imag=recipi_imag
#                                 )
#             return redirect  ( '/recipie/')
#         queryset=Recipi.objects.all()
#         if request.GET.get('Search'):
#                 queryset=queryset.filter(recipi_name__icontains=request.GET.get('Search'))
         
#         context={'rcepies':queryset}

#         print (queryset)
#         return render (request, 'recepies.html',context)


def login_store(request):
        if(request.method=="POST"):
           username = request.POST.get('store_username')
          
           password=request.POST['store_password']
           print(password)
           print(username)

           if not  Store.objects.filter(store_username=username).exists():
               messages.error(request,"USERNAME not found ")
               return redirect('/second_page/')
           try:
                user = Store.objects.get(store_username=username)
           except Store.DoesNotExist:
                user = None
           store1 = authenticate(store_username=username, store_password=password)
           
           print(store1)
           
           if user is not None and user.store_password == password:
                
                return redirect ( f"/show_veges/<{username}>/")
                

               

           else:
    
               messages.error(request,"invalid username or password")
               return redirect('/login/')

           
        
        return render(request,'login_store.html')


# def show_veges(request):
     

#      queryset=vegetables.objects.filter(Store__store_username=store_username)
#      total_marks=queryset.aggregate(total_marks=Sum('marks'))
#      return render (request, 'student_marks.html',{"queryset": queryset,"total_marks":total_marks}) 

def show_veges(request,store_username):
                print(store_username)
                if(request.method=="POST"):
                        data=request.POST
                        selected_category = data.get('category')
                        
                        vege_imag=request.FILES.get("vege_imag")
                        vege_descr=data.get("vege_descr")
                        vege_name=data.get("vege_name")
                        vege_price=data.get("vege_price")
                        vege_count=data.get("vege_count")
                        print(vege_name)
                        print(vege_descr)
                        print(vege_imag)
                        stores=Store.objects.get(store_username=store_username[1:len(store_username)-1])
                        print(stores)
                        vegetables.objects.create(
                               store=stores,
                        vege_name=vege_name,
                        vege_descr=vege_descr,
                        vege_imag=vege_imag,
                        vege_count=vege_count,
                        vege_price=vege_price,
                        selected_category=selected_category
                        )
                        
                         
                        return redirect ( f"/show_veges/{store_username}/")


                k1=vegetables.objects.filter(store__store_username=store_username[1:len(store_username)-1]).values()
                k=Store.objects.filter(store_username=store_username[1:len(store_username)-1]).values()
                print(k)
                context={"stores_veges_all":k1,"Store_username":k}
                # [0]["store_username"]

                
                return render(request, "show_veges.html",context)


def user_veges_show(request):
       k=vegetables.objects.all()
       context={"stores_veges_all":k}
       return render(request, "show_allveges.html",context)

def delete_vege(request,id ):
      print(id)
      k1= vegetables.objects.filter(id=id).values()[0]["store_id"]
      k2=Store.objects.filter(id=k1).values()[0]["store_username"]
      queryset=vegetables.objects.get(id=id)
      queryset.delete()
      
      
      return redirect ( f"/show_veges/<{k2}>/")
      
def update_vege(request , id ):
      queryset=vegetables.objects.get(id=id)
      if request.method=="POST":
        data=request.POST
        selected_category = data.get('category')
        vege_imag=request.FILES.get("vege_imag")
        vege_descr=data.get("vege_descr")
        vege_name=data.get("vege_name")
        vege_price=data.get("vege_price")
        vege_count=data.get("vege_count")
        queryset.vege_descr=vege_descr
        queryset.vege_price=vege_price
        queryset.vege_count=vege_count
        queryset.vege_name=vege_name
        queryset.selected_category=selected_category

        if vege_imag:
          queryset.vege_imag=vege_imag

        queryset.save()
        
        k1= vegetables.objects.filter(id=id).values()[0]["store_id"]
        k2=Store.objects.filter(id=k1).values()[0]["store_username"]
        
        return redirect ( f"/show_veges/<{k2}>/")      
      context={'recipie':queryset}

      return render  ( request ,'update_vege.html',context)



def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        name = request.POST.get('name')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        store1 = User1.objects.filter(username=username).exists()
        if(store1):
                        messages.info(request, "Username is Already taken")
                        return redirect('/register_user/')
        if(int (age)<0):
              messages.info(request, "Age Should be greater than zero Enter Valid Age")
              return redirect('/register_user/')
              
        user = User1.objects.create(
            username=username,
            password=password,
            address=address,
            name=name,
            age=age,
            phone_number=phone_number
        )
        user.save()
        print(user)
        return redirect('/login_user/')  

    return render(request, 'register_user.html')





def login_user(request):
        if request.method == 'POST':
           data=request.POST
           print(data)
           username = request.POST.get('username')
           password = request.POST.get('password')
           print(username) 
           print(password) 
           if not  User1.objects.filter(username=username).exists():
               messages.error(request,"USERNAME not found ")
               return redirect('/register_user/')
           try:
                user = User1.objects.get(username=username)
           except User1.DoesNotExist:
                user = None
           store1 = authenticate(username=username, password=password)
           
           print(store1)
           
           if user is not None and user.password == password:
                
                return redirect ( f"/user_dashboard/<{username}>/")
                

               

           else:
    
               messages.error(request,"invalid username or password")
               return redirect('/login_user/')

           
        
        return render(request,'login_user.html')


def user_dashboard(request,username):
        k=username[1:len(username)-1]
        user = User1.objects.get(username=k)
        print(user)  
        context={'user_details': user}
        return render(request, 'user_dashboard.html',context )  


def fruit_show(request):
      user = vegetables.objects.filter(selected_category__iexact="fruits"  )
      print(user)  
      context={'fruitlist': user}
      return render(request, 'fruit_show1.html',context ) 

def homeproduct_show(request):
      user = vegetables.objects.filter(selected_category__iexact="home_products"  )
      print(user)  
      context={'homelist': user}
      return render(request, 'home_products1.html',context ) 


def vegetables_show(request):
      user = vegetables.objects.filter(selected_category__iexact="vegetables"  )
      print(user)  
      context={'homelist': user}
      return render(request, 'home_products1.html',context ) 

def addtocart(request):
      
      return render(request, "checkout_page.html")