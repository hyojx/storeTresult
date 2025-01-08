from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from dataclass import Nutrition,Vitastiq,Inbody,Agesensor,NutritionDetail,Supplements
from PIL import Image
from pdf2image import convert_from_path
from reportlab.lib.colors import Color
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle
from dataclasses import fields
import random
from datetime import date # 모듈추가

filepath="static/image/basic/"
resultfilepath="static/result/"
mainfont='NanumGothic'
boldfont='NanumGothicBold'
Eboldfont='NanumGothicExtraBold'
lightfont='NanumGothicLight'

# 폰트 등록 함수
def register_fonts():
    # macOS의 산돌고딕 네오 폰트 경로
    #font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
    #pdfmetrics.registerFont(TTFont('AppleGothic', font_path))

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

# 점수로 그래프 그리는 함수
def draw_part1_graph(c,height,total_score):
    c.setDash()
    baseX=73
    baseY=400
    baseW=30
    baseH=10
    bet=12

    c.setFillColorRGB(0.5,0.5,0.5)
    c.setFont(mainfont, 8)
    text_width = pdfmetrics.stringWidth("20점 ", mainfont, 8)
    c.drawString(baseX-3-text_width,height-baseY+(bet*2.6),"20점 ")

    text_width = pdfmetrics.stringWidth("40점 ", mainfont, 8)
    c.drawString(baseX-6-text_width,height-baseY+(bet*5.6),"40점 ")

    text_width = pdfmetrics.stringWidth("60점 ", mainfont, 8)
    c.drawString(baseX-9-text_width,height-baseY+(bet*8.6),"60점 ")

    text_width = pdfmetrics.stringWidth("40점 ", mainfont, 8)
    c.drawString(baseX-12-text_width,height-baseY+(bet*11.6),"80점 ")

    c.setFont(mainfont,10)

    c.setFillColorRGB(243/255,58/255,12/255) # RED
    c.drawString(baseX+baseW+2,height-baseY+(bet*1)+2," 관리시급")
    c.setFillColorRGB(1,120/255,2/255)  #ORENGE
    c.drawString(baseX+baseW+6,height-baseY+(bet*4)+2," 관리필요")
    c.setFillColorRGB(1,206/255,21/255)  #YELLOW
    c.drawString(baseX+baseW+8,height-baseY+(bet*7)+2," 경계")
    c.setFillColorRGB(133/255,205/255,1/255)  #GREEN
    c.drawString(baseX+baseW+12,height-baseY+(bet*10)+2," 양호")
    c.setFillColorRGB(46/255,117/255,182/255)  #BLUE
    c.drawString(baseX+baseW+14,height-baseY+(bet*13)+2," 매우양호")


    # 빨간색
    if 0<total_score<= 6.6:
        for i in range(0,1):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(1,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)

    if 6.6<total_score<= 13.2:
        for i in range(0,2):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(2,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)

    if 13.2<total_score<= 20:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)     

    # 주황색
    if 20<total_score<= 26.6:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,4):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(4,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 

    if 26.6<total_score<= 33.2:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,5):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)    
        for i in range(5,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 

    if 33.2<total_score<= 40:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)    
        for i in range(6,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)    

    # 노란색
    if 40<total_score<= 46.6:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,7):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)       
        for i in range(7,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)     

    if 46.6<total_score<= 53.2:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,8):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)       
        for i in range(8,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 

    if 53.2<total_score<= 60:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,9):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)       
        for i in range(9,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)     

    #초록색
    if 60<total_score<= 66.6:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,9):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)  
        for i in range(9,10):
            c.setFillColorRGB(133/255,205/255,1/255)
            c.setStrokeColorRGB(133/255,205/255,1/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)         
        for i in range(10,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 

    if 66.6<total_score<= 73.2:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,9):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)  
        for i in range(9,11):
            c.setFillColorRGB(133/255,205/255,1/255)
            c.setStrokeColorRGB(133/255,205/255,1/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)         
        for i in range(11,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)    

    if 73.2<total_score<= 80:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,9):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)  
        for i in range(9,12):
            c.setFillColorRGB(133/255,205/255,1/255)
            c.setStrokeColorRGB(133/255,205/255,1/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)         
        for i in range(12,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)      
            
    # 파란색
    if 80<total_score<= 86.6:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,9):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)  
        for i in range(9,12):
            c.setFillColorRGB(133/255,205/255,1/255)
            c.setStrokeColorRGB(133/255,205/255,1/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(12,13):
            c.setFillColorRGB(46/255,117/255,182/255)
            c.setStrokeColorRGB(46/255,117/255,182/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)            
        for i in range(13,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 

    if 86.6<total_score<= 93.2:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,9):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)  
        for i in range(9,12):
            c.setFillColorRGB(133/255,205/255,1/255)
            c.setStrokeColorRGB(133/255,205/255,1/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(12,14):
            c.setFillColorRGB(46/255,117/255,182/255)
            c.setStrokeColorRGB(46/255,117/255,182/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)            
        for i in range(14,15):
            c.setFillColorRGB(0.75,0.75,0.75)
            c.setStrokeColorRGB(0.75,0.75,0.75)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)  

    if 93.2<total_score<= 100:
        for i in range(0,3):
            c.setFillColorRGB(243/255,58/255,12/255)
            c.setStrokeColorRGB(243/255,58/255,12/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)
        for i in range(3,6):
            c.setFillColorRGB(1,120/255,2/255)
            c.setStrokeColorRGB(1,120/255,2/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(6,9):
            c.setFillColorRGB(1,206/255,21/255)
            c.setStrokeColorRGB(1,206/255,21/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)  
        for i in range(9,12):
            c.setFillColorRGB(133/255,205/255,1/255)
            c.setStrokeColorRGB(133/255,205/255,1/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1) 
        for i in range(12,15):
            c.setFillColorRGB(46/255,117/255,182/255)
            c.setStrokeColorRGB(46/255,117/255,182/255)
            c.roundRect(baseX-(1*i),height-baseY+(bet*i), baseW+(2*i), baseH,2,fill=1)     

# Main 점수 표시 함수
def draw_score_string(c,height,score):
    if 0<=score<=20:
        c.setFont(boldfont, 16)
        c.setFillColorRGB(243/255,58/255,12/255) #RED color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,boldfont, 14)

        c.setFont(boldfont, 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")

    if 20<score<=40:
        c.setFont(boldfont, 16)
        c.setFillColorRGB(1,120/255,2/255) #ORENGE color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,boldfont, 14)

        c.setFont(boldfont, 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")

    if 40<score<=60:
        c.setFont(boldfont, 16)
        c.setFillColorRGB(1,206/255,21/255) #YELLOW color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,boldfont, 14)

        c.setFont(boldfont, 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")        

    if 60<score<=80:
        c.setFont(boldfont, 16)
        c.setFillColorRGB(133/255,205/255,1/255) #GREEN color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,boldfont, 14)

        c.setFont(boldfont, 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")    

    if 80<score<=100:
        c.setFont(boldfont, 16)
        c.setFillColorRGB(46/255,117/255,182/255) #BLUE color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,boldfont, 14)

        c.setFont(boldfont, 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")    

# 테이블 컬러 커스터마이징
def CustomStyle(Nutrition):
    Yellow=Color(1,208/255,20/255)
    Red=Color(1,111/255,111/255)
    Green=Color(134/255,206/255,2/255)
    StyleList=[]
    #탄수화물
    if Nutrition.Carb=="과다":
        StyleList.append(('BACKGROUND', (2, 0), (2, 0), Red))
    elif Nutrition.Carb=="적정":
        StyleList.append(('BACKGROUND', (1, 0), (1, 0), Green))
    elif Nutrition.Carb=="부족":
        StyleList.append(('BACKGROUND', (0, 0), (0, 0), Yellow))    
    
    #단백질
    if Nutrition.Protein=="과다":
        StyleList.append(('BACKGROUND', (2, 1), (2, 1), Red))
    elif Nutrition.Protein=="적정":
        StyleList.append(('BACKGROUND', (1, 1), (1, 1), Green))
    elif Nutrition.Protein=="부족":
        StyleList.append(('BACKGROUND', (0, 1), (0, 1), Yellow))

    #지방
    if Nutrition.Fat=="과다":
        StyleList.append(('BACKGROUND', (2, 2), (2, 2), Red))
    elif Nutrition.Fat=="적정":
        StyleList.append(('BACKGROUND', (1, 2), (1, 2), Green))
    elif Nutrition.Fat=="부족":
        StyleList.append(('BACKGROUND', (0, 2), (0, 2), Yellow))  

    #식이섬유
    if Nutrition.Fiber=="과다":
        StyleList.append(('BACKGROUND', (2, 3), (2, 3), Red))
    elif Nutrition.Fiber=="적정":
        StyleList.append(('BACKGROUND', (1, 3), (1, 3), Green))
    elif Nutrition.Fiber=="부족":
        StyleList.append(('BACKGROUND', (0, 3), (0, 3), Yellow))  

    #나트륨
    if Nutrition.Sodium=="과다":
        StyleList.append(('BACKGROUND', (2, 4), (2, 4), Red))
    elif Nutrition.Sodium=="적정":
        StyleList.append(('BACKGROUND', (1, 4), (1, 4), Green))  

    #당류
    if Nutrition.Sugar=="과다":
        StyleList.append(('BACKGROUND', (2, 5), (2, 5), Red))
    elif Nutrition.Sugar=="적정":
        StyleList.append(('BACKGROUND', (1, 5), (1, 5), Green))

    #포화지방
    if Nutrition.SatFat=="과다":
        StyleList.append(('BACKGROUND', (2, 6), (2, 6), Red))
    elif Nutrition.SatFat=="적정":
        StyleList.append(('BACKGROUND', (1, 6), (1, 6), Green))

    #콜레스테롤
    if Nutrition.Cholesterol=="과다":
        StyleList.append(('BACKGROUND', (2, 7), (2, 7), Red))
    elif Nutrition.Cholesterol=="적정":
        StyleList.append(('BACKGROUND', (1, 7), (1, 7), Green))                       
    
    
    return StyleList

# 섭취량 표에 영양소별 식품 이미지 삽입
def Food_Image(c,Nutrition,height):
    
    #탄수화물
    if Nutrition.Carb=="과다":
        c.drawImage(filepath+"Carb.png", 498, height - 214, 50,23,mask='auto')
    elif Nutrition.Carb=="적정":
        c.drawImage(filepath+"Carb.png", 433, height - 214, 50,23,mask='auto')
    elif Nutrition.Carb=="부족":
        c.drawImage(filepath+"Carb.png", 368, height - 214, 50,23,mask='auto')    
    
    #단백질
    if Nutrition.Protein=="과다":
        c.drawImage(filepath+"Pro.png", 498, height - 242.5, 50,23,mask='auto')
    elif Nutrition.Protein=="적정":
        c.drawImage(filepath+"Pro.png", 433, height - 242.5, 50,23,mask='auto')
    elif Nutrition.Protein=="부족":
        c.drawImage(filepath+"Pro.png", 368, height - 242.5, 50,23,mask='auto')

    #지방
    if Nutrition.Fat=="과다":
        c.drawImage(filepath+"Fat.png", 498, height - 270.5, 50,23,mask='auto')
    elif Nutrition.Fat=="적정":
        c.drawImage(filepath+"Fat.png", 433, height - 270.5, 50,23,mask='auto')
    elif Nutrition.Fat=="부족":
        c.drawImage(filepath+"Fat.png", 368, height - 270.5, 50,23,mask='auto')

    #식이섬유
    if Nutrition.Fiber=="과다":
        c.drawImage(filepath+"Fiber.png", 498, height - 298.5, 50,23,mask='auto')
    elif Nutrition.Fiber=="적정":
        c.drawImage(filepath+"Fiber.png", 433, height - 298.5, 50,23,mask='auto')
    elif Nutrition.Fiber=="부족":
        c.drawImage(filepath+"Fiber.png", 368, height - 298.5, 50,23,mask='auto')

    #나트륨
    if Nutrition.Sodium=="과다":
        c.drawImage(filepath+"Sod.png", 498, height - 327.5, 50,23,mask='auto')
    elif Nutrition.Sodium=="적정":
        c.drawImage(filepath+"Sod.png", 433, height - 327.5, 50,23,mask='auto')

    #당류
    if Nutrition.Sugar=="과다":
        c.drawImage(filepath+"Sugar.png", 498, height - 355.5, 50,23,mask='auto')
    elif Nutrition.Sugar=="적정":
        c.drawImage(filepath+"Sugar.png", 433, height - 355.5, 50,23,mask='auto')

    #포화지방
    if Nutrition.SatFat=="과다":
        c.drawImage(filepath+"SatF.png", 498, height - 384, 50,23,mask='auto')
    elif Nutrition.SatFat=="적정":
        c.drawImage(filepath+"SatF.png", 433, height - 384, 50,23,mask='auto')

    #콜레스테롤
    if Nutrition.Cholesterol=="과다":
        c.drawImage(filepath+"Cho.png", 498, height - 412.5, 50,23,mask='auto')
    elif Nutrition.Cholesterol=="적정": 
        c.drawImage(filepath+"Cho.png", 433, height - 412.5, 50,23,mask='auto')                       
    
    return

# 피드백 세팅하는 함수
def set_feedback(Nutrition):
    over_feedback=""
    under_feedback=""
    if Nutrition.Carb=="과다":
        over_feedback+="탄수화물, "
    elif Nutrition.Carb=="부족":
        under_feedback+="탄수화물, "

    if Nutrition.Protein=="과다":
        over_feedback+="단백질, "
    elif Nutrition.Protein=="부족":
        under_feedback+="단백질, "

    if Nutrition.Fat=="과다":
        over_feedback+="지방, "
    elif Nutrition.Fat=="부족":
        under_feedback+="지방, "

    if Nutrition.Fiber=="부족":
        under_feedback+="식이섬유, "    

    if Nutrition.Sodium=="과다":
        over_feedback+="나트륨, "

    if Nutrition.Sugar=="과다":
        over_feedback+="당류, "

    if Nutrition.SatFat=="과다":
        over_feedback+="포화지방, "    

    if Nutrition.Cholesterol=="과다":
        over_feedback+="콜레스테롤, "   

    over_feedback=over_feedback[:-2]  
    under_feedback=under_feedback[:-2]

    if over_feedback:
        if 0<(ord(over_feedback[-1])-0xAC00)%28:
            print((ord(over_feedback[-1])-0xAC00)%28)
            over_feedback+="은"
        else: 
            over_feedback+="는" 
            
    if under_feedback:
        if 0<(ord(under_feedback[-1])-0xAC00)%28:
            print((ord(under_feedback[-1])-0xAC00)%28)
            under_feedback+="은"
        else: 
            under_feedback+="는"        

    feedbacks=[over_feedback, under_feedback] 
    return feedbacks                
    
# 한눈에 보는 나의 식습관
def draw_part2(c,Nutrition,height):
    #색상안내
    c.setFillColorRGB(1,208/255,20/255)
    c.circle(468,height-135,5,fill=1,stroke=0)
    c.setFillColorRGB(134/255,206/255,2/255)
    c.circle(500,height-135,5,fill=1,stroke=0)
    c.setFillColorRGB(1,111/255,111/255)
    c.circle(532,height-135,5,fill=1,stroke=0)
    c.setFillColorRGB(0.25,0.25,0.25)
    c.setFont(mainfont, 8)
    c.drawString(475,height-138,'부족')
    c.drawString(507,height-138,'적정')
    c.drawString(539,height-138,'과다')

    # 한줄피드백 작성 (07.09 4시 수정)
    feedbacks=set_feedback(Nutrition)
    c.setFont(mainfont, 10)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    if feedbacks[0]=="":
        c.drawString(315,height-160,'과다하게 섭취하는 영양소는 없어요')
    else: 
        if 250<pdfmetrics.stringWidth(feedbacks[0]+" 과다해요.",mainfont,10):
            c.setFont(mainfont, 8)
            c.drawString(315,height-160,feedbacks[0]+" 과다해요.")
        else:    
            c.drawString(315,height-160,feedbacks[0]+" 과다해요.")

    if feedbacks[1]=="":
        c.drawString(315,height-175,'부족하게 섭취하는 영양소는 없어요')
    else: 
        c.drawString(315,height-175,feedbacks[1]+" 부족해요.")    

    # 표 그리기
    BaseX2=315
    BaseY2=height-205
    c.setFillColorRGB(0, 0, 0)
    c.setFont(mainfont, 8)
    c.drawString(BaseX2,BaseY2,"탄수화물")
    c.drawString(BaseX2,BaseY2-28,"단백질")
    c.drawString(BaseX2,BaseY2-56,"지방")
    c.drawString(BaseX2,BaseY2-84,"식이섬유")
    c.drawString(BaseX2,BaseY2-112,"나트륨")
    c.drawString(BaseX2,BaseY2-140,"당류")
    c.drawString(BaseX2,BaseY2-168,"포화지방")
    c.drawString(BaseX2,BaseY2-196,"콜레스테롤")

    # Define table data (8 rows x 3 columns)
    data = [[''] * 3 for _ in range(8)]

    #파스텔 컬러지정
    Wyellow=Color(1,246/255,208/255)
    Wgreen=Color(222/255,236/255,194/255)
    Wred=Color(1,226/255,226/255)
    White=Color(1,1,1)

    # 테이블 스타일 지정
    style = TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), Wyellow),   # First column background color
        ('BACKGROUND', (1, 0), (1, -1), Wgreen),    # Second column background color
        ('BACKGROUND', (2, 0), (2, -1), Wred),      # Third column background color
        ('LINEBEFORE', (0, 0), (-1, -1), 1, White), # White lines
        ('LINEAFTER', (0, 0), (-1, -1), 1, White),
        ('LINEABOVE', (0, 0), (-1, -1), 1, White),
        ('LINEBELOW', (0, 0), (-1, -1), 1, White),
        ('INNERGRID', (0, 0), (-1, -1), 1, White),
    ])
    
    SL=CustomStyle(Nutrition)
    addStyle=TableStyle(SL)

    # 테이블 생성
    table = Table(data, colWidths=[23*mm] * 3, rowHeights=[10*mm] * 8)
    table.setStyle(style)
    table.setStyle(addStyle)
    
    # 테이블 그리기
    table.wrapOn(c, A4[0], A4[1])
    table.drawOn(c, BaseX2+45, BaseY2-210)

    Food_Image(c,Nutrition,height)

# 별 그리기 (07.09 7시 수정)
def draw_star(c,Vitastiq,height):
    star_size=18
    baseX=105
    baseY=height-502
    bet=107

    if Vitastiq.Mg=="낮음"or Vitastiq.Mg=="경미":
        c.drawImage(filepath+"Star_red.png", baseX, baseY, star_size,star_size,mask='auto')

    if Vitastiq.Biotin=="낮음" or Vitastiq.Biotin=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*1), baseY, star_size,star_size,mask='auto')

    if Vitastiq.Se=="낮음" or Vitastiq.Se=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*2), baseY, star_size,star_size,mask='auto')

    if Vitastiq.VitB2=="낮음" or Vitastiq.VitB2=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*3), baseY, star_size,star_size,mask='auto')

    if Vitastiq.Folate=="낮음" or Vitastiq.Folate=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*4), baseY, star_size,star_size,mask='auto')

    if Vitastiq.Zn=="낮음" or Vitastiq.Zn=="경미":
        c.drawImage(filepath+"Star_red.png", baseX, baseY-68, star_size,star_size,mask='auto')

    if Vitastiq.VitC=="낮음" or Vitastiq.VitC=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*1), baseY-68, star_size,star_size,mask='auto')

    if Vitastiq.VitB1=="낮음" or Vitastiq.VitB1=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*2), baseY-68, star_size,star_size,mask='auto')

    if Vitastiq.VitE=="낮음" or Vitastiq.VitE=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*3), baseY-68, star_size,star_size,mask='auto')

    if Vitastiq.VitB6=="낮음" or Vitastiq.VitB6=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*4), baseY-68, star_size,star_size,mask='auto')        
             
    return

