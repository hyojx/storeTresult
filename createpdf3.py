from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from dataclass import Agesensor,SkinState
from PIL import Image
from pdf2image import convert_from_path
from dataclasses import fields
from reportlab.lib.colors import Color
import random
from reportlab.lib.pagesizes import letter
from datetime import date # 모듈추가


filepath="static/image/skin/"
resultfilepath="static/result/"
#mainfontname='AppleGothic'
mainfont='NanumGothic'
boldfont='NanumGothicBold'
Eboldfont='NanumGothicExtraBold'
lightfont='NanumGothicLight'

pink1=Color(243/255,181/255,168/255)
pink2=Color(248/255,215/255,208/255)
orange1=Color(244/255,180/255,93/255)
orange2=Color(250/255,220/255,180/255)
green1=Color(152/255,191/255,73/255) #07.09 7시 수정
green2=Color(229/255,239/255,209/255)

# 폰트 등록 함수
def register_fonts():
    # macOS의 산돌고딕 네오 폰트 경로
    #font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
    #pdfmetrics.registerFont(TTFont(mainfontname, font_path))
    font_path="static/fonts/"
    pdfmetrics.registerFont(TTFont(mainfont,font_path+"NanumGothic.ttf"))
    pdfmetrics.registerFont(TTFont(boldfont,font_path+"NanumGothicBold.ttf"))
    pdfmetrics.registerFont(TTFont(Eboldfont,font_path+"NanumGothicExtraBold.ttf"))
    pdfmetrics.registerFont(TTFont(lightfont,font_path+"NanumGothicLight.ttf"))

# 문자열 중앙배치 함수
def draw_centered_string(c, text, y, font_name, font_size, page_width):
    c.setFont(font_name, font_size)
    text_width = pdfmetrics.stringWidth(text, font_name, font_size)
    x = (page_width - text_width) / 2
    c.drawString(x, y, text)

# 문자열 공간중앙배치 함수
def draw_centered_string_in(c, text, startp,y, font_name, font_size, width):
    c.setFont(font_name, font_size)
    text_width = pdfmetrics.stringWidth(text, font_name, font_size)
    x = ((width - text_width) / 2)+startp
    c.drawString(x, y, text)    

# 피부 유형결정
def set_skin_category(SkinState):
    skincat=""
    # 피부타입
    if SkinState.Type=="지성":
        skincat+="O"
    elif SkinState.Type=="복합성":
        skincat+="C" 
    elif SkinState.Type=="건성":
        skincat+="D"
    else:
        skincat+="_"  
    # 민감도
    if SkinState.TState=="깨끗함" or SkinState.TState=="거의 깨끗함" or SkinState.TState=="보통":
        skincat+="R"
    elif SkinState.TState=="나쁨" or SkinState.TState=="매우 나쁨":
        skincat+="S"
    else:
        skincat+="_"    
    # 색소
    if SkinState.CState=="깨끗함" or SkinState.CState=="거의 깨끗함" or SkinState.CState=="보통":
        skincat+="N"
    elif SkinState.CState=="나쁨" or SkinState.CState=="매우 나쁨":
        skincat+="P"
    else:
        skincat+="_"  
    # 주름
    if SkinState.WState=="깨끗함" or SkinState.WState=="거의 깨끗함" or SkinState.WState=="보통":
        skincat+="T"
    elif SkinState.WState=="나쁨" or SkinState.WState=="매우 나쁨":
        skincat+="W"
    else:
        skincat+="_"    
    # 모공
    if SkinState.HState=="깨끗함" or SkinState.HState=="거의 깨끗함" or SkinState.HState=="보통":
        skincat+="S"
    elif SkinState.HState=="나쁨" or SkinState.HState=="매우 나쁨":
        skincat+="L"
    else:
        skincat+="_"      
              
    return skincat

