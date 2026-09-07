const pptxgen=require('pptxgenjs');
const NAVY='1C1F8F', DEEP='0F1257', OFF='F5F2EA', INK='15161C', GRAY='7A7F8E', ONNAVY='B7BCE8', OFFW='F5F2EA', YEL='F2B705', HAIR='2A2E9C', HAIRL='D6D3CA';
const F='Pretendard'; const IMG='./img/'; // 매장 사진 크롭본을 이 폴더에 두고 실행
const pres=new pptxgen(); pres.layout='LAYOUT_16x9'; pres.title='시드니요거랩 브랜드 제안';
const W=10,H=5.625,M=0.6;
const T=(s,t,o)=>s.addText(t,Object.assign({isTextBox:true,fontFace:F,margin:0},o));
const disp=(s,t,x,y,w,h,c,size=40)=>T(s,t,{x,y,w,h,fontSize:size,bold:true,color:c,lineSpacingMultiple:1.18,charSpacing:-1,valign:'top'});
const h1=(s,t,x,y,w,c,size=26,h)=>T(s,t,{x,y,w,h:h||size/50,fontSize:size,bold:true,color:c,lineSpacingMultiple:1.2,charSpacing:-0.5,valign:'top'});
const body=(s,t,x,y,w,h,c,size=11)=>T(s,t,{x,y,w,h,fontSize:size,color:c,lineSpacingMultiple:1.5,valign:'top'});
const lab=(s,t,x,y,c)=>T(s,t,{x,y,w:7,h:0.22,fontSize:8.5,color:c,charSpacing:2.5,bold:true});
const num=(s,t,x,y,c)=>T(s,t,{x,y,w:0.6,h:0.25,fontSize:9,color:c,bold:true,charSpacing:1});
const hair=(s,x,y,w,c)=>s.addShape(pres.shapes.LINE,{x,y,w,h:0,line:{color:c,width:0.5}});
const rect=(s,x,y,w,h,c,o={})=>s.addShape(pres.shapes.RECTANGLE,Object.assign({x,y,w,h,fill:{color:c},line:{color:c,width:0}},o));
const pg=(s,n,c)=>T(s,String(n).padStart(2,'0'),{x:W-M-0.5,y:H-0.45,w:0.5,h:0.2,fontSize:8.5,color:c,align:'right',charSpacing:1});
const dark=s=>{s.background={color:NAVY};};
const rows=(s,items,x,y,w,pitch,c,hc,size=11)=>items.forEach((t,i)=>{const yy=y+i*pitch; hair(s,x,yy,w,hc); body(s,t,x,yy+0.12,w,pitch-0.12,c,size);});

// 01 Cover
{const s=pres.addSlide(); s.addImage({path:IMG+'p_cover.jpg',x:0,y:0,w:W,h:H}); rect(s,0,0,W,H,DEEP,{fill:{color:DEEP,transparency:38}});
 lab(s,'SYDNEY YOGURT LAB   —   BRAND PROPOSAL 2026.09',M,0.55,OFFW);
 s.addText([{text:'광안리의 시드니를\n',options:{color:OFFW}},{text:'목적지 브랜드',options:{color:YEL}},{text:'로 만드는 12개월',options:{color:OFFW}}],{x:M,y:2.35,w:8.8,h:2.2,isTextBox:true,fontFace:F,margin:0,fontSize:40,bold:true,lineSpacingMultiple:1.2,charSpacing:-1.5,valign:'top'});
 T(s,'시드니요거랩 대표님께',{x:M,y:4.95,w:5,h:0.25,fontSize:10,color:ONNAVY});
 s.addNotes('목표는 매출이 아니라 브랜드 자산. 런던베이글뮤지엄처럼 "가야 하는 곳"이 되는 것. 배달은 겨울 바닥이자 확장 데이터.');}

