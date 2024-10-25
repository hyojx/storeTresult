import gradio as gr
from dataclass import Nutrition,Vitastiq,Inbody,Agesensor,DietGoal,InbodyDetail,SkinState,NutritionDetail,Supplements
from createpdf import create_basic_pdf
from createpdf2 import create_diet_pdf
from createpdf3 import create_skin_pdf



def update_ratio(slider_value):
    return slider_value, 100 - slider_value

def process_basic_inputs(Name,Gender,Height,Store,Activity,Age,EatScore,Carb,Protein,Fat,Fiber,Sodium,Sugar,SatFat,Cholesterol,Unused,Biotin,VitC,Mg,VitB1,VitB2,Zn,Se,VitB6,VitE,Folate,InbodyScore,Weight,BodyFat,ApproWeight,FatFree,WeightMax,MuscleMax,FatMax,Recomcal,SkeletalMuscle,Rating,Rank,CarbH,CarbV,ProteinL,ProteinV,FatH,FatV,FiberL,FiberV,SodiumH,SodiumV,SugarH,SugarV,SatFatH,SatFatV,CholesterolH,CholesterolV):
    Nutri=Nutrition(EatScore=EatScore, Carb=Carb, Protein=Protein, Fat=Fat, Fiber=Fiber, Sodium=Sodium, Sugar=Sugar, SatFat=SatFat, Cholesterol=Cholesterol,UserHeight=Height)
    Vita=Vitastiq(Unused=Unused,Biotin=Biotin, VitC=VitC, Mg=Mg, VitB1=VitB1, VitB2=VitB2, Zn=Zn, Se=Se, VitB6=VitB6, VitE=VitE, Folate=Folate)
    Inbo=Inbody(InbodyScore=InbodyScore,Weight=Weight,BodyFat=BodyFat,ApproWeight=ApproWeight,FatFree=FatFree,WeightMax=WeightMax,MuscleMax=MuscleMax,FatMax=FatMax,Recomcal=Recomcal,SkeletalMuscle=SkeletalMuscle)
    Age=Agesensor(Rating,Rank)
    NutriD=NutritionDetail(CarbH=CarbH,CarbV=CarbV,ProteinL=ProteinL,ProteinV=ProteinV,FatH=FatH,FatV=FatV,FiberL=FiberL,FiberV=FiberV,SodiumH=SodiumH,SodiumV=SodiumV,SugarH=SugarH,SugarV=SugarV,SatFatH=SatFatH,SatFatV=SatFatV,CholesterolH=CholesterolH,CholesterolV=CholesterolV)
    Supple=Supplements(sup1="영양진단 영양제1",sup2="영양진단 영양제2",sup3="영양진단 영양제3",sup4="영양진단 영양제4",inter1="근력",inter2="소화기/장건강",inter3="면역력")
    img_adress=create_basic_pdf(Nutri,Vita,Inbo,Age,Name,Gender,NutriD,Supple,Store,Activity,Age)

    return img_adress

def process_diet_inputs(Name,GWeight,NMeal,RCal,Period,FoodR,WorkOutR,InbodyScore,Weight,BodyFat,BMI,ApproWeight,WeightMax,MuscleMax,FatMax,MuscleControl,FatFree,SkeletalMuscle,UpperLF,UpperRF,LowerLF,LowerRF,UpperLS,UpperRS,LowerLS,LowerRS,Rating,Rank):
    DGoal=DietGoal(Gweight=GWeight,NMeal=NMeal,Rcal=RCal,Period=Period,FoodR=FoodR,WorkOutR=WorkOutR)
    Inbo=Inbody(InbodyScore=InbodyScore,Weight=Weight,BodyFat=BodyFat,BMI=BMI,ApproWeight=ApproWeight,WeightMax=WeightMax,MuscleMax=MuscleMax,FatMax=FatMax,MuscleControl=MuscleControl,FatFree=FatFree,SkeletalMuscle=SkeletalMuscle)
    InboD=InbodyDetail(UpperLF=UpperLF,UpperRF=UpperRF,LowerLF=LowerLF,LowerRF=LowerRF,UpperLS=UpperLS,UpperRS=UpperRS,LowerLS=LowerLS,LowerRS=LowerRS)
    Age=Agesensor(Rating=Rating,Rank=Rank)

    img_adress=create_diet_pdf(Name,Inbo,Age,DGoal,InboD)

    return img_adress

