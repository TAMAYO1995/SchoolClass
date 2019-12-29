# -*- coding: utf-8 -*-
#201444087 신건호
#직업분포 및 직업별 셋트  , 상위랭킹(대균열 시즌별) (미팅 진행 후 방향)
#대균열 시즌별 직업분포, 랭커 시즌별 대균열 파라곤레벨  
#파라곤레벨 설명 https://www.ign.com/wikis/diablo-3/Paragon_Levels
#한국서버 기준

import pandas as pd
import json
import requests
import matplotlib.pyplot as plt
import matplotlib
import datetime
from matplotlib import font_manager #font_manager 하위 모듈 불러오기

#과제 진행 시 futurewarning이라는 경고에러가 콘솔창에 출력되어 없애버렸습니다. 
import warnings
warnings.filterwarnings(action='ignore') 

#한글
font_location="C:\\Windows\\Fonts\\malgun.ttf" #한글폰트가 저장된 로컬 위치 지정
font_name = font_manager.FontProperties(fname=font_location).get_name() #폰트 불러오기
matplotlib.rc('font', family=font_name) #한글 폰트 지정하기
#마이너스 숫자 폰트 깨짐 방지
matplotlib.rcParams['axes.unicode_minus'] = False


#season Leaderborad
#19시즌
season_19_url = 'your api' 
season_19 = requests.get(season_19_url) # get 형식으로 json 데이터 요청
season_19_data = json.loads(season_19.text) # json 데이터 (str)를 파이썬 딕셔너리형으로 변환

#print(season_19.status_code) # 상태 코드 

diablo_s_19 = pd.DataFrame()
diablo_s_19 = diablo_s_19.append(
    {"season":"","rank":"","heroClass":"","completedTime":"","paragonLevel":""
    },
    ignore_index= True)

print(diablo_s_19)

#for 문을 사용하여 데이터 추출
num = len(season_19_data["row"]) # row의 개수를 가져와 몇번 반복할지를 판단
#print(num) # 데이터의 길이 만큼 반복합니다.
for i in range(0,num):  
    try:
        diablo_s_19.ix[i,"season"] = "19"
        diablo_s_19.ix[i,"rank"] = season_19_data["row"][i]["data"][0]["number"]
        diablo_s_19.ix[i,"heroClass"] = season_19_data["row"][i]["player"][0]["data"][2]["string"]
        diablo_s_19.ix[i,"completedTime"] = datetime.datetime.fromtimestamp(season_19_data["row"][i]["data"][2]["timestamp"]/1000)
        diablo_s_19.ix[i,"paragonLevel"] = season_19_data["row"][i]["player"][0]["data"][5]["number"]
    except KeyError: #timestamp에 keyError 오류가 발생하여 예외처리를 했습니다.
        season_19_data["row"][i]["data"][2]["timestamp"] = "NULL"   

diablo_s_19 = diablo_s_19.fillna(0) #Nan 값 0으로 채우기  
print(diablo_s_19)

#18시즌
season_18_url = 'your api' 
season_18 = requests.get(season_18_url) # get 형식으로 json 데이터 요청
season_18_data = json.loads(season_18.text) # json 데이터 (str)를 파이썬 딕셔너리형으로 변환


diablo_s_18 = pd.DataFrame()
diablo_s_18 = diablo_s_18.append(
    {"season":"","rank":"","heroClass":"","completedTime":"","paragonLevel":""
    },
    ignore_index= True)

#for 문을 사용하여 데이터 추출
num = len(season_18_data["row"]) # row의 개수를 가져와 몇번 반복할지를 판단
#print(num) # 데이터의 길이 만큼 반복합니다.
for i in range(0,num):
    try:
        diablo_s_18.ix[i,"season"] = "18"
        diablo_s_18.ix[i,"rank"] = season_18_data["row"][i]["data"][0]["number"]
        diablo_s_18.ix[i,"heroClass"] = season_18_data["row"][i]["player"][0]["data"][2]["string"]
        diablo_s_18.ix[i,"completedTime"] = datetime.datetime.fromtimestamp(season_18_data["row"][i]["data"][2]["timestamp"]/1000)
        diablo_s_18.ix[i,"paragonLevel"] = season_18_data["row"][i]["player"][0]["data"][5]["number"]
    except KeyError: #timestamp에 keyError 오류가 발생하여 예외처리를 했습니다.
        season_18_data["row"][i]["data"][2]["timestamp"] = "NULL"   