// 02 결론
{const s=pres.addSlide(); dark(s); lab(s,'01  /  CONCLUSION',M,0.55,ONNAVY);
 disp(s,'광고를 사는 게 아니라\n브랜드 자산을\n쌓는 12개월입니다.',M,1.25,4.7,3.2,OFFW,32);
 const c=[['목표','런던베이글뮤지엄형 목적지 브랜드. 소수 직영, 굿즈, 팝업, 줄 서는 매장.'],['출발점','네이버 안은 이미 잘 됩니다(리뷰 184, 구글 5.0). 비어 있는 건 세계관·굿즈·원본 페이지·배달입니다.'],['방법','세계관 → 의식 → 콘텐츠 엔진 → 확장 검증 → 측정. 매장은 체험, 배달은 완성형으로 분리.']];
 c.forEach((v,i)=>{const y=1.3+i*1.15; hair(s,5.7,y,3.7,HAIR); num(s,String(i+1).padStart(2,'0'),5.7,y+0.15,YEL); T(s,v[0],{x:6.2,y:y+0.12,w:3.2,h:0.3,fontSize:13,bold:true,color:OFFW}); body(s,v[1],6.2,y+0.45,3.2,0.7,ONNAVY,10);});
 pg(s,2,ONNAVY);}

// 03 현황
{const s=pres.addSlide(); s.background={color:OFF}; lab(s,'02  /  BASELINE   —   2026.09.06, 정식 오픈 100일차',M,0.55,GRAY);
 const st=[['587','인스타 팔로워','하루 약 6명 순증'],['184','플레이스 방문자 리뷰','하루 약 1.8건'],['30','플레이스 블로그 리뷰','제목에 "광안리 디저트"'],['5.0','구글 평점','리뷰 23 · 영문 표기 등록']];
 st.forEach((v,i)=>{const x=M+i*2.2; T(s,v[0],{x,y:1.1,w:2.1,h:1.1,fontSize:60,bold:true,color:NAVY,charSpacing:-3,valign:'top'}); hair(s,x,2.3,1.9,HAIRL); T(s,v[1],{x,y:2.4,w:2,h:0.28,fontSize:11,bold:true,color:INK}); T(s,v[2],{x,y:2.68,w:2,h:0.25,fontSize:9.5,color:GRAY});});
 rect(s,M,3.35,W-2*M,1.55,NAVY);
 T(s,'0',{x:M+0.35,y:3.42,w:1.3,h:1.4,fontSize:72,bold:true,color:YEL,charSpacing:-3,valign:'top'});
 T(s,'브랜드 자산으로 남는 것',{x:2.25,y:3.6,w:5,h:0.35,fontSize:15,bold:true,color:OFFW});
 body(s,'세계관 문서 없음, 굿즈 없음, 매장 소유 웹페이지 없음, 배달 없음. 팔로워와 리뷰는 매장 실력으로 쌓였지만 아직 "브랜드"로 축적되지 않았습니다.',2.25,3.98,6.7,0.8,ONNAVY,10.5);
 pg(s,3,GRAY);}

// 04 목표 브랜드 해부
{const s=pres.addSlide(); s.background={color:OFFW}; lab(s,'03  /  REFERENCE   —   LONDON BAGEL MUSEUM',M,0.55,GRAY);
 h1(s,'가져올 것과 버릴 것',M,1.0,8,NAVY,26);
 T(s,'그들의 방식',{x:M,y:1.75,w:3,h:0.3,fontSize:10,bold:true,color:GRAY,charSpacing:1}); T(s,'시드니요거랩 적용',{x:4.6,y:1.75,w:4,h:0.3,fontSize:10,bold:true,color:NAVY,charSpacing:1});
 const r=[['공간 자체가 콘텐츠 (런던 세계관)','"광안리의 시드니". 서프보드·캥거루는 이미 있음. 포토스팟 3곳 지정'],['희소성과 의식 (한정 메뉴, 오픈런)','월간 한정 토핑 드롭, 주말 한정 레시피, 1주년 한정 굿즈'],['굿즈 = 브랜드 자산 + 매출','스티커·에코백·리유저블 컵부터. 굿즈 매출 비중을 지표로 관리'],['직영 소수 확장, 매장마다 다른 콘셉트','2호점은 검색량·배달 주문 지역 데이터로 입지 결정'],['팝업으로 타지역 검증','부산 백화점 팝업 → 서울 팝업 → 2호점']];
 r.forEach((v,i)=>{const y=2.1+i*0.5; hair(s,M,y,W-2*M,HAIRL); body(s,v[0],M,y+0.1,3.7,0.4,GRAY,10.5); body(s,v[1],4.6,y+0.1,4.8,0.4,INK,10.5);});
 hair(s,M,4.6,W-2*M,HAIRL);
 body(s,'버릴 것: 20석에서 인위적 웨이팅 유도, 가맹 대량 확장, 가격 경쟁.',M,4.72,8.8,0.35,NAVY,10);
 pg(s,4,GRAY);}

