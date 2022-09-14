from django.shortcuts import render, get_list_or_404
from django.core.mail import send_mail

from mugic.models import Projeto

def portfolio(request):

    projetos = Projeto.objects.filter(is_published=True).order_by('-id')
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        clientmessage = request.POST.get('clientmessage')

        data = {
            'name': name,
            'email': email,
            'clientmessage': clientmessage
        }
        print(data)
        message = '''
        New message: {}

        From: {}
        '''.format(data['clientmessage'], data['email'])
        send_mail(data['name'], message, email, ['mugic.contact@gmail.com'])

    return render(request, "portfolio/pages/home.html", context={'projetos': projetos,})

def projeto(request, id):
    projeto = get_list_or_404(Projeto.objects.filter(pk=id).order_by('-id'))
    return render(request, "portfolio/pages/projetos-views.html", context={
        'projeto': projeto[0],
        'is_detail_page': True,
    })

    