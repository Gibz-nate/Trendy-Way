from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required 
from item.models import Item

from .models import Communication
from .forms import CommunicationMessageForm

# Create your views here.
@login_required
def new_conversation(request, item_pk ):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        
        return redirect('dashboard:index')


    conversation = Communication.objects.filter(item=item).filter(members__in=[request.user.id])    

    if conversation:
        return redirect('comms:detail', pk=conversation.first().id)

    if request.method == 'POST':
        form = CommunicationMessageForm(request.POST)

        if form.is_valid():
            conversation = Communication.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.communication =  conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)

    else:
        form = CommunicationMessageForm()

    return render(request, 'comms/new.html', {
        'form':form
    })   

@login_required
def inbox(request):
    conversation = Communication.objects.filter(members__in=[request.user.id])      


    return render(request, 'comms/inbox.html',{
        'conversation':conversation
    })
@login_required

def detail(request, pk):
    conversation = Communication.objects.filter(members__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form =  CommunicationMessageForm(request.POST) 

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.communication =  conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()


            return redirect('comms:detail', pk=pk)
    else:
        form = CommunicationMessageForm()





    return render(request, 'comms/detail.html',{
        'conversation':conversation,
        'form':form
    } )     







