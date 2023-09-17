# randomfloatapp/views.py
from django.shortcuts import render
from .models import RandomFloatGenerator
from .forms import InputStringForm
import random

def generate_random_float(request):
    input_string = None  # Initialize input_string with a default value

    if request.method == 'POST':
        form = InputStringForm(request.POST)
        if form.is_valid():
            input_string = form.cleaned_data['input_string']
            
            # Check if the string has already been entered and generate values only if it's a new string
            if not RandomFloatGenerator.objects.filter(input_string=input_string).exists():
                num_generated = 0  # Track the number of generated values
                while num_generated < 500:  # Generate 500 values
                    random_value = random.uniform(0, 1)
                    RandomFloatGenerator.objects.create(input_string=input_string, random_value=random_value)
                    num_generated += 1

    else:
        form = InputStringForm()
    
    if input_string:
        random_floats = RandomFloatGenerator.objects.filter(input_string=input_string)
    else:
        random_floats = []

    return render(request, 'preqinApp/generate_random_float.html', {'form': form, 'random_floats': random_floats})