# 인바디 유형결정
def set_category(Inbody):
    C_id=""
    weightP=(Inbody.Weight*115)/Inbody.WeightMax
    skeletalP=Inbody.SkeletalMuscle*110/Inbody.MuscleMax
    fatP=Inbody.BodyFat*160/Inbody.FatMax
    print(weightP)
    print(skeletalP)
    print(fatP)
    if 85 < weightP <115:
        if skeletalP <= 90 and 80<fatP <160:
            C_id="C_sw"
        elif skeletalP<= 110 and 160<=fatP:
            C_id="C_so"
        elif 110<=skeletalP and fatP<160:
            C_id="D_ss"
        elif 90<skeletalP<110 and 80<fatP<160:
            C_id="I_sh"
        elif 90<skeletalP<110 and fatP<80:
            C_id="D_ss"    
        else:
            C_id="N"    
    elif 115<=weightP:                    #(07.09 4시 수정)
        if skeletalP<=110 and 160<=fatP:
            C_id="C_ow"
        elif 110<=skeletalP and 80<fatP<160:
            C_id="D_os"
        elif 110<=skeletalP and 160<=fatP:
            C_id="I_oo"
        else:
            C_id="N"     
    elif weightP<=85:                     #(07.09 4시 수정)
        if 90<=skeletalP and fatP<=160:   # 로직 수정 07.15 오후
            C_id="D_ls"
        elif skeletalP<90 and fatP<=160:  # 로직 수정 07.15 오후
            C_id="I_lw"    
        else:
            C_id="N"             
    return C_id

