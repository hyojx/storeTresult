from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from dataclass import Inbody,Agesensor,DietGoal,InbodyDetail
from PIL import Image
from pdf2image import convert_from_path
from reportlab.lib.colors import Color
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Table, TableStyle
from dataclasses import fields
import random

filepath="static/image/diet/"
resultfilepath="static/result/"
#mainfontname='AppleGothic'
mainfont='NanumGothic'
boldfont='NanumGothicBold'
Eboldfont='NanumGothicExtraBold'
lightfont='NanumGothicLight'


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

# 인바디 유형결정
def set_category(Inbody):
    C_id=""
    weightP=Inbody.Weight/(Inbody.Weight+Inbody.WeightControl)*100
    skeletalP=Inbody.FatFree/(Inbody.FatFree+Inbody.MuscleControl)*100
    fatP=Inbody.BodyFat/(Inbody.BodyFat+Inbody.FatControl)*100
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
        if 90<skeletalP and fatP<=80:
            C_id="D_ls"
        elif skeletalP<90 and fatP<=80:
            C_id="I_lw"    
        else:
            C_id="N"             
    return C_id

#07.09 수정---------------------------------------------------------------------
#인바디 유형별 코멘트 작성 
def write_comment(c,Inbody_cat,height):
    height1=height-385
    height2=height-520
    height3=height-550
    height4=height-580
    
    if Inbody_cat=="C_sw":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"표준체중 허약형 (C자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 체중, 체지방량으로는 정상이지만 근육량이 부족한 상태')
        c.drawString(32,height3,'• 부족한 단백질 섭취와 근력운동이 원인')
        c.drawString(32,height4,'• 주 2-3회 근력운동을 진행하여 근육량 늘리기')

    elif Inbody_cat=="C_so":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"표준체중 비만형 (C자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 체중, 근육량은 정상이지만 체지방이 과다한 상태')
        c.drawString(32,height3,'• 탄수화물, 지방 위주의 과도한 칼로리 섭취가 원인') 
        c.drawString(32,height4,'• 주 3회 30분 이상의 유산소 운동과 주 2-3회 근력 운동을')
        c.drawString(32,height4-15,'    진행하여 체지방량은 줄이고, 근육량은 늘리기')

    elif Inbody_cat=="C_ow":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"과체중 허약형 (C자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 근육량과 비교하여 체중과 체지방량이 과다한 상태')
        c.drawString(32,height3,'• 탄수화물, 지방 위주의 과도한 칼로리 섭취 및 부족한')
        c.drawString(32,height3-15,'    근력운동이 원인')
        c.drawString(32,height4-10,'• 주 3회 30분 이상의 유산소 운동과 주 2-3회 근력 운동을')
        c.drawString(32,height4-25,'    진행하여 체지방량은 줄이고, 근육량은 늘리기')

    elif Inbody_cat=="D_ss":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"표준체중 강인형 (D자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 날씬하면서 근육이 탄탄하게 잘 다듬어져 있는 유형')
        c.drawString(32,height3,'• 현재와 같이 균형잡힌 식습관과 유산소 운동, 근력운동의')
        c.drawString(32,height3-15,'    병행을 통해 현재 상태 유지하기')


    elif Inbody_cat=="D_ls": 
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"저체중 강인형 (D자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 근육량 대비 체중과 체지방이 부족한 유형')
        c.drawString(32,height3,'• 과도한 체지방 감량이 원인으로 체지방을 감량하는') 
        c.drawString(32,height3-15,'    유산소 운동 보다는 근력운동을 통해 현재 골격근 유지하기')

    elif Inbody_cat=="D_os":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"과체중 강인형 (D자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 체중이 표준이상이지만 체지방량에 비해 골격근이 발달한')
        c.drawString(32,height2-15,'    운동선수 유형')
        c.drawString(32,height3-10,'• 체지방량이 과다해지지 않도록 유산소운동을 통해')
        c.drawString(32,height3-25,'    체지방량 관리하기')

    elif Inbody_cat=="I_sh":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"표준체중 건강형 (I자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 체중, 근육량 체지방량이 모두 표준으로 밸런스가 잘 맞는')
        c.drawString(32,height2-15,'    건강한 유형')
        c.drawString(32,height3-10,'• 주 3회, 30분 이상의 유산소 운동과 주 2-3회 근력 운동을')
        c.drawString(32,height3-25,'    진행하여 체지방량이 표준이상으로 넘어가지 않는것을')
        c.drawString(32,height3-25-15,'    목표로 하기')

    elif Inbody_cat=="I_lw":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"저체중 허약형 (I자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 체중, 근육량, 체지방량이 모두 부족한 마른몸매 유형')
        c.drawString(32,height3,'• 음식 섭취량이 부족한 것이 원인')    
        c.drawString(32,height4,'• 섭취량을 늘리고 근력운동을 통해 근육량을 표준으로 끌어올리기')    


    elif Inbody_cat=="I_oo":
    #elif Inbody_cat=="C_so":    
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"과체중 비만형 (I자)"')
        c.setFont(mainfont, 9)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(32,height2,'• 체중, 근육량, 체지방량이 모두 표준 이상인 유형')
        c.drawString(32,height3,'• 주 3일 30분 이상 유산소 운동을 통해 체지방 감량하기')      

    elif Inbody_cat=="N":
        c.setFont(mainfont, 11)
        c.setFillColorRGB(0.5, 0.5, 0.5)
        c.drawString(35,height1,'"유형을 분류할 수 없습니다. 인바디 값을 확인해주세요."')
    return