diablo_s_18 = diablo_s_18.fillna(0)   
#print(diablo_s_18)

#17시즌
season_17_url = 'your api' 
season_17 = requests.get(season_17_url) # get 형식으로 json 데이터 요청
season_17_data = json.loads(season_17.text) # json 데이터 (str)를 파이썬 딕셔너리형으로 변환


diablo_s_17 = pd.DataFrame()
diablo_s_17 = diablo_s_17.append(
    {"season":"","rank":"","heroClass":"","completedTime":"","paragonLevel":""
    },
    ignore_index= True)

#for 문을 사용하여 데이터 추출
num = len(season_17_data["row"]) # row의 개수를 가져와 몇번 반복할지를 판단
#print(num) # 데이터의 길이 만큼 반복합니다.
for i in range(0,num):
    try:
        diablo_s_17.ix[i,"season"] = "17"
        diablo_s_17.ix[i,"rank"] = season_17_data["row"][i]["data"][0]["number"]
        diablo_s_17.ix[i,"heroClass"] = season_17_data["row"][i]["player"][0]["data"][2]["string"]
        diablo_s_17.ix[i,"completedTime"] = datetime.datetime.fromtimestamp(season_17_data["row"][i]["data"][2]["timestamp"]/1000)
        diablo_s_17.ix[i,"paragonLevel"] = season_17_data["row"][i]["player"][0]["data"][5]["number"]
    except KeyError: #timestamp에 keyError 오류가 발생하여 예외처리를 했습니다.
        season_17_data["row"][i]["data"][2]["timestamp"] = "NULL"  
         
diablo_s_17 = diablo_s_17.fillna(0)   
#print(diablo_s_17)

#16시즌
season_16_url = 'your api' 
season_16 = requests.get(season_16_url) # get 형식으로 json 데이터 요청
season_16_data = json.loads(season_16.text) # json 데이터 (str)를 파이썬 딕셔너리형으로 변환


diablo_s_16 = pd.DataFrame()
diablo_s_16 = diablo_s_16.append(
    {"season":"","rank":"","heroClass":"","completedTime":"","paragonLevel":""
    },
    ignore_index= True)

#for 문을 사용하여 데이터 추출
num = len(season_16_data["row"]) # row의 개수를 가져와 몇번 반복할지를 판단
#print(num) # 데이터의 길이 만큼 반복합니다.
for i in range(0,num):
    try:
        diablo_s_16.ix[i,"season"] = "16"
        diablo_s_16.ix[i,"rank"] = season_16_data["row"][i]["data"][0]["number"]
        diablo_s_16.ix[i,"heroClass"] = season_16_data["row"][i]["player"][0]["data"][2]["string"]
        diablo_s_16.ix[i,"completedTime"] = datetime.datetime.fromtimestamp(season_16_data["row"][i]["data"][2]["timestamp"]/1000)
        diablo_s_16.ix[i,"paragonLevel"] = season_16_data["row"][i]["player"][0]["data"][5]["number"]
    except KeyError: #timestamp에 keyError 오류가 발생하여 예외처리를 했습니다.
        season_16_data["row"][i]["data"][2]["timestamp"] = "NULL"   

diablo_s_16 = diablo_s_16.fillna(0)   
#print(diablo_s_16)

#15시즌
season_15_url = 'your api' 
season_15 = requests.get(season_15_url) # get 형식으로 json 데이터 요청
season_15_data = json.loads(season_15.text) # json 데이터 (str)를 파이썬 딕셔너리형으로 변환


diablo_s_15 = pd.DataFrame()
diablo_s_15 = diablo_s_15.append(
    {"season":"","rank":"","heroClass":"","completedTime":"","paragonLevel":""
    },
    ignore_index= True)

