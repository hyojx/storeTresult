<h2>작성된 파일에 대한 간단한 설명</h2>

**1. app.py**
- gradio 인터페이스 실행하여 input 수집
- 측정결과를 받아서 dataclass로 저장하고 pdf 생성함수를 호출

**2. create_pdf**
- 전달된 input 받아서 pdf 파일생성
- 이미지로 변환하여 저장하고 이미지 파일 주소를 반환

**3. dataclass**
- 구현에 필요한 dataclass
- 측정하는 기기 별로 구성