from django.shortcuts import render,redirect
from .models import Tweet
from .forms import Tweetform, UserRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.


def index(request):
    return render(request,'index.html')


#To list all the tweets in one page we will use queryset of ORM  | saare tweets ko ek page pr list krne ke liye hum queryset use krnge mtlb ORM.

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html', {'tweets':tweets})

#TO create Tweet using form and if the data is prefilled.
@login_required
def Tweet_create(request):          #if user already filled the form then we will use method.POST and if they give file then we use FILES
    if request.method=="POST":      #by using this POST we can get already filled tweet if its not already filled we send it to the else part.
        form= Tweetform(request.POST, request.FILES)
        if form.is_valid():                     #by using this we can check the security that the form is valid or not
            tweet=form.save(commit=False)    #by using we can save the data but not in the database 
            tweet.user=request.user     #by using this we will assign the request.user to tweet.user
            tweet.save()                    #we can save the form
            return redirect('tweet_list')
                    
    else:                       #this else section is used user wants to create the tweet using this form and 
        form = Tweetform()          #this will invoke when user don't have prefilled tweet then we render this form
        return render(request, 'tweet_form.html', {'form':form})
    
@login_required    
def Tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method=='POST':
        form = Tweetform(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save(commit=False)
            tweet.user=request.user
            form.save()
            return redirect('tweet_list')
    else:
        form= Tweetform(instance=tweet)    #We are taking instance=tweet so that we can get a prefilled tweet for editing and the tweet which is passing we gave it some value.
    return render(request,'tweet_form.html', {'form':form})

@login_required
def Tweet_delete(request, tweet_id):
    tweet= get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})


def Register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'registration/register.html',{'form':form})



def Aboutus(request):
    return render(request, 'aboutus.html')

def Contactus(request):
    return render(request,'contactus.html')