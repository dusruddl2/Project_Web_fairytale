from django.shortcuts import render

# Create your views here.

import json
import openai

openai.api_key = "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"

# Create your views here.

def func_Make(request):
    return render(request, 'ProjectFinal/make.html')

def func_Fairytale(request):
    character_name = request.GET.get('character_name')
    character_age = request.GET.get('character_age')
    character_gender = request.GET.get('character_gender')
    character_personality = request.GET.get('character_personality')

    listener_age = request.GET.get('listener_age')
    listener_gender = request.GET.get('listener_gender')

    detail_mood = request.GET.get('detail_mood')
    detail_keyword = request.GET.get('detail_keyword')
    detail_length = request.GET.get('detail_length')

    context = {
        "character_name": character_name,
        "character_age": character_age,
        "character_gender": character_gender,
        "character_personality": character_personality,

        "listener_age": listener_age,
        "listener_gender": listener_gender,

        "detail_mood": detail_mood,
        "detail_keyword": detail_keyword,
        "detail_length": detail_length
    }

    context['ask_str'] = make_question(context)
    context['result_chatgpt'] = eval(openapi_chatgpt(context['ask_str']))

    context['detail_length'] = len(context['result_chatgpt'])
    context['result_content'] = ""
    context['result_background'] = ""

    if "chapter_1" in context['result_chatgpt'] :
        context['result_title'] = context['result_chatgpt']['chapter_1']['chapter_title']
        for i in range(1, context['detail_length']):
            type_name = f"chapter_{i}"
            context['result_content'] += context['result_chatgpt'][type_name]['chapter_content']
            context['result_background'] += context['result_chatgpt'][type_name]['chapter_background']
            # print(context['result_chatgpt'][type_name]['chapter_background'])
    else:
        for i in range(1, context['detail_length']):
            context['result_title'] = context['result_chatgpt']['chapter1']['chapter_title']
            type_name = f"chapter{i}"
            context['result_content'] += context['result_chatgpt'][type_name]['chapter_content']
            context['result_background'] += context['result_chatgpt'][type_name]['chapter_background']
            # print(context['result_chatgpt'][type_name]['chapter_background'])

    context['result_image'] = openapi_dalle(context['result_background'],1,'1024x1024')

    print(context['result_content'])
    print(context['result_image'])
    return render(request, 'ProjectFinal/fairytale.html', context)



def openapi_chatgpt(question):

    completion = openai.ChatCompletion.create(
      model = 'gpt-3.5-turbo',
      messages = [
          {"role": "system", "content": "You are a helpful assistant."},
          {"role": "user", "content": f"{question}"},
      ],
      temperature = 0
    )
    return completion['choices'][0]['message']['content']

def openapi_dalle(description, img_cnt , img_size):
    response = openai.Image.create(
        prompt = description,
        n = img_cnt,
        size = img_size
    )
    return response['data'][0]['url']


def make_question(input_info):
    result_str = f"Can you make a story in the form of 'JSON' using the following conditions by {input_info['detail_length']} chapters? Each chapter should include"
    result_str += f"(1) ‘chapter_number’ (2) ‘chapter_title‘ (3) ‘chapter_content’ (at least 5 sentences) (4) ‘chapter_atmosphere’ (5) ‘chapter_background’"
    result_str += f"1. Characters 1-1. Main character 1-1-1. name: {input_info['character_name']} 1-1-2. gender: {input_info['character_gender']} 1-1-3. characteristics: {input_info['character_personality']}"
    #     result_str += f"1-2. Sub character 1-2-1. name: {} 1-2-2. gender: {} 1-2-3. characteristics: {}"
    result_str += f"2. Target audience 2-1. age: {input_info['listener_age']} 2-2. gender: {input_info['listener_gender']}"
    result_str += f"3. Story 3-1. keyword: {input_info['detail_keyword']} 3-2. atmosphere: {input_info['detail_mood']} 3-3. the number of chapters: {input_info['detail_length']}"

    return result_str

def make_question_kor(input_info):
    result_str = f"나는 {input_info['listener_age']}살 {input_info['listener_gender']} 아이를 위해 {input_info['detail_keyword']}가 주제인 동화를 제작하려 해."
    result_str += f"주인공 이름은 {input_info['character_name']}이며 성별은 {input_info['character_gender']}이고 {input_info['character_personality']}으면 좋겠어."
    result_str += f"결과적으로 나는 그 아이를 위해 {input_info['detail_mood']}느낌나는 동화를 제작하려 해. 동화의 길이는 총 {input_info['detail_length']} 챕터로 구성해줘. "
    result_str += f"동화의 구성은 챕터 순차번호인 'chapter_idx', 챕터 타이틀인 'chapter_title' , 챕터 내용인 'chapter_content',"
    result_str += f"각 챕터의 분위기를 나타내는 'chapter_mood',  각 챕터가 발생한 장소를 설명한 'chapter_background'로 나타내줘."
    result_str += f"'chapter_title'은 1개의 문장, 'chapter_content'는 최소 5줄의 문장으로 구성해줬으면 해. "
    result_str += f"마지막으로 'character'이라는 변수에 주인공 이름인 'name'과 주인공 생김새인 'face'로 추가해줘."
    result_str += f"또 주인공과 같이 나오는 조연들은 'sub_character'이라는 변수에 각 조연들의 이름을'sub_name', "
    result_str += f"조연들의 생김새는 'sub_face'에 넣어줘. "
    result_str += f"최종적으로 dictionary 형식의 데이터만 결과값으로 나에게 줘."

    return result_str

# def make_story(fairytale_info, fairytale_len):
#     result_str = ""
#
#     for i in range(1, len(fairytale_len)):
#         chapter_type = f"chapter_{i}"
#         print(f"{i} >>>>>>>>>>> {fairytale_info[chapter_type]['chapter_content']}")
#         result_str += f"{fairytale_info[chapter_type]['chapter_content']}"
#         result_str += "\n"
#
#     return result_str