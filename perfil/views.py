from django.shortcuts import render
from django.views import View

# Create your views here.

class ProfileView(View):

    def get(self, request):

        
        user = request.user;
        print(user)

        
        print(request)

        return render(request, 'profile/home.html')
