from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import collections.abc
collections.Hashable = collections.abc.Hashable

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot = ChatBot('chatbot',read_only=False,
              logic_adapters=[
                      {
                      "import_path": "chatterbot.logic.BestMatch",
                      #"default_response" : "Sorry, I dont know what that means",
                      #"maximun_similarity_threshold" : 0.90 
                     
                      }
                      ]
                      )

list_to_train = [
        
      "hi",
      "hi, there",
      "What's your name?",
      "I'm just a chatbot",
      "What is your fav food?",
      "I like cheese",
      "What is your fav sports?",
      "swimming",
      "do you have children?",
      "no" 

]

chatterbotCorpusTrainer = ChatterBotCorpusTrainer(bot)
 

#list_trainer = ListTrainer(bot)
#list_trainer.train(list_to_train)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request,'blog/index.html')

def specific(request):
  
  return HttpResponse("list1")

def article(request,article_id):
   return render(request,'blog/index.html',{'article_id'})
   
def getResponse(request):
   userMessage= request.GET.get('userMessage')
   chatResponse = str(bot.get_response(userMessage))
   return HttpResponse(chatResponse)