# 판교점 인바디 유형결정
def set_category_small(Inbody,UserHeight,Gender):
    C_id=""
    SWeight=((UserHeight*UserHeight)/10000)*22
    if Gender=="남성":
        SFatFree=Inbody.Weight*0.8
    elif Gender=="여성":
        SFatFree=Inbody.Weight*0.72    
    weightP=Inbody.Weight/SWeight*100
    skeletalP=(Inbody.FatFree/SFatFree)*100
    if (SFatFree-Inbody.FatFree)<=0:
        fatP=Inbody.BodyFat/(Inbody.BodyFat+(SWeight-Inbody.Weight))*100
    else:    
        fatP=Inbody.BodyFat/(Inbody.BodyFat+((SWeight-Inbody.Weight)-(SFatFree-Inbody.FatFree)))*100
    print(weightP)
    print(skeletalP)
    print(fatP)
    if 85 < weightP <115:
        if skeletalP <= 90 and 80<fatP <160:
            C_id="C_sw"
        elif skeletalP<= 110 and 160<=fatP:
            C_id="C_so"
        elif 110<=skeletalP and fatP<160:
            C_id="D_ss"
        elif 90<skeletalP<110 and 80<fatP<160:
            C_id="I_sh"
        elif 90<skeletalP<110 and fatP<80:
            C_id="D_ss"    
        else:
            C_id="N"    
    elif 115<=weightP:                  
        if skeletalP<=110 and 160<=fatP:
            C_id="C_ow"
        elif 110<=skeletalP and 80<fatP<160:
            C_id="D_os"
        elif 110<=skeletalP and 160<=fatP:
            C_id="I_oo"
        else:
            C_id="N"     
    elif weightP<=85:           
        if 90<=skeletalP and fatP<=80:  
            C_id="D_ls"
        elif skeletalP<90 and fatP<=80:  
            C_id="I_lw"    
        else:
            C_id="N"             
    return C_id    

# FS 인바디 유형결정
def set_category_fs(InbodyCat):
    #'표준체중 허약형','표준체중 비만형','표준체중 강인형','표준체중 건강형','과체중 허약형','과체중 강인형','과체중 비만형','저체중 강인형','저체중 허약형'
    if InbodyCat=="표준체중 허약형":
        C_id="C_sw"
    elif InbodyCat=="표준체중 비만형":
        C_id="C_so"
    elif InbodyCat=="표준체중 강인형":
        C_id="D_ss"      
    elif InbodyCat=="표준체중 건강형":
        C_id="I_sh" 
    elif InbodyCat=="과체중 허약형":
        C_id="C_ow"
    elif InbodyCat=="과체중 강인형":
        C_id="D_os"      
    elif InbodyCat=="과체중 비만형":
        C_id="I_oo"
    elif InbodyCat=="저체중 강인형":
        C_id="D_ls"  
    elif InbodyCat=="저체중 허약형":
        C_id="I_lw"    
    else:
        C_id="N"     
    return C_id                  

#인바디 유형별 코멘트 작성
def write_comment(c,Inbody_cat,height):
    if Inbody_cat=="C_sw":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 허약형 (C자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 체지방량으로는 정상이지만 골격근이 부족한 유형')
        c.drawString(32,height-815,'•근육을 구성하는 단백질이 부족한 것이 원인')

    elif Inbody_cat=="C_so":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 비만형 (C자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 근육량은 정상이지만 체지방이 과다한 유형')
        c.drawString(32,height-815,'•탄수화물, 지방 위주의 과도한 칼로리 섭취가 원인') 

    elif Inbody_cat=="C_ow":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"과체중 허약형 (C자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중과 체지방량이 골격근량 대비하여 과다한 유형')
        c.drawString(32,height-815,'•과도한 칼로리, 부족한 단백질 섭취, 근력운동 부족이 원인')

    elif Inbody_cat=="D_ss":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 강인형 (D자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•날씬하면서 근육이 탄탄하게 잘 다듬어져 있는 유형')
        c.drawString(32,height-815,'•균형잡힌 섭취와 유산소, 근력운동 병행을 통한 상태유지')

    elif Inbody_cat=="D_ss":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 강인형 (D자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•날씬하면서 근육이 탄탄하게 잘 다듬어져 있는 유형')
        c.drawString(32,height-815,'•균형잡힌 섭취와 유산소, 근력운동 병행을 통한 상태유지') 

    elif Inbody_cat=="D_ls":
    #elif Inbody_cat=="C_so":    
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"저체중 강인형 (D자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•근육량은 표준이상, 체중과 체지방량이 표준이하인 유형')
        c.drawString(32,height-815,'•근력운동, 균형잡힌 섭취를 통해 체지방, 골격근 유지 필요') 

    elif Inbody_cat=="D_os":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"과체중 강인형 (D자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•과체중이지만 체지방에 비해 골격근이 발달한 유형')
        c.drawString(32,height-815,'•주로 운동선수들에게 나타나는 유형으로 체지방 유지 필요')

    elif Inbody_cat=="I_sh":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 건강형 (I자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 골격근량, 체지방량이 모두 표준인 유형')
        c.drawString(32,height-815,'•유산소, 근력운동 병행을 통해 체지방량이 유지 필요')

    elif Inbody_cat=="I_lw":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"저체중 허약형 (I자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 골격근량, 체지방량이 모두 표준이하인 유형')
        c.drawString(32,height-815,'•섭취하는 영양소의 양이 전반적으로 부족한것이 원인')    

    elif Inbody_cat=="I_oo":
    #elif Inbody_cat=="C_so":    
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"과체중 비만형 (I자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 골격근량, 체지방량이 모두 표준이상인 유형')
        c.drawString(32,height-815,'•전체적으로 표준보다 체구성 성분이 많아서 나타나는 유형')      

    elif Inbody_cat=="N":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"유형을 분류할 수 없습니다. 인바디 값을 확인해주세요."')
    return
 
#인바디 그래프 그리기(270이상 기기)
def draw_inbody(c,Inbody,height):
    weightP=(Inbody.Weight*115)/Inbody.WeightMax
    skeletalP=Inbody.SkeletalMuscle*110/Inbody.MuscleMax
    fatP=Inbody.BodyFat*160/Inbody.FatMax

    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.setStrokeColorRGB(0.9, 0.9, 0.9)
    c.roundRect(90,height-710, 180, 15,7.5,fill=1)
    c.roundRect(90,height-740, 180, 15,7.5,fill=1)
    c.roundRect(90,height-770, 180, 15,7.5,fill=1)

    weightW=max(0,180*(weightP-55)/150)
    skeletalW=max(0,180*(skeletalP-70)/100)
    if fatP<=100:
        fatW=max(0,54*(fatP-40)/60)
    elif 100<fatP:    
        fatW=54+126*(fatP-100)/420

    if weightP<=85 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-710, weightW, 15,7.5,fill=1)

    if 85<weightP<115 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-710, weightW, 15,7.5,fill=1)

    if 115<=weightP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-710, weightW, 15,7.5,fill=1)   


    if skeletalP<=90 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-740, skeletalW, 15,7.5,fill=1)

    if 90<skeletalP<110 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-740, skeletalW, 15,7.5,fill=1)

    if 110<=skeletalP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-740, skeletalW, 15,7.5,fill=1)    

    # 로직 수정 07.16 3시 ---------------------------------------
    if fatP<=80 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)

    if 80<fatP<160 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)

    if 160<=fatP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)    
    # 로직 수정 07.16 3시 ---------------------------------------     

    c.setFillColorRGB(1,1,1)
    c.drawString(65+weightW,height-710+5,str(Inbody.Weight))    
    c.drawString(65+skeletalW,height-740+5,str(Inbody.SkeletalMuscle))  
    c.drawString(65+fatW,height-770+5,str(Inbody.BodyFat))

    c.setLineWidth(0.5)
    c.setStrokeColorRGB(0.9,0.9,0.9)
    c.line(126, height - 695, 126, height - 710)
    c.line(126, height - 725, 126, height - 740)
    c.line(126, height - 755, 126, height - 770)

    c.line(162, height - 695, 162, height - 710)
    c.line(162, height - 725, 162, height - 740)
    c.line(162, height - 755, 162, height - 770)

    return

