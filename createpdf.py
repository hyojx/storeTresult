from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from dataclass import Nutrition,Vitastiq,Inbody,Agesensor
from PIL import Image
from pdf2image import convert_from_path
from reportlab.lib.colors import Color
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle
from dataclasses import fields

filepath="image/"

# 폰트 등록 함수
def register_fonts():
    # macOS의 산돌고딕 네오 폰트 경로
    font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
    pdfmetrics.registerFont(TTFont('AppleGothic', font_path))

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
    c.setFont('AppleGothic', 8)
    text_width = pdfmetrics.stringWidth("20점 ", 'AppleGothic', 8)
    c.drawString(baseX-3-text_width,height-baseY+(bet*2.6),"20점 ")

    text_width = pdfmetrics.stringWidth("40점 ", 'AppleGothic', 8)
    c.drawString(baseX-6-text_width,height-baseY+(bet*5.6),"40점 ")

    text_width = pdfmetrics.stringWidth("60점 ", 'AppleGothic', 8)
    c.drawString(baseX-9-text_width,height-baseY+(bet*8.6),"60점 ")

    text_width = pdfmetrics.stringWidth("40점 ", 'AppleGothic', 8)
    c.drawString(baseX-12-text_width,height-baseY+(bet*11.6),"80점 ")

    c.setFont('AppleGothic',10)

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
        c.setFont('AppleGothic', 16)
        c.setFillColorRGB(243/255,58/255,12/255) #RED color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,'AppleGothic', 14)

        c.setFont('AppleGothic', 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")

    if 20<score<=40:
        c.setFont('AppleGothic', 16)
        c.setFillColorRGB(1,120/255,2/255) #ORENGE color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,'AppleGothic', 14)

        c.setFont('AppleGothic', 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")

    if 40<score<=60:
        c.setFont('AppleGothic', 16)
        c.setFillColorRGB(1,206/255,21/255) #YELLOW color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,'AppleGothic', 14)

        c.setFont('AppleGothic', 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")        

    if 60<score<=80:
        c.setFont('AppleGothic', 16)
        c.setFillColorRGB(133/255,205/255,1/255) #GREEN color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,'AppleGothic', 14)

        c.setFont('AppleGothic', 12)
        c.setFillColorRGB(0.5, 0.5, 0.5) #gray color
        c.drawString(50+text_width,height-200,"/ 100점")    

    if 80<score<=100:
        c.setFont('AppleGothic', 16)
        c.setFillColorRGB(46/255,117/255,182/255) #BLUE color
        score_t=str(score)+"점 "
        c.drawString(45,height-200,score_t)
        text_width = pdfmetrics.stringWidth(score_t,'AppleGothic', 14)

        c.setFont('AppleGothic', 12)
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

# 별 그리기
def draw_star(c,Vitastiq,height):
    star_size=18
    baseX=105
    baseY=height-502
    bet=107

    if Vitastiq.Mg=="낮은"or Vitastiq.Mg=="경미":
        c.drawImage(filepath+"Star_red.png", baseX, baseY, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX, baseY, star_size,star_size,mask='auto') 

    if Vitastiq.Biotin=="낮은" or Vitastiq.Biotin=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*1), baseY, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX+(bet*1), baseY, star_size,star_size,mask='auto')  

    if Vitastiq.Se=="낮은" or Vitastiq.Se=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*2), baseY, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX+(bet*2), baseY, star_size,star_size,mask='auto')

    if Vitastiq.VitB2=="낮은" or Vitastiq.VitB2=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*3), baseY, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX+(bet*3), baseY, star_size,star_size,mask='auto')  

    if Vitastiq.Folate=="낮은" or Vitastiq.Folate=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*4), baseY, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX+(bet*4), baseY, star_size,star_size,mask='auto')  

    if Vitastiq.Zn=="낮은" or Vitastiq.Zn=="경미":
        c.drawImage(filepath+"Star_red.png", baseX, baseY-68, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX, baseY-68, star_size,star_size,mask='auto')    

    if Vitastiq.VitC=="낮은" or Vitastiq.VitC=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*1), baseY-68, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX+(bet*1), baseY-68, star_size,star_size,mask='auto')  

    if Vitastiq.VitB1=="낮은" or Vitastiq.VitB1=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*2), baseY-68, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX+(bet*2), baseY-68, star_size,star_size,mask='auto')

    if Vitastiq.VitE=="낮은" or Vitastiq.VitE=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*3), baseY-68, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX+(bet*3), baseY-68, star_size,star_size,mask='auto')  

    if Vitastiq.VitB6=="낮은" or Vitastiq.VitB6=="경미":
        c.drawImage(filepath+"Star_red.png", baseX+(bet*4), baseY-68, star_size,star_size,mask='auto')
    else:
        c.drawImage(filepath+"Star_blue.png", baseX+(bet*4), baseY-68, star_size,star_size,mask='auto')             
             
    return

