import gradio as gr
from dataclass import Nutrition,Vitastiq,Inbody,Agesensor
from createpdf import create_pdf


def process_inputs(Name,EatScore,Carb,Protein,Fat,Fiber,Sodium,Sugar,SatFat,Cholesterol,Biotin,VitC,Mg,VitB1,VitB2,Zn,Se,VitB6,VitE,Folate,InbodyScore,Weight,BodyFat,ApproWeight,FatFree,WeightControl,MuscleControl,FatControl,Rating,Rank):
    Nutri=Nutrition(EatScore=EatScore, Carb=Carb, Protein=Protein, Fat=Fat, Fiber=Fiber, Sodium=Sodium, Sugar=Sugar, SatFat=SatFat, Cholesterol=Cholesterol)
    Vita=Vitastiq(Biotin=Biotin, VitC=VitC, Mg=Mg, VitB1=VitB1, VitB2=VitB2, Zn=Zn, Se=Se, VitB6=VitB6, VitE=VitE, Folate=Folate)
    Inbo=Inbody(InbodyScore,Weight,BodyFat,ApproWeight,FatFree,WeightControl,MuscleControl,FatControl)
    Age=Agesensor(Rating,Rank)

    img_adress=create_pdf(Nutri,Vita,Inbo,Age,Name)

    return img_adress

with gr.Blocks() as demo:
    gr.Markdown("""<h1>기본건강 종합결과 산출</h1>""")
    Name=gr.Textbox(label="이름",placeholder="내담자명을 입력해주세요",elem_id="name")
    
    with gr.Row(equal_height=True):
        with gr.Column():
            gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>1. 영양진단</h2>""")
            EatScore=gr.Number(minimum=0, maximum=100,label="Eat Score")
            with gr.Row():
                with gr.Column(min_width=200):
                    Carb=gr.Radio(["과다", "적정", "부족"], label="탄수화물")
                    Protein=gr.Radio(["과다", "적정", "부족"], label="단백질")
                    Fat=gr.Radio(["과다", "적정", "부족"], label="지방")
                    Fiber=gr.Radio(["적정", "부족"], label="식이섬유")
                with gr.Column(min_width=200):
                    Sodium=gr.Radio(["과다", "적정"], label="나트륨")
                    Sugar=gr.Radio(["과다", "적정"], label="당류")
                    SatFat=gr.Radio(["과다", "적정"], label="포화지방")
                    Cholesterol=gr.Radio(["과다", "적정"], label="콜레스테롤")

        with gr.Column():
            gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>2. 비타스틱</h2>""")
            with gr.Row():
                with gr.Column(min_width=200):
                    Biotin=gr.Radio(["낮은", "경미"], label="비오틴")
                    VitC=gr.Radio(["낮은", "경미"], label="비타민C")
                    Mg=gr.Radio(["낮은", "경미"], label="마그네슘")
                    VitB1=gr.Radio(["낮은", "경미"], label="비타민 B1") 
                    VitB2=gr.Radio(["낮은", "경미"], label="비타민 B2")

                with gr.Column(min_width=200):
                    Zn=gr.Radio(["낮은", "경미"], label="아연")
                    Se=gr.Radio(["낮은", "경미"], label="셀레늄")
                    VitB6=gr.Radio(["낮은", "경미"], label="비타민 B6")
                    VitE=gr.Radio(["낮은", "경미"], label="비타민 E") 
                    Folate=gr.Radio(["낮은", "경미"], label="엽산")     

    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>3. 인바디</h2>""")
    with gr.Row():
        InbodyScore=gr.Number(minimum=0, maximum=100, label="인바디 점수")
        Weight=gr.Number(minimum=0, maximum=300, label="체중")
        BodyFat=gr.Number(minimum=0, maximum=100, label="체지방량")
        ApproWeight=gr.Number(minimum=0, maximum=300, label="적정체중")
        FatFree=gr.Number(minimum=0, maximum=300, label="제지방량")

        WeightControl=gr.Number(minimum=-100, maximum=100, label="체중조절")
        MuscleControl=gr.Number(minimum=-100, maximum=100, label="근육조절")
        FatControl=gr.Number(minimum=-100, maximum=100, label="지방조절")

    gr.HTML("""<h2 style = 'border-radius: 5px; text-indent: 10px; padding-top: 5px; padding-bottom: 5px;'>4. Age Sensor</h2>""")
    with gr.Row():
        Rating=gr.Dropdown(["A","B","C","D","E"], label="등급(A ~ E)")
        Rank=gr.Number(value=None, minimum=0, maximum=100, label="등수(1 ~ 100)")    
        
    generate_btn = gr.Button("결과보기")
    output_image = gr.Image()

    generate_btn.click(
        fn=process_inputs,
        inputs=[Name,EatScore,Carb,Protein,Fat,Fiber,Sodium,Sugar,SatFat,Cholesterol,Biotin,VitC,Mg,VitB1,VitB2,Zn,Se,VitB6,VitE,Folate,InbodyScore,Weight,BodyFat,ApproWeight,FatFree,WeightControl,MuscleControl,FatControl,Rating,Rank],
        outputs=output_image
    )

demo.launch(share=True)

