## 컬럼간 종속관계 파악해 묶어서 확인하기

## Null

## 기타 garbage

## col by col

### key cols
- apartment_id
  - Data Type : Category
  - ***train에 없는 아파트 값이 test에는 존재***
- city
  - Data Type : 1/0 binary
  - train에는 6:10, test에는 5:10 정도로 부산:서울
  - 당연히 서울이 비쌈

- transaction_real_price
  - Data Type : 연속형
  - log를 씌우면 정규분포에 가까워 진다.

### feature cols

#### Date

- transaction_year_month
  - yyyymm 형태의 연속형 변수
- transaction_date
  - 연속형? 주기성이 있는 연속형? 카테고리?
  - **전처리 : 말 일 날짜를 합치자**
- 날짜 정보 합치기
  - 마지막날로 합치는 것보다는 시작날 1일 기준으로 합치는 게 나을 듯
- 추가적인 날짜 정보 : 시계열의 특성
  - ***주기성이 있는지?***

#### 위치 정보 - 단지 정보와 연관

- 위치 특성은 단지 단위로 특정되어 있다.
- 위/경도를 따로 쓸 필요 없이 단지 정보로 대체 가능
- ***법정동 코드를 활용해서 구/동 수준으로 새로운 피처 생산 가능***
- latitude
- longitude
- address_by_law

#### 단지 정보, 건물 정보

- ***같은 단지끼리는 유니크한가?***
- ***단지 종속적인 변수는 어떻게 묶을 것인가***
  - 일단 기본 컬럼도 쓰고, 단지와 묶어서 새로운 피처를 만들고
- year_of_completion
  - 연속형 변수
- total_parking_capacity_in_site
  - 연속형, 이산형
  - Null이 많다
    - 주차대수를 타겟으로 추정하기
- total_household_count_in_sites
  - 이산형,
  - Null 없음
- apartment_building_count_in_sites
  - 단지에 매우 종속적인 것처럼 보인다.
  - Null 없음
- tallest_building_in_sites
  - 이산형
  - 의미 : 얼마나 고층 빌딩이냐?
  - 단지와 크게 붙는 속성일 듯
- total_household_count_of_area_type
  - ***단지 단위는 아님***
  - ***뭔가 이용할 수 있을 거 같은데 지금은 안 떠오름***
  - Null 없음, 이산형
- lowest_building_in_sites : 최저층 동의 수?
  - Null 조금, 이산형
  - 커질수록 단지 종속적
- heat_type
  - 개별난방 vs 구역난방 vs 중앙난방 + Null
    - 이걸 타겟값으로 학습..??
  - ***난방연료와 관계***
- heat_fuel
  - ***가스 vs 열병합 + Null***
    - 열병합은 지역 종속적인데 위치 정보로 추론할 것인가
    - 난방 방식과도 관련 있을 듯
  - 열병합이 좀 더 비쌈

#### 개별 집 정보

- exclusive_use_area
  - 연속형 변수 : 어떻게 보면 이산형
  - 매우 가격과 상관관계가 큼
- floor
  - 이산형, 연속형
  - 일단 층이 올라가면 비싸지는 경향
  - ***이게 '고층 건물'이 비싼 건지,
    층이 높아서 비싼 건지 구별할 필요가 있음***
    - 단지 내 최고층 수와 비교할 것!!!
- ***supply_area*** : 공급면적=전용면적+공용면적
  - 이산형
  - Null 없음
  - room_id와 굉장히 상관관계
    - ***room_id를 빼면 단지의 공용면적 추정도 가능***
- ***room_id*** : 전용면적 평형 아이디
  - (평형 =(전용면적㎡+ 주거공용면적㎡)*0.3025)), (1평형=3.3058㎡)
  - Null 없음, 이산형
  - 추세보다는 특정 평형대가 비싸거나, 싸다 : 단지 종속적인 경향
- room_count
  - Null 좀 있음, 이산형
    - 같은 전용면적, 공급면적으로 추론
- bathroom_count
  - Null 좀 있음, 이산형
    - 같은 전용면적, 공급면적으로 추론
- front_door_structure
  - ***정확하게 무엇을 의미하는지 불분명***
    - 집 현관 말고 아파트 복도를 말하는 건가?
      아니면 집 바닥이 한층 올라와서 구별되어 있는 거?
  - ***계단식 vs 복도식 vs mixed +Null***
    - 아마 단지 자체가 비어있을 듯
    - 음 뭐랑 관계가 있지?
    - 그냥 학습?