# 피부 코멘트 작성
def skin_comment(c,skin_cat,height):
    if skin_cat[0]=="C":
        y=height-185
        btw=25
    else :
        y=height-195
        btw=28  

    c.setFillColorRGB(1,1,1)
    draw_centered_string_in(c,skin_cat,20,height-155,boldfont,30,170)
    count=1

    if skin_cat[0]=="O":
        draw_centered_string_in(c,"# 주기적인 피지케어",20,y,boldfont,15,170)
    elif skin_cat[0]=="C":
        draw_centered_string_in(c,"# 복합성(Combination)",20,y,boldfont,15,170)
        draw_centered_string_in(c,"# 피지 & 보습관리",20,y-(btw),boldfont,15,170)
        count+=1
    elif skin_cat[0]=="D":
        draw_centered_string_in(c,"# 보습관리",20,y,boldfont,15,170)   

    if skin_cat[1]=="R":
        draw_centered_string_in(c,"# 튼튼한 피부장벽",20,y-(btw*count),boldfont,15,170)  
        count+=1
    elif skin_cat[1]=="S":
        draw_centered_string_in(c,"# 저자극 피부관리",20,y-(btw*count),boldfont,15,170)
        count+=1

    if skin_cat[2]=="N":
        draw_centered_string_in(c,"# 맑고 환한 피부",20,y-(btw*count),boldfont,15,170)  
        count+=1
    elif skin_cat[2]=="P":
        draw_centered_string_in(c,"# 햇빛 차단 필수",20,y-(btw*count),boldfont,15,170)    
        count+=1

    if skin_cat[3]=="T":
        draw_centered_string_in(c,"# 탱탱한 피부",20,y-(btw*count),boldfont,15,170)  
        count+=1
    elif skin_cat[3]=="W":
        draw_centered_string_in(c,"# 주름 관리 필요",20,y-(btw*count),boldfont,15,170)     
        count+=1

    if skin_cat[4]=="S":
        draw_centered_string_in(c,"# 작고 깨끗한 모공",20,y-(btw*count),boldfont,15,170)  
        count+=1
    elif skin_cat[4]=="L":
        draw_centered_string_in(c,"# 모공 타이트닝 필요",20,y-(btw*count),boldfont,15,170)      
        count+=1


    return

# 피부 알파벳 작성(리스트 위치를 명시하는걸로 바꾸고 _도 확인하기)
def skin_alpha(c,skin_cat,height):
    print(skin_cat)
    if "O" in skin_cat:
        c.setFont(mainfont,30)
        c.setFillColor(pink1)
        c.drawString(233,height-210,"O")

        if skin_cat[1]=="R":
            c.drawString(305,height-210,"R")
        elif skin_cat[1]=="S":
            c.drawString(305,height-285,"S")
        
        if skin_cat[2]=="N":
            c.drawString(375,height-210,"N")
        elif skin_cat[2]=="P":
            c.drawString(376,height-285,"P")

        if skin_cat[3]=="T":
            c.drawString(446,height-210,"T")
        elif skin_cat[3]=="W":
            c.drawString(442,height-285,"W")  

        if skin_cat[4]=="S":
            c.drawString(518,height-210,"S")
        elif skin_cat[4]=="L":
            c.drawString(520,height-285,"L")          

        c.setFillColorRGB(1,1,1)
        c.drawString(234,height-285,"D")

        if skin_cat[1]=="S":
            c.drawString(305,height-210,"R")
        elif skin_cat[1]=="R":
            c.drawString(305,height-285,"S")
        elif skin_cat[1]=="_":
            c.drawString(305,height-210,"R")
            c.drawString(305,height-285,"S")
        
        if skin_cat[2]=="P":
            c.drawString(375,height-210,"N")
        elif skin_cat[2]=="N":
            c.drawString(376,height-285,"P")
        elif skin_cat[2]=="_":
            c.drawString(375,height-210,"N")
            c.drawString(376,height-285,"P")

        if skin_cat[3]=="W":
            c.drawString(446,height-210,"T")
        elif skin_cat[3]=="T":
            c.drawString(442,height-285,"W")  
        elif skin_cat[3]=="_":
            c.drawString(446,height-210,"T") 
            c.drawString(442,height-285,"W")   

        if skin_cat[4]=="L":
            c.drawString(518,height-210,"S")
        elif skin_cat[4]=="S":
            c.drawString(520,height-285,"L")
        elif skin_cat[4]=="_":
            c.drawString(518,height-210,"S") 
            c.drawString(520,height-285,"L")       

    elif "D" in skin_cat:
        c.setFont(mainfont,30)
        c.setFillColorRGB(1,1,1)
        c.drawString(233,height-210,"O")

        if skin_cat[1]=="S":
            c.drawString(305,height-210,"R")
        elif skin_cat[1]=="R":
            c.drawString(305,height-285,"S")
        elif skin_cat[1]=="_":
            c.drawString(305,height-210,"R")
            c.drawString(305,height-285,"S")
        
        if skin_cat[2]=="P":
            c.drawString(375,height-210,"N")
        elif skin_cat[2]=="N":
            c.drawString(376,height-285,"P")
        elif skin_cat[2]=="_":
            c.drawString(375,height-210,"N")
            c.drawString(376,height-285,"P")

        if skin_cat[3]=="W":
            c.drawString(446,height-210,"T")
        elif skin_cat[3]=="T":
            c.drawString(442,height-285,"W")  
        elif skin_cat[3]=="_":
            c.drawString(446,height-210,"T") 
            c.drawString(442,height-285,"W")   

        if skin_cat[4]=="L":
            c.drawString(518,height-210,"S")
        elif skin_cat[4]=="S":
            c.drawString(520,height-285,"L")
        elif skin_cat[4]=="_":
            c.drawString(518,height-210,"S") 
            c.drawString(520,height-285,"L") 

        c.setFillColor(green1)
        c.drawString(234,height-285,"D")   
        
        if skin_cat[1]=="R":
            c.drawString(305,height-210,"R")
        elif skin_cat[1]=="S":
            c.drawString(305,height-285,"S")
        
        if skin_cat[2]=="N":
            c.drawString(375,height-210,"N")
        elif skin_cat[2]=="P":
            c.drawString(376,height-285,"P")

        if skin_cat[3]=="T":
            c.drawString(446,height-210,"T")
        elif skin_cat[3]=="W":
            c.drawString(442,height-285,"W")  

        if skin_cat[4]=="S":
            c.drawString(518,height-210,"S")
        elif skin_cat[4]=="L":
            c.drawString(520,height-285,"L")  

    elif "C" in skin_cat:
        c.setFont(mainfont,30)
        c.setFillColor(orange1)
        c.drawString(233,height-210,"O")
        c.drawString(234,height-285,"D")

        if skin_cat[1]=="R":
            c.drawString(305,height-210,"R")
        elif skin_cat[1]=="S":
            c.drawString(305,height-285,"S")
        
        if skin_cat[2]=="N":
            c.drawString(375,height-210,"N")
        elif skin_cat[2]=="P":
            c.drawString(376,height-285,"P")

        if skin_cat[3]=="T":
            c.drawString(446,height-210,"T")
        elif skin_cat[3]=="W":
            c.drawString(442,height-285,"W")  

        if skin_cat[4]=="S":
            c.drawString(518,height-210,"S")
        elif skin_cat[4]=="L":
            c.drawString(520,height-285,"L") 

        c.setFillColorRGB(1,1,1)

        if skin_cat[1]=="S":
            c.drawString(305,height-210,"R")
        elif skin_cat[1]=="R":
            c.drawString(305,height-285,"S")
        elif skin_cat[1]=="_":
            c.drawString(305,height-210,"R")
            c.drawString(305,height-285,"S")
        
        if skin_cat[2]=="P":
            c.drawString(375,height-210,"N")
        elif skin_cat[2]=="N":
            c.drawString(376,height-285,"P")
        elif skin_cat[2]=="_":
            c.drawString(375,height-210,"N")
            c.drawString(376,height-285,"P")

        if skin_cat[3]=="W":
            c.drawString(446,height-210,"T")
        elif skin_cat[3]=="T":
            c.drawString(442,height-285,"W")  
        elif skin_cat[3]=="_":
            c.drawString(446,height-210,"T") 
            c.drawString(442,height-285,"W")   

        if skin_cat[4]=="L":
            c.drawString(518,height-210,"S")
        elif skin_cat[4]=="S":
            c.drawString(520,height-285,"L")
        elif skin_cat[4]=="_":
            c.drawString(518,height-210,"S") 
            c.drawString(520,height-285,"L")

    return

