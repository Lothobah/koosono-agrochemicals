# use to protect each category of users from accessing others homepage
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect,HttpResponse


class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self,request,view_func,view_args,view_kwargs):
        modulename=view_func.__module__
        print(modulename)
        user=request.user
        print(user)
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "agrochemicals_management_system.HodViews":
                    pass
                elif modulename == "agrochemicals_management_system.views" or modulename == "django.views.static":
                    pass
                else:
                    return HttpResponseRedirect(reverse("products"))
            
            else:
                return HttpResponseRedirect(reverse("home"))
        #elif user.is_not_authenticated:
            
                
            
        else:
            '''if modulename == "Student_Management_System.Website_Views" or modulename == "django.views.static":
                pass
            elif modulename == "Student_Management_System.views":
                pass
            else:
                return HttpResponseRedirect(reverse("web_home"))'''
            if request.path == reverse("home") or request.path == reverse("do_login") or request.path == reverse("reset_password") or modulename == "django.contrib.auth.views":
                pass  
            else:
                return HttpResponseRedirect(reverse("home"))
