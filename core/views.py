from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from social_django.models import UserSocialAuth
from core.models import Profile
from django.conf import settings  
from datetime import datetime
import qrcode
import uuid
import os
import jwt

def get_token(qr_input:dict):
    SECRET_KEY = "python_jwt"
    encode_data = jwt.encode(payload=qr_input,key=SECRET_KEY, algorithm="HS256")
    return encode_data

def make_qrcode(qr_input:dict):
    img=qrcode.make(qr_input)
    file_name='{}{:-%Y%m%d%H%M%S}'.format(str(uuid.uuid4().hex), datetime.now())
    path_file=os.getcwd()
    img.save(f'{path_file}{settings.MEDIA_URL}qr_code_images/{file_name}.png')
    return file_name

@login_required(login_url='signin')
def update(request,uid):
      
    if request.method == 'POST':
        address= request.POST["address"]
        city= request.POST["city"]
        phone= int(request.POST["phone"])
        image = request.FILES.get('image')
        
        p=Profile(address=address,city=city,phone=phone,user_id=uid,profileimg=image)
        p.save()
        message="Your informaiton has been updated !"
        p=Profile.objects.get(user_id=uid)
        user_object=User.objects.get(id=uid)
        qr_input={
        'address':p.address,
        'city':p.city,
        'phone':p.phone,
        'name':user_object.username
                }
        token=get_token(qr_input)      
        qr_name=make_qrcode(qr_input)
        qr_to_be_saved=f'qr_code_images/{qr_name}.png' #file name and path of qr code 
        p.qrcode=qr_to_be_saved
        p.token=token
        p.save()
        context={
        'message':message,
        'p':p
        }
        return render(request, 'dashboard.html',context)   
    else:

        return render(request,'index.html'  )

@login_required
def home(request):
    return render(request,'index.html')    