#07.09 수정-----------------------------------------------------------------------

#인바디 그래프 그리기
def draw_inbody(c,Inbody,height):
    weightP=Inbody.Weight/(Inbody.Weight+Inbody.WeightControl)*100
    skeletalP=Inbody.FatFree/(Inbody.FatFree+Inbody.MuscleControl)*100
    fatP=Inbody.BodyFat/(Inbody.BodyFat+Inbody.FatControl)*100

    height1=height-420
    height2=height-450
    height3=height-480

    c.setFillColorRGB(0.9, 0.9, 0.9)
    c.setStrokeColorRGB(0.9, 0.9, 0.9)
    c.roundRect(90,height1, 180, 15,7.5,fill=1)
    c.roundRect(90,height2, 180, 15,7.5,fill=1)
    c.roundRect(90,height3, 180, 15,7.5,fill=1)

    weightW=180*(weightP-55)/150
    skeletalW=180*(skeletalP-70)/100
    if fatP<=100:
        fatW=54*(fatP-40)/60
    elif 100<fatP:    
        fatW=54+126*(fatP-100)/420

    if weightP<=85 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height1, weightW, 15,7.5,fill=1)

    if 85<weightP<115 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height1, weightW, 15,7.5,fill=1)

    if 115<=weightP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height1, weightW, 15,7.5,fill=1)   


    if skeletalP<=90 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height2, skeletalW, 15,7.5,fill=1)

    if 90<skeletalP<110 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height2, skeletalW, 15,7.5,fill=1)

    if 110<=skeletalP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height2, skeletalW, 15,7.5,fill=1)    


    if fatP<=85 :
        c.setFillColorRGB(1,208/255,20/255)
        c.setStrokeColorRGB(1,208/255,20/255)
        c.roundRect(90,height3, fatW, 15,7.5,fill=1)

    if 85<fatP<115 :
        c.setFillColorRGB(134/255,206/255,2/255)
        c.setStrokeColorRGB(134/255,206/255,2/255)
        c.roundRect(90,height3, fatW, 15,7.5,fill=1)

    if 115<=fatP :
        c.setFillColorRGB(1,111/255,111/255)
        c.setStrokeColorRGB(1,111/255,111/255)
        c.roundRect(90,height3, fatW, 15,7.5,fill=1)     

    c.setLineWidth(0.5)
    c.setStrokeColorRGB(0.9,0.9,0.9)
    c.line(126, height1+15, 126, height1)
    c.line(126, height2+15, 126, height2)
    c.line(126, height3+15, 126, height3)

    c.line(162, height1+15, 162, height1)
    c.line(162, height2+15, 162, height2)
    c.line(162, height3+15, 162, height3)

    return

# 인바디 유형 그리기
def draw_alpha(c,Inbody_cat,height):
    if "C" in Inbody_cat:
        c.drawImage(filepath+'C_in.png',145,height-480,68,76,mask='auto')

    elif "D" in Inbody_cat:
        c.drawImage(filepath+'D_in.png',145,height-480,68,76,mask='auto')    

    elif "I" in Inbody_cat:
        c.drawImage(filepath+'I_in.png',150,height-480,50,76,mask='auto')   
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