# 피부 고민 표시
def skin_concern(c,SkinState,height):
    if "유/수분 밸런스" in SkinState.Concern:
        c.drawImage(filepath+'PStar.png',218,height-233,10,10,mask='auto')
    if "민감성(여드름)" in SkinState.Concern:
        c.drawImage(filepath+'PStar.png',289,height-233,10,10,mask='auto')
    if "잡티" in SkinState.Concern:
        c.drawImage(filepath+'PStar.png',354,height-233,10,10,mask='auto')
    if "주름" in SkinState.Concern:
        c.drawImage(filepath+'PStar.png',423,height-233,10,10,mask='auto')
    if "모공크기" in SkinState.Concern:
        c.drawImage(filepath+'PStar.png',502,height-233,10,10,mask='auto')
    return

# T/U 좌표지정 
def set_grid(SkinState,height):
    grid={'Tx':0,'Ty':0,'Ux':0,'Uy':0,'smaller':False}
    if SkinState.TZWater=="Dehydrated":
        grid['Tx']=145
    elif SkinState.TZWater=="Normal":
        grid['Tx']=189 
    elif SkinState.TZWater=="Moisture":
        grid['Tx']=233 

    if SkinState.UZWater=="Dehydrated":
        grid['Ux']=145
    elif SkinState.UZWater=="Normal":
        grid['Ux']=189 
    elif SkinState.UZWater=="Moisture":
        grid['Ux']=233   

    if SkinState.TZOil=="Low":
        grid['Ty']=height-508
    elif SkinState.TZOil=="Sebum":
        grid['Ty']=height-468
    elif SkinState.TZOil=="High":
        grid['Ty']=height-428

    if SkinState.UZOil=="Low":
        grid['Uy']=height-508
    elif SkinState.UZOil=="Sebum":
        grid['Uy']=height-468
    elif SkinState.UZOil=="High":
        grid['Uy']=height-428   

    if grid["Tx"]==grid['Ux'] and grid["Ty"]==grid["Uy"]:
        grid["Tx"]-=8
        grid["Ux"]+=8
        grid["smaller"]=True          

    return grid