# 인바디 유형결정
def set_category(Inbody):
    C_id=""
    weightP=Inbody.Weight/(Inbody.Weight+Inbody.WeightControl)*100
    skeletalP=Inbody.FatFree/(Inbody.FatFree+Inbody.MuscleControl)*100
    fatP=Inbody.BodyFat/(Inbody.BodyFat+Inbody.FatControl)*100
    if 85 < weightP <115:
        if skeletalP <= 90 and 80<fatP <160:
            C_id="C_sw"
        elif skeletalP<= 110 and 160<=fatP:
            C_id="C_so"
        elif 110<=skeletalP and fatP<160:
            C_id="D_ss"
        elif 90<skeletalP<110 and 80<fatP<160:
            C_id="I_sh"
    if 115<=weightP:
        if skeletalP<=110 and 160<=fatP:
            C_id="C_ow"
        if 110<=skeletalP and 80<fatP<160:
            C_id="D_os"
        if 110<=skeletalP and 160<=fatP:
            C_id="I_oo"
    if weightP<=85:
        if 90<skeletalP and fatP<=80:
            C_id="D_ls"
        if skeletalP<90 and fatP<=80:
            C_id="I_lw"            
    return C_id

#인바디 유형별 코멘트 작성
def write_comment(c,Inbody_cat,height):
    if Inbody_cat=="C_sw":
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 허약형 (C자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 체지방량으로는 정상이지만 골격근이 부족한 유형')
        c.drawString(32,height-815,'•근육을 구성하는 단백질이 부족한 것이 원인')

    elif Inbody_cat=="C_so":
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 비만형 (C자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 근육량은 정상이지만 체지방이 과다한 유형')
        c.drawString(32,height-815,'•탄수화물, 지방 위주의 과도한 칼로리 섭취가 원인') 

    elif Inbody_cat=="C_ow":
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"과체중 허약형 (C자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중과 체지방량이 골격근량 대비하여 과다한 유형')
        c.drawString(32,height-815,'•과도한 칼로리, 부족한 단백질 섭취, 근력운동 부족이 원인')

    elif Inbody_cat=="D_ss":
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 강인형 (D자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•날씬하면서 근육이 탄탄하게 잘 다듬어져 있는 유형')
        c.drawString(32,height-815,'•균형잡힌 섭취와 유산소, 근력운동 병행을 통한 상태유지')

    elif Inbody_cat=="D_ss":
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 강인형 (D자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•날씬하면서 근육이 탄탄하게 잘 다듬어져 있는 유형')
        c.drawString(32,height-815,'•균형잡힌 섭취와 유산소, 근력운동 병행을 통한 상태유지') 

    elif Inbody_cat=="D_ls":
    #elif Inbody_cat=="C_so":    
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"저체중 강인형 (D자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•근육량은 표준이상, 체중과 체지방량이 표준이하인 유형')
        c.drawString(32,height-815,'•근력운동, 균형잡힌 섭취를 통해 체지방, 골격근 유지 필요') 

    elif Inbody_cat=="D_os":
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"과체중 강인형 (D자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•과체중이지만 체지방에 비해 골격근이 발달한 유형')
        c.drawString(32,height-815,'•주로 운동선수들에게 나타나는 유형으로 체지방 유지 필요')

    elif Inbody_cat=="I_sh":
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"표준체중 건강형 (I자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 골격근량, 체지방량이 모두 표준인 유형')
        c.drawString(32,height-815,'•유산소, 근력운동 병행을 통해 체지방량이 유지 필요')

    elif Inbody_cat=="I_lw":
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"저체중 허약형 (I자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 골격근량, 체지방량이 모두 표준이하인 유형')
        c.drawString(32,height-815,'•섭취하는 영양소의 양이 전반적으로 부족한것이 원인')    

    elif Inbody_cat=="I_oo":
    #elif Inbody_cat=="C_so":    
        c.setFont('AppleGothic', 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height-675,'"과체중 비만형 (I자)"')
        c.setFont('AppleGothic', 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height-800,'•체중, 골격근량, 체지방량이 모두 표준이상인 유형')
        c.drawString(32,height-815,'•전체적으로 표준보다 체구성 성분이 많아서 나타나는 유형')                              
    return

#인바디 그래프 그리기
def draw_inbody(c,Inbody,height):
    weightP=Inbody.Weight/(Inbody.Weight+Inbody.WeightControl)*100
    skeletalP=Inbody.FatFree/(Inbody.FatFree+Inbody.MuscleControl)*100
    fatP=Inbody.BodyFat/(Inbody.BodyFat+Inbody.FatControl)*100

    print(weightP)
    print(skeletalP)
    print(fatP)

    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.setStrokeColorRGB(0.9, 0.9, 0.9)
    c.roundRect(90,height-710, 180, 15,7.5,fill=1)
    c.roundRect(90,height-740, 180, 15,7.5,fill=1)
    c.roundRect(90,height-770, 180, 15,7.5,fill=1)

    weightW=180*(weightP-55)/150
    skeletalW=180*(skeletalP-70)/100
    if fatP<=100:
        fatW=54*(fatP-40)/60
    elif 100<fatP:    
        fatW=54+126*(fatP-100)/420
    
    print(weightW)
    print(skeletalW)
    print(fatW)

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


    if fatP<=85 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)

    if 85<fatP<115 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)

    if 115<=fatP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height-770, fatW, 15,7.5,fill=1)     

    c.setLineWidth(0.5)
    c.setStrokeColorRGB(0.9,0.9,0.9)
    c.line(126, height - 695, 126, height - 710)
    c.line(126, height - 725, 126, height - 740)
    c.line(126, height - 755, 126, height - 770)

    c.line(162, height - 695, 162, height - 710)
    c.line(162, height - 725, 162, height - 740)
    c.line(162, height - 755, 162, height - 770)

    return

#인바디 유형 그리기
def draw_alpha(c,Inbody_cat,height):
    if "C" in Inbody_cat:
        c.drawImage(filepath+'C_in.png',145,height-770,68,76,mask='auto')

    if "D" in Inbody_cat:
        c.drawImage(filepath+'D_in.png',145,height-770,68,76,mask='auto')    

    if "I" in Inbody_cat:
        c.drawImage(filepath+'I_in.png',150,height-770,50,76,mask='auto')    

    return

# 에이지 센서 패널
def draw_panel(c,Agesensor,height):
    
    baseX=320
    baseY=height-750
    if Agesensor.Rating =="A":
        c.drawImage(filepath+'A.png',baseX,baseY,130,69,mask='auto')
        print("코드실행A")
    elif Agesensor.Rating =="B":
        c.drawImage(filepath+'B.png',baseX,baseY,130,69,mask='auto')
        print("코드실행B")
    elif Agesensor.Rating =="C":
        c.drawImage(filepath+'C.png',baseX,baseY,130,69,mask='auto')    
    elif Agesensor.Rating =="D":
        c.drawImage(filepath+'D.png',baseX,baseY,130,69,mask='auto')    
    elif Agesensor.Rating =="E":
        c.drawImage(filepath+'E.png',baseX,baseY,130,69,mask='auto')    

    c.setFont('AppleGothic', 40)
    c.setFillColorRGB(1,208/255,20/255)
    rating=str(Agesensor.Rating)
    c.drawString(baseX+165+3,baseY+35,rating)

    c.setFont('AppleGothic', 15)
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawString(baseX+195+3,baseY+40,"등급")  

    c.setFont('AppleGothic', 12)
    rank=str(Agesensor.Rank)+"등 / 100명"
    c.drawString(baseX+155+3,baseY+10,rank)  

    c.setFont('AppleGothic', 8)
    c.setFillColorRGB(0.2,0.2,0.2)
    c.drawString(baseX-10,baseY+28,"2%")
    c.drawString(baseX+8,baseY+60,"14%")
    c.drawString(baseX+55,baseY+73,"34%")
    c.drawString(baseX+103,baseY+60,"43%")
    c.drawString(baseX+128,baseY+28,"7%")

    c.roundRect(baseX-5,baseY-70, 140, 65,10)
    c.roundRect(baseX+145,baseY-70, 95, 65,10)

    c.setFont('AppleGothic', 10)
    c.setFillColorRGB(0.1,0.1,0.1)
    c.drawString(baseX+5,baseY-20,"AGEs(당독소)란?")
    c.setFont('AppleGothic', 8.5)
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawString(baseX+5,baseY-35,"포도당, 과당과 같은 당이 단백질")
    c.drawString(baseX+5,baseY-47,"또는 지방에 결합하여 당화된")
    c.drawString(baseX+5,baseY-59,"물질로 노화 시 증가")

    c.setFont('AppleGothic', 10)
    c.setFillColorRGB(0.1,0.1,0.1)
    c.drawString(baseX+155,baseY-20,"당독소 과다증")
    c.setFont('AppleGothic', 8.5)
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawString(baseX+155,baseY-35,"노화,비만,당뇨,")
    c.drawString(baseX+155,baseY-47,"노안,간염")
    c.drawString(baseX+155,baseY-59,"뇌 기능 장애")
    return


# PDF 파일 생성
def create_pdf(Nutrition,Vitastiq,Inbody,Agesensor,Name):
    filename=filepath+'Basic_Health_Report.pdf'
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    register_fonts()
    
    # 제목1 추가 (한글) - 페이지 가운데에 배치
    draw_centered_string(c, "Greating store healthcare", height - 40, "AppleGothic", 12, width)
    draw_centered_string(c, "기본건강 프로그램 결과차트", height - 70, "AppleGothic", 20, width)
    
    # 선 그리기 (x1, y1, x2, y2)
    c.setLineWidth(0.7)  # 라인의 굵기 설정
    c.setStrokeColorRGB(0.75, 0.75, 0.75)  # 라인의 색상 설정
    c.line(450, height - 100, 550, height - 100)
    
    # 내담자명
    c.drawImage(filepath+'user.png',455,height-100,20,20,mask='auto')

    username= Name+"님"
    c.setFont('AppleGothic', 13)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(485,height-95,username)
    
    # 사각형 그리기 (x, y, width, height)
    c.roundRect(20,height-430, 265+5, 310,15)
    c.roundRect(300,height-430, 265+5, 310,15)
    c.roundRect(20,height-625, 545+5, 185,15)
    c.roundRect(20,height-820-10, 265+5, 185+10,15)
    c.roundRect(300,height-820-10, 265+5, 185+10,15)
    

    #-------------- part1 그리팅 헬스 스코어 --------------

    # 본문 채우기 
    c.setFont('AppleGothic', 12)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(35,height-140,"그리팅 헬스 스코어")
    c.setFont('AppleGothic', 10)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(35,height-160,"•4가지 항목의 종합적인 점수에요.")

    # 4가지 점수표현 칸
    c.drawImage(filepath+"score.png", 185, height - 240, 80,45,mask='auto')
    c.drawImage(filepath+"score.png", 185, height - 295, 80,45,mask='auto')
    c.drawImage(filepath+"score.png", 185, height - 350, 80,45,mask='auto')
    c.drawImage(filepath+"score.png", 185, height - 405, 80,45,mask='auto')

    # 점수
    vitascore=100
    for field in fields(Vitastiq):
        field_name = field.name
        field_value = getattr(Vitastiq, field_name)
        if field_value=="경미":
            vitascore=vitascore-10
        if field_value=="낮은":
            vitascore=vitascore-5

    EatS=str(Nutrition.EatScore)+"점"
    VitaS=str(vitascore)+"점"
    InboS=str(Inbody.InbodyScore)+"점"
    AgeS=str(100-Agesensor.Rank)+"점"

    print(type(Nutrition.EatScore))
    print(type(vitascore))
    print(type(Inbody.InbodyScore))
    print(type(100-Agesensor.Rank))
    TotalScore=float(Nutrition.EatScore+vitascore+Inbody.InbodyScore+100-Agesensor.Rank)/4
    
    print(str(TotalScore)+"---------")

    c.setFont('AppleGothic', 10)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(213,height-231,EatS)
    c.drawString(213,height-287,VitaS)
    c.drawString(213,height-342,InboS)
    c.drawString(213,height-396,AgeS)

    c.setFont('AppleGothic', 9)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(195,height-211,"영양 섭취 상태")
    c.drawString(196,height-266,"비타민/무기질")
    c.drawString(210,height-321,"인바디")
    c.drawString(198,height-376,"AGEs sensor")

    # 가운데 라인
    c.setDash([3, 2], 0)  # 대시 패턴 설정: 길이 3의 대시와 길이 2의 공백을 반복
    c.line(170, height - 195, 170, height - 405)  # (100, height-100)에서 시작하여 (400, height-100)까지 선 그리기

    # 점수표현
    draw_score_string(c,height,TotalScore)
    draw_part1_graph(c,height,TotalScore)

    #-------------- part2 한 눈에 보는 나의 식습관 --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont('AppleGothic', 12)
    c.drawString(315,height-140,"한 눈에 보는 나의 식습관")

    #색상안내
    c.setFillColorRGB(1,208/255,20/255)
    c.circle(468,height-135,5,fill=1,stroke=0)
    c.setFillColorRGB(134/255,206/255,2/255)
    c.circle(500,height-135,5,fill=1,stroke=0)
    c.setFillColorRGB(1,111/255,111/255)
    c.circle(532,height-135,5,fill=1,stroke=0)
    c.setFillColorRGB(0.25,0.25,0.25)
    c.setFont('AppleGothic', 8)
    c.drawString(475,height-138,'부족')
    c.drawString(507,height-138,'적정')
    c.drawString(539,height-138,'과다')

    # 한줄피드백 작성
    c.setFont('AppleGothic', 10)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(315,height-160,'✓ 지방, 나트륨은 과다해요.')
    c.drawString(315,height-175,'✓ 단백질 식이섬유는 부족해요.')

    # 표 그리기
    BaseX2=315
    BaseY2=height-205
    c.setFillColorRGB(0, 0, 0)
    c.setFont('AppleGothic', 8)
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

    #-------------- part3 비타민/무기질 --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont('AppleGothic', 12)
    c.drawString(35,height-460,"비타민/무기질")
    c.drawImage(filepath+"Vit_Min.png",30,height-610,530,130,mask='auto')

    c.drawImage(filepath+"Star_red.png",160,height-468,20,20,mask='auto')
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.setFont('AppleGothic', 10)
    c.drawString(183,height-462,"체내 영양소가 낮은 경향으로 보여요.")

    c.drawImage(filepath+"Star_blue.png",355,height-468,20,20,mask='auto')
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.setFont('AppleGothic', 10)
    c.drawString(378,height-462,"체내 영양소가 적정한 경향으로 보여요.")

    draw_star(c,Vitastiq,height)

    #-------------- part4 인바디 --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont('AppleGothic', 12)
    c.drawString(35,height-655,"인바디")

    Inbody_cat=set_category(Inbody)
    print(Inbody_cat)
    write_comment(c,Inbody_cat,height)

    c.setFont('AppleGothic', 9)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(37,height-705,'체중')
    c.drawString(37,height-735,'골격근량')
    c.drawString(37,height-765,'체지방량')

    draw_inbody(c,Inbody,height)
    draw_alpha(c,Inbody_cat,height)

    #-------------- part5 Age sensor --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont('AppleGothic', 12)
    c.drawString(315,height-655,"AGEs sensor")
    
    draw_panel(c,Agesensor,height)
    
    #-------------- 페이지 저장 및 이미지 변환 --------------

    # 페이지 저장
    c.showPage()
    c.save()

    # PDF를 이미지로 변환
    images = convert_from_path(filename)
    # 첫 번째 페이지를 이미지로 저장
    img_path = filepath+"Basic_Health_Report.png"
    images[0].save(img_path, "PNG")

    return img_path 

# PDF 생성 테스트용
if __name__ == "__main__":
    Nutri=Nutrition(EatScore=60, Carb="과다", Protein="적정", Fat="부족", Fiber="부족", Sodium="과다", Sugar="적정", SatFat="적정", Cholesterol="적정")
    Vita=Vitastiq(Biotin="", VitC="", Mg="", VitB1="", VitB2="", Zn="", Se="경미", VitB6="낮은", VitE="경미", Folate="낮은")
    Inbo=Inbody(InbodyScore=66,Weight=59.1,BodyFat=22.8,FatFree=19.5,ApproWeight=52.9,WeightControl=-7.4,MuscleControl=3.5,FatControl=-10.9)
    Age=Agesensor(Rating="B",Rank=30)
    create_pdf(Nutri,Vita,Inbo,Age,"김건강")
