# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from templated_email import send_templated_mail #criar o arquivo de template do email

def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        send_templated_mail(
        		template_name='email',
        		from_email= email,
        		recipient_list=[''],
        		context={
            		'nome':nome,
            		'telefone':telefone,
            		'mensagem':mensagem,
            		'assunto':assunto,
            		'email':email,
        		},
			)

        
    return render(request, 'index.html',)