# 점수 그래프 그리기
def draw_skin_graph(c,SkinState,height):

    baseX=315
    baseY=height-412

    # 기본 그래프 형태
    c.setFont(boldfont, 9)
    c.setFillColorRGB(0.3, 0.3, 0.3)
    c.drawString(baseX,height-405,'민감지수')
    c.drawString(baseX,height-450,'색소 침착 지수')
    c.drawString(baseX,height-495,'눈가 주름 지수')
    c.drawString(baseX,height-540,'모공 크기')

    c.setFont(mainfont, 7)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    if SkinState.TAScore<10:
        c.drawString(baseX+220,height-385,"Caution")
    else:    
        c.drawString(baseX+65,height-385,"Normal")
        c.drawString(baseX+220,height-385,"Caution")

    c.setFillColorRGB(234/255,236/255,239/255)
    c.setStrokeColorRGB(234/255,236/255,239/255)
    c.roundRect(baseX+70,baseY,170,20,10,fill=True)
    c.roundRect(baseX+70,baseY-45,170,20,10,fill=True)
    c.roundRect(baseX+70,baseY-90,170,20,10,fill=True)
    c.roundRect(baseX+70,baseY-135,170,20,10,fill=True)

    # 값에 따른 색 및 길이
    if SkinState.TScore == SkinState.TAScore==0:
        pass
    elif SkinState.TAScore < SkinState.TScore:     #07.09 7시 수정
        c.setFillColorRGB(255/255,111/255,111/255)
        c.setStrokeColorRGB(255/255,111/255,111/255) 
    elif SkinState.TScore <= SkinState.TAScore:    #07.09 7시 수정
        c.setFillColorRGB(139/255,199/255,0)
        c.setStrokeColorRGB(139/255,199/255,0)

    if SkinState.TScore==0:
        pass
    elif SkinState.TScore<12:
        c.roundRect(baseX+70,baseY,20.4,20,10,fill=True)
    else:    
        c.roundRect(baseX+70,baseY,170*SkinState.TScore/100,20,10,fill=True)    



    if SkinState.CScore == SkinState.CAScore==0:
        pass
    elif SkinState.CAScore < SkinState.CScore:     #07.09 7시 수정
        c.setFillColorRGB(255/255,111/255,111/255)
        c.setStrokeColorRGB(255/255,111/255,111/255)
    elif SkinState.CScore <= SkinState.CAScore:    #07.09 7시 수정
        c.setFillColorRGB(139/255,199/255,0)
        c.setStrokeColorRGB(139/255,199/255,0)

    if SkinState.CScore==0:
        pass
    elif SkinState.CScore<12:
        c.roundRect(baseX+70,baseY-45,20.4,20,10,fill=True)
    else:    
        c.roundRect(baseX+70,baseY-45,170*SkinState.CScore/100,20,10,fill=True)    



    if SkinState.WScore == SkinState.WAScore==0:
        pass
    elif SkinState.WAScore < SkinState.WScore:      #07.09 7시 수정
        c.setFillColorRGB(255/255,111/255,111/255)
        c.setStrokeColorRGB(255/255,111/255,111/255)
    elif SkinState.WScore <= SkinState.WAScore:     #07.09 7시 수정
        c.setFillColorRGB(139/255,199/255,0)
        c.setStrokeColorRGB(139/255,199/255,0) 

    if SkinState.WScore==0:
        pass
    elif SkinState.WScore<12:
        c.roundRect(baseX+70,baseY-90,20.4,20,10,fill=True)
    else:    
        c.roundRect(baseX+70,baseY-90,170*SkinState.WScore/100,20,10,fill=True)      



    if SkinState.HScore == SkinState.HAScore==0:
        pass
    elif SkinState.HAScore < SkinState.HScore:     #07.09 7시 수정
        c.setFillColorRGB(255/255,111/255,111/255)
        c.setStrokeColorRGB(255/255,111/255,111/255)
    elif SkinState.HScore <= SkinState.HAScore:    #07.09 7시 수정
        c.setFillColorRGB(139/255,199/255,0)
        c.setStrokeColorRGB(139/255,199/255,0)

    if SkinState.HScore==0:
        pass
    elif SkinState.HScore<12:
        c.roundRect(baseX+70,baseY-135,20.4,20,10,fill=True)
    else:    
        c.roundRect(baseX+70,baseY-135,170*SkinState.HScore/100,20,10,fill=True)    



    c.setFont(mainfont,10)
    c.setFillColorRGB(1,1,1)
    if SkinState.TScore<=12:
        c.drawString(baseX+74,height-405,str(SkinState.TScore))
    else:        
        c.drawString(baseX+47+(170*SkinState.TScore/100),height-405,str(SkinState.TScore))

    if SkinState.CScore<=12:
        c.drawString(baseX+74,height-450,str(SkinState.CScore))
    else:
        c.drawString(baseX+47+(170*SkinState.CScore/100),height-450,str(SkinState.CScore))
    if SkinState.WScore<=12:
        c.drawString(baseX+74,height-495,str(SkinState.WScore))
    else:
        c.drawString(baseX+47+(170*SkinState.WScore/100),height-495,str(SkinState.WScore))
    if SkinState.HScore<=12:
        c.drawString(baseX+74,height-540,str(SkinState.HScore))
    else:
        c.drawString(baseX+47+(170*SkinState.HScore/100),height-540,str(SkinState.HScore))    
    # 로직 수정 07.15 오후------------------------------------------------------------------
    c.setFont(mainfont, 8)
    c.setFillColorRGB(0.7, 0.7, 0.7)
    if SkinState.TAScore==0:
        pass
    elif SkinState.TAScore<10:
        c.drawString(baseX+65+(170*SkinState.TAScore/100),baseY+22,"▼") 
        c.drawString(baseX+65+(170*SkinState.TAScore/100),baseY+30,str(SkinState.TAScore))
    else :
        c.drawString(baseX+65+(170*SkinState.TAScore/100),baseY+22,"▼")
        c.drawString(baseX+63+(170*SkinState.TAScore/100),baseY+30,str(SkinState.TAScore))

    if SkinState.CAScore==0:
        pass
    elif SkinState.CAScore<10:
        c.drawString(baseX+65+(170*SkinState.CAScore/100),baseY-23,"▼")
        c.drawString(baseX+65+(170*SkinState.CAScore/100),baseY-15,str(SkinState.CAScore))
    else :
        c.drawString(baseX+65+(170*SkinState.CAScore/100),baseY-23,"▼")
        c.drawString(baseX+63+(170*SkinState.CAScore/100),baseY-15,str(SkinState.CAScore))
    
    if SkinState.WAScore==0:
        pass
    elif SkinState.WAScore<10:
        c.drawString(baseX+65+(170*SkinState.WAScore/100),baseY-68,"▼")
        c.drawString(baseX+65+(170*SkinState.WAScore/100),baseY-60,str(SkinState.WAScore))
    else :
        c.drawString(baseX+65+(170*SkinState.WAScore/100),baseY-68,"▼")
        c.drawString(baseX+63+(170*SkinState.WAScore/100),baseY-60,str(SkinState.WAScore))

    if SkinState.HAScore==0:
        pass
    elif SkinState.HAScore<10:
        c.drawString(baseX+65+(170*SkinState.HAScore/100),baseY-113,"▼")
        c.drawString(baseX+65+(170*SkinState.HAScore/100),baseY-105,str(SkinState.HAScore))
    else :
        c.drawString(baseX+65+(170*SkinState.HAScore/100),baseY-113,"▼")
        c.drawString(baseX+63+(170*SkinState.HAScore/100),baseY-105,str(SkinState.HAScore))
     # 로직 수정 07.15 오후------------------------------------------------------------------