# 인바디 디테일 코멘트 세팅
def set_comment(IDetail):
    comments={
    "first_Fcomment":"",
    "second_Fcomment":"",
    "first_Scomment":"",
    "second_Scomment":"",
    "fat_img":"",
    "muscle_img":""
    }
    idetail_flist=[IDetail.UpperLF,IDetail.UpperRF,IDetail.LowerLF,IDetail.LowerRF]
    idetail_slist=[IDetail.UpperLS,IDetail.UpperRS,IDetail.LowerLS,IDetail.LowerRS]

    highfat_count=idetail_flist.count("이상")
    lowfat_count=idetail_flist.count("이하")

    highske_count=idetail_slist.count("이상")
    lowske_count=idetail_slist.count("이하")


    # 체지방 코멘트 정하기 
    if highfat_count==0 and 1<=lowfat_count:
        comments["first_Fcomment"]="체지방 부족"

        if lowfat_count==4:
            comments["second_Fcomment"]="전신" 
            comments["fat_img"]="LF_all.png"

        elif lowfat_count==3:
            if IDetail.UpperLF==IDetail.UpperRF=="이하":
                if IDetail.LowerLF=="이하":
                    comments["second_Fcomment"]="상체, 왼쪽 하체"
                    comments["fat_img"]="LF_uadl.png"
                elif IDetail.LowerRF=="이하":
                    comments["second_Fcomment"]="상체, 오른쪽 하체"
                    comments["fat_img"]="LF_uadr.png"
            elif IDetail.LowerLF==IDetail.LowerRF=="이하":
                if IDetail.UpperLF=="이하":
                    comments["second_Fcomment"]="하체, 왼쪽 상체"
                    comments["fat_img"]="LF_ulda.png"
                elif IDetail.UpperRF=="이하":
                    comments["second_Fcomment"]="하체, 오른쪽 상체"
                    comments["fat_img"]="LF_urda.png"

        elif lowfat_count==2:
            if IDetail.UpperLF==IDetail.UpperRF=="이하":
                comments["second_Fcomment"]="상체"
                comments["fat_img"]="LF_ua.png"
            elif IDetail.LowerLF==IDetail.LowerRF=="이하":
                comments["second_Fcomment"]="하체"
                comments["fat_img"]="LF_da.png"
            elif IDetail.UpperLF==IDetail.LowerRF=="이하":
                comments["second_Fcomment"]="왼쪽 상체, 오른쪽 하체"
                comments["fat_img"]="LF_uldr.png"
            elif IDetail.UpperLF==IDetail.LowerLF=="이하":
                comments["second_Fcomment"]="왼쪽 상체, 왼쪽 하체" 
                comments["fat_img"]="LF_uldl.png"
            elif IDetail.UpperRF==IDetail.LowerRF=="이하":
                comments["second_Fcomment"]="오른쪽 상체, 오른쪽 하체"
                comments["fat_img"]="LF_urdr.png"
            elif IDetail.UpperRF==IDetail.LowerLF=="이하":
                comments["second_Fcomment"]="오른쪽 상체, 왼쪽 하체"   
                comments["fat_img"]="LF_urdl.png"  

        elif lowfat_count==1:
            if IDetail.UpperLF=="이하":
                comments["second_Fcomment"]="왼쪽 상체"
                comments["fat_img"]="LF_ul.png"
            elif IDetail.LowerLF=="이하":
                comments["second_Fcomment"]="왼쪽 하체"
                comments["fat_img"]="LF_dl.png"
            elif IDetail.UpperRF=="이하":
                comments["second_Fcomment"]="오른쪽 상체"
                comments["fat_img"]="LF_ur.png"
            elif IDetail.LowerRF=="이하":
                comments["second_Fcomment"]="오른쪽 하체" 
                comments["fat_img"]="LF_dr.png"

    elif 1<=highfat_count:
        comments["first_Fcomment"]="체지방 집중감량"

        if highfat_count==4:
            comments["second_Fcomment"]="전신 체지방"
            comments["fat_img"]="HF_all.png"

        elif highfat_count==3:
            if IDetail.UpperLF==IDetail.UpperRF=="이상":
                if IDetail.LowerLF=="이상":
                    comments["second_Fcomment"]="상체, 왼쪽 하체"
                    comments["fat_img"]="HF_uadl.png"
                elif IDetail.LowerRF=="이상":
                    comments["second_Fcomment"]="상체, 오른쪽 하체"
                    comments["fat_img"]="HF_uadr.png"
            elif IDetail.LowerLF==IDetail.LowerRF=="이상":
                if IDetail.UpperLF=="이상":
                    comments["second_Fcomment"]="하체, 왼쪽 상체"
                    comments["fat_img"]="HF_ulda.png"
                elif IDetail.UpperRF=="이상":
                    comments["second_Fcomment"]="하체, 오른쪽 상체"
                    comments["fat_img"]="HF_urda.png"

        elif highfat_count==2:
            if IDetail.UpperLF==IDetail.UpperRF=="이상":
                comments["second_Fcomment"]="상체"
                comments["fat_img"]="HF_ua.png"
            elif IDetail.LowerLF==IDetail.LowerRF=="이상":
                comments["second_Fcomment"]="하체"
                comments["fat_img"]="HF_da.png"
            elif IDetail.UpperLF==IDetail.LowerRF=="이상":
                comments["second_Fcomment"]="왼쪽 상체, 오른쪽 하체"
                comments["fat_img"]="HF_uldr.png"
            elif IDetail.UpperLF==IDetail.LowerLF=="이상":
                comments["second_Fcomment"]="왼쪽 상체, 왼쪽 하체" 
                comments["fat_img"]="HF_uldl.png"
            elif IDetail.UpperRF==IDetail.LowerRF=="이상":
                comments["second_Fcomment"]="오른쪽 상체, 오른쪽 하체"
                comments["fat_img"]="HF_urdr.png"
            elif IDetail.UpperRF==IDetail.LowerLF=="이상":
                comments["second_Fcomment"]="오른쪽 상체, 왼쪽 하체"  
                comments["fat_img"]="HF_urdl.png"    

        elif highfat_count==1:
            if IDetail.UpperLF=="이상":
                comments["second_Fcomment"]="왼쪽 상체"
                comments["fat_img"]="HF_ul.png"
            elif IDetail.LowerLF=="이상":
                comments["second_Fcomment"]="왼쪽 하체"
                comments["fat_img"]="HF_dl.png"
            elif IDetail.UpperRF=="이상":
                comments["second_Fcomment"]="오른쪽 상체"
                comments["fat_img"]="HF_ur.png"
            elif IDetail.LowerRF=="이상":
                comments["second_Fcomment"]="오른쪽 하체" 
                comments["fat_img"]="HF_dr.png"

    else: 
        comments["first_Fcomment"]="체지방 적정"
        comments["second_Fcomment"]="전신 체지방 적정" 
        comments["fat_img"]="AF_good.png"



    # 근육량 코멘트 정하기

    if lowske_count==0 and 1<=highske_count:
        comments["first_Scomment"]="근육량 유지"

        if 2<=highske_count:
            comments["second_Scomment"]="상체/하체 밸런스"   #추가로 구분필요

            if highske_count==4:
                comments["muscle_img"]="HM_all.png"
            elif highske_count==3:
                if IDetail.UpperLS==IDetail.UpperRS=="이상":
                    if IDetail.LowerLS=="이상":
                        comments["muscle_img"]="HM_uadl.png"
                    elif IDetail.LowerRS=="이상":
                        comments["muscle_img"]="HM_uadr.png"
                elif IDetail.LowerLS==IDetail.LowerRS=="이상":
                    if IDetail.UpperLS=="이상":
                        comments["muscle_img"]="HM_ulda.png"
                    elif IDetail.UpperRS=="이상":
                        comments["muscle_img"]="HM_urda.png"
            # 2024 .07.01 수정            
            elif highske_count==2:
                if IDetail.UpperLS==IDetail.UpperRS=="이상":
                    comments["muscle_img"]="HM_ua.png"
                elif IDetail.LowerLS==IDetail.LowerRS=="이상":
                    comments["muscle_img"]="HM_da.png"
                elif IDetail.UpperLS==IDetail.LowerRS=="이상":
                    comments["muscle_img"]="HM_uldr.png"
                elif IDetail.UpperLS==IDetail.LowerLS=="이상":
                    comments["muscle_img"]="HM_uldl.png"
                elif IDetail.UpperRS==IDetail.LowerRS=="이상":
                    comments["muscle_img"]="HM_urdr.png"
                elif IDetail.UpperRS==IDetail.LowerLS=="이상":
                    comments["muscle_img"]="HM_urdl.png"            

        elif highske_count==1:
            if IDetail.UpperLS=="이상":
                comments["second_Scomment"]="상체 밸런스"
                comments["muscle_img"]="HM_ul.png"
            elif IDetail.LowerLS=="이상":
                comments["second_Scomment"]="하체 밸런스"
                comments["muscle_img"]="HM_dl.png"
            elif IDetail.UpperRS=="이상":
                comments["second_Scomment"]="상체 밸런스"
                comments["muscle_img"]="HM_ur.png"
            elif IDetail.LowerRS=="이상":
                comments["second_Scomment"]="하체 밸런스" 
                comments["muscle_img"]="HM_dr.png"

    elif 1<=lowske_count:
        comments["first_Scomment"]="근육량 강화"

        if lowske_count==4:
            comments["second_Scomment"]="전신" 
            comments["muscle_img"]="LM_all.png"

        elif lowske_count==3:
            if IDetail.UpperLS==IDetail.UpperRS=="이하":
                if IDetail.LowerLS=="이하":
                    comments["second_Scomment"]="상체, 왼쪽 하체"
                    comments["muscle_img"]="LM_uadl.png"
                elif IDetail.LowerRS=="이하":
                    comments["second_Scomment"]="상체, 오른쪽 하체"
                    comments["muscle_img"]="LM_uadr.png"
            elif IDetail.LowerLS==IDetail.LowerRS=="이하":
                if IDetail.UpperLS=="이하":
                    comments["second_Scomment"]="하체, 왼쪽 상체"
                    comments["muscle_img"]="LM_ulda.png"
                elif IDetail.UpperRS=="이하":
                    comments["second_Scomment"]="하체, 오른쪽 상체"
                    comments["muscle_img"]="LM_urda.png"

        elif lowske_count==2:
            if IDetail.UpperLS==IDetail.UpperRS=="이하":
                comments["second_Scomment"]="상체"
                comments["muscle_img"]="LM_ua.png"
            elif IDetail.LowerLS==IDetail.LowerRS=="이하":
                comments["second_Scomment"]="하체"
                comments["muscle_img"]="LM_da.png"
            elif IDetail.UpperLS==IDetail.LowerRS=="이하":
                comments["second_Scomment"]="왼쪽 상체, 오른쪽 하체"
                comments["muscle_img"]="LM_uldr.png"
            elif IDetail.UpperLS==IDetail.LowerLS=="이하":
                comments["second_Scomment"]="왼쪽 상체, 왼쪽 하체" 
                comments["muscle_img"]="LM_uldl.png"
            elif IDetail.UpperRS==IDetail.LowerRS=="이하":
                comments["second_Scomment"]="오른쪽 상체, 오른쪽 하체"
                comments["muscle_img"]="LM_urdr.png"
            elif IDetail.UpperRS==IDetail.LowerLS=="이하":
                comments["second_Scomment"]="오른쪽 상체, 왼쪽 하체"  
                comments["muscle_img"]="LM_urdl.png"   

        elif lowske_count==1:
            if IDetail.UpperLS=="이하":
                comments["second_Scomment"]="왼쪽 상체"
                comments["muscle_img"]="LM_ul.png"
            elif IDetail.LowerLS=="이하":
                comments["second_Scomment"]="왼쪽 하체"
                comments["muscle_img"]="LM_dl.png"
            elif IDetail.UpperRS=="이하":
                comments["second_Scomment"]="오른쪽 상체"
                comments["muscle_img"]="LM_ur.png"
            elif IDetail.LowerRS=="이하":
                comments["second_Scomment"]="오른쪽 하체"  
                comments["muscle_img"]="LM_dr.png"

    else: 
        comments["first_Scomment"]="근육량 적정"
        comments["second_Scomment"]="전신 근육량 적정" 
        comments["muscle_img"]="AM_good.png"   

       

    return comments



