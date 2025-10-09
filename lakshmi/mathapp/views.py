from django.shortcuts import render
def calculate_BMI(request):
  context = {}
  context['BMI'] = "0"
  context['height'] = "0"
  context['weight'] = "0"
  if (request.method=="POST"):
    print("POST method is used")
    height = request.POST.get("height","0")
    weight = request.POST.get("weight","0")
    print("Request=", request)
    print("Height=", height)
    print("Weight=", weight)
    BMI = float(weight)/(float(height)*float(height))
    context['BMI'] = BMI
    context['height'] = height
    context['weight'] = weight
    print("BMI=", BMI)
  return render (request,'mathapp/math.html',context)

