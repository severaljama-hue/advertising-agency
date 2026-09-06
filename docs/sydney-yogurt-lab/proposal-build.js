const pptxgen=require('pptxgenjs');
const NAVY='1C1F8F', DEEP='0F1257', OFF='F5F2EA', INK='15161C', GRAY='7A7F8E', ONNAVY='B7BCE8', OFFW='F5F2EA', YEL='F2B705', HAIR='2A2E9C', HAIRL='D6D3CA';
const F='Pretendard'; const IMG='./img/'; // 매장 사진 크롭본 (리포 미포함)
const pres=new pptxgen(); pres.layout='LAYOUT_16x9'; pres.title='시드니요거랩 제안';
const W=10,H=5.625,M=0.6;
const T=(s,t,o)=>s.addText(t,Object.assign({isTextBox:true,fontFace:F,margin:0},o));
const disp=(s,t,x,y,w,h,c,size=40)=>T(s,t,{x,y,w,h,fontSize:size,bold:true,color:c,lineSpacingMultiple:1.18,charSpacing:-1,valign:'top'});
const h1=(s,t,x,y,w,c,size=26)=>T(s,t,{x,y,w,h:size/50,fontSize:size,bold:true,color:c,lineSpacingMultiple:1.2,charSpacing:-0.5});
const body=(s,t,x,y,w,h,c,size=11)=>T(s,t,{x,y,w,h,fontSize:size,color:c,lineSpacingMultiple:1.5,valign:'top'});
const lab=(s,t,x,y,c)=>T(s,t,{x,y,w:6,h:0.22,fontSize:8.5,color:c,charSpacing:2.5,bold:true});
const num=(s,t,x,y,c)=>T(s,t,{x,y,w:0.6,h:0.25,fontSize:9,color:c,bold:true,charSpacing:1});
const hair=(s,x,y,w,c)=>s.addShape(pres.shapes.LINE,{x,y,w,h:0,line:{color:c,width:0.5}});
const rect=(s,x,y,w,h,c,o={})=>s.addShape(pres.shapes.RECTANGLE,Object.assign({x,y,w,h,fill:{color:c},line:{color:c,width:0}},o));
const pg=(s,n,c)=>T(s,String(n).padStart(2,'0'),{x:W-M-0.5,y:H-0.45,w:0.5,h:0.2,fontSize:8.5,color:c,align:'right',charSpacing:1});
const dark=s=>{s.background={color:NAVY};};

// 01 Cover
{const s=pres.addSlide(); s.addImage({path:IMG+'p_cover.jpg',x:0,y:0,w:W,h:H}); rect(s,0,0,W,H,DEEP,{fill:{color:DEEP,transparency:38}});
 lab(s,'SYDNEY YOGURT LAB   —   PROPOSAL 2026.09',M,0.55,OFFW);
 s.addText([{text:'네이버 밖에서도\n찾아오게 만드는 ',options:{color:OFFW}},{text:'3개월',options:{color:YEL}}],{x:M,y:2.15,w:8.5,h:2.3,isTextBox:true,fontFace:F,margin:0,fontSize:42,bold:true,lineSpacingMultiple:1.18,charSpacing:-1.5,valign:'top'});
 T(s,'시드니요거랩 대표님께',{x:M,y:4.95,w:5,h:0.25,fontSize:10,color:ONNAVY});
 s.addNotes('결론 한 줄: 네이버 안은 이미 잘 되고 있다. 비어 있는 곳은 네이버 밖이다. 3개월 안에 채우고 숫자로 보인다.');}

// 02 결론
{const s=pres.addSlide(); dark(s); lab(s,'01  /  CONCLUSION',M,0.55,ONNAVY);
 disp(s,'네이버 안은\n이미 잘 되고 있습니다.\n비어 있는 곳은\n네이버 밖입니다.',M,1.25,4.6,3.4,OFFW,34);
 const c=[['잘 되고 있는 것','플레이스 리뷰 184건, 블로그 리뷰 30건, 구글 평점 5.0. 오픈 100일 매장으로는 높은 수치입니다.'],['비어 있는 것','매장 소유 웹페이지가 없습니다. 구글·빙·ChatGPT·Perplexity가 읽을 원본이 0입니다.'],['제안','원본 만들기, 유입 만들기, 측정과 조정. 14일마다 같은 지표를 다시 재서 전후 숫자로 보고합니다.']];
 c.forEach((v,i)=>{const y=1.3+i*1.15; hair(s,5.7,y,3.7,HAIR); num(s,String(i+1).padStart(2,'0'),5.7,y+0.15,YEL);
  T(s,v[0],{x:6.2,y:y+0.12,w:3.2,h:0.3,fontSize:13,bold:true,color:OFFW}); body(s,v[1],6.2,y+0.45,3.2,0.7,ONNAVY,10);});
 pg(s,2,ONNAVY);}

