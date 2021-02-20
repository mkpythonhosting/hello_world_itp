from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages,auth
from django.contrib.auth.models import User


# Create your views here.
def homemenu(request):
	return render(request, "menu/home_page.html")


def aboutmenu(request):
	return render(request, "menu/about_page.html")


def registermenu(request):
    #return HttpResponse('<h1>Hello, I am learning Django!</h1>')
    # Logic to register the User
    # if request is GET then display the registration form
    # else if its POST request then process the Form - validate the user info and perform the action
    if request.method == 'POST':
    	print("I am in POST request")
    	username=request.POST['username']
    	email=request.POST['email']
    	password=request.POST['password']
    	c_pass=request.POST['c_pass']
    	print("username :",username)
    	print("email :",email)
    	print("password1 :",password)
    	print("password2 :",c_pass)

    	if(password==c_pass):
    		if User.objects.filter(username=username).exists():
    			print('The username is not available/its already exists')
    			return redirect('login_page')
    		else:
    			user = User.objects.create_user(username=username,password=password,email=email)
    			user.save()
    			print("You are now registered and can login")
    			return redirect('login_page')
    	else:
    		print('Password do not match,please enter again')
    		return redirect("register_page")
    else:
    	print("I am in GET request")
    	return render(request,'menu/register_page.html')


def loginmenu(request):
	if request.method == 'POST':
		print("I am in POST request")
		unameEntered=request.POST['username']
		passEntered=request.POST['password']
		print("username :",unameEntered)
		userObject = auth.authenticate(username=unameEntered, password=passEntered)

		if userObject is not None:
			auth.login(request,userObject)
			print("User logged in")
			return redirect("home_page")
		else:
			print("Username/password invalid")
			return redirect("register_page")
	else:
		return render(request,"menu/login_page.html")







	# Steps
    # 1. Retrieve input entered by User by using request parameter
    # 2. Authenticate the User by passing username/password
    # 3. If success then return to Home page else show the error and ask for relogin
	# if request.method == 'POST':
	# 	username = request.POST["username"]
	# 	password = request.POST["password"]
		
	# 	user = auth.authenticate(username=username, password=password)
	# 	return render(request,'menu/login_page.html')
	# emailse:
	# 	return render(request,'menu/login_page.html')


def logout(request):
	if user is not None:
		auth.login(request,user)
		messages.success(request, "You are now logged in")
		return redirect('dashboard')
	else:
		messages.error(request,'Invalid username/password')
		return redirect('login')


			#Success if user variable is not NONE
      # CAll login to create the session
  #print("Invalid User/password")
	