#for 문을 사용하여 데이터 추출
num = len(season_15_data["row"]) # row의 개수를 가져와 몇번 반복할지를 판단
#print(num) # 데이터의 길이 만큼 반복합니다.
for i in range(0,num):
    try:
        diablo_s_15.ix[i,"season"] = "15"
        diablo_s_15.ix[i,"rank"] = season_15_data["row"][i]["data"][0]["number"]
        diablo_s_15.ix[i,"heroClass"] = season_15_data["row"][i]["player"][0]["data"][2]["string"]
        diablo_s_15.ix[i,"completedTime"] = datetime.datetime.fromtimestamp(season_15_data["row"][i]["data"][2]["timestamp"]/1000)
        diablo_s_15.ix[i,"paragonLevel"] = season_15_data["row"][i]["player"][0]["data"][5]["number"]
    except KeyError: #timestamp에 keyError 오류가 발생하여 예외처리를 했습니다.
        season_15_data["row"][i]["data"][2]["timestamp"] = "NULL"   

diablo_s_15 = diablo_s_15.fillna(0)   
#print(diablo_s_15)

#14시즌
season_14_url = 'your api' 
season_14 = requests.get(season_14_url) # get 형식으로 json 데이터 요청
season_14_data = json.loads(season_14.text) # json 데이터 (str)를 파이썬 딕셔너리형으로 변환


diablo_s_14 = pd.DataFrame()
diablo_s_14 = diablo_s_14.append(
    {"season":"","rank":"","heroClass":"","completedTime":"","paragonLevel":""
    },
    ignore_index= True)

#for 문을 사용하여 데이터 추출
num = len(season_14_data["row"]) # row의 개수를 가져와 몇번 반복할지를 판단
#print(num) # 데이터의 길이 만큼 반복합니다.
for i in range(0,num):
    try:
        diablo_s_14.ix[i,"season"] = "14"
        diablo_s_14.ix[i,"rank"] = season_14_data["row"][i]["data"][0]["number"]
        diablo_s_14.ix[i,"heroClass"] = season_14_data["row"][i]["player"][0]["data"][2]["string"]
        diablo_s_14.ix[i,"completedTime"] = datetime.datetime.fromtimestamp(season_14_data["row"][i]["data"][2]["timestamp"]/1000)
        diablo_s_14.ix[i,"paragonLevel"] = season_14_data["row"][i]["player"][0]["data"][5]["number"]
    except KeyError: #timestamp에 keyError 오류가 발생하여 예외처리를 했습니다.
        season_14_data["row"][i]["data"][2]["timestamp"] = "NULL"   

diablo_s_14 = diablo_s_14.fillna(0)   
#print(diablo_s_14)



#대균열 시즌별 직업분포도

#19시즌 데이터 추출하기
wizard19_num = len(diablo_s_19[diablo_s_19.heroClass == 'wizard']) #마법사
demonHunter19_num = len(diablo_s_19[diablo_s_19.heroClass == 'demon hunter']) # 악사
monk19_num = len(diablo_s_19[diablo_s_19.heroClass == 'monk']) #수도사
crusader19_num = len(diablo_s_19[diablo_s_19.heroClass == 'crusader']) #성기사
necromancer19_num = len(diablo_s_19[diablo_s_19.heroClass == 'necromancer']) #강령술사
witchDoctor19_num = len(diablo_s_19[diablo_s_19.heroClass == 'witch doctor']) #부두술사
barbarian19_num = len(diablo_s_19[diablo_s_19.heroClass == 'barbarian']) #야만용사

#18시즌 데이터 추출하기
wizard18_num = len(diablo_s_18[diablo_s_18.heroClass == 'wizard']) #마법사
demonHunter18_num = len(diablo_s_18[diablo_s_18.heroClass == 'demon hunter']) # 악사
monk18_num = len(diablo_s_18[diablo_s_18.heroClass == 'monk']) #수도사
crusader18_num = len(diablo_s_18[diablo_s_18.heroClass == 'crusader']) #성기사
necromancer18_num = len(diablo_s_18[diablo_s_18.heroClass == 'necromancer']) #강령술사
witchDoctor18_num = len(diablo_s_18[diablo_s_18.heroClass == 'witch doctor']) #부두술사
barbarian18_num = len(diablo_s_18[diablo_s_18.heroClass == 'barbarian']) #야만용사