// 03 현황
{const s=pres.addSlide(); s.background={color:OFF}; lab(s,'02  /  BASELINE   —   2026.09.06, 정식 오픈 100일차',M,0.55,GRAY);
 const st=[['587','인스타 팔로워','하루 약 6명 순증'],['184','플레이스 방문자 리뷰','하루 약 1.8건'],['30','플레이스 블로그 리뷰','제목에 "광안리 디저트"'],['5.0','구글 평점','리뷰 23 · 영문 표기 등록']];
 st.forEach((v,i)=>{const x=M+i*2.2; T(s,v[0],{x,y:1.1,w:2.1,h:1.1,fontSize:60,bold:true,color:NAVY,charSpacing:-3,valign:'top'}); hair(s,x,2.3,1.9,HAIRL);
  T(s,v[1],{x,y:2.4,w:2,h:0.28,fontSize:11,bold:true,color:INK}); T(s,v[2],{x,y:2.68,w:2,h:0.25,fontSize:9.5,color:GRAY});});
 rect(s,M,3.35,W-2*M,1.55,NAVY);
 T(s,'0',{x:M+0.35,y:3.42,w:1.3,h:1.4,fontSize:72,bold:true,color:YEL,charSpacing:-3,valign:'top'});
 T(s,'매장 소유 웹페이지',{x:2.25,y:3.6,w:5,h:0.35,fontSize:15,bold:true,color:OFFW});
 body(s,'네이버 안의 숫자는 매장 실력으로 이미 만들어졌습니다. 이 칸이 이번 제안의 대상입니다. 구글과 AI가 읽을 원본이 아직 없습니다.',2.25,3.98,6.7,0.8,ONNAVY,10.5);
 pg(s,3,GRAY);}

// 04 발견 경로
{const s=pres.addSlide(); s.background={color:OFFW}; s.addImage({path:IMG+'p_cup.jpg',x:0,y:0,w:3.75,h:H});
 lab(s,'03  /  DISCOVERY',4.35,0.55,GRAY);
 h1(s,'지나가다 들르는 매장이 아니라,\n검색해서 찾아오는 매장입니다.',4.35,1.05,5.1,NAVY,20);
 body(s,'광안역 5번 출구 457m, 해변 안쪽 골목. 리뷰 184건은 이미 그렇게 찾아온 결과입니다.',4.35,2.05,5.0,0.6,GRAY,10.5);
 const rows=[['네이버 검색·지도','작동 중',true],['구글 지도','작동 중 · 5.0',true],['인스타그램','작동 중 · 587',true],['열린 웹 · AI 답변','원본 없음',false]];
 rows.forEach((r,i)=>{const y=2.85+i*0.55; hair(s,4.35,y,5.05,HAIRL); T(s,r[0],{x:4.35,y:y+0.12,w:3,h:0.3,fontSize:12.5,bold:true,color:INK});
  T(s,r[1],{x:7.4,y:y+0.14,w:2.0,h:0.3,fontSize:10,color:r[2]?GRAY:NAVY,bold:!r[2],align:'right'});});
 hair(s,4.35,5.05,5.05,HAIRL); pg(s,4,GRAY);}