def create_diet_pdf(Name,Inbody,Agesensor,DGoal,IDetail):
#def create_diet_pdf(DietGoal,Inbody,InbodyDetail,Agesensor,Name):
    filename=resultfilepath+'Diet_Report.pdf'
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    register_fonts()
    
    # 제목1 추가 (한글) - 페이지 가운데에 배치
    draw_centered_string(c, "Greating store healthcare", height - 40, mainfont, 12, width)
    draw_centered_string(c, "다이어트 프로그램 결과차트", height - 70, boldfont, 20, width)
    
    # 선 그리기 (x1, y1, x2, y2)
    c.setLineWidth(0.7)  # 라인의 굵기 설정
    c.setStrokeColorRGB(0.75, 0.75, 0.75)  # 라인의 색상 설정
    c.line(450, height - 100, 550, height - 100)
    
    # 내담자명
    c.drawImage(filepath+'user.png',455,height-100,20,20,mask='auto')

    username= Name+"님"
    c.setFont(boldfont, 13)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(485,height-95,username)
    
    # 사각형 그리기 (x, y, width, height)
    c.roundRect(20,height-325, 220, 210,15)
    c.roundRect(250,height-325, 320, 210,15)
    c.roundRect(20,height-625, 270, 290,15)
    c.roundRect(300,height-625, 270, 290,15)
    c.roundRect(20,height-830, 270, 195,15)
    c.roundRect(300,height-830, 270, 195,15)
    
    
    #-------------- part1 다이어트 플랜 --------------

    # 본문 채우기 
    c.setFont(boldfont, 12)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(35,height-140,"한눈에 보는 나의 다이어트 플랜")

    c.setLineWidth(1)  # 라인의 굵기 설정

    c.setFillColorRGB(199/255, 219/255, 241/255)
    c.setStrokeColorRGB(89/255,187/255,226/255)
    c.roundRect(38,height-205,190,40,20,fill=True)

    c.setFillColorRGB(251/255,200/255,179/255)
    c.setStrokeColorRGB(247/255, 150/255, 110/255)
    c.roundRect(38,height-255,190,40,20,fill=True)

    c.setFillColorRGB(254/255,222/255,180/255)
    c.setStrokeColorRGB(252/255, 184/255, 92/255)
    c.roundRect(38,height-305,190,40,20,fill=True)

    c.setFont(mainfont, 10)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(48,height-189,DGoal.Period)
    c.drawString(66,height-189,"동안 하루 총")
    c.drawString(176,height-189,"조절해요!")
    c.drawString(48,height-239,"하루 식사로는")
    c.drawString(168,height-239,"줄여요!")
    c.drawString(48,height-289,"하루 운동으로는")
    c.drawString(175,height-289,"소모해요!")
    
    if DGoal.Period=="2주":
        period=14
    elif DGoal.Period=="3주":
        period=21
    elif DGoal.Period=="4주":
        period=28 
    elif DGoal.Period=="2달":
        period=56 
    elif DGoal.Period=="3달":
        period=84
    elif DGoal.Period=="4달":
        period=112
    elif DGoal.Period=="5달":
        period=140            

    
    reducecal=(Inbody.Weight-DGoal.Gweight)*7000/period
    dayreduce=round(reducecal)

    foodcontrol=round(dayreduce*DGoal.FoodR/10)
    
    workcontrol=round(dayreduce*DGoal.WorkOutR/10)


    c.setFillColorRGB(1,1,1)
    c.setStrokeColorRGB(1,1,1)
    c.roundRect(127,height-195,45,20,10,fill=True)
    c.roundRect(117,height-245,45,20,10,fill=True)
    c.roundRect(125,height-295,45,20,10,fill=True)

    c.setFont(mainfont, 8)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(133,height-188,str(dayreduce)+"kcal")

    c.setFont(mainfont, 8)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(123,height-238,str(foodcontrol)+"kcal")

    c.setFont(mainfont, 8)
    c.setFillColorRGB(0, 0, 0)
    c.drawString(131,height-288,str(workcontrol)+"kcal")

    
    #-------------- part2 나의 체형 알아보기 --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont(boldfont, 12)
    c.drawString(265,height-140,"나의 체형 알아보기")

    # 한줄피드백 작성 (07.09 4시 수정)
    c.setFont(mainfont, 10)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    if Inbody.BMI<18.5:
        c.drawString(265,height-160,'" BMI '+str(Inbody.BMI)+', 저체중 "')
        c.drawImage(filepath+'Low.png',265,height-312,290,136,mask='auto')
    elif 18.5<=Inbody.BMI<25:
        c.drawString(265,height-160,'" BMI '+str(Inbody.BMI)+', 정상체중 "')
        c.drawImage(filepath+'Normal.png',265,height-312,290,136,mask='auto') 
    elif 25<=Inbody.BMI<30:
        c.drawString(265,height-160,'" BMI '+str(Inbody.BMI)+', 과체중 "')
        c.drawImage(filepath+'Over.png',265,height-312,290,136,mask='auto')   
    elif 30<=Inbody.BMI<40:
        c.drawString(265,height-160,'" BMI '+str(Inbody.BMI)+', 비만 "')
        c.drawImage(filepath+'Obes.png',265,height-312,290,136,mask='auto')  
    elif 40<=Inbody.BMI:
        c.drawString(265,height-160,'" BMI '+str(Inbody.BMI)+', 고도비만 "')
        c.drawImage(filepath+'HighObes.png',265,height-312,290,136,mask='auto')              

    #-------------- part3 인바디 --------------
    # 본문 채우기 
    c.setFillColorRGB(0, 0, 0)
    c.setFont(boldfont, 12)
    c.drawString(35,height-360,"인바디")

    Inbody_cat=set_category(Inbody)
    print("Inbody_cat"+Inbody_cat)
    write_comment(c,Inbody_cat,height)

    c.setFont(boldfont, 9)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(37,height-415,'체중')
    c.drawString(37,height-445,'골격근량')
    c.drawString(37,height-475,'체지방량')

    draw_inbody(c,Inbody,height)
    draw_alpha(c,Inbody_cat,height)

    #-------------- part4 체중관리 계획 --------------
    # 본문 채우기 (07.09 5시 수정)
    user_fat_control=-round(Inbody.Weight+Inbody.MuscleControl-DGoal.Gweight,1)
    if 0<user_fat_control and 0<Inbody.MuscleControl:
        comment="지방은 "+str(user_fat_control)+"kg 늘리고, 근육은 "+str(Inbody.MuscleControl)+"kg 늘리기"
    elif user_fat_control<0 and Inbody.MuscleControl<0:
        comment="지방은 "+str(user_fat_control)+"kg 줄이고, 근육은 "+str(Inbody.MuscleControl)+"kg 줄이기"
    elif user_fat_control<0 and 0<Inbody.MuscleControl:
        comment="지방은 "+str(user_fat_control)+"kg 줄이고, 근육은 "+str(Inbody.MuscleControl)+"kg 늘리기"
    elif 0<user_fat_control and Inbody.MuscleControl<0:
        comment="지방은 "+str(user_fat_control)+"kg 늘리고, 근육은 "+str(Inbody.MuscleControl)+"kg 줄이기"        
    c.setFillColorRGB(0, 0, 0)
    c.setFont(boldfont, 12)
    c.drawString(315,height-360,"체중관리 계획")

    c.setFont(mainfont, 10)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(315,height-380,comment)

    c.setFillColorRGB(1,227/255,163/255)
    c.setStrokeColorRGB(1,227/255,163/255)
    c.roundRect(315,height-420, 60, 20,10,fill=True)
    c.setFillColorRGB(0,0,0)
    c.setFont(mainfont, 12)
    c.drawString(333,height-415,"지방")

    c.setFillColorRGB(223/255,183/255,187/255)
    c.setStrokeColorRGB(223/255,183/255,187/255)
    c.roundRect(315,height-545, 60, 20,10,fill=True)
    c.setFillColorRGB(0,0,0)
    c.setFont(mainfont, 12)
    c.drawString(333,height-540,"근육")

    c.drawImage(filepath+'fat_img.png',320,height-490,60,61,mask='auto')
    c.drawImage(filepath+'fat_hand.png',392,height-488,86,60,mask='auto')
    c.drawImage(filepath+'muscle_img.png',328,height-602,50,40,mask='auto')
    c.drawImage(filepath+'muscle_hand.png',410,height-613,46,60,mask='auto')

    c.setStrokeColorRGB(0.75,0.75,0.75)
    c.line(315, height - 505, 560, height - 505)

    c.setLineWidth(1.5)
    c.setStrokeColorRGB(0.75,0.75,0.75)
    c.roundRect(485,height-475, 70, 30,15)
    c.roundRect(485,height-600, 70, 30,15)

    c.setFont(boldfont, 12)
    c.setFillColorRGB(1, 0, 0)
    if 0<user_fat_control:
        draw_centered_string_in(c,"+ "+str(user_fat_control)+"kg",485,height-464,boldfont,12,70)
        #c.drawString(495,height-465,"+ "+str(user_fat_control)+"kg")
    else:     
        draw_centered_string_in(c,str(user_fat_control)+"kg",485,height-464,boldfont,12,70)
        #c.drawString(495,height-465,str(user_fat_control)+"kg")
