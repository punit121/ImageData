from django.shortcuts import render
import subprocess, sys, shlex
from subprocess import check_output
import os
from subprocess import Popen, PIPE
# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
#from .serializers import EmbedSerializer
from .forms import UploadImageForm
from .models import ImageModel
from django.core.files.storage import FileSystemStorage
from django.core.management import call_command
from io import StringIO
import json
import time

def get_file_data():
	with open('data.txt') as data_file:
		value = json.load(data_file)
	return value	

	

def index(request):
	if request.method == "POST":
		form = UploadImageForm(request.POST, request.FILES)
		if form.is_valid():
			myfile = request.FILES['image']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			uploaded_file_url = fs.url(filename)
			#m = ImageModel.objects.get(pk=id)
			#m.image = form.cleaned_data['image']
			#m.save()

		#parser_classes = (MultiPartParser, FormParser)


		img_url= uploaded_file_url
		#file_serializer = FileSerializer(data=request.data)

		print(img_url)

		os.chdir('hawkeye/TensorFlow_Image_Classification')
		#out = StringIO()
		cmd = "python classify_image.py --image_file test_images/road_bike_25.jpg"
		#call_command('python classify_image.py --image_file test_images/car_test.jpeg', stdout=out)
		#data = request.get('python classify_image.py --image_file test_images/car_test.jpeg')
		args = shlex.split(cmd)
		#p = subprocess.Popen(args)
		#(out,err) = p.communicate()[0]
		p=subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)
		out=p.communicate()
		print(out)
		#value = p.stdout.read()
		#print (p.stdout.readlines())
		#out = p.stderr.read(1)
		#value1 = json.dumps(p.communicate())
		value = get_file_data()

		print("Tensor Flow print done \n now returning value")
		#value = json.loads(out)
		#print(out)
		#value=out
		os.chdir('..')
		os.chdir('..')
		#time.sleep(6)
		os.chdir('hawkeye/nude.py')
		cmd_nude="python main.py "+img_url
		print(cmd_nude)
		q=subprocess.Popen(cmd_nude, shell=True, stderr=subprocess.PIPE)
		out1=q.communicate()
		print(out1)
		os.chdir('..')
		os.chdir('..')





		return render(request, 'hawkeye/result.html',{'value':value})

	else:
		return render(request, 'hawkeye/index.html')	