def process_skin_inputs(Name,Concern,Type,TZWater,UZWater,TZOil,UZOil,CScore,CAScore,CState,WScore,WAScore,WState,TScore,TAScore,TState,HScore,HAScore,HState,Rating,Rank):
    Skin=SkinState(Concern=Concern,Type=Type,TZWater=TZWater,UZWater=UZWater,TZOil=TZOil,UZOil=UZOil,CScore=CScore,CAScore=CAScore,CState=CState,WScore=WScore,WAScore=WAScore,WState=WState,TScore=TScore,TAScore=TAScore,TState=TState,HScore=HScore,HAScore=HAScore,HState=HState)
    Age=Agesensor(Rating=Rating,Rank=Rank)
    img_adress=create_skin_pdf(Name,Skin,Age)

    return img_adress


with gr.Blocks() as basic_health:
    gr.Markdown("""<h1 style = 'border-radius: 5px; padding-top: 10px; padding-bottom: 10px;'>기본건강 고객정보 입력</h1>""")
    with gr.Row():
        Name=gr.Textbox(label="이름",placeholder="내담자명을 입력해주세요",elem_id="name")
        Gender=gr.Radio(['남성','여성'],label="성별")
        Height=gr.Number(minimum=0,maximum=300,label="키(cm)")
        Age=gr.Number(minimum=0,maximum=200,label="나이(만)")
        Store=gr.Dropdown(['판교점','중동점','본사'],label="지점")
        Activity=gr.Dropdown(['비활동적','저활동적','활동적','매우 활동적'],label="활동량")
    
    with gr.Column():
        gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>1. 영양진단</h2>""")
        EatScore=gr.Number(minimum=0, maximum=100,label="Eat Score")
        with gr.Column():
            with gr.Row():
                Carb=gr.Radio(["과다", "적정", "부족"], label="탄수화물",min_width=60)
                Protein=gr.Radio(["과다", "적정", "부족"], label="단백질",min_width=60)
                Fat=gr.Radio(["과다", "적정", "부족"], label="지방",min_width=60)
                Fiber=gr.Radio(["적정", "부족"], label="식이섬유",min_width=60)
            with gr.Row():
                CarbH=gr.Number(minimum=0,maximum=1000, label="탄수화물 최대값",min_width=60)
                CarbV=gr.Number(minimum=0,maximum=1000, label="탄수화물 섭취량",min_width=60)
                ProteinL=gr.Number(minimum=0,maximum=1000,label="단백질 최소값",min_width=60)
                ProteinV=gr.Number(minimum=0,maximum=1000,label="단백질 섭취량",min_width=60)
                FatH=gr.Number(minimum=0,maximum=1000,label="지방 최소값",min_width=60)
                FatV=gr.Number(minimum=0,maximum=1000,label="지방 섭취량",min_width=60)
                FiberL=gr.Number(minimum=0,maximum=1000,label="식이섬유 최소값",min_width=60)
                FiberV=gr.Number(minimum=0,maximum=1000,label="식이섬유 섭취량",min_width=60)    
            with gr.Row():
                Sodium=gr.Radio(["과다", "적정"], label="나트륨",min_width=60)
                Sugar=gr.Radio(["과다", "적정"], label="당류",min_width=60)
                SatFat=gr.Radio(["과다", "적정"], label="포화지방",min_width=60)
                Cholesterol=gr.Radio(["과다", "적정"], label="콜레스테롤",min_width=60)
            with gr.Row():
                SodiumH=gr.Number(minimum=0,maximum=1000, label="나트륨 최대값",min_width=60)
                SodiumV=gr.Number(minimum=0,maximum=1000, label="나트륨 섭취량",min_width=60)
                SugarH=gr.Number(minimum=0,maximum=1000,label="당류 최대값",min_width=60)
                SugarV=gr.Number(minimum=0,maximum=1000,label="당류 섭취량",min_width=60)
                SatFatH=gr.Number(minimum=0,maximum=1000,label="포화지방 최대값",min_width=60)
                SatFatV=gr.Number(minimum=0,maximum=1000,label="포화지방 섭취량",min_width=60)
                CholesterolH=gr.Number(minimum=0,maximum=1000,label="콜레스테롤 최대값",min_width=60)
                CholesterolV=gr.Number(minimum=0,maximum=1000,label="콜레스테롤 섭취량",min_width=60)     

    with gr.Column():
        gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>2. 비타스틱</h2>""")
        with gr.Column():
            # 체크박스 추가
            unused = gr.Checkbox(label="미사용", value=False, min_width=60)
            with gr.Row():
                Biotin=gr.Radio(["낮은", "경미"], label="비오틴",min_width=60)                    
                VitC=gr.Radio(["낮은", "경미"], label="비타민C",min_width=60)
                Mg=gr.Radio(["낮은", "경미"], label="마그네슘",min_width=60)
                VitB1=gr.Radio(["낮은", "경미"], label="비타민 B1",min_width=60) 
                VitB2=gr.Radio(["낮은", "경미"], label="비타민 B2",min_width=60)

            with gr.Row():
                Zn=gr.Radio(["낮은", "경미"], label="아연",min_width=60)
                Se=gr.Radio(["낮은", "경미"], label="셀레늄",min_width=60)
                VitB6=gr.Radio(["낮은", "경미"], label="비타민 B6",min_width=60)
                VitE=gr.Radio(["낮은", "경미"], label="비타민 E",min_width=60) 
                Folate=gr.Radio(["낮은", "경미"], label="엽산",min_width=60)     

    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>3. 인바디</h2>""")
    with gr.Row():
        InbodyScore=gr.Number(minimum=0, maximum=100, label="인바디 점수",min_width=80)
        Weight=gr.Number(minimum=0, maximum=300, label="체중",min_width=80)
        BodyFat=gr.Number(minimum=0, maximum=100, label="체지방량",min_width=80)
        ApproWeight=gr.Number(minimum=0, maximum=300, label="적정체중",min_width=80)
        FatFree=gr.Number(minimum=0, maximum=300, label="제지방량",min_width=80)

        WeightMax=gr.Number(minimum=0, maximum=200, label="체중 정상벙위 상한",min_width=80)
        MuscleMax=gr.Number(minimum=0, maximum=200, label="근육 정상범위 상한",min_width=80)
        FatMax=gr.Number(minimum=0, maximum=200, label="지방 정상범위 상한",min_width=80)
        Recomcal=gr.Number(minimum=0, maximum=10000,label="권장열량",min_width=80)
        SkeletalMuscle=gr.Number(minimum=0, maximum=1000,label="골격근량",min_width=80)

    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>4. Age Sensor</h2>""")
    with gr.Row():
        Rating=gr.Dropdown(["A","B","C","D","E"], label="등급(A ~ E)")
        Rank=gr.Number(value=None, minimum=0, maximum=100, label="등수(1 ~ 100)")    
        
    generate_btn = gr.Button("결과보기")
    output_image = gr.Image()

    generate_btn.click(
        fn=process_basic_inputs,
        inputs=[Name,Gender,Height,Store,Activity,Age,
                EatScore,Carb,Protein,Fat,Fiber,Sodium,Sugar,SatFat,Cholesterol,
                unused,Biotin,VitC,Mg,VitB1,VitB2,Zn,Se,VitB6,VitE,Folate,
                InbodyScore,Weight,BodyFat,ApproWeight,FatFree,WeightMax,MuscleMax,FatMax,Recomcal,SkeletalMuscle,
                Rating,Rank,
                CarbH,CarbV,ProteinL,ProteinV,FatH,FatV,FiberL,FiberV,SodiumH,SodiumV,SugarH,SugarV,SatFatH,SatFatV,CholesterolH,CholesterolV],
        outputs=output_image
    )