// 05 전략 기둥
{const s=pres.addSlide(); dark(s); lab(s,'04  /  FIVE PILLARS',M,0.55,ONNAVY);
 disp(s,'다섯 개의 기둥',M,1.0,8,0.8,OFFW,30);
 const p=[['세계관','광안리의 시드니. 네이비·크림·서프. 레시피 이름은 시드니 지명. 대표의 시드니 2023–2025가 오리진.'],['의식','무게 맞히기, 레시피 보드, 월간 토핑 드롭, 겨울 캠페인 "시드니의 여름".'],['콘텐츠 엔진','손님 컵 UGC + 브랜드 채널 + 크리에이터. 애칭 "시요랩" 공식화.'],['확장 검증','배달·팝업·굿즈 채널의 주문·방문 지역 데이터가 2호점 근거.'],['측정','브랜드 검색량, 웨이팅 일수, 굿즈 비중, 타지역 방문 비율, 배달 재주문율.']];
 p.forEach((v,i)=>{const x=M+i*1.78; hair(s,x,2.15,1.6,HAIR); num(s,String(i+1).padStart(2,'0'),x,2.3,YEL); T(s,v[0],{x,y:2.6,w:1.6,h:0.3,fontSize:13,bold:true,color:OFFW}); body(s,v[1],x,2.95,1.6,2.0,ONNAVY,9.5);});
 pg(s,5,ONNAVY);}

// 06 세계관
{const s=pres.addSlide(); s.background={color:OFFW}; s.addImage({path:IMG+'p_wall.jpg',x:M,y:0.55,w:4.6,h:2.3});
 lab(s,'05  /  WORLD   —   광안리의 시드니',5.5,0.55,GRAY);
 h1(s,'이미 절반은\n만들어져 있습니다.',5.5,0.85,4,NAVY,22,1.2);
 body(s,'서프보드, 캥거루, 영어 간판, 코알라 이모지. 남은 건 이름 체계와 반복입니다.',5.5,2.1,3.9,0.7,GRAY,10.5);
 const r=[['레시피 이름','Bondi · Manly · Coogee · Bronte. 시드니 해변 이름으로 조합을 명명'],['애칭','"시요랩" 공식화. 해시태그와 굿즈에 사용'],['비주얼','네이비 1C1F8F · 크림 · 서프 그래픽. 컵·스티커·사이니지 통일'],['포토스팟','서프보드 벽, 캥거루, 토핑 바 정면. 릴스 고정 앵글 3개']];
 r.forEach((v,i)=>{const y=3.1+i*0.48; hair(s,M,y,W-2*M,HAIRL); T(s,v[0],{x:M,y:y+0.12,w:1.6,h:0.3,fontSize:10.5,bold:true,color:NAVY}); body(s,v[1],2.3,y+0.1,7.1,0.38,INK,10.5);});
 hair(s,M,5.02,W-2*M,HAIRL); pg(s,6,GRAY);}

// 07 의식
{const s=pres.addSlide(); dark(s); lab(s,'06  /  RITUALS',M,0.55,ONNAVY);
 disp(s,'다시 오게 만드는\n네 가지 장치',M,1.0,8,1.4,OFFW,28);
 const r=[['레시피 보드','손님이 조합에 이름을 붙여 올리면 매월 3개를 손님 이름으로 메뉴판에 등재. 점원이 만드는 요아정은 복제 불가.'],['월간 토핑 드롭','매월 1일 한정 토핑 공개, 수량 명시. 인스타 예고 → 매장 소진 → 다음 달 예고.'],['무게 맞히기','이미 하고 있는 100일 이벤트를 상시 의식으로. 정답자 무료, 사진은 UGC.'],['시드니의 여름','시드니는 12~2월이 여름. 광안리 겨울에 여름 토핑·비주얼로 비수기를 브랜드 서사로 전환.']];
 r.forEach((v,i)=>{const x=M+(i%2)*4.5, y=2.7+Math.floor(i/2)*1.2; hair(s,x,y,4.2,HAIR); T(s,v[0],{x,y:y+0.12,w:4.2,h:0.3,fontSize:13,bold:true,color:OFFW}); body(s,v[1],x,y+0.45,4.2,0.75,ONNAVY,9.5);});
 pg(s,7,ONNAVY);}

