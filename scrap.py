from bs4 import BeautifulSoup
import requests
import pdb
import pandas as pd
  
while True:
  Input=input('\n**********Type "exit" for Terminate programme ************ \n\nEnter the URL  :')
  # r=requests.get('https://gitlab.com/users/sign_in').text
  # r=requests.get('https://coreyms.com').text
  # r=requests.get('https://stackoverflow.com/questions/24962673/beautiful-soup-getting-tag-id')

  if 'exit' in Input.lower():
    print('Terminated Successfully')
    break
  try:
    r=requests.get(Input)
  except Exception as e:
    print('\n!!Opps check the given URL',e)
    continue
  if r.status_code==200:
    pass
  else:
    print("\nError while trying the given url",r.status_code)
    continue
  soup=BeautifulSoup(r.text,'lxml')
  # print(soup.prettify())
  forms_resultset=soup.find_all('form')
  if len(forms_resultset)==0:
    print('\nGiven HTML url does not has form inside.\nTry entering another url')
    continue
  else:
    # print(forms_resultset)
    name=[]
    type_=[]
    for i in forms_resultset:
      lable=i.find_all('label')
      inputs=i.find_all('input')
      buttons=i.find_all('button')
    # print(lable,inputs)
    # pdb.set_trace()
      c=0
      
      for i in lable:

        for j in inputs:
      #     print("came",i['for'],type(j.name),j)
          if j.get('id',False) and i['for']==j['id']:
            # print(i.text,j['type'])
            name.append(i.text)
            type_.append(j['type'])
          elif j.get('type',False) and j['type']=='submit':
            #for making it to effect to only one iteration
            if c==1:
              pass
            else:
              # print("came for button in Form")
              name.append(j['value'])
              type_.append('submit')

        c=1
      for i in buttons:
        if i.get('type',False):
          if i['type']=='submit':
            if i.get('value',False):
              name.append(i['value'])
            else:
              name.append(i.text)
            type_.append('submit')
  # print(name,type_)
  
  temp_data={'Name':name,'Type':type_}
  already_exist=False
  temp_ob=pd.DataFrame(temp_data)
  skip=False
  print('\n\n',temp_ob)
  try:
    temp_in=input('\n\n---------------Found above immediate DataFrame from given URL-----------------------\nDo you want to append? :(y/n default y)')
  except Exception as e:
    print('error happend in input taking default as yes')
  if temp_in.lower()=='n':
    skip=True
  if not skip:  
    try:
      ob=pd.read_csv('Entity.csv',index_col=0)
      already_exist=True
      # print('Came because file exists')
    except FileNotFoundError as e:
      # print("came in Error",e)
      ob=temp_ob
    # data={'Name':[1,2,3,4,6,7,8],'Type':[1,3,44,5,6,7,8]}
    if already_exist:
      # print('came to append ',temp_data)
      # print('ob before',ob)
      
    
      ob=ob.append(temp_ob,ignore_index=True)
      # print('ob after',ob)
    # ob=pd.DataFrame(data)
    # print(ob)
    ob.to_csv('Entity.csv')
    print('\n Hurray!!! Added Data to file Successfully')