# 에이지 센서 패널
def draw_panel(c,Agesensor,height):
    
    baseX=38
    baseY=height-690
    if Agesensor.Rating =="A":
        c.drawImage(filepath+'A.png',baseX,baseY,130,69,mask='auto')
    elif Agesensor.Rating =="B":
        c.drawImage(filepath+'B.png',baseX,baseY,130,69,mask='auto')
    elif Agesensor.Rating =="C":
        c.drawImage(filepath+'C.png',baseX,baseY,130,69,mask='auto')    
    elif Agesensor.Rating =="D":
        c.drawImage(filepath+'D.png',baseX,baseY,130,69,mask='auto')    
    elif Agesensor.Rating =="E":
        c.drawImage(filepath+'E.png',baseX,baseY,130,69,mask='auto')    

    c.setFont(boldfont, 40)
    c.setFillColorRGB(1,208/255,20/255)
    rating=str(Agesensor.Rating)
    c.drawString(baseX+165+3,baseY+35,rating)

    c.setFont(boldfont, 15)
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawString(baseX+195+3,baseY+40,"등급")  

    c.setFont(boldfont, 12)
    rank=str(Agesensor.Rank)+"등 / 100명"
    c.drawString(baseX+155+3,baseY+10,rank)  

    c.setFont(mainfont, 8)
    c.setFillColorRGB(0.2,0.2,0.2)
    c.drawString(baseX-10,baseY+28,"2%")
    c.drawString(baseX+8,baseY+60,"14%")
    c.drawString(baseX+55,baseY+73,"34%")
    c.drawString(baseX+103,baseY+60,"43%")
    c.drawString(baseX+128,baseY+28,"7%")

    c.setStrokeColorRGB(0.75,0.75,0.75)
    c.setLineWidth(0.7)
    c.roundRect(baseX-5,baseY-70, 140, 65,10)
    c.roundRect(baseX+145,baseY-70, 95, 65,10)
    c.roundRect(baseX-5,baseY-132, 245, 55,10)

    # 소제목 스타일 지정
    c.setFont(boldfont, 10)
    c.setFillColorRGB(0.1,0.1,0.1)
    c.drawString(baseX+5,baseY-20,"AGEs(당독소)란?")
    c.drawString(baseX+155,baseY-20,"당독소 과다증")
    c.drawString(baseX+5,baseY-95,"피부에 미치는 영향")

    # 본문 스타일 지정
    c.setFont(mainfont, 8.5)
    c.setFillColorRGB(0.5,0.5,0.5)

    c.drawString(baseX+5,baseY-35-1,"포도당, 과당과 같은 당이 단백질")
    c.drawString(baseX+5,baseY-47-1,"또는 지방에 결합하여 당화된")
    c.drawString(baseX+5,baseY-59-1,"물질로 노화 시 증가")

    c.drawString(baseX+155,baseY-35-1,"노화,비만,당뇨,")
    c.drawString(baseX+155,baseY-47-1,"노안,간염")
    c.drawString(baseX+155,baseY-59-1,"뇌 기능 장애")

    c.drawString(baseX+5,baseY-110,"스프링과 같은 유연하고 부드러운 형태의 피부층이 AGEs와")
    c.drawString(baseX+5,baseY-122,"결합하면 딱딱하게 굳어져 탄성이 저하")

    return