with gr.Blocks() as diet:
    gr.Markdown("""<h1 style = 'border-radius: 5px; padding-top: 10px; padding-bottom: 10px;'>다이어트 고객정보 입력</h1>""")
    Name=gr.Textbox(label="이름",placeholder="내담자명을 입력해주세요",elem_id="name")  

    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>1. 체중조절 목표</h2>""")
    with gr.Row():
        GWeight=gr.Number(minimum=0, maximum=300, label="목표체중",min_width=80)
        NMeal=gr.Number(minimum=0, maximum=5, label="섭취 끼니",min_width=80)
        RCal=gr.Number(minimum=0, maximum=4000, label="권장칼로리",min_width=80)
        Period=gr.Dropdown(["2주","3주","4주","2달","3달","4달","5달"], label="감량기간")

    with gr.Row():
        slider = gr.Slider(minimum=0, maximum=10,step=1, value=5, label="식사 : 운동 비율")
        FoodR = gr.Number(value=5, label="식사", interactive=False)
        WorkOutR = gr.Number(value=5, label="운동", interactive=False)
        slider.change(fn=update_ratio, inputs=slider, outputs=[FoodR, WorkOutR])    

    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>2. 인바디</h2>""")
    gr.HTML("""<h3 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>인바디 기본정보</h3>""")
    with gr.Row():
        InbodyScore=gr.Number(minimum=0, maximum=100, label="인바디 점수",min_width=80)
        Weight=gr.Number(minimum=0, maximum=300, label="체중",min_width=80)
        BodyFat=gr.Number(minimum=0, maximum=100, label="체지방량",min_width=80)
        Bmi=gr.Number(minimum=0, maximum=100, label="BMI",min_width=80)
        ApproWeight=gr.Number(minimum=0, maximum=300, label="적정체중",min_width=80)
        WeightMax=gr.Number(minimum=0, maximum=200, label="체중 정상범위 상한",min_width=80)
        MuscleMax=gr.Number(minimum=0, maximum=200, label="근육 정상범위 상한",min_width=80)
        FatMax=gr.Number(minimum=0, maximum=200, label="지방 정상범위 상한",min_width=80)
        MuscleControl=gr.Number(minimum=-100,maximum=100,label="근육조절",min_width=80)
        FatFree=gr.Number(minimum=0, maximum=100, label="제지방량",min_width=80)
        SkeletalMuscle=gr.Number(minimum=0, maximum=1000, label="골격근량",min_width=80)


    gr.HTML("""<h3 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>집중관리 부위</h3>""")
    with gr.Row():
        with gr.Group():
            gr.HTML("""<h5 style = 'text-indent: 10px; padding-top: 5px; padding-bottom: 5px; background-color: white;'>체지방량</h5>""")
            with gr.Row():
                UpperLF=gr.Radio(["이하", "표준","이상"], label="상체 왼쪽",min_width=80)
                UpperRF=gr.Radio(["이하", "표준","이상"], label="상체 오른쪽",min_width=80)
            with gr.Row():
                LowerLF=gr.Radio(["이하", "표준","이상"], label="하체 왼쪽",min_width=80)
                LowerRF=gr.Radio(["이하", "표준","이상"], label="하체 오른쪽",min_width=80)

        with gr.Group():
            gr.HTML("""<h5 style = 'text-indent: 10px; padding-top: 5px; padding-bottom: 5px; background-color: white;'>골격근량</h5>""")
            with gr.Row():
                UpperLS=gr.Radio(["이하", "표준","이상"], label="상체 왼쪽",min_width=80)
                UpperRS=gr.Radio(["이하", "표준","이상"], label="상체 오른쪽",min_width=80)
            with gr.Row():
                LowerLS=gr.Radio(["이하", "표준","이상"], label="하체 왼쪽",min_width=80)
                LowerRS=gr.Radio(["이하", "표준","이상"], label="하체 오른쪽",min_width=80)                   
                

    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>4. Age Sensor</h2>""")
    with gr.Row():
        Rating=gr.Dropdown(["A","B","C","D","E"], label="등급(A ~ E)")
        Rank=gr.Number(value=None, minimum=0, maximum=100, label="등수(1 ~ 100)")        
        
    generate_btn = gr.Button("결과보기")
    output_image = gr.Image()

    generate_btn.click(
        fn=process_diet_inputs,
        inputs=[Name,GWeight,NMeal,RCal,Period,FoodR,WorkOutR,InbodyScore,Weight,BodyFat,Bmi,ApproWeight,WeightMax,MuscleMax,FatMax,MuscleControl,FatFree,SkeletalMuscle,UpperLF,UpperRF,LowerLF,LowerRF,UpperLS,UpperRS,LowerLS,LowerRS,Rating,Rank],
        outputs=output_image
    )    
 

with gr.Blocks() as skin:
    gr.Markdown("""<h1 style = 'border-radius: 5px; padding-top: 10px; padding-bottom: 10px;'>미용 고객정보 입력</h1>""")
    Name=gr.Textbox(label="이름",placeholder="내담자명을 입력해주세요",elem_id="name")  
    
    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>1. 피부측정</h2>""")
    with gr.Row():
        Concern=gr.CheckboxGroup(["유/수분 밸런스", "민감성(여드름)","잡티","주름","모공크기"],label="고객 피부 고민")
        Type=gr.Radio(["건성", "지성","복합성"],label="보습")

    with gr.Group():
        gr.HTML("""<h5 style = 'text-indent: 10px; padding-top: 5px; padding-bottom: 5px; background-color: white;'>수분</h5>""")
        with gr.Row():
            TZWater=gr.Radio(["Normal", "Moisture","Dehydrated"], label="T ZONE",min_width=80)
            UZWater=gr.Radio(["Normal", "Moisture","Dehydrated"], label="U ZONE",min_width=80)
        gr.HTML("""<h5 style = 'text-indent: 10px; padding-top: 5px; padding-bottom: 5px; background-color: white;'>유분</h5>""")    
        with gr.Row():
            TZOil=gr.Radio(["Low", "Sebum","High"], label="T ZONE",min_width=80)
            UZOil=gr.Radio(["Low", "Sebum","High"], label="U ZONE",min_width=80)    

    with gr.Group():
        gr.HTML("""<h5 style = 'text-indent: 10px; padding-top: 5px; padding-bottom: 5px; background-color: white;'>색소</h5>""")  
        with gr.Row():
            CScore=gr.Number(minimum=0, maximum=100, label="종합점수",min_width=80,scale=1)
            CAScore=gr.Number(minimum=0, maximum=100, label="연령대 평균점수",min_width=80,scale=1)
            CState=gr.Radio(["깨끗함", "거의 깨끗함","보통","나쁨","매우 나쁨"], label="피부상태",min_width=80,scale=2)
        gr.HTML("""<h5 style = 'text-indent: 10px; padding-top: 5px; padding-bottom: 5px; background-color: white;'>주름</h5>""") 
        with gr.Row():
            WScore=gr.Number(minimum=0, maximum=100, label="종합점수",min_width=80,scale=1)
            WAScore=gr.Number(minimum=0, maximum=100, label="연령대 평균점수",min_width=80,scale=1)
            WState=gr.Radio(["깨끗함", "거의 깨끗함","보통","나쁨","매우 나쁨"], label="피부상태",min_width=80,scale=2)  
        gr.HTML("""<h5 style = 'text-indent: 10px; padding-top: 5px; padding-bottom: 5px; background-color: white;'>여드름(민감)</h5>""") 
        with gr.Row():
            TScore=gr.Number(minimum=0, maximum=100, label="종합점수",min_width=80,scale=1)
            TAScore=gr.Number(minimum=0, maximum=100, label="연령대 평균점수",min_width=80,scale=1)
            TState=gr.Radio(["깨끗함", "거의 깨끗함","보통","나쁨","매우 나쁨"], label="피부상태",min_width=80,scale=2)       
        gr.HTML("""<h5 style = 'text-indent: 10px; padding-top: 5px; padding-bottom: 5px; background-color: white;'>모공</h5>""") 
        with gr.Row():
            HScore=gr.Number(minimum=0, maximum=100, label="종합점수",min_width=80,scale=1)
            HAScore=gr.Number(minimum=0, maximum=100, label="연령대 평균점수",min_width=80,scale=1)
            HState=gr.Radio(["깨끗함", "거의 깨끗함","보통","나쁨","매우 나쁨"], label="피부상태",min_width=80,scale=2)       
        
    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>2. Age Sensor</h2>""")
    with gr.Row():
        Rating=gr.Dropdown(["A","B","C","D","E"], label="등급(A ~ E)")
        Rank=gr.Number(value=None, minimum=0, maximum=100, label="등수(1 ~ 100)")        
        
    generate_btn = gr.Button("결과보기")
    output_image = gr.Image()

    generate_btn.click(
        fn=process_skin_inputs,
        inputs=[Name,Concern,Type,TZWater,UZWater,TZOil,UZOil,CScore,CAScore,CState,WScore,WAScore,WState,TScore,TAScore,TState,HScore,HAScore,HState,Rating,Rank],
        outputs=output_image
    )      


demo = gr.TabbedInterface([basic_health, diet,skin], ["기본건강", "다이어트","피부미용"])
demo.launch()