#07.09 수정--------------------------------------------------------------------------------------------
    c.setFillColorRGB(0, 0, 1)
    if 0<Inbody.MuscleControl:
        draw_centered_string_in(c,"+ "+str(Inbody.MuscleControl)+"kg",485,height-588,boldfont,12,70)
        #c.drawString(495,height-590,"+ "+str(Inbody.MuscleControl)+"kg")
    else:
        draw_centered_string_in(c,str(Inbody.MuscleControl)+"kg",485,height-588,boldfont,12,70)
        #c.drawString(495,height-590,str(Inbody.MuscleControl)+"kg")
#07.09 수정--------------------------------------------------------------------------------------------        

    #-------------- part5 집중관리 부위 --------------    
    c.setFillColorRGB(0, 0, 0)
    c.setFont(boldfont, 12)
    c.drawString(35,height-655,"집중 관리 부위")

    comments=set_comment(IDetail)
    
    c.setFillColorRGB(1, 217/255,102/255)
    c.setStrokeColorRGB(1, 217/255,102/255)
    c.roundRect(30,height-680, 12+pdfmetrics.stringWidth(comments["first_Fcomment"],mainfont,8), 12,6,fill=True)
    c.setFillColorRGB(0,0,0)
    c.setFont(mainfont, 8)
    c.drawString(36,height-677,comments['first_Fcomment'])

    c.setFillColorRGB(1, 155/255,155/255)
    c.setStrokeColorRGB(1, 155/255,155/255)
    c.roundRect(160,height-680, 12+pdfmetrics.stringWidth(comments["first_Scomment"],mainfont,8), 12,6,fill=True)
    c.setFillColorRGB(0,0,0)
    c.setFont(mainfont, 8)
    c.drawString(166,height-677,comments['first_Scomment'])

    c.setLineWidth(0.5)
    c.setStrokeColorRGB(0.75,0.75,0.75)
    c.line(155,height-688,155,height-820)

    
    c.setFillColorRGB(0.5,0.5,0.5)
    c.setFont(mainfont, 8)
    c.drawString(35,height-695,comments["second_Fcomment"])
    
    c.setFillColorRGB(0.5,0.5,0.5)
    c.setFont(mainfont, 8)
    c.drawString(167,height-695,comments["second_Scomment"])

    # 이미지 파일 넣기
    c.drawImage(filepath+comments['muscle_img'],195,height-820,47,110,mask='auto') 
    c.drawImage(filepath+comments['fat_img'],65,height-820,47,110,mask='auto') 
    


                            
    #-------------- part6 Age sensor --------------
    # 본문 채우기 
    if Agesensor.Rating=="" or Agesensor.Rank==0:
        c.drawImage(filepath+'AGEsBlur.png',310,height-820,250,164,mask='auto')
    else:
        c.setFillColorRGB(0, 0, 0)
        c.setFont(boldfont, 12)
        c.drawString(315,height-655,"AGEs sensor")
        c.setStrokeColorRGB(0.75,0.75,0.75)
        c.setLineWidth(0.7)
        draw_panel(c,Agesensor,height)
    
    #-------------- 페이지 저장 및 이미지 변환 --------------

    # 1페이지 저장
    c.showPage()

    #---------------------------------------- 상품추천 페이지 제작 -------------------------------------------
    # 선 그리기 (x1, y1, x2, y2)
    c.setLineWidth(0.7)  # 라인의 굵기 설정
    c.setStrokeColorRGB(0.7, 0.7, 0.7)  # 라인의 색상 설정
    c.line(10, height - 265, 580, height - 265)
    c.line(10, height - 540, 580, height - 540)
    
    c.setFont(boldfont, 18)
    c.setFillColorRGB(0,0,0)
    c.drawString(25,height-35,"맞춤 식재료")
    c.drawString(25,height-295,"맞춤 샐러드")
    c.drawString(25,height-570,"맞춤 주스")
    c.drawString(310,height-570,"맞춤 상품")

    # 샐러드 칼로리 구간 결정
    if (DGoal.Rcal-foodcontrol)/3<=1000:
        salad_cal=300
    elif 1000<(DGoal.Rcal-foodcontrol)/3<=1300:
        salad_cal=400
    elif 1300<(DGoal.Rcal-foodcontrol)/3<=1700:
        salad_cal=500 
    elif 1700<(DGoal.Rcal-foodcontrol)/3:
        salad_cal=600       

    # 코멘트 작성
    c.setFont(mainfont, 12)
    c.setFillColorRGB(0.2,0.2,0.2)
    c.drawString(25,height-58,'"다이어터를 위해 에너지 대사에 도움을 주는 식재료"')
    c.drawString(25,height-318,'"하루 '+str(foodcontrol)+"kcal를 줄이기 위한 "+str(salad_cal)+'kcal 샐러드 토핑추천"')
    c.drawString(25,height-593,'"신진대사를 활발하게 하는 영양소 가득"')
    c.setFont(mainfont, 10)
    c.setFillColorRGB(0.5,0.5,0.5)
    c.drawString(30,height-335,"저칼로리 드레싱과 함께 했을 때 "+str(salad_cal)+"kcal에요.")


    # 식재료 추천
    c.drawImage(filepath+'I'+random.choice(['21','22'])+'.png',30,height-250,158,175,mask='auto')
    c.drawImage(filepath+'I'+random.choice(['23','24'])+'.png',215,height-250,158,175,mask='auto')
    c.drawImage(filepath+'I'+random.choice(['25','26'])+'.png',400,height-250,158,175,mask='auto')

    c.setFillColorRGB(191/255,191/255,191/255)
    c.setStrokeColorRGB(191/255,191/255,191/255)
    c.roundRect(320,height-63,70,20,10,fill=True)
    c.roundRect(400,height-63,70,20,10,fill=True)
    c.roundRect(480,height-63,70,20,10,fill=True)

    c.setFillColorRGB(1,1,1)
    c.setFont(boldfont, 11)
    c.drawString(330,height-57,"#비타민B1")
    c.drawString(411,height-57,"#판토텐산")
    c.drawString(495,height-57,"#비오틴")
     
    c.drawImage(filepath+"DS0.png",470,height-335,100,50) 

    # 샐러드 추천
    if salad_cal==300:
        c.drawImage(filepath+"DS1.png",20,height-530,551,180,mask='auto')
    elif salad_cal==400:
        c.drawImage(filepath+"DS2.png",20,height-530,551,180,mask='auto')
    elif salad_cal==500:
        c.drawImage(filepath+"DS3.png",20,height-530,551,180,mask='auto')    
    elif salad_cal==600:
        c.drawImage(filepath+"DS4.png",20,height-530,551,180,mask='auto')    

    c.setStrokeColorRGB(0.6,0.6,0.6)
    c.setLineWidth(0.2)
    c.roundRect(22,height-530,180,180,10)
    c.roundRect(206,height-530,180,180,10)
    c.roundRect(395,height-530,180,180,10)     #07.09 7시 수정

    # 주스 추천
    c.setStrokeColorRGB(0.6,0.6,0.6)
    c.setLineWidth(0.2)
    c.roundRect(22,height-820,270,190,10)
    c.drawImage(filepath+"DJ1.png",22,height-820,270,190,mask='auto')

    c.setFillColorRGB(191/255,191/255,191/255)
    c.setStrokeColorRGB(191/255,191/255,191/255)
    c.roundRect(30,height-623,70,20,10,fill=True)
    c.roundRect(110,height-623,70,20,10,fill=True)
    c.roundRect(190,height-623,70,20,10,fill=True)

    c.setFillColorRGB(1,1,1)
    c.setFont(boldfont, 11)
    c.drawString(40,height-616.5,"#비타민B1")
    c.drawString(121,height-616.5,"#판토텐산")
    c.drawString(205,height-616.5,"#비오틴")

    # 상품 추천
    c.setStrokeColorRGB(0.6,0.6,0.6)
    c.setLineWidth(0.2)
    c.drawImage(filepath+"DP"+str(random.randint(1,5))+".png",310,height-695,270,115,mask='auto')
    c.drawImage(filepath+"DF"+str(random.randint(1,3))+".png",310,height-820,270,115,mask='auto')
    c.roundRect(310,height-820,270,115,10)
    c.roundRect(310,height-695,270,115,10)
    c.setFont(mainfont, 12)
    c.setFillColorRGB(0.2,0.2,0.2)
    c.drawString(320,height-599,'가벼운 한끼를 위해 꿀조합 "간식"')
    c.drawString(320,height-724,'지치지 않는 다이어트 서포트 "영양제"')


    # 2페이지 저장
    c.showPage()

    print(salad_cal)
    if salad_cal==300:
        c.drawImage(filepath+"300.png",0,0,width,height)
    elif salad_cal==400:
        c.drawImage(filepath+"400.png",0,0,width,height)    
    elif salad_cal==500:
        c.drawImage(filepath+"500.png",0,0,width,height)
    elif salad_cal==600:
        c.drawImage(filepath+"600.png",0,0,width,height)    

    c.showPage()

    c.save()

    # PDF를 이미지로 변환
    images = convert_from_path(filename)
    # 첫 번째 페이지를 이미지로 저장
    img_path = resultfilepath+"Basic_Diet_Report.png"
    images[0].save(img_path, "PNG")

    return img_path 

if __name__=="__main__":
    Inbo=Inbody(InbodyScore=66,Weight=59.1,BodyFat=22.8,FatFree=37,ApproWeight=52.9,WeightControl=-7.4,MuscleControl=3.5,FatControl=-10.9)
    Age=Agesensor(Rating="",Rank=30)
    DGoal=DietGoal(Period="2주",Gweight=58,Rcal=2800,FoodR=5,WorkOutR=5)
    IDetail=InbodyDetail(UpperLF="표준",UpperRF="이상",LowerLF="표준",LowerRF="이상",UpperLS="표준",UpperRS="이하",LowerLS="표준",LowerRS="이상")
    create_diet_pdf("김건강",Inbo,Age,DGoal,IDetail)