// 05 왜 네이버 밖
{const s=pres.addSlide(); dark(s); lab(s,'04  /  WHY OUTSIDE NAVER',M,0.55,ONNAVY);
 disp(s,'세 종류의 손님은\n네이버를 쓰지 않습니다.',M,1.05,8,1.4,OFFW,30);
 const c=[['외국인 관광객','광안리는 외국인 방문이 늘고 있습니다. 이들은 구글 지도와 트립어드바이저로 찾습니다. 매장 언어가 이미 영어라 준비가 절반은 되어 있습니다.'],['AI에게 묻는 손님','"광안리 요거트 아이스크림 추천"을 ChatGPT·Perplexity·구글 AI에 묻습니다. 이들은 인스타와 플레이스를 읽지 못하고 열린 웹의 HTML만 인용합니다.'],['이름이 겹치는 문제','"Yogurt Lab"은 미국 프랜차이즈와 멜버른 매장이 먼저 쓰고 있습니다. 공식 페이지가 없으면 AI는 시드니요거랩을 구분하지 못합니다.']];
 c.forEach((v,i)=>{const x=M+i*2.95; hair(s,x,2.85,2.7,HAIR); num(s,String(i+1).padStart(2,'0'),x,3.0,YEL); T(s,v[0],{x,y:3.3,w:2.7,h:0.3,fontSize:13.5,bold:true,color:OFFW}); body(s,v[1],x,3.65,2.65,1.5,ONNAVY,10);});
 pg(s,5,ONNAVY);}

// 06 경쟁
{const s=pres.addSlide(); s.background={color:OFF}; lab(s,'05  /  COMPETITION',M,0.55,GRAY);
 h1(s,'카테고리 관심은 받아 오고,\n승부는 요아정이 못 하는 것으로.',M,1.05,6.5,NAVY,22);
 const cols=[2.5,5.4]; T(s,'요아정',{x:cols[0],y:2.15,w:2.6,h:0.3,fontSize:11,bold:true,color:GRAY}); T(s,'시드니요거랩',{x:cols[1],y:2.15,w:2.6,h:0.3,fontSize:11,bold:true,color:NAVY});
 s.addImage({path:IMG+'p_menu.jpg',x:8.2,y:0.95,w:1.2,h:1.2});
 const rows=[['방식','점원이 만들어 줌','손님이 직접 담고 무게로 계산'],['가격','컵 + 토핑별 추가 요금','100g 4,500원, 컵 한 종류'],['규모','전국 400개점 이상','광안리 1개점, 20석'],['근거','SNS 인증 문화, 정점 논쟁','대표의 시드니 근무 2023–2025']];
 rows.forEach((r,i)=>{const y=2.6+i*0.55; hair(s,M,y,W-2*M,HAIRL); T(s,r[0],{x:M,y:y+0.14,w:1.5,h:0.3,fontSize:10,color:GRAY,bold:true}); T(s,r[1],{x:cols[0],y:y+0.12,w:2.7,h:0.3,fontSize:11.5,color:GRAY}); T(s,r[2],{x:cols[1],y:y+0.12,w:3.8,h:0.3,fontSize:11.5,color:INK,bold:true});});
 hair(s,M,4.8,W-2*M,HAIRL);
 T(s,'국내 셀프서브 매장 존재 여부는 별도 조사 예정. 호주 Yo-Chi는 국내 진출이 확인되지 않음.',{x:M,y:4.9,w:8,h:0.25,fontSize:8.5,color:GRAY});
 pg(s,6,GRAY);}

// 07 제안 1
{const s=pres.addSlide(); dark(s); lab(s,'06  /  PHASE 1   —   MONTH 1',M,0.55,ONNAVY);
 h1(s,'원본 만들기',M,1.05,5,OFFW,30);
 body(s,'sydneyyogurtlab.com 한 장으로 시작합니다.',M,1.8,5,0.35,ONNAVY,11);
 const b=['도메인 확보, 랜딩 한 장 게시. 주소·영업시간·가격·6종 메뉴·FAQ를 크롤러가 읽는 HTML로','AI 크롤러용 사실 요약(llms.txt)과 구조화 데이터. 동명 브랜드와 무관함을 명시','구글 서치콘솔·빙 웹마스터·네이버 서치어드바이저 등록, 사이트맵 제출','플레이스·구글·인스타·블로그의 웹사이트 칸에 연결. 표기 통일','트립어드바이저 무료 리스팅, 대표자 인증'];
 b.forEach((t,i)=>{const y=2.35+i*0.5; num(s,String(i+1).padStart(2,'0'),M,y+0.03,YEL); body(s,t,M+0.5,y,4.6,0.5,OFFW,10);});
 T(s,'시안은 이미 만들어져 있습니다. 도메인만 연결하면 게시됩니다.',{x:M,y:4.95,w:5,h:0.25,fontSize:9.5,color:ONNAVY});
 s.addShape(pres.shapes.RECTANGLE,{x:6.75,y:0.55,w:2.53,h:4.93,fill:{color:DEEP},line:{color:ONNAVY,width:0.5}});
 s.addImage({path:IMG+'landing-mobile-top.png',x:6.82,y:0.62,w:2.39,h:4.66});
 }

