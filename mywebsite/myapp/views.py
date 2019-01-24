from django.shortcuts import render
from django.shortcuts import redirect
from myapp.models import User, educators, file
from django.core.files.storage import FileSystemStorage
from collections import namedtuple
from PIL import Image
import cv2
import numpy
import scipy.misc
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

image_dir= os.path.join(BASE_DIR, "media")


# Create your views here.

def upload(request):
        list=[]
        if request.method=="POST":
                uploaded_file=request.FILES['document']
                name=request.POST.get('name')
                educourse=request.POST.get('educourse')
                filename=uploaded_file.name
                fs=FileSystemStorage();
                fs.save(uploaded_file.name,uploaded_file)
                file.objects.create(filename=filename,name=name,educourse=educourse)  
                imagePath = os.path.join(image_dir, filename)
                cascPath = r'/home/nagsen/mywebsite/haarcascade_frontalface_default.xml'
                print(imagePath)
# Create the haar cascade
                faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
                image = cv2.imread(imagePath)
                print(image)
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
                faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = 0
)

                print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
                for (x, y, w, h) in faces:
                       cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

     
                np_im=image
                np_im = np_im - 18
                new_im = Image.fromarray(np_im) 

                new_im.save("example.png")

                response = redirect('/myapp/signup/upload')
                return response
                            
              
                

# Create the haar cascade
                
                   
                   
                     
                     
               
        return render(request,'myapp/upload.html')
def nk(request):
        return render(request,'myapp/nk.html')

