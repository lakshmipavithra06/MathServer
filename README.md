# Ex.05 Design a Website for Server Side Processing
## Date:09.10.2025

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
```
views.py 

from django.shortcuts import render
def calculate_power(request):
    P = 1
    if request.method=="POST":
        I=float(request.POST.get("Current"))
        R=float(request.POST.get("resistance"))
        P*=(I**2)*R
        print(f"Current: {I} ampere,resistance: {R} ohm,Power: {P} watt")
        return render(request,'powerapp/math.html',{"Current":I,"resistance":R,"power":P})
    return render(request,'powerapp/math.html',{"Current":I,"resistance":R,"power":P})

urls.py

from django.contrib import admin
from django.urls import path
from powerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('your-endpoint',views.calculate_power,name="calculate_power"),
]
math.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Power calculating</title>
    <style>
        h2,form,h3,p{
            text-align: center;
            width :100%;
        }
        div{
            margin: 235px;
            padding: auto;
        }
        legend{
            font-size: 20px;
            font-family: sans-serif;
        }
    </style>
</head>
<body>
    <fieldset>
    <legend>ISRAVEL Y (25018187)</legend>
   <div><h2>Power calculator</h2>
    <form method="POST">
        {% csrf_token %}
        <label>Current (ampere):</label>
        <input type="text" name="Current" required>
        
        <label>Resistance (ohm):</label>
        <input type="text" name="resistance" required>
        
        <button type="submit">Calculate Power</button>
    </form>
    {% if power %}
    <h2>P(power) equals to I<sup>2</sup>(square of current) times R(resistence)</h2>
    <h3>Input values</h3>
    <p>Current : {{Current}} ampere<br>Resistance : {{resistance}} ohm</p>
    <h3>Power : {{power}} watt</h3>
    {% endif %}
    </div></fieldset>

</body>
</html>
```

## SERVER SIDE PROCESSING:
![Screenshot_16-10-2025_112332_github com](https://github.com/user-attachments/assets/0bd54891-5807-449a-b87a-6626e739dd88)

## HOMEPAGE:
![Screenshot_16-10-2025_112413_github com](https://github.com/user-attachments/assets/0a1a1b97-8f01-4d3a-a396-c4f65b081f0d)


## RESULT:
The program for performing server side processing is completed successfully.