// 08 제안 2
{const s=pres.addSlide(); s.background={color:OFF}; lab(s,'07  /  PHASE 2   —   MONTH 2',M,0.55,GRAY);
 h1(s,'유입 만들기',M,1.05,4.5,NAVY,30);
 body(s,'원본이 생긴 뒤에 돈을 씁니다.\n순서가 반대면 돈이 샙니다.',M,1.85,4.2,0.8,GRAY,11);
 s.addImage({path:IMG+'p_wall.jpg',x:4.8,y:0.55,w:4.6,h:2.3});
 const it=[['플레이스 광고','"광안리 디저트·요거트" 지역 키워드로 소액 시작. 클릭당 비용과 저장·길찾기 전환을 2주마다 기록'],['인스타·릴스 지역 광고','광안리 반경 3km, 여행 관심사 타깃. 소재는 손님이 만든 컵(UGC)'],['크리에이터 3~5명','네이버 클립·릴스. 내돈내산 표기 준수. 목표는 랜딩으로 가는 링크'],['외국인 리뷰 QR','구글·트립어드바이저 영어 리뷰 요청 카드를 카운터에 비치']];
 it.forEach((v,i)=>{const x=M+i*2.2; hair(s,x,3.25,2.0,NAVY); T(s,v[0],{x,y:3.38,w:2.0,h:0.3,fontSize:11.5,bold:true,color:INK}); body(s,v[1],x,3.72,2.0,1.3,GRAY,9.5);});
 pg(s,8,GRAY);}

// 09 측정
{const s=pres.addSlide(); s.background={color:OFFW}; lab(s,'08  /  PHASE 3   —   MONTH 3',M,0.55,GRAY);
 h1(s,'측정과 조정',M,1.05,4.5,NAVY,30);
 T(s,'"고쳤다"로 끝내지 않습니다.\n14일마다 같은 자로 잽니다.',{x:5.4,y:1.1,w:4.0,h:0.7,fontSize:11,color:GRAY,align:'right',lineSpacingMultiple:1.5});
 const B=[{type:'none'},{type:'none'},{type:'solid',color:HAIRL,pt:0.5},{type:'none'}];
 const hd=t=>({text:t,options:{fontFace:F,fontSize:8.5,bold:true,color:GRAY,charSpacing:1,valign:'bottom',border:[{type:'none'},{type:'none'},{type:'solid',color:NAVY,pt:0.75},{type:'none'}]}});
 const c=(t,o={})=>({text:t,options:Object.assign({fontFace:F,fontSize:10.5,color:INK,valign:'middle',border:B},o)});
 const rows=[[hd('지표'),hd('기준선 9/6'),hd('측정 방법'),hd('주기')],
  [c('플레이스 순위 "광안리 요거트"'),c('미측정',{color:GRAY}),c('비로그인 모바일 검색'),c('14일')],
  [c('플레이스 저장 · 길찾기 · 전화'),c('대표님 계정 확인',{color:GRAY}),c('스마트플레이스 통계'),c('14일')],
  [c('방문자 리뷰 수'),c('184',{bold:true}),c('플레이스'),c('14일')],
  [c('구글 리뷰 수 · 평점'),c('23 · 5.0',{bold:true}),c('비즈니스 프로필'),c('14일')],
  [c('인스타 팔로워 순증 / 일'),c('약 6',{bold:true}),c('인사이트'),c('14일')],
  [c('랜딩 노출 · 클릭'),c('0',{bold:true}),c('서치콘솔 · 서치어드바이저'),c('14일')],
  [c('AI 답변 인용 여부'),c('미인용',{bold:true}),c('ChatGPT · Perplexity · 네이버 AI 브리핑, 같은 질문 3종'),c('14일')]];
 s.addTable(rows,{x:M,y:1.95,w:W-2*M,colW:[2.7,1.6,3.6,0.9],rowH:0.33,margin:[0,0.05,0,0]});
 body(s,'목표 수치는 1차 재측정(게시 14일 후) 결과를 보고 대표님과 함께 정합니다. 효과 없는 채널은 예산을 옮깁니다.',M,4.75,8.8,0.4,INK,10);
 pg(s,9,GRAY);}

