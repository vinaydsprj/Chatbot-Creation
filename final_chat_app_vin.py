import json 
import numpy as np
from tensorflow import keras
from sklearn.preprocessing import LabelEncoder
from time import sleep
import colorama
import random
colorama.init()
from colorama import Fore, Style, Back

import random
import pickle
from final_api import delay_prediction_fun

with open("intents.json") as file:
    data = json.load(file)


def chat():
    # load trained model
    model = keras.models.load_model('chat_model.h5')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20
    
    while True:
        print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        inp = input()
       # print("the input entered by the user is",inp)
        if inp.lower() == "quit":
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                             truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

       # print("the predicted tag is",tag[0])

        for i in data['intents']:

            if tag[0]=='delay':


                    if i['tag'] == tag:
                       # original_input=inp
                       # print(original_input.split(','))
                      #  bw=original_input.split(',')
                        dtr=[]
                      #  for tt in bw:
                            # print(tt.split(':'))
                           #  print(tt.split(':')[1])
                       #      tgt=tt.split(':')[1]
                       #      dtr.append(tgt)
                       # print(dtr) 
                        # dtr=[]
                        val1 = input("Enter start station name: ")
                        #print(val)
                        val2 = input("Enter destination station name: ")
                        #print(val)
                        val3 = input("Enter train number: ")
                        #print(val)
                        val4 = input("Enter day: ")
                        #print(val)
                        dtr.append(val1)
                        dtr.append(val2)
                        dtr.append(val3)
                        dtr.append(val4)
                        dtr[0]=dtr[0].upper()
                        dtr[1]=dtr[1].upper()
                        # driver.get("https://www.thetrainline.com/train-companies")
                        #dtr[3]=dtr[3].upper()
                        dtr[3]=dtr[3].capitalize()
                       # print(dtr)
                        delay_rst=delay_prediction_fun(dtr[0],dtr[1],dtr[2],dtr[3])
                       # print("the predicted delay is ",delay_rst)
                        delay_rst = "{:.2f}".format(delay_rst)
                        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, "The dealay will be " ,delay_rst, "Minutes ")

            elif tag[0]=='ticketprice':
                        


                   if i['tag'] == tag:
    #                    original_input=inp
                       # print(original_input.split(','))
    #                    bw=original_input.split(',')
    #                    dtr=[]
    #                    for tt in bw:
                            # print(tt.split(':'))
                           #  print(tt.split(':')[1])
    #                         tgt=tt.split(':')[1]
    #                         dtr.append(tgt)
                        dtr=[]
                        val1 = input("Enter start station name: ")
                        #print(val)
                        val2 = input("Enter destination station name: ")
                        #print(val)
                        dtr.append(val1)
                        dtr.append(val2)

                        dtr[0]=dtr[0].capitalize()
                        dtr[1]=dtr[1].capitalize()
                        from lowest_price_main import train_min_prices

                        sleep(5)

                        delay_rst, v_link =train_min_prices(dtr[0],dtr[1])
                        # print("the predicted delay is ",delay_rst)
                        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL ,"Economical ticket found is worth GBP  ",delay_rst ,". Use this link to book the ticket: " , v_link )
                        #train_min_prices
                       # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL ,"Use this link to book the ticket: ", v_link)
            else:
          #  print(tag)

                    if i['tag'] == tag:
                        print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL , np.random.choice(i['responses']))

        #print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
chat()
