# IAM_Drone

드론에서 사욛될 Python 프로그램입니다.

현재 이 코드는 드론의 녹화 관련 코드가 생략된 코드입니다. 

이는 현재 구현 상 녹화 기능을 사용하려면 카메라가 2개 필요하기 때문에, 따로 웹캠 같은 장비가 없으시다면 코드 실행이 불가능하기 때문입니다.

## 의존성
다음의 의존성을 필요로 합니다.
1. `openCV` : 카메라 및 인코딩에 사용
2. `numpy` : openCV의 의존성
3. `bleak` : 블루투스 자동 연결
4. `netifaces` : 네트워크 연결 관련

### 설치방법
pip를 이용해 설치할 수 있습니다.

`pip install opencv-python`

`pip install bleak`

`pip install netifaces`

## 파일에 대한 설명
`DroneServerNoRecord`
: 메인 소스코드입니다. 드론의 기본적인 정보의 송수신을 담당합니다.

`SendStreamByCPU`
: 영상 스트리밍 코드입니다. 현재는 `openCV`를 이용한 CPU 가속을 사용하고 있습니다. `turboJPEG`를 사용한 가속을 사용하였으나, 현재는 어떠한 이유에서인지 정상작동하고 있지 않습니다. 추후 수정 예정입니다.

