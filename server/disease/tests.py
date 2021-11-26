from django.test import TestCase
from .models import Crop, Disease
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from disease import views

# Create your tests here.

crops = Crop.objects.all()
crops = list(crops.values())

diseases= Disease.objects.all()
diseases= list(diseases.values())

class CropApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Crop.objects.create(id=1, name='고추')
        Crop.objects.create(id=2, name='엘리스')
        

    def test_crop(self):
        url = reverse(views.crop_all)

        res = self.client.get(url)
        data = res.json()['data']
 
        # get 요청 확인 테스트
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # 테스트로 생성한 작물과 실제 데이터 베이스에 있는 작물과 같은지 확인
        self.assertEqual(data[0], crops[0])
        

class DiseaseAllApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()        
        

    def test_disease_all(self):
        url = reverse(views.disease_all)
        res = self.client.get(url)
        
        # get 요청 확인 
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        
        # DB 조회 확인 및 수량 확인
        self.assertEqual(len(diseases), 20)

class DiseaseEachApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.id = Crop.objects.create(id=1, name='고추')
        self.id = list(Crop.objects.all().values())[0]['id']
        Disease.objects.create(id=1, crops_id=self.id, name='고추탄저병', english_name='Anthracnose',image='a', symptom="주로 과실에 발생한다. 과실에는 처음에 감염부위가 수침상으로 약간 움푹 들어간 원형반점으로 나타나고, 진전되면 병반이 원형 내지 부정형의 겹무늬 증상으로 확대된다. 병반부위에는 담황색 내지 황갈색의 포자덩어리가 형성되고, 심하게 병든 과실은 비틀어지고 미이라처럼 말라버린다. 성숙과의 병반은 간혹 흑색의 겹무늬 증상을 띄는 것도 있으며, 수확 후 건조하는 과정에서 병 증상이 나타나는 것도 있다.", cause="병원균은 종자 혹은 병든 부위에서 자낭각과 균사의 형태로 겨울을 지내고 1차 전염원이 된다. 병의 전반은 주로 분생포자에 의해 이루어지며, 시설재배 포장보다는 노지포장에서 병 발생이 심하다. 노지포장에서는 여름철 장마기에 분생포자가 주로 비, 바람에 의해 전반된다. 노지재배의 풋고추에서는 7월 초순부터 병이 발생하기 시작하여 수확기까지 계속 발생한다.", prevention=["건전종자를 파종하고, 건전묘를 이식한다.",
        "종자를 소독하여 파종한다.",
        "이 병에 잘 걸리지 않는 품종을 선택하여 재배한다.",
        "등록약제를 병 발생 초기부터 살포한다."], pesticides=[])

    def test_disease_each(self):
        
        url = reverse(views.disease_each, kwargs={'id': 1})
        
        # print(Disease.objects.filter(id=1).values())
        # list(Disease.objects.filter(id=1).values())
        res = self.client.get(url)

        test_data = res.json()['data']['pesticides']=[ "캡틴에이 입상수화제", "새론 수화제", "발라 액제", "델란 입상수화제", "영일베스트 유현탁제", "차세대 수화제", "아리메타실엠지 수화제", "아리베노밀 수화제"]
        test_data = res.json()['data']
 
        # get 요청 확인 
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        # 테스트로 생성한 작물과 실제 데이터 베이스에 있는 작물과 같은지 확인
        self.assertEqual(test_data, diseases[0])