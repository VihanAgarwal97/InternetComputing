from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from models import Message


@login_required
def home(request):
    return render(request, 'messenger/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'messenger/signup.html', {'form': form})

def sent(request):
    sent_msgs = Message.objects.filter(author = request.user.id, sent=True)
    print(sent_msgs)
    return render(request,'messenger/sent.html',{'msgs': sent_msgs})

def inbox(request):
    msgs = Message.objects.filter(receiver = request.user.id, sent=True)
    return render(request,'messenger/inbox.html', {'msgs':msgs})

def drafts(request):
    drft_msgs = Message.objects.filter(author = request.user.id, sent=False)
    return render(request,'messenger/drafts.html', {'msgs':drft_msgs})

def create(request, id=None):
    #Is the request a POST or GET?
    if request.method == "POST":
        #POST REQUEST
        resp = request.POST
        #Is this updating a current message or creating a new message?        
        if(id==None):
            #NEW
            sendto= int(resp.get("sendto"))
            #Check if the user has chosen to send the message or save it as a draft
            if(resp.get("action") == "send"):
                #SEND
                new_msg = Message(text = resp.get('msg'), sent = True, author = request.user, receiver = User.objects.get(id= sendto))
                new_msg.save()
            else:
                #SAVE
                new_msg = Message(text = resp.get('msg'), sent = False, author = request.user, receiver = User.objects.get(id= sendto))
                new_msg.save()
        else:
            #EXISTING MESSAGE
            curr_msg = Message.objects.get(id = id)
            curr_msg.text = resp.get('msg')
            sendto= int(resp.get("sendto"))
            curr_msg.receiver = User.objects.get(id=sendto)
            
            #Check if the user has chosen to send the message or save it as a draft
            if(resp.get("action") == "send"):
                #SEND
                curr_msg.sent = True
                curr_msg.save()
            else:
                #SAVE
                curr_msg.sent = False
                curr_msg.save()
        return render(request, 'messenger/home.html')
    else:
        #GET REQUEST
        userSet = User.objects.all()
        if(id==None):
            msg = ""
            return render(request,'messenger/create.html',{'userList' : userSet, "msg":msg})
        else:
            msg = Message.objects.get(id = id)
            return render(request, 'messenger/create.html', {'userList' : userSet, "msg":msg})