// 10 로드맵
{const s=pres.addSlide(); dark(s); lab(s,'09  /  ROADMAP',M,0.55,ONNAVY);
 h1(s,'원본  →  유입  →  측정',M,1.05,8,OFFW,30);
 hair(s,M,2.15,W-2*M,HAIR);
 const m=[['MONTH 1','원본 만들기',['도메인 · 랜딩 게시','서치콘솔 · 빙 · 서치어드바이저','표기 통일, 트립어드바이저','기준선 측정']],['MONTH 2','유입 만들기',['플레이스 광고 시작','인스타 지역 광고','크리에이터 3~5명','외국인 리뷰 QR']],['MONTH 3','측정과 조정',['14일 재측정 2회','예산 재배분','FAQ · 시즌 페이지 추가','트립닷컴 입점 문의 (12월)']]];
 m.forEach((v,i)=>{const x=M+i*2.95; s.addShape(pres.shapes.OVAL,{x:x-0.06,y:2.09,w:0.12,h:0.12,fill:{color:i===0?YEL:OFFW},line:{color:i===0?YEL:OFFW,width:0}});
  lab(s,v[0],x,2.4,i===0?YEL:ONNAVY); T(s,v[1],{x,y:2.7,w:2.6,h:0.4,fontSize:17,bold:true,color:OFFW});
  body(s,v[2].join('\n'),x,3.25,2.6,1.7,ONNAVY,10.5);});
 pg(s,10,ONNAVY);}

// 11 약속 / 하지 않는 것
{const s=pres.addSlide(); rect(s,0,0,5,H,NAVY); rect(s,5,0,5,H,OFF);
 lab(s,'10  /  COMMITMENTS',M,0.55,ONNAVY); h1(s,'약속하는 것',M,1.05,4,OFFW,24);
 const a=['측정 없이 "완료"라고 말하지 않습니다','14일마다 같은 지표를 전후 비교로 보고합니다','페이지와 데이터에는 화면에 보이는 사실만 씁니다','대표님 계정은 권한 공유 방식으로만 다룹니다'];
 a.forEach((t,i)=>{const y=1.85+i*0.65; hair(s,M,y,3.8,HAIR); body(s,t,M,y+0.14,3.8,0.45,OFFW,11);});
 lab(s,'NOT DOING',5.6,0.55,GRAY); h1(s,'하지 않는 것',5.6,1.05,4,NAVY,24);
 const b=['리뷰 구매, 블로그 대량 체험단, 백링크 구매','"순위 보장", "인용 보장" 문구','화면과 다른 메타 · 구조화 데이터, 숨긴 텍스트'];
 b.forEach((t,i)=>{const y=1.85+i*0.65; hair(s,5.6,y,3.8,HAIRL); body(s,t,5.6,y+0.14,3.8,0.45,INK,11);});
 body(s,'걸리는 것은 단기 순위가 아니라 플레이스와 도메인 전체입니다.',5.6,4.1,3.8,0.6,GRAY,10);
 pg(s,11,GRAY);}

// 12 확인 요청
{const s=pres.addSlide(); s.addImage({path:IMG+'p_sprinkle.jpg',x:0,y:0,w:4,h:H}); rect(s,4,0,6,H,NAVY);
 lab(s,'11  /  DECISIONS NEEDED',4.6,0.55,ONNAVY); h1(s,'대표님께\n확인을 요청드립니다.',4.6,1.05,5,OFFW,24);
 const q=['도메인 sydneyyogurtlab.com 구매 주체 (매장 명의 권장)','네이버 스마트플레이스 · 구글 프로필 관리자 권한 공유 방식','월 광고 예산 상한 (플레이스 + 인스타 + 크리에이터)','인스타 팔로잉 0 정책 유지 여부','시드니 근무 이력(2023–2025)의 브랜드 스토리 공개 여부'];
 q.forEach((t,i)=>{const y=2.2+i*0.48; num(s,String(i+1).padStart(2,'0'),4.6,y+0.03,YEL); body(s,t,5.1,y,4.3,0.45,OFFW,10.5);});
 T(s,'회신 주시면 착수일과 1차 측정일을 잡아 다시 보고드리겠습니다.',{x:4.6,y:4.85,w:4.8,h:0.3,fontSize:10,color:ONNAVY});}

pres.writeFile({fileName:'/root/deckqa/proposal_v3.pptx'}).then(()=>console.log('ok')).catch(e=>{console.error(e);process.exit(1)});