#인바디 그래프 그리기(피트러스 라이트)
def draw_inbody_small(c,Inbody,UserHeight,Gender,height):
    SWeight=((UserHeight*UserHeight)/10000)*22
    if Gender=="남성":
        SFatFree=Inbody.Weight*0.8
    elif Gender=="여성":
        SFatFree=Inbody.Weight*0.72    
    weightP=Inbody.Weight/SWeight*100
    skeletalP=(Inbody.FatFree/SFatFree)*100
    if (SFatFree-Inbody.FatFree)<=0:
        fatP=Inbody.BodyFat/(Inbody.BodyFat+(SWeight-Inbody.Weight))*100
    else:    
        fatP=Inbody.BodyFat/(Inbody.BodyFat+((SWeight-Inbody.Weight)-(SFatFree-Inbody.FatFree)))*100

    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.setStrokeColorRGB(0.9, 0.9, 0.9)
    c.roundRect(90,height-710, 180, 15,7.5,fill=1)
    c.roundRect(90,height-740, 180, 15,7.5,fill=1)
    c.roundRect(90,height-770, 180, 15,7.5,fill=1)

    weightW=max(0,180*(weightP-55)/150)
    skeletalW=max(0,180*(skeletalP-70)/100)
    if fatP<=100:
        fatW=max(0,54*(fatP-40)/60)
    elif 100<fatP:    
        fatW=54+126*(fatP-100)/420

    """if Gender=="남성":
        fatW=180*(fatP)/50
    elif Gender=="여성":    
        fatW=180*(fatP-8)/50"""

    if weightP<=85 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-710, weightW, 15,7.5,fill=1)

    if 85<weightP<115 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-710, weightW, 15,7.5,fill=1)

    if 115<=weightP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-710, weightW, 15,7.5,fill=1)   


    if skeletalP<=90 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-740, skeletalW, 15,7.5,fill=1)

    if 90<skeletalP<110 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-740, skeletalW, 15,7.5,fill=1)

    if 110<=skeletalP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-740, skeletalW, 15,7.5,fill=1)    

    # 로직 수정 07.16 3시 ---------------------------------------
    if fatP<=80 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)

    if 80<fatP<160 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)

    if 160<=fatP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)    
    # 로직 수정 07.16 3시 ---------------------------------------     

    c.setFillColorRGB(1,1,1)
    c.drawString(65+weightW,height-710+5,str(Inbody.Weight))    
    c.drawString(65+skeletalW,height-740+5,str(Inbody.FatFree))  
    c.drawString(65+fatW,height-770+5,str(Inbody.BodyFat))

    c.setLineWidth(0.5)
    c.setStrokeColorRGB(0.9,0.9,0.9)
    c.line(126, height - 695, 126, height - 710)
    c.line(126, height - 725, 126, height - 740)
    c.line(126, height - 755, 126, height - 770)

    c.line(162, height - 695, 162, height - 710)
    c.line(162, height - 725, 162, height - 740)
    c.line(162, height - 755, 162, height - 770)

    return    

#인바디 그래프 그리기(인바디 가정용)
def draw_inbody_home(c,height,C_id,Inbody):
    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.setStrokeColorRGB(0.9, 0.9, 0.9)
    c.roundRect(90,height-710, 180, 15,7.5,fill=1)
    c.roundRect(90,height-740, 180, 15,7.5,fill=1)
    c.roundRect(90,height-770, 180, 15,7.5,fill=1)

    if C_id=="D_ls" or C_id=="I_lw":
        c.setFillColorRGB(1,208/255,20/255) #Yellow
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-710, 30, 15,7.5,fill=1)
        weightW=30
    elif C_id=="C_sw" or C_id=="D_ss" or C_id=="I_sh" or C_id=="C_so":
        c.setFillColorRGB(134/255,206/255,2/255) #Green
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-710, 54, 15,7.5,fill=1)
        weightW=54
    elif C_id=="C_ow" or C_id=="D_os" or C_id=="I_oo":
        c.setFillColorRGB(1,111/255,111/255) #Red
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-710, 90, 15,7.5,fill=1)
        weightW=90
    c.setFillColorRGB(1,1,1)
    c.drawString(65+weightW,height-710+5,str(Inbody.Weight))    

    if C_id=="C_sw" or C_id == "C_so"or C_id=="I_lw":
        c.setFillColorRGB(1,208/255,20/255) #Yellow
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-740, 30, 15,7.5,fill=1)
        fatfreeW=30
    elif C_id=="I_sh" or C_id=="D_ls" or C_id=="C_ow":
        c.setFillColorRGB(134/255,206/255,2/255) #Green
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-740, 54, 15,7.5,fill=1)
        fatfreeW=54
    elif C_id=="D_ss" or C_id=="I_oo" or C_id=="D_os":
        c.setFillColorRGB(134/255,206/255,2/255) #Green
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-740, 90, 15,7.5,fill=1)
        fatfreeW=90
    c.setFillColorRGB(1,1,1)
    c.drawString(65+fatfreeW,height-740+5,str(Inbody.Weight-Inbody.BodyFat)) 

    if C_id=="D_ls" or C_id=="I_lw":
        c.setFillColorRGB(134/255,206/255,2/255) #Green
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-770, 30, 15,7.5,fill=1)
        fatW=30
    elif C_id=="C_sw" or C_id=="D_ss" or C_id=="I_sh" or C_id=="D_os":
        c.setFillColorRGB(1,208/255,20/255) #Yellow
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-770, 54, 15,7.5,fill=1)
        fatW=54
    elif C_id=="C_ow" or C_id=="C_so" or C_id=="I_oo":
        c.setFillColorRGB(1,111/255,111/255) #Red
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-770, 90, 15,7.5,fill=1)   
        fatW=90 
    c.setFillColorRGB(1,1,1)
    c.drawString(65+fatW,height-770+5,str(Inbody.BodyFat))

    c.setLineWidth(0.5)
    c.setStrokeColorRGB(0.9,0.9,0.9)
    c.line(126, height - 695, 126, height - 710)
    c.line(126, height - 725, 126, height - 740)
    c.line(126, height - 755, 126, height - 770)

    c.line(162, height - 695, 162, height - 710)
    c.line(162, height - 725, 162, height - 740)
    c.line(162, height - 755, 162, height - 770)

    return

#인바디 그래프 그리기(270이하 추가 그래프_체지방률,골격근량,복주지방률,내장지방레벨)
def draw_inbody_small_adddetail(c,Inbody,UserHeight,Gender,height):
    BFR=Inbody.BodyFatRatio
    SMM=Inbody.SkeletalMuscle    
    WHR=Inbody.WaistHipRatio
    VFL=Inbody.VisceralFatLevel

    if Gender=="남성":
        BFRmax=20
        BFRmin=10
        SMMmax=8*UserHeight*UserHeight/10000
        SMMmin=7*UserHeight*UserHeight/10000
    else:
        BFRmax=28
        BFRmin=18
        SMMmax=6.7*UserHeight*UserHeight/10000
        SMMmin=5.7*UserHeight*UserHeight/10000    
    WHRmax=75
    WHRmin=25
    VFLmax=10
    VFLmin=5

    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.setStrokeColorRGB(0.9, 0.9, 0.9)
    c.roundRect(370,height-680-15, 180, 15,7.5,fill=1)
    c.roundRect(370,height-710-10, 180, 15,7.5,fill=1)
    c.roundRect(370,height-740-5, 180, 15,7.5,fill=1)
    c.roundRect(370,height-770, 180, 15,7.5,fill=1)

    BFRwidth=max(0,180*(BFR)/60)
    SMMwidth=max(0,180*(SMM)/(Inbody.Weight-Inbody.BodyFat))
    WHRwidth=max(0,180*(WHR)/100)
    VFLwidth=max(0,180*(VFL)/20)

    if BFR<BFRmin :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(370,height-680-15, BFRwidth, 15,7.5,fill=1)

    if BFRmin<=BFR<=BFRmax :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(370,height-680-15, BFRwidth, 15,7.5,fill=1)

    if BFRmax<BFR :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(370,height-680-15, BFRwidth, 15,7.5,fill=1)   


    if SMM<SMMmin :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(370,height-710-10, SMMwidth, 15,7.5,fill=1)

    if SMMmin<=SMM<=SMMmax :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(370,height-710-10, SMMwidth, 15,7.5,fill=1)

    if SMMmax<SMM :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(370,height-710-10, SMMwidth, 15,7.5,fill=1)    

    
    if WHR<WHRmin :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(370,height-740-5, WHRwidth, 15,7.5,fill=1)

    if WHRmin<=WHR<=WHRmax :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(370,height-740-5, WHRwidth, 15,7.5,fill=1)

    if WHRmax<WHR :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(370,height-740-5, WHRwidth, 15,7.5,fill=1) 



    if VFL<VFLmin :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(370,height-770, VFLwidth, 15,7.5,fill=1)

    if VFLmin<=VFL<=VFLmax :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(370,height-770, VFLwidth, 15,7.5,fill=1)

    if VFLmax<VFL :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(370,height-770, VFLwidth, 15,7.5,fill=1)      
        

    c.setFillColorRGB(1,1,1)
    c.drawString(345+BFRwidth,height-690,str(BFR))    
    c.setFillColorRGB(1,1,1)
    c.drawString(345+SMMwidth,height-715,str(SMM))  
    c.drawString(345+WHRwidth,height-740,str(WHR))  
    c.drawString(345+VFLwidth,height-770+5,str(VFL))

    c.setLineWidth(0.5)
    c.setStrokeColorRGB(1,1,1)
    #최소값 표기
    c.line((BFRmin*180)/60+370, height - 665-15, (BFRmin*180)/60+370, height - 680-15)
    c.line((SMMmin*180)/(Inbody.Weight-Inbody.BodyFat)+370, height - 695-10, (SMMmin*180)/(Inbody.Weight-Inbody.BodyFat)+370, height - 710-10)
    c.line((WHRmin*180)/100+370, height - 725-5, (WHRmin*180)/100+370, height - 740-5)
    c.line((VFLmin*180)/20+370, height - 755, (VFLmin*180)/20+370, height - 770)
    #최대값 표기
    c.line((BFRmax*180)/60+370, height - 665-15, (BFRmax*180)/60+370, height - 680-15)
    c.line((SMMmax*180)/(Inbody.Weight-Inbody.BodyFat)+370, height - 695-10, (SMMmax*180)/(Inbody.Weight-Inbody.BodyFat)+370, height - 710-10)
    c.line((WHRmax*180)/100+370, height - 725-5, (WHRmax*180)/100+370, height - 740-5)
    c.line((VFLmax*180)/20+370, height - 755, (VFLmax*180)/20+370, height - 770)

    return   

