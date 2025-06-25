from django.shortcuts import render, redirect
from django.contrib.auth import login,logout, authenticate , get_user_model
from django.contrib import messages
from .models import ValidRollNumber
from notes.models import Note


CustomUser = get_user_model()

def home(request):
    return render(request, "home.html")



def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     message = request.POST.get("message")

    #     messages.success(request, "Thank you for reaching out! We will get back to you soon.")
    #     return render(request, "contact.html")

    return render(request, "contact.html") 





def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        roll_number = request.POST["roll"]
        depertment = request.POST["depertment"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "auth/signup.html")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, "auth/signup.html")
        elif CustomUser.objects.filter(roll_number=roll_number).exists():
            messages.error(request, "Roll Number already exists")
            return render(request, "auth/signup.html")
        elif not ValidRollNumber.objects.filter(roll_number=roll_number).exists():
            messages.error(request, "Invalid Roll Number")
            return render(request, "auth/signup.html")
        elif not depertment:
            messages.error(request, "Depertment is required")
            return render(request, "auth/signup.html")
        else:
            user = CustomUser.objects.create_user(username=username, roll_number=roll_number, email=email, password=password, depertment=depertment)
            user.save()
            user.backend = 'Noteshare.backends.EmailRollNumberBackend'
            login(request, user)
            messages.success(request, "Account created successfully! ")
            return redirect("login")
    return render(request, "auth/signup.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        roll_no = request.POST['roll']
        password = request.POST["password"]

        user = authenticate(request, email=email, roll_no=roll_no, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "auth/login.html")
    return render(request, "auth/login.html")


def logout_view(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect("login")


def about_view(request):
    return render(request, "about.html")


def contact_view(request):
    # if request.method == "POST":
    #     name = request.POST.get("name")
    #     email = request.POST.get("email")
    #     message = request.POST.get("message")

    #     messages.success(request, "Thank you for reaching out! We will get back to you soon.")
    #     return render(request, "contact.html")

    return render(request, "contact.html") 



def share_notes(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        file = request.FILES.get('file')
        if title and content:
            Note.objects.create(
                title=title,
                content=content,
                file=file,
                author=request.user
            )
            messages.success(request, "Note shared successfully!")
            return redirect("share_notes")
            
        else:
            messages.error(request, "Title and content are required.")            
    notes = Note.objects.order_by('-created_at')      
    return render(request, "notes.html",{'notes':notes})