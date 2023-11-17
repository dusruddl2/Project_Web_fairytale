![taleteller](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/80a316ed-1050-45f3-829a-62a7179ed322)
<br>
<br>
# Taleteller

미취학 아동의 양육비 절감, 아동 교육의 발전을 위해 시작한 프로젝트로,<br>
**몇 가지 입력을 통해 다양한 동화를 만들어내는 서비스**입니다.
<br>
**청자에 대한 정보, 원하는 동화의 정보, 동화 주인공의 정보**를 입력 받은 후에, <br>
**ChatGPT를 통해 동화를 생성**하였고
그 옆에 **DALLE2 모델을 통해 동화에 적절한 이미지도 제작**하였습니다.
<br>
<br>
<br>
<br>

# 최종 결과물
[![image](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/d6f1cb61-e52b-41cc-b373-671e06456049)](https://www.notion.so/dusruddl2/22abe16d8c3d4d118aed46b4e7bd5dac)
<br>
<br>
<br>
<br>

# 목차

- [💡 아이디어 배경](#-아이디어-배경)
   - [1. 미취학 아동의 양육비 절감](#1-미취학-아동의-양육비-절감)
   - [2. 디지털 시대의 발전으로 인한 동화책의 온라인 수요 증가](#2-디지털-시대의-발전으로-인한-동화책의-온라인-수요-증가)
   
- [👩🏻‍💻 개발 목표 및 내용](#-개발-목표-및-내용)
   - [목표) ChatGPT와 DALLE2를 이용한 동화 콘텐츠 생성 서비스 개발](#목표-chatgpt와-dalle2를-이용한-동화-콘텐츠-생성-서비스-개발)
   - [1. 생성에 필요한 사전 정보 입력](#1-생성에-필요한-사전-정보-입력)
      - [1-1. 청자에 대한 정보 입력](#1-1-청자에-대한-정보-입력)
      - [1-2. 원하는 동화의 정보 입력](#1-2-원하는-동화의-정보-입력)
      - [1-3. 동화 주인공의 정보 입력](#1-3-동화-주인공의-정보-입력)
   - [+ 로딩 아이콘 제작](#로딩-아이콘-제작)
   - [2. 동화와 일러스트레이션 생성 및 출력](#2-동화와-일러스트레이션-생성-및-출력)
   
- [👩🏻‍💻 개선점 및 추후개발](#-개선점-및-추후개발)
   - [1. 한글 지원](#1-한글-지원)
   - [2. 이미지 입력](#2-이미지-입력)
   - [3. 음성 입력](#3-음성-입력)
   - [4. 챕터 별 구성](#4-챕터-별-구성)
   - [5. 음성 서비스 추가](#5-음성-서비스-추가)
   - [6. 동화 저장](#6-동화-저장)
   
- [📜 서비스 구성 및 구조](#-서비스-구성-및-구조)

- [😊 기대효과 및 활용 방안](#-기대효과-및-활용-방안)
   - [1. 육아 비용 절감에 기여해 가계 부담을 덜어냄](#1-육아-비용-절감에-기여해-가계-부담을-덜어냄)
   - [2. 아동 교육 분야에 활용되어 상호작용적 학습 지원](#2-아동-교육-분야에-활용되어-상호작용적-학습-지원)
   - [3. 동화 작가들에게 영감과 출발점 제공](#3-동화-작가들에게-영감과-출발점-제공)


<br>
<br>
<br>
<br>

# 💡 아이디어 배경
## 1. 미취학 아동의 양육비 절감
학부모들은 매년 신간 도서의 평균 가격 증가로 인해 어린 자녀들을 위한 동화책 구매에 부담을 느끼고 있습니다. 2022년 대한출판문화협회의 발표에 따르면, 발행 도서 평균 가격은 1만 7869원으로 전년 대비 4.4% 증가했다고 합니다. 특히 육아의 특성상 동화책을 대량으로 구매해야 하는 경우가 많기에 동화책 구매가 육아 경제에 큰 부담으로 다가오고 있습니다.
<br>
## 2. 디지털 시대의 발전으로 인한 동화책의 온라인 수요 증가
실제 여러 독서 플랫폼에서는 코로나 이후 아동서적 전자책 대여가 2-3배 가량 증가했다고 발표했습니다. 이에 발맞춰 ‘Taleteller’은 디지털 형태의 혁신적인 동화책 서비스를 제안하며, 기존 동화책과는 달리 상호작용이 가능한 형태를 제공합니다.
<br>
<br>

# 👩🏻‍💻 개발 목표 및 내용

## 목표) ChatGPT와 DALLE2를 이용한 동화 콘텐츠 생성 서비스 개발
## 1. 생성에 필요한 사전 정보 입력
사전 정보를 입력하는 단계는
‘청자INFO’, ‘동화INFO’, ‘주인공INFO’로 나누어져 있습니다.

이때, 모든 정보를 입력하지 않더라도 설정된 초기값에 의해서 동화가 제작됩니다.
### 1-1. 청자에 대한 정보 입력
청자에 따라 원하는 동화가 달라질 수 있기에 나이와 성별을 입력할 수 있습니다.

|입력 전 화면|입력 후 화면|
|------|---|
|![taleteller_청자](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/d885d19c-084b-4c4f-b2b2-250f78feec40)|![taleteller_청자2](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/8dcd10fe-55fd-4321-85a3-f44110bfa847)|
<br>

### 1-2. 원하는 동화의 정보 입력
청자가 원하는 분위기, 주제, 동화의 길이(챕터의 개수)를 입력할 수 있습니다

|입력 전 화면|입력 후 화면|
|------|---|
|![taleteller_동화](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/53a37414-25ab-42da-a231-a929c5ce5e7c)|![taleteller_동화2](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/b407dd47-c767-4234-b4eb-c7b50177c2a0)|
<br>

### 1-3. 동화 주인공의 정보 입력

|입력 전 화면|입력 후 화면|
|------|---|
|![taleteller_주인공](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/e46d796c-e5e2-4536-b6ca-35a903e62af1)|![taleteller_주인공2](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/2ebd33e7-5a31-41aa-ad17-a0e533f22236)|
<br>

### 로딩 아이콘 제작
![loading](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/1f5259cf-14c2-45a7-9de9-e43dc54bd491)


<br>
<br>

## 2. 동화와 일러스트레이션 생성 및 출력

1단계에서 사용자가 입력한 정보를 바탕으로, ChatGPT 3.5 Turbo가 동화를 생성합니다. 질문을 할 때, 추가적으로 각각 챕터의 (1) 번호 (2) 제목 (3) 내용 (4) 분위기 (5) 배경에 대한 정보도 요청하여 제공받습니다. 그리고 챕터에 대한 배경 정보를 DALLE2에게 전달하고 관련 이미지를 생성합니다.
![result](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/1866beb9-3f16-46ed-b41b-04c9efd61b3b)

<br>
<br>

# 👩🏻‍💻 개선점 및 추후개발
## 1. 한글 지원
현재는 토큰 수가 적은 영어 입력만을 제공하고 있지만 한글까지 확장 예정입니다.

## 2. 이미지 입력
3단계로 나눈 사전정보 입력 뿐 아니라 아이의 일기와 글을 통해서도 동화를 제작할 수 있도록 이미지 형태의 입력 방식도 추가할 것입니다. OCR을 이용하여 키워드를 추출하여 입력으로 활용하면 더욱 다양한 콘텐츠를 생성할 수 있습니다.

## 3. 음성 입력
SK텔레콤의 인공지능 스피커인 NUGU와 결합할 수 있도록 음성 입력도 고려하고 있습니다.

## 4. 챕터 별 구성
현재는 각 챕터를 분리하지 않고 모두 합친 결과를 출력하지만, 추후에는 챕터 별로 나눠 이미지를 생성한 후, ‘image-to-video’ 모델을 이용하여 더욱 생동감 있는 동화를 제작할 예정입니다.

## 5. 음성 서비스 추가
Google gTTS를 활용해 text 형태의 동화를 음성으로 변환하여 아이들의 시각뿐 아니라 청각까지 만족시키는 것을 목표로 하고 있습니다.

## 6. 동화 저장
마음에 드는 동화는 저장하여 나중에 다시 볼 수 있고, 이를 기반으로 자신만의 이야기를 만들어내는 창의성을 지원하는 저장 서비스를 추가할 예정입니다.


<br>
<br>

# 📜 서비스 구성 및 구조
![image](https://github.com/dusruddl2/Project_Web_fairytale/assets/81481259/5fd0ef5b-c721-4112-856a-c2799e728ab6)

<br>
<br>

# 😊 기대효과 및 활용 방안
## 1. 육아 비용 절감에 기여해 가계 부담을 덜어냄
동화책은 일반적으로 전집 형태로 구매되며, 새로운 내용을 접하기 위해 다양한 종류의 책을 소유하는 경향이 있습니다. 따라서 한 가정에서 많은 양의 동화책을 소유하게 됩니다. 대한출판문화협회에서 발간한 2022년 출판시장 통계보고서에 따르면 유아, 아동 분야의 서적이 신간 발행 부수 중 25.7%의 가장 많은 비중을 차지하고 있으며, 매출액에서도 1/3을 차지하고 있습니다. 그러나 출산율이 감소하는 현 시대에는 이러한 소비 양상이 가계 부담을 더욱 늘리는 결과로 이어질 수 있습니다. 따라서 동화책 Generative 서비스 ‘Taleteller’는 이러한 문제를 해소하는데 도움을 줄 수 있습니다.

## 2. 아동 교육 분야에 활용되어 상호작용적 학습 지원
2-1) 언어 발달 지원
‘Taleteller’가 생성한 동화를 읽고 듣는 과정에서 어휘력과 문법 능력을 향상시킬 수 있습니다. 또한 사용자가 영어로 input을 제공할 경우 영어 동화도 생성되기 때문에 외국어 발음과 단어 학습에 도움이 됩니다.
2-2) 독서 습관 형성
아이들이 직접 이야기 구조, 캐릭터 개발, 테마 등을 설정함으로써 맞춤형 동화책을 제작할 수 있습니다. 이를 통해 어린이들의 흥미를 끌고 독서를 더욱 즐겁게 만들어 독서 습관을 형성할 수 있습니다.
2-3) 창의적 사고 및 상상력 개발
‘Taleteller’를 통해 생성된 다양한 주제의 동화들을 바탕으로 상상력을 자유롭게 발휘할 수 있습니다. 또한, 추후에 아이들이 직접 동화를 만드는 창의적 글쓰기를 통해 이야기 구조, 캐릭터 개발, 테마 등에 대한 문학적 이해력도 향상시킬 수 있습니다.

## 3. 동화 작가들에게 영감과 출발점 제공
동화 작가들은 종종 새로운 이야기를 창작하는 데 어려움을 겪을 때가 있습니다. ‘Taleteller’은 이들에게 창작과정에서 영감을 제공하고 출발점을 잡아줍니다. 서비스를 통한 다양한 동화 이야기는 작가들에게 창작에 대한 확장적인 시야를 제공할 수 있고 다양한 아이디어를 발굴할 수 있으며, 이를 통해 독창성을 발휘할 수 있습니다.