#인바디 유형 그리기
def draw_alpha(c,Inbody_cat,height):
    if "C" in Inbody_cat:
        c.drawImage(filepath+'C_in.png',145,height-770,68,76,mask='auto')

    elif "D" in Inbody_cat:
        c.drawImage(filepath+'D_in.png',145,height-770,68,76,mask='auto')    

    elif "I" in Inbody_cat:
        c.drawImage(filepath+'I_in.png',150,height-770,50,76,mask='auto')   
    elif "N" in Inbody_cat:
        print("유형을 분류할 수 없는 항목")
    return

# 에이지 센서 패널
def draw_panel(c,Agesensor,height):
    
    baseX=320
    baseY=height-750
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
    c.drawString(baseX+160,baseY+35,rating)

    c.setFont(boldfont, 15)
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawString(baseX+195,baseY+40,"등급")  

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

    c.roundRect(baseX-5,baseY-70, 140, 65,10)
    c.roundRect(baseX+145,baseY-70, 95, 65,10)

    c.setFont(boldfont, 10)
    c.setFillColorRGB(0.1,0.1,0.1)
    c.drawString(baseX+5,baseY-20,"AGEs(당독소)란?")
    c.setFont(mainfont, 8.5)
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawString(baseX+5,baseY-35,"포도당, 과당과 같은 당이 단백질")
    c.drawString(baseX+5,baseY-47,"또는 지방에 결합하여 당화된")
    c.drawString(baseX+5,baseY-59,"물질로 노화 시 증가")

    c.setFont(boldfont, 10)
    c.setFillColorRGB(0.1,0.1,0.1)
    c.drawString(baseX+155,baseY-20,"당독소 과다증")
    c.setFont(mainfont, 8.5)
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawString(baseX+155,baseY-35,"노화,비만,당뇨,")
    c.drawString(baseX+155,baseY-47,"노안,간염")
    c.drawString(baseX+155,baseY-59,"뇌 기능 장애")
    return

# 상품추천 유형구분 함수
def set_product_cat(Gender,Vitastiq,Agesensor):
    if Vitastiq.Unused==True :
        Pcategory="항산화"
    else:
        i=0
        scorelist=[None]*10 # Mg,Biotin,Se,VitB2,Folate,Zn,VitC,VitE,VitB6,VitB1   
        for field in fields(Vitastiq):
            field_name = field.name
            if field_name=="Unused":
                pass  
            else:
                field_value = getattr(Vitastiq, field_name)
                if field_value =="낮음":      #07.09 7시 수정
                    scorelist[i]=90
                elif field_value=="경미":
                    scorelist[i]=95
                else : 
                    scorelist[i]=100
                i+=1
        print(scorelist)   
        activeS = (scorelist[1]+scorelist[9]+scorelist[3])/3
        antiageS = (scorelist[6]+scorelist[7]+scorelist[2])/3
        immunS = (scorelist[4]+scorelist[5])/2
        muscleS= (scorelist[0]+scorelist[8])/2

        variables = [
        ('활력', activeS),
        ('항산화', antiageS),
        ('면역력', immunS),
        ('근력', muscleS)
        ]
        
        if Agesensor.Rating=="A" or Agesensor.Rating=="B" or Agesensor.Rating=="":
            sorted_variables = sorted(variables, key=lambda x: x[1]) # 오름차순 정렬 (07.09 4시 수정)
            print(sorted_variables)
            if sorted_variables[0][1]==sorted_variables[1][1]==sorted_variables[2][1]==sorted_variables[3][1]:
                if Gender=="남성":
                    Pcategory="근력"
                elif Gender=="여성":
                    Pcategory="면역력"
            elif sorted_variables[0][1]==sorted_variables[1][1]==sorted_variables[2][1]:
                Pcategory=random.choice(sorted_variables[0:3])[0]   
            elif sorted_variables[0][1]==sorted_variables[1][1]: 
                Pcategory=random.choice(sorted_variables[0:2])[0]  
            else:
                Pcategory=sorted_variables[0][0] 

# 07.09 오후 급하게 수정필요-----------------------------------------------------------------
        if Agesensor.Rating=="C" or Agesensor.Rating=="D" or Agesensor.Rating=="E":
            sorted_variables = sorted(variables, key=lambda x: x[1]) # 오름차순 정렬 (07.09 4시 수정)
            print(sorted_variables)
            if sorted_variables[0][1]==sorted_variables[1][1]==sorted_variables[2][1]==sorted_variables[3][1]:
                if Gender=="남성":
                    Pcategory="근력"
                elif Gender=="여성":
                    Pcategory="면역력"
            elif sorted_variables[1][1]==sorted_variables[2][1]==sorted_variables[3][1]:
                Pcategory=sorted_variables[0][0]      
            else:        
                if sorted_variables[0][1]==sorted_variables[1][1]==sorted_variables[2][1] or sorted_variables[1][1]==sorted_variables[2][1]:
                    subset=[sorted_variables[0][0],sorted_variables[1][0],sorted_variables[2][0]]
                else:     
                    subset=[sorted_variables[0][0],sorted_variables[1][0]]

                if '항산화' in subset:
                    Pcategory="항산화"
                else:
                    if sorted_variables[0][1]==sorted_variables[1][1]==sorted_variables[2][1]:
                        Pcategory=random.choice(sorted_variables[0:3])[0]
                    elif sorted_variables[0][1]==sorted_variables[1][1]: 
                        Pcategory=random.choice(sorted_variables[0:2])[0]    
                    else: 
                        Pcategory=sorted_variables[0][0]    
        print (Pcategory)
    return Pcategory

# 식재료 이미지 세팅함수
def set_ingre_image(Pcat):
    img_list=[None]*3
    if Pcat =="활력":
        base=0
        for i in range(0,3):
            img_list[i]='I'+str(random.choice([1+base,2+base]))+'.png'
            base=2*(i+1)

    elif Pcat =="항산화":
        base=0
        for i in range(0,3):
            img_list[i]='I'+str(random.choice([7+base,8+base]))+'.png'
            base=2*(i+1)  

    elif Pcat =="면역력":    #07.09 5시 수정
        base=0
        for i in range(0,2):
            img_list[i]='I'+str(random.choice([13+base,14+base]))+'.png'
            base=2*(i+1)  

    elif Pcat =="근력":     #07.09 5시 수정
        base=0
        for i in range(0,2):
            img_list[i]='I'+str(random.choice([17+base,18+base]))+'.png'
            base=2*(i+1)

    return img_list

# 반찬 유형구분 함수
def set_sidedish_cat(Nutri,NutriD):
    if Nutri.EatScore==0:
        Scategory='A'
    else:    
        Achecklist=[]
        Bchecklist=[]
        Cchecklist=[]
        Dchecklist=[]

        if Nutri.Carb=="과다":
            Achecklist.append(100-(abs(NutriD.CarbV-NutriD.CarbH)/NutriD.CarbH*100))

        if Nutri.Protein=="부족":
            Bchecklist.append(100-(abs(NutriD.ProteinV-NutriD.ProteinL)/NutriD.ProteinL*100))

        if Nutri.Fat=="과다":
            Dchecklist.append(100-(abs(NutriD.FatV-NutriD.FatH)/NutriD.FatH*100))    

        if Nutri.Fiber=="부족":
            Achecklist.append(100-(abs(NutriD.FiberV-NutriD.FiberL)/NutriD.FiberL*100))    

        if Nutri.Sodium=="과다":
            Cchecklist.append(100-(abs(NutriD.SodiumV-NutriD.SodiumH)/NutriD.SodiumH*100)) 

        if Nutri.Sugar=="과다":
            Achecklist.append(100-(abs(NutriD.SugarV-NutriD.SugarH)/NutriD.SugarH*100))     

        if Nutri.SatFat=="과다":
            Dchecklist.append(100-(abs(NutriD.SatFatV-NutriD.SatFatH)/NutriD.SatFatH*100))  

        if Nutri.Cholesterol=="과다":
            Dchecklist.append(100-(abs(NutriD.CholesterolV-NutriD.CholesterolH)/NutriD.CholesterolH*100)) 

        if not Achecklist: 
            Ascore=100
        else:
            Asum=0
            for Alist in Achecklist:
                Asum+=Alist 
            Ascore=Asum/len(Achecklist)

        if not Bchecklist:
            Bscore=100
        else:
            Bscore=Bchecklist[0]    

        if not Cchecklist:
            Cscore=100
        else:
            Cscore=Cchecklist[0]       

        if not Dchecklist: 
            Dscore=100
        else:
            Dsum=0
            for Dlist in Dchecklist:
                Dsum+=Dlist 
            Dscore=Dsum/len(Dchecklist)   

        scorelist=[('A',Ascore),('B',Bscore),('C',Cscore),('D',Dscore)]      
        Scategory = min(scorelist, key=lambda x: x[1])[0]         
    return Scategory    

# 반찬 이미지 세팅 함수
def set_sidedish_image(recomcal,Scat):
    img_list=[None]*3

    if Scat=="A":
        if recomcal<=1500:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([1+base,2+base]))+'.png'
                base=2*(i+1)
        elif 1500<recomcal<=2000:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([7+base,8+base]))+'.png'
                base=2*(i+1)
        elif 2000<recomcal<=2500:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([13+base,14+base]))+'.png'
                base=2*(i+1) 
        elif 2500<recomcal<=3000:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([19+base,20+base]))+'.png'
                base=2*(i+1)
        elif 3000<recomcal:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([25+base,26+base]))+'.png'
                base=2*(i+1)  

    if Scat=="B":
        if recomcal<=1500:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([31+base,32+base]))+'.png'
                base=2*(i+1)
        elif 1500<recomcal<=2000:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([37+base,38+base]))+'.png'
                base=2*(i+1)
        elif 2000<recomcal<=2500:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([43+base,44+base]))+'.png'
                base=2*(i+1) 
        elif 2500<recomcal<=3000:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([49+base,50+base]))+'.png'
                base=2*(i+1)
        elif 3000<recomcal:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([55+base,56+base]))+'.png'
                base=2*(i+1)   

    if Scat=="C":
        if recomcal<=1500:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([61+base,62+base]))+'.png'
                base=2*(i+1)
        elif 1500<recomcal<=2000:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([67+base,68+base]))+'.png'
                base=2*(i+1)
        elif 2000<recomcal<=2500:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([73+base,74+base]))+'.png'
                base=2*(i+1) 
        elif 2500<recomcal<=3000:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([79+base,80+base]))+'.png'
                base=2*(i+1)
        elif 3000<recomcal:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([85+base,86+base]))+'.png'
                base=2*(i+1) 

    if Scat=="D":
        if recomcal<=1500:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([91+base,92+base]))+'.png'
                base=2*(i+1)
        elif 1500<recomcal<=2000:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([97+base,98+base]))+'.png'
                base=2*(i+1)
        elif 2000<recomcal<=2500:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([103+base,104+base]))+'.png'
                base=2*(i+1) 
        elif 2500<recomcal<=3000:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([109+base,110+base]))+'.png'
                base=2*(i+1)
        elif 3000<recomcal:
            base=0
            for i in range (0,3):
                img_list[i]='case'+str(random.choice([115+base,116+base]))+'.png'
                base=2*(i+1)                                                     
                        
    return img_list