#17시즌 데이터 추출하기
wizard17_num = len(diablo_s_17[diablo_s_17.heroClass == 'wizard']) #마법사
demonHunter17_num = len(diablo_s_17[diablo_s_17.heroClass == 'demon hunter']) # 악사
monk17_num = len(diablo_s_17[diablo_s_17.heroClass == 'monk']) #수도사
crusader17_num = len(diablo_s_17[diablo_s_17.heroClass == 'crusader']) #성기사
necromancer17_num = len(diablo_s_17[diablo_s_17.heroClass == 'necromancer']) #강령술사
witchDoctor17_num = len(diablo_s_17[diablo_s_17.heroClass == 'witch doctor']) #부두술사
barbarian17_num = len(diablo_s_17[diablo_s_17.heroClass == 'barbarian']) #야만용사

#16시즌 데이터 추출하기
wizard16_num = len(diablo_s_16[diablo_s_16.heroClass == 'wizard']) #마법사
demonHunter16_num = len(diablo_s_16[diablo_s_16.heroClass == 'demon hunter']) # 악사
monk16_num = len(diablo_s_16[diablo_s_16.heroClass == 'monk']) #수도사
crusader16_num = len(diablo_s_16[diablo_s_16.heroClass == 'crusader']) #성기사
necromancer16_num = len(diablo_s_16[diablo_s_16.heroClass == 'necromancer']) #강령술사
witchDoctor16_num = len(diablo_s_16[diablo_s_16.heroClass == 'witch doctor']) #부두술사
barbarian16_num = len(diablo_s_16[diablo_s_16.heroClass == 'barbarian']) #야만용사

#15시즌 데이터 추출하기
wizard15_num = len(diablo_s_15[diablo_s_15.heroClass == 'wizard']) #마법사
demonHunter15_num = len(diablo_s_15[diablo_s_15.heroClass == 'demon hunter']) # 악사
monk15_num = len(diablo_s_15[diablo_s_15.heroClass == 'monk']) #수도사
crusader15_num = len(diablo_s_15[diablo_s_15.heroClass == 'crusader']) #성기사
necromancer15_num = len(diablo_s_15[diablo_s_15.heroClass == 'necromancer']) #강령술사
witchDoctor15_num = len(diablo_s_15[diablo_s_15.heroClass == 'witch doctor']) #부두술사
barbarian15_num = len(diablo_s_15[diablo_s_15.heroClass == 'barbarian']) #야만용사

#14시즌 데이터 추출하기
wizard14_num = len(diablo_s_14[diablo_s_14.heroClass == 'wizard']) #마법사
demonHunter14_num = len(diablo_s_14[diablo_s_14.heroClass == 'demon hunter']) # 악사
monk14_num = len(diablo_s_14[diablo_s_14.heroClass == 'monk']) #수도사
crusader14_num = len(diablo_s_14[diablo_s_14.heroClass == 'crusader']) #성기사
necromancer14_num = len(diablo_s_14[diablo_s_14.heroClass == 'necromancer']) #강령술사
witchDoctor14_num = len(diablo_s_14[diablo_s_14.heroClass == 'witch doctor']) #부두술사
barbarian14_num = len(diablo_s_14[diablo_s_14.heroClass == 'barbarian']) #야만용사

x = ["마법사","악마사냥꾼","수도사","성기사","강령술사","부두술사","야만용사"]
y19 = [wizard19_num , demonHunter19_num , monk19_num , crusader19_num , necromancer19_num , witchDoctor19_num , barbarian19_num]
y18 = [wizard18_num , demonHunter18_num , monk18_num , crusader18_num , necromancer18_num , witchDoctor18_num , barbarian18_num]
y17 = [wizard17_num , demonHunter17_num , monk17_num , crusader17_num , necromancer17_num , witchDoctor17_num , barbarian17_num]
y16 = [wizard16_num , demonHunter16_num , monk16_num , crusader16_num , necromancer16_num , witchDoctor16_num , barbarian16_num]
y15 = [wizard15_num , demonHunter15_num , monk15_num , crusader15_num , necromancer15_num , witchDoctor15_num , barbarian15_num]
y14 = [wizard14_num , demonHunter14_num , monk14_num , crusader14_num , necromancer14_num , witchDoctor14_num , barbarian14_num]