// 08 콘텐츠 엔진
{const s=pres.addSlide(); s.background={color:OFF}; lab(s,'07  /  CONTENT ENGINE',M,0.55,GRAY);
 h1(s,'손님이 만들고, 우리가 증폭하고,\n검색이 받아냅니다.',M,1.0,8.5,NAVY,22,1.2);
 const steps=[['UGC','손님 컵, 레시피 보드, 무게 맞히기. 해시태그 #시요랩'],['브랜드 채널','릴스 주 3회, 클립, 스레드. 앵글 3개 고정으로 제작비 절감'],['크리에이터','부산 맛집·여행 월 3~5명. 내돈내산 표기. 목표는 링크'],['검색·지도·원본','플레이스 광고, 구글, sydneyyogurtlab.com. AI가 읽는 원본']];
 steps.forEach((v,i)=>{const x=M+i*2.2; hair(s,x,2.55,2.0,NAVY); num(s,String(i+1).padStart(2,'0'),x,2.7,NAVY); T(s,v[0],{x,y:3.0,w:2.0,h:0.3,fontSize:12.5,bold:true,color:INK}); body(s,v[1],x,3.35,2.0,1.2,GRAY,9.5);});
 rect(s,M,4.55,W-2*M,0.55,NAVY);
 T(s,'원본 페이지 시안은 제작 완료. 도메인 sydneyyogurtlab.com 연결만 남았습니다.',{x:M+0.25,y:4.55,w:8.3,h:0.55,fontSize:10.5,bold:true,color:OFFW,valign:'middle'});
 pg(s,8,GRAY);}

// 09 배달
{const s=pres.addSlide(); s.background={color:OFFW}; s.addImage({path:IMG+'p_menu.jpg',x:7.6,y:0.55,w:1.8,h:1.8});
 lab(s,'08  /  DELIVERY',M,0.55,GRAY);
 h1(s,'매장은 체험, 배달은 완성형.\n섞지 않습니다.',M,1.0,6.5,NAVY,22,1.2);
 body(s,'배달로 셀프서브를 복제하면 매장의 희소성이 사라집니다. 배달은 야식 시간대 완성형 5종만 팝니다. 요아정이 증명한 겨울 야식 수요를 가져오되, 브랜드는 매장에 남깁니다.',M,2.15,6.6,0.9,GRAY,10.5);
 const r=[['운영','18:00~22:00 · 반경 3km · 배민 단독 시작 · 11월 런칭'],['메뉴 5종','Bondi 플레인+그래놀라+꿀 · Manly 초콜릿+누텔라 · Coogee 저당 딸기+베리잼 · Bronte 저당 망고+코코넛 · Dubai 피스타치오+카다이프'],['패키지','네이비 실링 컵, 시요랩 스티커, 레시피 보드 안내 카드 동봉 → 매장 방문 유도'],['지표','주문 수, 재주문율, 주문 지역 분포(2호점 근거)']];
 const ys=[3.05,3.5,4.15,4.6]; r.forEach((v,i)=>{const y=ys[i]; hair(s,M,y,W-2*M,HAIRL); T(s,v[0],{x:M,y:y+0.11,w:1.4,h:0.3,fontSize:10.5,bold:true,color:NAVY}); body(s,v[1],2.0,y+0.09,7.4,(ys[i+1]||5.05)-y-0.1,INK,9.5);});
 hair(s,M,5.05,W-2*M,HAIRL); pg(s,9,GRAY);}