# PDF 파일 생성
def create_basic_pdf(Nutrition,Vitastiq,Inbody,Agesensor,Name,Gender,NutriD,Supple,Store,Activity,Age,InbodyCat):
    filename=resultfilepath+'Basic_Health_Report.pdf'
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    print("width : "+str(width))
    print("height : "+str(height))
    register_fonts()
    
    # 제목1 추가 (한글) - 페이지 가운데에 배치
    # FS용 분기 생성(24.12.12)
    if Store=="FS":
        draw_centered_string(c, "영양상담 결과 리포트", height - 67, boldfont, 23, width)
    else:
        draw_centered_string(c, "Greating store healthcare", height - 40, mainfont, 12, width)
        draw_centered_string(c, "맞춤영양 프로그램 결과차트", height - 70, boldfont, 20, width) #07.09 5시 수정
        
    # 선 그리기 (x1, y1, x2, y2)
    c.setLineWidth(0.7)  # 라인의 굵기 설정
    c.setStrokeColorRGB(0.75, 0.75, 0.75)  # 라인의 색상 설정
    c.line(450, height - 100, 550, height - 100)
    c.line(33, height - 98, 97, height - 98)
    
    # 내담자명
    c.drawImage(filepath+'user.png',455,height-100,20,20,mask='auto')

    username= Name+"님"
    c.setFont(boldfont, 13)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(485,height-95,username)
    c.setFont(boldfont, 11)
    c.drawString(35,height-95,str(date.today().strftime("%Y.%m.%d")))
    
    # 사각형 그리기 (x, y, width, height)
    c.roundRect(20,height-430, 265+5, 310,15)
    c.roundRect(300,height-430, 265+5, 310,15)
    c.roundRect(20,height-625, 545+5, 185,15)
    # FS용 분기 생성(24.12.12)
    if Store=="FS":
        c.roundRect(20,height-820-10, 545+5, 185+10,15)
    else:    
        c.roundRect(20,height-820-10, 265+5, 185+10,15)
        c.roundRect(300,height-820-10, 265+5, 185+10,15)
    

    #-------------- part1 그리팅 헬스 스코어 --------------

    # 본문 채우기 
    c.setFont(boldfont, 12)
    c.setFillColorRGB(0, 0, 0)
    
    # 점수 계산
    vitascore=100
    for field in fields(Vitastiq):
        field_name = field.name
        field_value = getattr(Vitastiq, field_name)
        if field_value=="낮음":
            vitascore=vitascore-10
        if field_value=="경미":         #07.09 7시 수정
            vitascore=vitascore-5

    if Nutrition.EatScore==0:
        EatS="   -"
    else:
        EatS=str(Nutrition.EatScore)+"점"
        
    if Vitastiq.Unused==True:
        VitaS="   -"
    else:    
        VitaS=str(vitascore)+"점"

    if Inbody.InbodyScore==0:
        InboS="   -"
    else:
        InboS=str(Inbody.InbodyScore)+"점"

    # FS용 분기 생성(24.12.12)    
    if Store=="FS":
        pass
    else:
        if Agesensor.Rank==0:
            AgeS="   -"
        else:
            AgeS=str(100-Agesensor.Rank)+"점"

    # FS용 분기 생성(24.12.12)
    if Store=="FS":
        TotalScore=round(float(Nutrition.EatScore+vitascore+Inbody.InbodyScore)/3,1)
    else:    
        TotalScore=round(float(Nutrition.EatScore+vitascore+Inbody.InbodyScore+100-Agesensor.Rank)/4,1)
    
    print("Total Score : "+str(TotalScore))

    # FS용 분기 생성(25.01.07)
    # 점수표현
    if Store=="FS":
        if Nutrition.EatScore==0 or Inbody.InbodyScore==0 or Vitastiq.Unused==True:
            c.drawImage(filepath+"TotalBlur.png", 30, height - 400, 144,230,mask='auto')
        else:     
            draw_score_string(c,height,TotalScore)
            draw_part1_graph(c,height,TotalScore)    
    else:        
        if Nutrition.EatScore==0 or Inbody.InbodyScore==0 or Agesensor.Rank==0 or Vitastiq.Unused==True:
            c.drawImage(filepath+"TotalBlur.png", 30, height - 400, 144,230,mask='auto')
        else:     
            draw_score_string(c,height,TotalScore)
            draw_part1_graph(c,height,TotalScore)

    # FS용 분기 생성(24.12.12)
    if Store=="FS":
        c.setFont(boldfont, 12)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(35,height-140,"헬스 스코어")
        c.setFont(mainfont, 10)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-160,"•3가지 항목의 종합적인 점수에요.")

        # 4가지 점수표현 칸
        c.drawImage(filepath+"score.png", 185, height - 260-10, 80,45,mask='auto')
        c.drawImage(filepath+"score.png", 185, height - 315-10, 80,45,mask='auto')
        c.drawImage(filepath+"score.png", 185, height - 370-10, 80,45,mask='auto')

        c.setFont(mainfont, 10)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(213,height-251-10,EatS)
        c.drawString(213,height-307-10,VitaS)
        c.drawString(213,height-362-10,InboS)

        c.setFont(mainfont, 9)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(195,height-231-10,"영양 섭취 상태")
        c.drawString(196,height-286-10,"비타민/무기질")
        c.drawString(210,height-341-10,"인바디")

    else:    
        c.setFont(boldfont, 12)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(35,height-140,"그리팅 헬스 스코어")

        c.setFont(mainfont, 10)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-160,"•4가지 항목의 종합적인 점수에요.")

        # 4가지 점수표현 칸
        c.drawImage(filepath+"score.png", 185, height - 240, 80,45,mask='auto')
        c.drawImage(filepath+"score.png", 185, height - 295, 80,45,mask='auto')
        c.drawImage(filepath+"score.png", 185, height - 350, 80,45,mask='auto')
        c.drawImage(filepath+"score.png", 185, height - 405, 80,45,mask='auto')

        c.setFont(mainfont, 10)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(213,height-231,EatS)
        c.drawString(213,height-287,VitaS)
        c.drawString(213,height-342,InboS)
        c.drawString(213,height-396,AgeS)

        c.setFont(mainfont, 9)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(195,height-211,"영양 섭취 상태")
        c.drawString(196,height-266,"비타민/무기질")
        c.drawString(210,height-321,"인바디")
        c.drawString(198,height-376,"AGEs sensor")

    # 가운데 라인
    c.setDash([3, 2], 0)  # 대시 패턴 설정: 길이 3의 대시와 길이 2의 공백을 반복
    c.line(170, height - 195, 170, height - 405)  # (100, height-100)에서 시작하여 (400, height-100)까지 선 그리기
    c.setDash(1,0) # 대시 패턴 없애기

    #-------------- part2 한 눈에 보는 나의 식습관 --------------
    # 본문 채우기 
    if Nutrition.EatScore==0 :
        c.drawImage(filepath+"NutriBlur.png", 310, height - 400, 250,232,mask='auto')
    else:    
        c.setFillColorRGB(0, 0, 0)
        c.setFont(boldfont, 12)
        c.drawString(315,height-140,"한 눈에 보는 나의 식습관")
        draw_part2(c,Nutrition,height)

    #-------------- part3 비타민/무기질 --------------
    # 본문 채우기 
    if Vitastiq.Unused==True:
        c.drawImage(filepath+"VitaBlur.png", 30, height - 615, 530,143,mask='auto')
    else:    
        c.setFillColorRGB(0, 0, 0)
        c.setFont(boldfont, 12)
        c.drawString(35,height-460,"비타민/무기질")
        c.drawImage(filepath+"Vit_Min.png",30,height-610,530,130,mask='auto')

        c.drawImage(filepath+"Star_red.png",375,height-468,20,20,mask='auto')
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.setFont(mainfont, 10)
        c.drawString(400,height-462,"체내 영양소가 낮은 경향으로 보여요.")

        """c.drawImage(filepath+"Star_blue.png",355,height-468,20,20,mask='auto')
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.setFont('AppleGothic', 10)
        c.drawString(378,height-462,"체내 영양소가 적정한 경향으로 보여요.")"""

        draw_star(c,Vitastiq,height)

    #-------------- part4 인바디 --------------
    # 본문 채우기 
    if Inbody.InbodyScore==0 and Inbody.Weight==0 and Inbody.BodyFat==0 :
        c.drawImage(filepath+"InbodyBlur.png", 30, height - 810, 250,157,mask='auto')
    else:    
        c.setFillColorRGB(0, 0, 0)
        c.setFont(boldfont, 12)
        # FS용 분기 생성(24.12.12)
        if Store=="FS":
            c.drawString(35,height-655,"신체계측")
        else:    
            c.drawString(35,height-655,"인바디")

        if Store=="판교점":
            Inbody_cat=set_category_small(Inbody,Nutrition.UserHeight,Gender)
        # FS용 분기 생성(24.12.12)    
        elif Store=="FS":
            Inbody_cat=set_category_fs(InbodyCat)    
        else:    
            Inbody_cat=set_category(Inbody)
        print("Inbody_cat"+Inbody_cat)
        write_comment(c,Inbody_cat,height)

        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(37,height-705,'체중')
        # FS용 분기 생성(24.12.12)
        if Store=="판교점":
            c.drawString(37,height-735,'제지방량')
        elif Store=="FS":
            c.drawString(37,height-735,'제지방량')
        else:    
            c.drawString(37,height-735,'골격근량')
        c.drawString(37,height-765,'체지방량')

        # FS용 분기 생성(24.12.12)
        if Store=="판교점":
            draw_inbody_small(c,Inbody,Nutrition.UserHeight,Gender,height)
        elif Store=="FS":
            draw_inbody_home(c,height,Inbody_cat,Inbody)
        else:    
            draw_inbody(c,Inbody,height)
        draw_alpha(c,Inbody_cat,height)

    #-------------- part5 Age sensor or Inbody --------------
    # FS용 분기 생성(24.12.12)
    if Store=="FS":
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(313,height-655-14,'기초대사량')
        c.drawString(313,height-675-15,'체지방률')
        c.drawString(313,height-705-10,'골격근량')
        c.drawString(313,height-735-5,'복부지방률')
        c.drawString(313,height-765,'내장지방레벨')
        c.drawString(370,height-655-14,str(format(Inbody.BMR,','))+"kcal") 

        draw_inbody_small_adddetail(c,Inbody,Nutrition.UserHeight,Gender,height)
        
        c.setFillColorRGB(0.97, 0.97, 0.97)
        c.roundRect(315,height-823,230,40,5,fill=1)
        c.setFont(mainfont, 8)
        c.setFillColorRGB(0, 0, 0)
        c.drawString(326,height-795,'※ 제지방량이란?')
        c.setFont(mainfont, 7)
        c.drawString(328,height-806,'체중에서 체지방량을 뺀 뼈,근육,장기 등의 무게로 근육량에 영향을')
        c.drawString(328,height-816,'많이 받으며 체지방량이 증가하면 기초대사량도 함께 증가')

        c.setStrokeColorRGB(200/255,200/255,200/255)
        c.setLineWidth(0.7)
        c.setDash([3, 2], 0)  # 대시 패턴 설정: 길이 3의 대시와 길이 2의 공백을 반복
        c.line(290, height - 660, 290, height - 820)
        c.setDash(1,0) # 대시 패턴 없애기


    else:
        if Agesensor.Rating=="" or Agesensor.Rank==0:
            c.drawImage(filepath+"AGEsBlur.png", 310, height - 810, 250,157,mask='auto')
        else:    
            c.setFillColorRGB(0, 0, 0)
            c.setFont(boldfont, 12)
            c.drawString(315,height-655,"AGEs sensor")
        
            draw_panel(c,Agesensor,height)
    
    #-------------- 페이지 저장 및 이미지 변환 --------------

    # 1페이지 저장
    c.showPage()
    #---------------------------------------- 상품추천 페이지 제작 -------------------------------------------

    # 선 그리기 (x1, y1, x2, y2)
    c.setLineWidth(0.7)  # 라인의 굵기 설정
    c.setStrokeColorRGB(0.7, 0.7, 0.7)  # 라인의 색상 설정
    c.line(10, height - 40, 580, height - 40)
    c.line(10, height - 265-25, 580, height - 265-25)
    c.line(10, height - 530, 580, height - 525)

    c.drawImage(filepath+'Rectangle 11.png',15,height-830,184,290,mask='auto')
    
    c.setFillColorRGB(0,0,0)
    draw_centered_string(c,Name+"님 맞춤상품 솔루션",height-30,boldfont,18,width)

    c.setFont(boldfont, 18)
    c.setFillColorRGB(0,0,0)
    c.drawString(25,height-35-30,"식재료")
    c.drawString(25,height-295-25,"반찬")
    c.drawString(55,height-565,"영양제")
    c.drawString(206,height-570,"착즙 주스")
    c.drawString(360,height-570,"상품")

    # 유형결정 및 식재료 추천
    Pcat=set_product_cat(Gender,Vitastiq,Agesensor)
    Pimg_list=set_ingre_image(Pcat)
    print(Pimg_list)
    if Pimg_list[2]!=None:
        c.drawImage(filepath+Pimg_list[0],30,height-250-30,158,175,mask='auto')
        c.drawImage(filepath+Pimg_list[1],215,height-250-30,158,175,mask='auto')
        c.drawImage(filepath+Pimg_list[2],400,height-250-30,158,175,mask='auto')

        c.setFillColorRGB(191/255,191/255,191/255)
        c.setStrokeColorRGB(191/255,191/255,191/255)
        c.roundRect(300,height-63-30,70,20,10,fill=True)
        c.roundRect(380,height-63-30,70,20,10,fill=True)
        c.roundRect(460,height-63-30,70,20,10,fill=True)

    elif Pimg_list[2]==None:
        c.drawImage(filepath+Pimg_list[0],30,height-250-30,158,175,mask='auto')
        c.drawImage(filepath+Pimg_list[1],215,height-250-30,158,175,mask='auto')

        c.setFillColorRGB(191/255,191/255,191/255)
        c.setStrokeColorRGB(191/255,191/255,191/255)
        c.roundRect(300,height-63-30,70,20,10,fill=True)
        c.roundRect(380,height-63-30,70,20,10,fill=True)

    c.setFillColorRGB(1,1,1)
    c.setFont(boldfont, 11)
    if Pcat=="활력":
        c.drawString(315,height-57-30,"#비오틴")
        c.drawString(390,height-57-30,"#비타민B1")
        c.drawString(469,height-57-30,"#비타민B2")

    if Pcat=="항산화":
        c.drawString(311,height-57-30,"#비타민C")
        c.drawString(394,height-57-30,"#비타민E")
        c.drawString(476,height-57-30,"#셀레늄")  

    if Pcat=="면역력":
        c.drawString(319,height-57-30," #아연")
        c.drawString(399,height-57-30," #엽산")   

    if Pcat=="근력":
        c.drawString(310,height-57-30,"#마그네슘")
        c.drawString(389,height-57-30,"#비타민B6")       

    # 반찬 추천 유형결정 및 반찬 추천
    Scat=set_sidedish_cat(Nutrition,NutriD)
    if Store=="판교점":
        if 19<=Age and Gender=="남성":
            if Activity=="비활동적":
                actLevel=1
            elif Activity=="저활동적":
                actLevel=1.11
            elif Activity=="활동적":
                actLevel=1.25
            elif Activity=="매우 활동적":
                actLevel=1.48            
            Recomcal=662+(-9.53*Age)+actLevel*((15.91*Inbody.Weight)+(539.6*Nutrition.UserHeight/100))
        elif 19<=Age and Gender=="여성":
            if Activity=="비활동적":
                actLevel=1
            elif Activity=="저활동적":
                actLevel=1.12
            elif Activity=="활동적":
                actLevel=1.27
            elif Activity=="매우 활동적":
                actLevel=1.45
            Recomcal=354+(-6.91*Age)+actLevel*((9.36*Inbody.Weight)+(726*Nutrition.UserHeight/100))
        elif 1<=Age<19 and Gender=="남성":
            if Activity=="비활동적":
                actLevel=1
            elif Activity=="저활동적":
                actLevel=1.13
            elif Activity=="활동적":
                actLevel=1.26
            elif Activity=="매우 활동적":
                actLevel=1.42
            Recomcal=88.5+(-61.91*Age)+actLevel*((26.7*Inbody.Weight)+(903*Nutrition.UserHeight/100))       
        elif 1<=Age<19 and Gender=="여성":
            if Activity=="비활동적":
                actLevel=1
            elif Activity=="저활동적":
                actLevel=1.16
            elif Activity=="활동적":
                actLevel=1.31
            elif Activity=="매우 활동적":
                actLevel=1.56
            Recomcal=135.3+(-30.8*Age)+actLevel*((10.0*Inbody.Weight)+(934*Nutrition.UserHeight/100))

        Simg_list=set_sidedish_image(Recomcal,Scat)
    else :     
        Simg_list=set_sidedish_image(Inbody.Recomcal,Scat) 
    
    c.drawImage(filepath+Simg_list[0],30,height-510-5,150,154,mask='auto')
    c.drawImage(filepath+Simg_list[1],215,height-510-5,150,154,mask='auto')
    c.drawImage(filepath+Simg_list[2],400,height-510-5,150,154,mask='auto')

    c.setFillColorRGB(255/255,239/255,225/255)
    c.setStrokeColorRGB(255/255,239/255,225/255)
    c.roundRect(467,height-322-25,80,20,10,fill=True)

    c.setFont(boldfont, 10)
    c.setFillColorRGB(0,0,0)
    c.drawString(482,height-315.5-25,"메인 식재료")

    # 케이스에 따른 코멘트 작성
    c.setFont(mainfont, 12)
    c.setFillColorRGB(0.2,0.2,0.2)
    c.drawString(25,height-58-30,'"나에게 부족한 영양소를 채워주는 맞춤 식재료"')

    if Scat=="A":
        c.drawString(25,height-318-25,'"저당/고식이섬유 맞춤 반찬으로 구성하는 집밥"')
        c.drawString(360,height-595,"나에게 맞는 저당/고식이섬유 건강상품")
    elif Scat=="B":
        c.drawString(25,height-318-25,'"단백질이 풍부한 맞춤 반찬으로 구성하는 집밥"')
        c.drawString(360,height-595,"나에게 부족한 단백질을 채워줄 건강상품")    
    elif Scat=="C":
        c.drawString(25,height-318-25,'"저나트륨 맞춤 반찬으로 구성하는 집밥"')
        c.drawString(360,height-595,"나에게 맞는 저나트륨 건강상품")  
    elif Scat=="D":
        c.drawString(25,height-318-25,'"저지방 맞춤 반찬으로 구성하는 집밥"')
        c.drawString(360,height-595,"나에게 맞는 저지방 건강상품")   
         
    c.drawString(206,height-595,Pcat+'에 좋은 영양소 가득') 

