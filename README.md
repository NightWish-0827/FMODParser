# FMODParser
FMOD에서 생성한 Event를 Plugin없이 Audiio.CC에서 Read할 수 있게 해주는 파싱 시스템입니다. 

이 파싱 시스템은 제 레포에 있는 Audio.CC를 사용하지 않으시면 사용하기 어려워요. 

사실 그냥 Json Data 하나 ChartData 하나씩 만 만들면 되는데, 할 줄 알면 내걸 왜 쓰는? 

정신상태가 안좋아짐. 

# Summary

FMOD 를 사용하여 만든 이벤트의 Parameter XML Index 를 Json화 하여 [AudioCC ](https://www.notion.so/AudioCC-397cd118c09f4e66a815f6e08e99671a?pvs=21) 에서 
Read 할 수 있도록 함. 

현재는 리듬 게임 채보 제작에 기능을 충실하게 하여

1. Loop Region 
2. Marker (Named Marker) 
3. BPM Marker

의 값들을 이벤트 XML Index에서 Parsing하여 Json으로 Export. 

# About

1. Loop Region, Marker, BPM Marker. FMOD Studio의 Timeline Base 이벤트를 Read 함
   
2. Read 한 XML 파일을 [AudioCC] 에서 로드할 수 있는 Json 형태로 변환 불필요 값 제거 / 주석
   
3. 폴더 단위 파싱
    
4. 별도 EXE 파일 제공
   
5. Reader / Editor인 [AudioCC] 를 통해 Unity Scriptable Object에 Parsing 한 Data Import 지원

# About Details

- Loop Region, Marker, BPM Marker. FMOD Studio의 Timeline Base 이벤트를 Read 하고 Json 화
    
    
    정상적으로 FMOD Studio의 Project가 생성되었다면 다음과 같은 폴더들이 생성됨. 
    
    ![pic1.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/1143b4b3-9268-4979-a0e7-8e43961108b4/pic1.png)
    
    해당 Project의 Metadata 폴더에 접근하면, Event라는 폴더가 추가로 존재 
    
    ![pic2.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/b6dee976-d10c-4214-b219-35fe0941a45b/pic2.png)
    
    Event 폴더의 내부는 사용자가 FMOD Studio에서 작업한 이벤트들과 해당 이벤트들의 파라미터
    등이 XML Index화 되어 저장되어 있음.
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/14a89072-0af0-4c3e-a1cf-d9c4655a9cf5/image.png)
    
    해당 XML 파일들을 Event 폴더 Parsing 하여 전부 Json화 함.  
    
    Json 양식은 [AudioCC ](https://www.notion.so/AudioCC-397cd118c09f4e66a815f6e08e99671a?pvs=21) 에서 채보, 액션 에디팅을 작업할 수 있는 Scriptable Object의 
    양식으로 보정하여 불필요 값들은 필터링 후 Export.
    

- 스크린샷
    
    
    > parse_fmod.exe
    > 
    
    ![image.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/b7c2f6b3-1d04-45d5-aa77-9b1e51915388/image.png)
    
    > Parsing 전 / 후
    > 
    
    ![Parsing 전](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/3b4d2e8a-efe1-449f-b67a-35222dfa4712/image.png)
    
    Parsing 전
    
    ![Parsing 후 ](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/8a33c22b-5b97-4fbd-8bd4-4e4c39c6e62b/image.png)
    
    Parsing 후 
    
    > FMOD Studio → Unity 로 Marker 이식
    > 
    
    ![FMOD Studio에서의 BPM, Marker의 Timeline Position](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/00f2cb40-3166-47c0-ac06-bf522d000ef1/image.png)
    
    FMOD Studio에서의 BPM, Marker의 Timeline Position
    
    ![Unity  [AudioCC ](https://www.notion.so/AudioCC-397cd118c09f4e66a815f6e08e99671a?pvs=21) Editor 에서 불러오기 한 결과. BPM과 Marker의 Postion이 임포트 되었음.   ](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/776cd2fd-e58d-42f2-9d50-cd5eae3f546a/image.png)
    
    Unity  [AudioCC ](https://www.notion.so/AudioCC-397cd118c09f4e66a815f6e08e99671a?pvs=21) Editor 에서 불러오기 한 결과. BPM과 Marker의 Postion이 임포트 되었음.   
    
    ![Scriptable Object를 통한 이중 Debug / Editing ](https://prod-files-secure.s3.us-west-2.amazonaws.com/0bd1f676-8630-4eb8-b18f-42deb0493ecb/b1e8d73d-b068-47ef-b9c0-4973b7aacd1b/image.png)
    
    Scriptable Object를 통한 이중 Debug / Editing

사진이 단 한장도 보이지 않아서 우울해요. 암튼 잘 된다에요.
