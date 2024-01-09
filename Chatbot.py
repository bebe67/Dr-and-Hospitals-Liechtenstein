import random

responses = { "hello" : ['Hi, how can I help you today?','Hello, how do you fell today?'],
             "hi" : ['hey, there!',"what's up?"],
             "i am feeling sick": ["so sorry to hear so you can visit the doctor here: https://play.teleporthq.io/projects/lovable-solid-kangaroo-k4geji/preview/d687d8c9-576c-4bb2-816c-115e1c2d7e3b","hope you get well soon, you can visit the hospitals here:https://play.teleporthq.io/projects/lovable-solid-kangaroo-k4geji/preview/15443d3d-885d-4c06-98fc-d79c48ddda80"],
             "my ears hurts" : ["oh, am so sorry to hear so, please visit the doctors here: https://play.teleporthq.io/projects/lovable-solid-kangaroo-k4geji/preview/64679e62-715a-47e9-bf2e-45002c93cc39"], 
             "my tooth really hurts" : ["so sorry to hear so, please visit:  https://play.teleporthq.io/projects/lovable-solid-kangaroo-k4geji/preview/e66a7042-b3a3-4458-86f6-2e559d0baa98 "],
             "my heart is not good" : ["oh, am so sorry to hear so, please visit: https://play.teleporthq.io/projects/lovable-solid-kangaroo-k4geji/preview/1185f2ef-f7e8-407a-94d9-43494d103635 "],
             "can you show me the departments you have?" : ["sure, i'd be happy to help, please visit: https://play.teleporthq.io/projects/lovable-solid-kangaroo-k4geji/preview/eb5467cb-33c9-445e-95d1-1539a3f364db"],
             "goodbye": ['Goodbye','Hope you get well soon','Bye']
             }

while True:
    user_text = input('You:  ')
    if user_text.lower() in responses:
        bot_reply = random.choice(responses[user_text.lower()])
        
        print("Bot Reply: ", bot_reply)
    else:
        print("Bot Reply: I don't unserstand, sorry") 