from django.db import models


# 차량정보
class Car(models.Model):
    car_weight_choice = (
        ('1톤', '1톤'), ('2.5톤', '2.5톤'), ('5톤', '5톤'), ('기타', '기타')
    )
    weight = models.CharField(choices=car_weight_choice, max_length=5)  # 차량무게


# 이사업체 정보
class Company(models.Model):
    name = models.CharField(max_length=50)                           # 업체명
    owner_name = models.CharField(max_length=20)                     # 대표이사 이름
    tel = models.CharField(max_length=11)                            # 연락처
    address = models.CharField(max_length=50)                        # 주소
    registration_number = models.CharField(unique=True, max_length=10) # 사업자번호
    registration_date = models.DateField()                           # 사업자등록일자
    workers_count = models.IntegerField()                            # 직원수
    cars_count = models.ManyToManyField(Car, through='CompanyCarCount', blank=True) # 차량수
    is_matching = models.BooleanField(default=False)                 # 매칭가능여부


# 업체당 차량별 댓수 정보
class CompanyCarCount(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)          # 차 FK
    count = models.IntegerField(default=0)                          # 차 댓수
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # 이사업체 정보 FK


# 고객정보
class Customer(models.Model):
    name = models.CharField(max_length=10)                  # 고객이름
    tel = models.CharField(max_length=11)                   # 연락처
    joined_date = models.DateTimeField(auto_now_add=True)   # 등록일
    is_agree_terms = models.BooleanField(default=False)     # 이용약관동의여부
    is_agree_third_party = models.BooleanField(default=False)   # 견적요청을 위한 개인정보 제3자 제공동의여부
    is_agree_marketing = models.BooleanField(default=False) # 마케팅 정보수신 동의여부


# 고객 피드백 이력
class MoveFeedback(models.Model):
    level_choice = (
        (5, '매우만족'),
        (4, '만족'),
        (3, '보통'),
        (2, '불만족'),
        (1, '매우불만족')
    )
    company = models.ForeignKey(Company, models.CASCADE)            # 업체정보 FK
    is_agree_public = models.BooleanField(default=False)            # 정보공개동의여부
    professional_level = models.IntegerField(choices=level_choice)  # 전문성 만족도
    price_level = models.IntegerField(choices=level_choice)         # 가격 만족도
    kindness_level = models.IntegerField(choices=level_choice)      # 친절 만족도
    is_revisit = models.BooleanField(default=False)                 # 재방문 의사
    contract_price = models.IntegerField()                          # 계약가격
    move_date = models.DateField()                                  # 이사일
    created_date = models.DateTimeField(auto_now_add=True)          # 피드백 작성일
    content = models.CharField(max_length=1000)                     # 피드백 내용


# 가정이사 신청정보
class RequestHouseMove(models.Model):
    customer = models.ForeignKey(Customer, models.CASCADE)  # 고객정보 FK
    starting_address = models.CharField(max_length=50)      # 출발지 주소정보
    starting_floors = models.CharField(max_length=8)        # 출발지 층수
    destination_address = models.CharField(max_length=50)   # 도착지 주소정보
    destination_floors = models.CharField(max_length=8)     # 도착지 층수
    move_date = models.DateField()                          # 요청이사일자
    is_storage = models.BooleanField(default=False)         # 보관이사 여부
    feedback = models.OneToOneField(MoveFeedback, on_delete=models.CASCADE, null=True)  # 피드백

