from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import TodolistSerializer
from .models import Todolist

#GET Data
@api_view(['GET'])

def all_todolist(request):
	alltodolist = Todolist.objects.all() #ดึงข้อมูลจาก model Todolist
	serializer = TodolistSerializer(alltodolist,many=True)
	return Response(serializer.data, status=status.HTTP_200_OK)

# POST Data (save data to database)
@api_view(['POST'])
def post_todolist(request):
	if request.method == 'POST':
		serializer = TodolistSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def update_todolist(request,TID):
	# localhost:8000/api/update-todolist/13
	todo = Todolist.objects.get(id=TID)

	if request.method == 'PUT':
		data = {}
		serializer = TodolistSerializer(todo,data=request.data)
		if serializer.is_valid():
			serializer.save()
			data['status'] = 'update'
			return Response(data=data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_todolist(request,TID):
	todo = Todolist.objects.get(id=TID)

	if request.method == 'DELETE':
		delete = todo.delete()
		data = {}
		if delete:
			data['status'] = 'delete'
			statuscode = status.HTTP_200_OK
		else:
			data['status'] = 'Failed'
			statuscode = status.HTTP_400_BAD_REQUEST

		return Response(data=data, status=statuscode)



data = [
	{
		"title":"เบอร์เกอร์หมู",
		"subtitle":"เป็นอาหารชนิดหนึ่งที่ถือว่าอยู่ในประเภทเดียวกับแซนด์วิช",
		"image_url":"https://raw.githubusercontent.com/jiejieji/BasicAPI/main/hamber.jpg",
		"detail":"แฮมเบอร์เกอร์ (อังกฤษ: hamburger) หรือเรียกสั้น ๆ ว่า เบอร์เกอร์ (burger) เป็นอาหารชนิดหนึ่งที่ถือว่าอยู่ในประเภทเดียวกับแซนด์วิช ประกอบด้วยเนื้อสัตว์ปรุงแล้วที่มีลักษณะเป็นแผ่นสอดไส้อยู่ตรงกลาง อาทิ เนื้อวัว เนื้อหมู เนื้อปลาทอด หรือเป็นเนื้อสัตว์หลายประเภทผสมกัน ประกบบนล่างด้วยขนมปังแผ่นกลม /n/nมีการสอดไส้ด้วยผักชนิดต่างๆ เช่น มะเขือเทศ ผักกาดหอม หอมหัวใหญ่ ชีสและเครื่องปรุงรสอื่น เช่น มัสตาร์ด มายองเนส ซอสมะเขือเทศ เป็นต้น แฮมเบอร์เกอร์เป็นอาหารที่ได้รับความนิยมและแพร่หลายไปทั่วโลก"
	},
	{
		"title":"เบอร์เกอร์ไก่",
		"subtitle":"เป็นอาหารชนิดหนึ่งที่ถือว่าอยู่ในประเภทเดียวกับแซนด์วิช",
		"image_url":"https://raw.githubusercontent.com/jiejieji/BasicAPI/main/chicken-burger.jpg",
		"detail":"แฮมเบอร์เกอร์ (อังกฤษ: hamburger) หรือเรียกสั้น ๆ ว่า เบอร์เกอร์ (burger) เป็นอาหารชนิดหนึ่งที่ถือว่าอยู่ในประเภทเดียวกับแซนด์วิช ประกอบด้วยเนื้อสัตว์ปรุงแล้วที่มีลักษณะเป็นแผ่นสอดไส้อยู่ตรงกลาง อาทิ เนื้อวัว เนื้อหมู เนื้อปลาทอด หรือเป็นเนื้อสัตว์หลายประเภทผสมกัน ประกบบนล่างด้วยขนมปังแผ่นกลม /n/nมีการสอดไส้ด้วยผักชนิดต่างๆ เช่น มะเขือเทศ ผักกาดหอม หอมหัวใหญ่ ชีสและเครื่องปรุงรสอื่น เช่น มัสตาร์ด มายองเนส ซอสมะเขือเทศ เป็นต้น แฮมเบอร์เกอร์เป็นอาหารที่ได้รับความนิยมและแพร่หลายไปทั่วโลก"
	},
	{
		"title":"ชีสเบอร์เกอร์",
		"subtitle":"เป็นอาหารชนิดหนึ่งที่ถือว่าอยู่ในประเภทเดียวกับแซนด์วิช",
		"image_url":"https://raw.githubusercontent.com/jiejieji/BasicAPI/main/burger.jpg",
		"detail":"แฮมเบอร์เกอร์ (อังกฤษ: hamburger) หรือเรียกสั้น ๆ ว่า เบอร์เกอร์ (burger) เป็นอาหารชนิดหนึ่งที่ถือว่าอยู่ในประเภทเดียวกับแซนด์วิช ประกอบด้วยเนื้อสัตว์ปรุงแล้วที่มีลักษณะเป็นแผ่นสอดไส้อยู่ตรงกลาง อาทิ เนื้อวัว เนื้อหมู เนื้อปลาทอด หรือเป็นเนื้อสัตว์หลายประเภทผสมกัน ประกบบนล่างด้วยขนมปังแผ่นกลม /n/nมีการสอดไส้ด้วยผักชนิดต่างๆ เช่น มะเขือเทศ ผักกาดหอม หอมหัวใหญ่ ชีสและเครื่องปรุงรสอื่น เช่น มัสตาร์ด มายองเนส ซอสมะเขือเทศ เป็นต้น แฮมเบอร์เกอร์เป็นอาหารที่ได้รับความนิยมและแพร่หลายไปทั่วโลก"
	}
 

]


def Home(request):
	return JsonResponse(data=data,safe=False,json_dumps_params={'ensure_ascii': False})
