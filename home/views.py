from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout
from .models import NumeroUrgence
from .models import Kit
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from django.urls import path
from .forms import FavoriteKitForm
from django.contrib import messages
from django.http import JsonResponse
import html
import google.generativeai as genai

def index(request):
   context = {
        'segment': 'index',
        'numero_urgences': NumeroUrgence.objects.all(),
         'products' : Product.objects.all(),
         'kit': Kit.objects.all()
          
    }
   return render(request, "pages/index.html", context)

def tables(request):
  context = {
    'segment': 'tables'
  }
  return render(request, "pages/dynamic-tables.html", context)



def add_to_favorites(request, kit_id):
    if request.method == 'POST':
        form = FavoriteKitForm(request.POST)
        if form.is_valid():
            favorite_kit = form.save(commit=False)
            favorite_kit.user = request.user
            favorite_kit.kit_id = kit_id
            favorite_kit.save()
            return redirect('index')  # Redirect to index page after adding to favorites
    else:
        form = FavoriteKitForm()
    return render(request, 'favorite_kits.html', {'form': form})

# Define a view function for 'favorite_kits'
def favorite_kits(request):
    # Fetch favorite kits associated with the current user
    favorite_kits = FavoriteKit.objects.filter(user=request.user)

    # Pass favorite kits to the template context
    return render(request, 'favorite_kits.html', {'favorite_kits': favorite_kits})

#def purchase_kit(request, id):
#    if request.method == 'POST':
#        kit = Kit.objects.get(id=id)
#        kit.purchase_count += 1
#        kit.save()
#        return redirect('index')  # Redirect to the desired page after the purchase
#    else:
#        return redirect('index') 


# Configure the API key
genai.configure(api_key="Je l'ai supprimmé pour maitre le repositary en public")


system_instruction = "Hello! I'm Urgiebot, your emergency assistance bot. My purpose is to provide aid during emergencies and disasters.Here's how our conversation will go:,I'll start by introducing myself and explaining my purpose,Then, I'll ask you to specify the type of catastrophe you're interested in.,Once you've made your selection, I'll provide concise yet comprehensive information about the chosen catastrophe,This information will include general details about the catastrophe, preventive measures you can take, and the essential items you'll need in your survival kit,Let's work together to ensure your safety and preparedness during emergencies!\n\n"


# Create the chatbot model
model = genai.GenerativeModel('gemini-1.5-pro-latest',
                              system_instruction=system_instruction,
                            )


chat = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["heyy"]
  },
  {
    "role": "model",
    "parts": ["Hi, I'm your urgiebot! I'm here to provide help during emergencies and disasters. \n\nTo get started, please tell me which type of catastrophe you'd like information on."]
  },
  {
    "role": "user",
    "parts": ["snowstorm"]
  },
  {
    "role": "model",
    "parts": [
    "<h2>Earthquake Preparedness</h2><br>",
    "<br>",
    "<b>General Information:</b> Earthquakes are sudden and violent shaking of the ground, caused by the movement of tectonic plates. They can strike without warning and cause significant damage to buildings and infrastructure. <br>",
    "<br>",
    "<b>Preventive Measures:</b><br>",
    "<br>",
    "* <b>Secure your space:</b> Identify and fix potential hazards in your home, like unsecured furniture and appliances. <br>",
    "* <b>Plan and practice:</b> Conduct earthquake drills with your family to ensure everyone knows what to do during and after an earthquake. <br>",
    "* <b>Learn first aid:</b> Basic first-aid skills can be crucial in the aftermath of an earthquake. <br>",
    "<br>",
    "<b>Survival Kit Essentials:</b><br>",
    "<br>",
    "* <b>Food and water:</b> Non-perishable food items and bottled water for at least 3 days. <br>",
    "* <b>First-aid kit:</b> Essential medical supplies for treating injuries. <br>",
    "* <b>Dust mask and goggles:</b> To protect your lungs and eyes from dust and debris. <br>",
    "* <b>Whistle:</b> To signal for help if trapped. <br>",
    "* <b>Sturdy shoes:</b> To protect your feet from broken glass and debris. <br>",
    "* <b>Wrench or pliers:</b> To shut off utilities if necessary. <br>",
    "* <b>Fire extinguisher:</b> Small fire extinguisher for potential fires. <br>",
    "* <b>Emergency radio and flashlight:</b> Battery-powered for communication and light. <br>",
    "* <b>Cash and important documents:</b> Keep copies of essential documents and some cash in a waterproof container. <br>",
    "<br>",
    "<b>Remember, during an earthquake, \"Drop, Cover, and Hold On.\" Stay away from windows and exterior walls. After the shaking stops, evacuate if necessary and be prepared for aftershocks.</b>"
  ]

  },
])



def chatbot_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        response = chat.send_message(user_input)
        decoded_response = html.unescape(response.text)
        return JsonResponse({'response': decoded_response})
    return render(request, "pages/chatbot.html")