// 10 확장 검증
{const s=pres.addSlide(); dark(s); lab(s,'09  /  EXPANSION PATH',M,0.55,ONNAVY);
 disp(s,'2호점은 감이 아니라\n데이터로 정합니다.',M,1.0,8,1.4,OFFW,28);
 const st=[['굿즈 1차','10월','스티커 세트 300 · 에코백 200 · 리유저블 컵 150. 굿즈 매출 비중 측정 시작'],['부산 백화점 팝업','1~2월','신세계 센텀 또는 롯데 광복. 타지역 방문 비율과 굿즈 판매 검증'],['1주년','5월','한정 굿즈·레시피. 브랜드 검색량 정점 만들기'],['서울 팝업 · 2호점 결정','6~8월','검색량 지역 분포 + 배달 주문 분포 + 팝업 데이터로 입지 리포트']];
 st.forEach((v,i)=>{const y=2.65+i*0.58; hair(s,M,y,W-2*M,HAIR); T(s,v[0],{x:M,y:y+0.12,w:2.6,h:0.3,fontSize:12,bold:true,color:OFFW}); T(s,v[1],{x:3.3,y:y+0.14,w:1.0,h:0.3,fontSize:10,color:YEL,bold:true}); body(s,v[2],4.4,y+0.1,5.0,0.45,ONNAVY,9.5);});
 pg(s,10,ONNAVY);}

// 11 로드맵
{const s=pres.addSlide(); s.background={color:OFF}; lab(s,'10  /  12-MONTH ROADMAP',M,0.55,GRAY);
 h1(s,'기반  →  겨울  →  1주년  →  성수기',M,1.0,8.5,NAVY,24);
 hair(s,M,1.95,W-2*M,NAVY);
 const m=[['9–10월','기반','브랜드북 v1 · 굿즈 1차\n랜딩 · 카카오채널\n레시피 보드 · 릴스 체계\n플레이스 광고 · 불꽃축제'],['11–2월','겨울','배달 런칭\n시드니의 여름 캠페인\n1월 저당 캠페인\n부산 백화점 팝업'],['3–5월','1주년','한정 굿즈·레시피\n2호점 입지 리포트\n토핑 키트 온라인\n서울 팝업 협의'],['6–8월','성수기','외국인 라인 강화\n대기 관리\n크리에이터 집중\n2호점 결정']];
 m.forEach((v,i)=>{const x=M+i*2.2; s.addShape(pres.shapes.OVAL,{x:x-0.06,y:1.89,w:0.12,h:0.12,fill:{color:i===0?YEL:NAVY},line:{color:i===0?YEL:NAVY,width:0}});
  lab(s,v[0],x,2.2,i===0?NAVY:GRAY); T(s,v[1],{x,y:2.5,w:2.0,h:0.4,fontSize:17,bold:true,color:NAVY}); body(s,v[2],x,3.0,2.0,1.9,INK,10.5);});
 pg(s,11,GRAY);}

// 12 예산
{const s=pres.addSlide(); s.background={color:OFFW}; lab(s,'11  /  BUDGET   —   추정, POS 확인 후 재산정',M,0.55,GRAY);
 h1(s,'초기 1,000 + 월 400',M,1.0,6,NAVY,26);
 body(s,'가정: 일 100컵 × 객단가 약 1.2만 원 = 월 매출 약 3,600만 원. 마케팅비 매출의 10~12%. 단위 만 원.',M,1.7,8.8,0.4,GRAY,10);
 T(s,'초기 일회성',{x:M,y:2.3,w:4,h:0.3,fontSize:11,bold:true,color:NAVY,charSpacing:1}); T(s,'월 운영',{x:5.3,y:2.3,w:4,h:0.3,fontSize:11,bold:true,color:NAVY,charSpacing:1});
 const a=[['굿즈 1차','300'],['포토스팟 · 사이니지','300'],['브랜드 촬영','200'],['배달 패키지 디자인','100'],['예비','100']];
 const b=[['인스타 · 릴스 광고','120'],['크리에이터','130'],['콘텐츠 제작','70'],['플레이스 광고','50'],['인쇄 · 툴','30']];
 [[a,M],[b,5.3]].forEach(([list,x])=>list.forEach((v,i)=>{const y=2.65+i*0.4; hair(s,x,y,4.1,HAIRL); T(s,v[0],{x,y:y+0.1,w:3,h:0.28,fontSize:10.5,color:INK}); T(s,v[1],{x:x+3.0,y:y+0.1,w:1.1,h:0.28,fontSize:10.5,bold:true,color:INK,align:'right'});}));
 hair(s,M,4.65,4.1,NAVY); hair(s,5.3,4.65,4.1,NAVY);
 T(s,'1,000',{x:M+3.0,y:4.72,w:1.1,h:0.3,fontSize:12,bold:true,color:NAVY,align:'right'}); T(s,'400 / 월',{x:8.3,y:4.72,w:1.1,h:0.3,fontSize:12,bold:true,color:NAVY,align:'right'});
 T(s,'대행 수수료 별도. 월 고정 + 성과 연동(브랜드 검색량 · 객수) 권장. 팝업 · 1주년은 별도 편성.',{x:M,y:5.1,w:8.8,h:0.25,fontSize:9,color:GRAY});
 pg(s,12,GRAY);}