def state_to_int(state):
    state_mapping = {
        "매우 나쁨": 1,
        "나쁨": 2,
        "보통": 3,
        "거의 깨끗함": 4,
        "깨끗함": 5,
        "":6
    }
    return state_mapping.get(state.lower(), 5)

# 순위 정하기
def set_rank(skin_state: SkinState):
    Glist=[]
    elements = {
        'C': (state_to_int(skin_state.CState), skin_state.CScore - skin_state.CAScore),
        'W': (state_to_int(skin_state.WState), skin_state.WScore - skin_state.WAScore),
        'T': (state_to_int(skin_state.TState), skin_state.TScore - skin_state.TAScore)
    }
    print(skin_state.CState+"/"+str(skin_state.CScore - skin_state.CAScore))
    print(skin_state.WState+"/"+str(skin_state.WScore - skin_state.WAScore))
    print(skin_state.TState+"/"+str(skin_state.TScore - skin_state.TAScore))
    sorted_elements = sorted(elements.items(), key=lambda x: (x[1][0], -x[1][1]))
    if skin_state.Type=="건성":   # 로직수정 07.15
        Glist.append("D")
        Glist.extend([sorted_elements[0][0],sorted_elements[1][0],sorted_elements[2][0]])   # 로직수정 07.15
    else :
        Slist=[skin_state.CState,skin_state.WState,skin_state.TState]
        num=Slist.count("")
        for i in range(0,3-num):
            Glist+=sorted_elements[i][0]
        Glist.append("D")
        for i in range(3-num,3):
            Glist+=sorted_elements[i][0]
    print(Glist)

    return Glist