plt.figure(1)
plt.plot(x,y19,'blue', label="19시즌 대균열")
plt.plot(x,y18,'red', label="18시즌 대균열")
plt.plot(x,y17,'black', label="17시즌 대균열")
plt.plot(x,y16,'purple', label="16시즌 대균열")
plt.plot(x,y15,'orange', label="15시즌 대균열")
plt.plot(x,y14,'green', label="14시즌 대균열")
plt.title("대균열 시즌별 직업분포도")
plt.grid(True) #grid(T/F) 로 격자 출력 여부 결정
plt.xlabel("직업")
plt.ylabel("유저 수")
plt.legend(loc="upper right")



#파라곤 레벨에 따른 등수

x = ["1등","2등","3등","4등","5등","6등","7등","8등","9등","10등"]

#19시즌 상위랭킹 파라곤레벨 리스트로 반환 후 인덱싱, 차례대로 1등부터 10등까지 
paragonLevel_s_19 = diablo_s_19.paragonLevel.tolist()
para19 = paragonLevel_s_19[0:10]

#18시즌  상위랭킹 파라곤레벨 리스트로 반환 후 인덱싱, 차례대로 1등부터 10등까지 
paragonLevel_s_18 = diablo_s_18.paragonLevel.tolist()
para18 = paragonLevel_s_18[0:10]

#17시즌 상위랭킹 파라곤레벨 리스트로 반환 후 인덱싱, 차례대로 1등부터 10등까지 
paragonLevel_s_17 = diablo_s_17.paragonLevel.tolist()
para17 = paragonLevel_s_17[0:10]

#16시즌  상위랭킹 파라곤레벨 리스트로 반환 후 인덱싱, 차례대로 1등부터 10등까지 
paragonLevel_s_16 = diablo_s_16.paragonLevel.tolist()
para16 = paragonLevel_s_16[0:10]

#15시즌  상위랭킹 파라곤레벨 리스트로 반환 후 인덱싱, 차례대로 1등부터 10등까지 
paragonLevel_s_15 = diablo_s_15.paragonLevel.tolist()
para15 = paragonLevel_s_15[0:10]

#14시즌  상위랭킹 파라곤레벨 리스트로 반환 후 인덱싱, 차례대로 1등부터 10등까지 
paragonLevel_s_14 = diablo_s_14.paragonLevel.tolist()
para14 = paragonLevel_s_14[0:10]

# 3 X 2 행렬로 이뤄진 하위 그래프
plt.figure(2)
plt.subplot(3,2,1)
plt.plot(x,para19)
plt.title("19시즌 등수")
plt.ylabel("파라곤레벨")
plt.ylim(100,1000)
plt.grid(True) #grid(T/F) 로 격자 출력 여부 결정

plt.subplot(3,2,2)
plt.plot(x,para18)
plt.title("18시즌 등수")
plt.ylabel("파라곤레벨")
plt.ylim(100,1000)
plt.grid(True) #grid(T/F) 로 격자 출력 여부 결정

plt.subplot(3,2,3)
plt.plot(x,para17)
plt.title("17시즌 등수")
plt.ylabel("파라곤레벨")
plt.ylim(100,1000)
plt.grid(True) #grid(T/F) 로 격자 출력 여부 결정

plt.subplot(3,2,4)
plt.plot(x,para16)
plt.title("16시즌 등수")
plt.ylabel("파라곤레벨")
plt.ylim(100,1000)
plt.grid(True) #grid(T/F) 로 격자 출력 여부 결정

plt.subplot(3,2,5)
plt.plot(x,para15)
plt.title("15시즌 등수")
plt.ylabel("파라곤레벨")
plt.ylim(100,1000)
plt.grid(True) #grid(T/F) 로 격자 출력 여부 결정

plt.subplot(3,2,6)
plt.plot(x,para14)
plt.title("14시즌 등수")
plt.ylabel("파라곤레벨")
plt.ylim(100,1000)
plt.grid(True) #grid(T/F) 로 격자 출력 여부 결정

plt.show()


