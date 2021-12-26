import vk_api 
from vk_api.longpoll import VkEventType, VkLongPoll 
import time 
  
token = vk_api.VkApi(token="токен") 
lox = VkLongPoll(token) 

def send(id, text, msgid, att): 
 token.method('messages.send',{'chat_id' : id, 'message' : text, 'random_id' : 0, 'attachment' : att, 'reply_to':msgid })
 
while True: 
 for event in lox.listen(): 
  if event.type == VkEventType.MESSAGE_NEW: 
   if event.from_chat: 
    idUser = event.user_id 
    id = event.chat_id 
    msg = event.text.lower() 
    msgid = event.message_id
    textspl = msg.split()
    
   if msg.startswith("бармить"):
     send(id, f"Ты сбармил {'  '.join(textspl[1:])}",msgid, '')