// 13 측정
{const s=pres.addSlide(); s.background={color:OFF}; lab(s,'12  /  MEASUREMENT',M,0.55,GRAY);
 h1(s,'브랜드가 쌓이는지\n숫자로 봅니다.',M,1.0,5,NAVY,24,1.2);
 T(s,'"고쳤다"로 끝내지 않습니다.\n같은 자로 매주 잽니다.',{x:5.4,y:1.05,w:4.0,h:0.7,fontSize:11,color:GRAY,align:'right',lineSpacingMultiple:1.5});
 const B=[{type:'none'},{type:'none'},{type:'solid',color:HAIRL,pt:0.5},{type:'none'}];
 const hd=t=>({text:t,options:{fontFace:F,fontSize:8.5,bold:true,color:GRAY,charSpacing:1,valign:'bottom',border:[{type:'none'},{type:'none'},{type:'solid',color:NAVY,pt:0.75},{type:'none'}]}});
 const c=(t,o={})=>({text:t,options:Object.assign({fontFace:F,fontSize:10,color:INK,valign:'middle',border:B},o)});
 const rows=[[hd('지표'),hd('출처'),hd('의미'),hd('주기')],
  [c('브랜드 검색량 "시드니요거랩 · 시요랩"'),c('네이버 데이터랩 · 키워드도구'),c('인지도의 가장 정직한 지표'),c('매주')],
  [c('일 객수 · 객단가 · 포장 비율'),c('POS'),c('최종 성과'),c('매주')],
  [c('웨이팅 발생 일수'),c('매장 기록'),c('목적지 브랜드 여부'),c('매주')],
  [c('굿즈 매출 비중'),c('POS'),c('브랜드 자산 화폐화'),c('매월')],
  [c('배달 주문 · 재주문율 · 지역 분포'),c('배민 통계'),c('겨울 바닥 + 2호점 근거'),c('매주')],
  [c('타지역 방문 비율'),c('리뷰 · 채널 설문'),c('확장 가능성'),c('매월')],
  [c('플레이스 순위 · 저장 · 리뷰, UGC 수'),c('스마트플레이스 · 해시태그'),c('탐색 · 확산'),c('격주')]];
 s.addTable(rows,{x:M,y:2.0,w:W-2*M,colW:[3.1,2.4,2.5,0.8],rowH:0.34,margin:[0,0.05,0,0]});
 pg(s,13,GRAY);}

// 14 결정 사항
{const s=pres.addSlide(); s.addImage({path:IMG+'p_sprinkle.jpg',x:0,y:0,w:4,h:H}); rect(s,4,0,6,H,NAVY);
 lab(s,'13  /  DECISIONS',4.6,0.55,ONNAVY); h1(s,'이렇게 가정하고\n시작하겠습니다.',4.6,0.95,5,OFFW,22,1.1);
 body(s,'다른 판단이면 알려 주십시오. 9월 안에 착수합니다.',4.6,2.05,4.8,0.35,ONNAVY,10);
 const q=['배달: 18~22시, 반경 3km, 완성형 5종, 11월 배민 런칭','굿즈 1차: 스티커 300 · 에코백 200 · 리유저블 컵 150','2호점: 부산 팝업 → 서울 팝업 순으로 검증 후 결정','"시요랩" 애칭 공식 사용','계정 권한 공유, 도메인 매장 명의 구매'];
 q.forEach((t,i)=>{const y=2.5+i*0.46; num(s,String(i+1).padStart(2,'0'),4.6,y+0.03,YEL); body(s,t,5.1,y,4.3,0.44,OFFW,10.5);});
 T(s,'착수 후 14일에 기준선 리포트, 매주 대시보드로 보고드립니다.',{x:4.6,y:4.95,w:4.8,h:0.3,fontSize:10,color:ONNAVY});}

pres.writeFile({fileName:'/root/deckqa/proposal_v4.pptx'}).then(()=>console.log('ok')).catch(e=>{console.error(e);process.exit(1)});