#07.09 수정--------------------------------------------------------------------------------------------
    # 맞춤 영양제 내용
    c.setFont(boldfont,8)
    c.setFillColorRGB(0,0,0)
    c.drawString(27,height-632,"▷ 건강 관심사 영양제 추천")

    c.setFont(mainfont,8)
    c.setFillColorRGB(0,0,0)
    c.drawString(27,height-630-20,"영양제 1")
    c.drawString(27,height-630-40,"영양제 2")
    c.drawString(27,height-630-60,"영양제 3")
    c.drawString(27,height-630-80,"영양제 4")
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawRightString(189,height-630-20,"#기능성 1")
    c.drawRightString(189,height-630-40,"#기능성 2")
    c.drawRightString(189,height-630-60,"#기능성 3")
    c.drawRightString(189,height-630-80,"#종합")

    c.setFont(boldfont,8)
    c.setFillColorRGB(0,0,0)
    c.drawString(27,height-732,"▷ 나에게 부족한 영양제 추천")

    c.setFont(mainfont,8)
    c.setFillColorRGB(0,0,0)
    if Pcat=="활력":
        biotinlist=["닥터트루 프리미엄 유기농 비오틴","프롬바이오 비오틴","바이너랩 마이 비오틴"]
        totallist=["솔가 멀티비타민"]
        c.drawString(27,height-730-20,"﹒"+random.choice(biotinlist))
        c.drawString(27,height-730-40,"﹒"+"프롬바이오 비타민B")
        c.drawString(27,height-730-60,"﹒"+"모비타 리버칸 릴렉스")
        c.drawString(27,height-730-80,"﹒"+random.choice(totallist))
        c.setFillColorRGB(0.5,0.5,0.5)
        c.drawRightString(189,height-730-20,"#비오틴")
        c.drawRightString(189,height-730-40,"#비타민 B1")
        c.drawRightString(189,height-730-60,"#비타민 B2")
        c.drawRightString(189,height-730-80,"#종합")

    elif Pcat=="근력":
        mglist=["퓨리탄 프라이드 마그네슘 500","닥터라인 마그네슘","닥터트루 프리미엄 마그네슘","엔바이탈 마그네슘 비타민B6 Ease"]   #07.09 7시 수정
        totallist=["솔가 멀티비타민"]
        c.drawString(27,height-730-20,"﹒"+random.choice(mglist))
        c.drawString(27,height-730-40,"﹒"+"엔바이탈 마그네슘 Vit B6 Ease")
        c.drawString(27,height-730-60,"﹒"+random.choice(totallist)) 
        c.setFillColorRGB(0.5,0.5,0.5)
        c.drawRightString(189,height-730-20,"#마그네슘")
        c.drawRightString(189,height-730-40,"#비타민 B6")
        c.drawRightString(189,height-730-60,"#종합")
        
    elif Pcat=="면역력":
        folatelist=["닥터트루 프리미엄 유기농 엽산 800","프롬바이오 활성 엽산"]
        totallist=["솔가 멀티비타민"]
        znlist=["퓨리탄프라이드 아연구미","닥터라인 셀렌+징크"]
        c.drawString(27,height-730-20,"﹒"+random.choice(folatelist))
        c.drawString(27,height-730-40,"﹒"+random.choice(znlist)) 
        c.drawString(27,height-730-60,"﹒"+random.choice(totallist)) 
        c.setFillColorRGB(0.5,0.5,0.5)
        c.drawRightString(189,height-730-20,"#엽산")
        c.drawRightString(189,height-730-40,"#아연")
        c.drawRightString(189,height-730-60,"#종합")

    elif Pcat=="항산화":
        totallist=["솔가 멀티비타민"]
        clist=["프롬바이오 비타민C 1000","비타바움 퓨어비타민C250","탑헬스 리포조미아 비타민C","솔가 에스터-C 비타민 1000"]
        selist=["솔가 셀레늄","닥터라인 셀렌 징크"]
        c.drawString(27,height-730-20,"﹒"+random.choice(clist))
        c.drawString(27,height-730-40,"﹒"+random.choice(selist))
        c.drawString(27,height-730-60,"﹒오리진 프리미엄 비타민 E 400IU")
        c.drawString(27,height-730-80,"﹒"+random.choice(totallist)) 
        c.setFillColorRGB(0.5,0.5,0.5)
        c.drawRightString(189,height-730-20,"#비타민C")
        c.drawRightString(189,height-730-40,"#셀레늄")
        c.drawRightString(189,height-730-60,"#비타민E")
        c.drawRightString(189,height-730-80,"#종합")          

    c.line(25, height - 620, 183, height - 620)
    c.line(25, height - 720, 183, height - 720)

    c.setFillColorRGB(191/255,191/255,191/255)
    c.setStrokeColorRGB(191/255,191/255,191/255)
    c.roundRect(25,height-595,70,16,8,fill=True)
    c.roundRect(105,height-595,70,16,8,fill=True)
    c.roundRect(25,height-615,70,16,8,fill=True)
    c.roundRect(105,height-615,70,16,8,fill=True)

    c.setFont(boldfont,8)
    c.setFillColorRGB(1,1,1)
    c.drawString(35,height-590,"#관심사1")
    c.drawString(115,height-590,"#관심사2")
    c.drawString(35,height-610,"#관심사3")
    c.drawString(115,height-610,"#"+Pcat)