def create_skin_pdf(Name,SkinState,Agesensor):
    filename=resultfilepath+'Skin_Report.pdf'
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    register_fonts()
    
    # 제목1 추가 (한글) - 페이지 가운데에 배치
    draw_centered_string(c, "Greating store healthcare", height - 40, mainfont, 12, width)
    draw_centered_string(c, "피부관리 프로그램 결과차트", height - 70, boldfont, 20, width) #07.09 5시 수정
    
    # 선 그리기 (x1, y1, x2, y2)
    c.setLineWidth(0.7)  # 라인의 굵기 설정
    c.setStrokeColorRGB(0.75, 0.75, 0.75)  # 라인의 색상 설정
    c.line(450, height - 100, 550, height - 100)
    c.line(33, height - 98, 97, height - 98)
    
    # 내담자명
    c.drawImage(filepath+'user.png',455,height-100,20,20,mask='auto')

    username= str(Name)+"님"
    c.setFont(boldfont, 13)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(485,height-95,username)
    c.setFont(boldfont, 11)
    c.drawString(35,height-95,str(date.today().strftime("%Y.%m.%d")))
    
    # 사각형 그리기 (x, y, width, height)
    c.roundRect(200,height-325,370, 210,15)
    c.roundRect(20,height-560, 270, 225,15)
    c.roundRect(300,height-560, 270, 225,15)
    c.roundRect(20,height-830, 270, 260,15)
    c.roundRect(300,height-830, 270, 260,15)  
    
    #-------------- part1 나의 피부유형 --------------
    # 본문 채우기 
    c.setFont(boldfont, 12)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(215,height-140,"나의 피부 유형")
    
    if SkinState.Type=="지성":
        c.setFillColor(pink1)
        c.roundRect(20,height-325, 170, 210,0,fill=True)
        c.drawImage(filepath+'Oback.png',210,height-325,350,175,mask='auto')
    elif SkinState.Type=="복합성":
        c.setFillColor(orange1)
        c.roundRect(20,height-325, 170, 210,0,fill=True)
        c.drawImage(filepath+'Cback.png',210,height-325,350,175,mask='auto')
    elif SkinState.Type=="건성":
        c.setFillColor(green1)
        c.roundRect(20,height-325, 170, 210,0,fill=True)    
        c.drawImage(filepath+'Dback.png',210,height-325,350,175,mask='auto')

    skin_cat=set_skin_category(SkinState)
    skin_comment(c,skin_cat,height)  
    skin_alpha(c,skin_cat,height)
    skin_concern(c,SkinState,height)

    #-------------- part2 나의 유수분 밸런스 --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont(boldfont, 12)
    c.drawString(35,height-360,"나의 유수분 밸런스")

    c.drawImage(filepath+'TUface.png',27,height-520,80,120,mask='auto')
    c.drawImage(filepath+'graph.png',105,height-540,180,160,mask='auto')
    
    # T/U 표시할 위치 및 크기 지정
    grid=set_grid(SkinState,height)
    if grid['smaller']==True:
        c.drawImage(filepath+'T.png',grid['Tx'],grid['Ty'],15,15,mask='auto')
        c.drawImage(filepath+'U.png',grid['Ux'],grid['Uy'],15,15,mask='auto')
    else :    
        c.drawImage(filepath+'T.png',grid['Tx'],grid['Ty'],20,20,mask='auto')
        c.drawImage(filepath+'U.png',grid["Ux"],grid["Uy"],20,20,mask='auto')

    #-------------- part3 피부 고민별 점수 --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont(boldfont, 12)
    c.drawString(315,height-360,"피부 고민별 점수")

    c.setFont(mainfont, 8)
    c.setFillColorRGB(0.7, 0.7, 0.7)
    c.drawString(445,height-360,"▼ 같은 성별/연령대의 평균 점수")

    draw_skin_graph(c,SkinState,height)

    #-------------- part4 Age sensor --------------    
    if Agesensor.Rating=="" or Agesensor.Rank==0:
        c.drawImage(filepath+'AGEsBlur2.png',25,height-820,270,237,mask='auto')
    else:    
        c.setFillColorRGB(0, 0, 0)
        c.setFont(boldfont, 12)
        c.drawString(35,height-595,"AGEs sensor")
        draw_panel(c,Agesensor,height)
    
    #-------------- part5 맞춤 성분 --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont(boldfont, 12)
    c.drawString(315,height-595,"맞춤성분")

    c.setFont(mainfont, 10)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(315,height-613,"나에게 필요한 피부 영양제 기능 순위")

    c.setFont(mainfont, 8)
    c.setFillColorRGB(0.7, 0.7, 0.7)
    c.drawString(485,height-592,"*영양/기능 정보 참고")

    # 순위 정하기 함수 써서 순위 리스트 반환받기
    Glist=set_rank(SkinState)
    setY=0
    for gradient in Glist:
        if gradient =="C":
            c. drawImage(filepath+'Cgra.png',308,height-670-setY,257,45,mask='auto')
            setY+=50
        elif gradient=="W":
            c. drawImage(filepath+'Wgra.png',308,height-670-setY,257,45,mask='auto')
            setY+=50
        elif gradient=="T":
            c. drawImage(filepath+'Tgra.png',308,height-670-setY,257,45,mask='auto')
            setY+=50
        elif gradient=="D":
            c. drawImage(filepath+'WOgra.png',308,height-670-setY,257,45,mask='auto')
            setY+=50

    c.drawImage(filepath+'1.png',318,height-655,17,30,mask='auto')
    c.drawImage(filepath+'2.png',318,height-705,17,30,mask='auto')  
    c.drawImage(filepath+'3.png',318,height-755,17,30,mask='auto')      

        
    
    #-------------- 페이지 저장 및 이미지 변환 --------------

    # 페이지 저장
    c.showPage()

    #---------------------------------------- 상품추천 페이지 제작 -------------------------------------------
    # 선 그리기 (x1, y1, x2, y2)
    c.setLineWidth(0.7)  # 라인의 굵기 설정
    c.setStrokeColorRGB(0.7, 0.7, 0.7)  # 라인의 색상 설정
    c.line(10, height - 40, 580, height - 40)
    c.line(10, height - 290, 580, height - 290)
    c.line(10, height - 560, 580, height - 560)
    
    c.setFont(boldfont, 18)
    c.setFillColorRGB(0,0,0)
    draw_centered_string(c,Name+"님 맞춤상품 솔루션",height-30,boldfont,18,width)
    c.drawString(25,height-65,"식재료")
    c.drawString(25,height-315,"샐러드")
    c.drawString(310,height-315,"영양제")
    c.drawString(25,height-590,"착즙 주스")
    c.drawString(310,height-590,"건강한 피부 식습관")

    c.setFont(mainfont, 12)
    c.setFillColorRGB(0.2,0.2,0.2)
    c.drawString(25,height-88,'"건강한 피부를 위한 맞춤 식재료"')
    c.drawString(25,height-339,'"내면까지 예뻐지는 이너뷰티 상품"')
    c.drawString(310,height-339,'"나의 피부고민을 해결해줄 영양제"')
    c.drawString(25,height-613,'"생기있는 나를 위한 뷰티 주스"')
    c.drawString(310,height-613,'"피부 건강에 좋지않은 음식 tip"')


    c.drawImage(filepath+'I'+random.choice(['7','8'])+'.png',30,height-280,158,175,mask='auto')
    c.drawImage(filepath+'I'+random.choice(['9','10'])+'.png',215,height-280,158,175,mask='auto')
    c.drawImage(filepath+'I'+random.choice(['11','12'])+'.png',400,height-280,158,175,mask='auto')

    c.setFillColorRGB(191/255,191/255,191/255)
    c.setStrokeColorRGB(191/255,191/255,191/255)
    c.roundRect(220,height-93,70,20,10,fill=True)
    c.roundRect(300,height-93,70,20,10,fill=True)
    c.roundRect(380,height-93,70,20,10,fill=True)

    c.setFillColorRGB(1,1,1)
    c.setFont(boldfont, 11)
    c.drawString(232,height-87,"#비타민C")
    c.drawString(312,height-87,"#비타민E")
    c.drawString(396.5,height-87,"#셀레늄")

    # 맞춤 상품 추천
    c.setStrokeColorRGB(0.6,0.6,0.6)
    c.setLineWidth(0.2)
    c.drawImage(filepath+"SS1.png",32,height-550,257,195,mask='auto')
    c.roundRect(22,height-550,270,195,10)    #07.09 7시 수정
    c.drawImage(filepath+"SF"+str(random.randint(1,5))+".png",310,height-535,270,167,mask='auto')

    # 주스 추천
    c.setStrokeColorRGB(0.6,0.6,0.6)
    c.setLineWidth(0.2)
    c.roundRect(22,height-830,270,200,10)
    c.drawImage(filepath+"SJ1.png",27,height-822,270,190,mask='auto') #위치,크기 수정 07.16 3시

    # 건기식 추천
    c.setStrokeColorRGB(0.6,0.6,0.6)
    c.setLineWidth(0.2)
    c.roundRect(310,height-830,270,200,10)
    c.drawImage(filepath+"SC1.png",316,height-820,260,180,mask='auto')

    # 2페이지 저장
    c.showPage()

    c.save()

    # PDF를 이미지로 변환
    images = convert_from_path(filename)
    # 첫 번째 페이지를 이미지로 저장
    img_path = resultfilepath+"Skin_Report.png"
    images[0].save(img_path, "PNG")

    return img_path 

if __name__=="__main__":
    SState=SkinState(Concern=["모공크기","잡티"],Type="건성",TZWater="Normal",UZWater="Normal",TZOil="Sebum",UZOil="Sebum",CScore=20,CAScore=40,CState="거의 깨끗함",WScore=80,WAScore=80,WState="거의 깨끗함",TScore=10,TAScore=15,TState="보통",HScore=40,HAScore=45,HState="매우 나쁨")
    Age=Agesensor(Rating="",Rank=30)
    create_skin_pdf("김건강",SState,Age)