#07.09 수정--------------------------------------------------------------------------------------------    


    # 케이스별 주스 추천 및 해시태그
    c.setFillColorRGB(191/255,191/255,191/255)
    c.setStrokeColorRGB(191/255,191/255,191/255)
    c.roundRect(290,height-573,55,16,8,fill=True)

    c.setFillColorRGB(1,1,1)
    c.setFont(boldfont, 10)

    if Pcat=="활력":
        c.drawImage(filepath+'BJ1.png',206,height-820,138,210,mask='auto')
        c.drawString(304,height-567.7,"#"+Pcat)
    if Pcat=="항산화":
        c.drawImage(filepath+'BJ2.png',206,height-820,138,210,mask='auto')
        c.drawString(299,height-567.7,"#"+Pcat)
    if Pcat=="면역력":
        c.drawImage(filepath+'BJ3.png',206,height-820,138,210,mask='auto')
        c.drawString(299,height-567.7,"#"+Pcat)
    if Pcat=="근력":
        c.drawImage(filepath+'BJ4.png',206,height-820,138,210,mask='auto')  
        c.drawString(304,height-567.7,"#"+Pcat)

    # 케이스별 상품추천 및 해시태그
    c.setFillColorRGB(191/255,191/255,191/255)
    c.setStrokeColorRGB(191/255,191/255,191/255)
    c.setFont(boldfont, 10)

    if Scat=="A":
        c.drawImage(filepath+'BPS'+str(random.randint(1,5))+'.png',360,height-715,223,106,mask='auto')
        c.drawImage(filepath+'BPD'+str(random.randint(1,5))+'.png',360,height-820,223,106,mask='auto')
        c.roundRect(445,height-573,45,16,8,fill=True)
        c.roundRect(495,height-573,70,16,8,fill=True)

        c.setFillColorRGB(1,1,1)
        c.drawString(455,height-568.7,"#저당")
        c.drawString(503,height-568.7,"#고식이섬유")

    elif Scat=="B":
        c.drawImage(filepath+'BPS'+str(random.randint(6,10))+'.png',360,height-715,223,106,mask='auto')
        c.drawImage(filepath+'BPD'+str(random.randint(6,10))+'.png',360,height-820,223,106,mask='auto')
        c.roundRect(445,height-573,60,16,8,fill=True)
    
        c.setFillColorRGB(1,1,1)
        c.drawString(456,height-568.7,"#고단백")

    elif Scat=="C":
        c.drawImage(filepath+'BPS'+str(random.randint(10,15))+'.png',360,height-715,223,106,mask='auto')
        c.drawImage(filepath+'BPD'+str(random.randint(10,15))+'.png',360,height-820,223,106,mask='auto')
        c.roundRect(445,height-573,60,16,8,fill=True)

        c.setFillColorRGB(1,1,1)
        c.drawString(452,height-568.7,"#저나트륨")

    elif Scat=="D": 
        c.drawImage(filepath+'BPS'+str(random.randint(16,20))+'.png',360,height-715,223,106,mask='auto')   
        c.drawImage(filepath+'BPD'+str(random.randint(16,20))+'.png',360,height-820,223,106,mask='auto')
        c.roundRect(445,height-573,45,16,8,fill=True)
        c.roundRect(495,height-573,70,16,8,fill=True)

        c.setFillColorRGB(1,1,1)
        c.drawString(450,height-568.7,"#저지방")
        c.drawString(503,height-568.7,"#고식이섬유")       

    c.setStrokeColorRGB(0.6,0.6,0.6)
    c.setLineWidth(0.2)
    c.roundRect(206,height-820,138,210,10)
    c.roundRect(360,height-820,223,210,10)                           

    
    # 2페이지 저장
    c.showPage()        

    c.save()

    # PDF를 이미지로 변환
    images = convert_from_path(filename)
    # 첫 번째 페이지를 이미지로 저장
    img_path = resultfilepath+"Basic_Health_Report.png"
    images[0].save(img_path, "PNG")

    return img_path 


# PDF 생성 테스트용
if __name__ == "__main__":
    Nutri=Nutrition(EatScore=70, Carb="과다", Protein="과다", Fat="과다", Fiber="적정", Sodium="과다", Sugar="과다", SatFat="과다", Cholesterol="과다",UserHeight=159)
    Vita=Vitastiq(Unused=False,Biotin="", VitC="낮음", Mg="", VitB1="낮음", VitB2="", Zn="낮음", Se="", VitB6="", VitE="", Folate="")
    Inbo=Inbody(InbodyScore=78,Weight=48,BodyFat=10.8,FatFree=0,ApproWeight=0,WeightMax=0,MuscleMax=0,FatMax=0,Recomcal=0,SkeletalMuscle=18.3,BodyFatRatio=23.9,WaistHipRatio=79,VisceralFatLevel=4,BMR=1114)
    Age=Agesensor(Rating="B",Rank=34)
    NutriD=NutritionDetail(CarbH=324.3,CarbV=74.9,ProteinL=34.9,ProteinV=19,FatH=66.5,FatV=22.6,FiberL=23.9,FiberV=8,SodiumH=2300,SodiumV=774,SugarH=50,SugarV=20.6,SatFatH=15.5,SatFatV=3.7,CholesterolH=300,CholesterolV=78)
    Supple=Supplements(sup1="추천 영양제 1번",sup2="추천 영양제 2번",sup3="추천 영양제 3번",sup4="추천 영양제 4번",inter1="근력",inter2="소화기/장건강",inter3="면역력")
    create_basic_pdf(Nutri,Vita,Inbo,Age,"김건강","여성",NutriD,Supple,"FS","활동적",24,'표준체중 허약형')