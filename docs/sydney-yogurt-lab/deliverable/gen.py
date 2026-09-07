# -*- coding: utf-8 -*-
import html
NAVY="#1C1F8F"; DEEP="#0F1257"; OFF="#F5F2EA"; INK="#15161C"; GRAY="#6F7482"; YEL="#F2B705"; LINE="#DAD7CE"; SOFT="#ECEAF8"
FONT="Pretendard, 'Noto Sans KR', -apple-system, 'Apple SD Gothic Neo', sans-serif"
MONO="'IBM Plex Mono', 'SFMono-Regular', Menlo, monospace"
HEAD='<!doctype html>\n<html>\n<head>\n  <meta charset="utf-8">\n  <script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&amp;family=IBM+Plex+Mono:wght@400;500;600&amp;display=swap">\n  <style>\n    body { margin: 0; font-family: %s; color: %s; -webkit-font-smoothing: antialiased; }\n    a { color: %s; } a:hover { color: %s; }\n    table { border-collapse: collapse; width: 100%%; }\n    th, td { text-align: left; vertical-align: top; padding: 9px 10px 9px 0; border-bottom: 1px solid %s; font-size: 13.5px; line-height: 1.5; }\n    th { font-weight: 600; color: %s; font-size: 11.5px; letter-spacing: 0.04em; border-bottom: 1.5px solid %s; padding-bottom: 7px; }\n    td:last-child, th:last-child { padding-right: 0; }\n    p { margin: 0; }\n  </style>\n</helmet>\n' % (FONT, INK, NAVY, DEEP, LINE, GRAY, NAVY)
TAIL='</x-dc>\n</body>\n</html>\n'
def e(s): return html.escape(s, quote=False)
def tag_fix(): return '<span style="display: inline-block; font-family: %s; font-size: 10px; font-weight: 600; letter-spacing: 0.06em; color: #FFFFFF; background: %s; padding: 2px 6px; border-radius: 2px; margin-left: 6px; vertical-align: middle;">확정</span>' % (MONO, NAVY)
def tag_asm(): return '<span style="display: inline-block; font-family: %s; font-size: 10px; font-weight: 600; letter-spacing: 0.06em; color: %s; border: 1px solid %s; padding: 1px 5px; border-radius: 2px; margin-left: 6px; vertical-align: middle;">가정</span>' % (MONO, NAVY, NAVY)
def label(num, text):
    return '<div style="display: flex; align-items: center; gap: 10px; margin: 0 0 14px 0;"><span style="font-family: %s; font-size: 12px; font-weight: 600; color: %s; letter-spacing: 0.08em;">%s</span><span style="font-family: %s; font-size: 11.5px; font-weight: 500; color: %s; letter-spacing: 0.08em;">%s</span></div>' % (MONO, YEL, num, MONO, GRAY, e(text))
def h2(text): return '<h2 style="font-size: 26px; font-weight: 700; line-height: 1.25; letter-spacing: -0.01em; color: %s; margin: 0 0 18px 0;">%s</h2>' % (NAVY, e(text))
def h3(text, tag=None):
    t = tag_fix() if tag=="fix" else (tag_asm() if tag=="asm" else "")
    return '<h3 style="font-size: 16px; font-weight: 700; line-height: 1.4; color: %s; margin: 26px 0 10px 0;">%s%s</h3>' % (INK, e(text), t)
def p(text, muted=False, size=15.5):
    return '<p style="font-size: %spx; line-height: 1.7; color: %s; margin: 0 0 10px 0;">%s</p>' % (size, GRAY if muted else INK, e(text))
def lead(text): return '<p style="font-size: 18px; line-height: 1.6; font-weight: 500; color: %s; margin: 0 0 14px 0;">%s</p>' % (INK, e(text))
def table(headers, rows, widths=None):
    out=['<table>']
    if headers:
        out.append('<thead><tr>')
        for i,h in enumerate(headers):
            w=' style="width: %s;"' % widths[i] if widths and widths[i] else ''
            out.append('<th%s>%s</th>' % (w, e(h)))
        out.append('</tr></thead>')
    out.append('<tbody>')
    for r in rows:
        out.append('<tr>')
        for i,c in enumerate(r):
            bold = ' style="font-weight: 600; color: %s;"' % INK if i==0 else ''
            out.append('<td%s>%s</td>' % (bold, e(c)))
        out.append('</tr>')
    out.append('</tbody></table>')
    return ''.join(out)
def ul(items):
    return '<div style="display: flex; flex-direction: column; gap: 6px; margin: 4px 0 10px 0;">' + ''.join('<div style="display: flex; gap: 10px; font-size: 15px; line-height: 1.65;"><span style="color: %s; flex: 0 0 auto;">–</span><span>%s</span></div>' % (NAVY, e(i)) for i in items) + '</div>'
def numlist(items):
    return '<div style="display: flex; flex-direction: column; gap: 8px; margin: 4px 0 10px 0;">' + ''.join('<div style="display: flex; gap: 12px; font-size: 15px; line-height: 1.65;"><span style="font-family: %s; font-size: 12px; font-weight: 600; color: %s; flex: 0 0 22px; padding-top: 3px;">%02d</span><span>%s</span></div>' % (MONO, YEL, n+1, e(i)) for n,i in enumerate(items)) + '</div>'
def section(num, kicker, title, body_html, tone="light"):
    bg = "#FFFFFF" if tone=="light" else OFF
    return '<section style="background: %s; padding: 48px 56px 40px 56px; border-top: 1px solid %s;">%s%s%s</section>' % (bg, LINE, label(num, kicker), h2(title), body_html)
def stat(n, l, s):
    return '<div style="display: flex; flex-direction: column; gap: 4px;"><div style="font-family: %s; font-size: 40px; font-weight: 600; line-height: 1; color: %s; letter-spacing: -0.02em;">%s</div><div style="font-size: 13px; font-weight: 600; color: %s;">%s</div><div style="font-size: 12px; color: %s;">%s</div></div>' % (MONO, NAVY, e(n), INK, e(l), GRAY, e(s))
def callout(text):
    return '<div style="background: %s; color: #FFFFFF; padding: 18px 22px; font-size: 15px; line-height: 1.65; margin: 16px 0 6px 0;">%s</div>' % (NAVY, e(text))

# ---------- COVER ----------
cover = HEAD + '''<div style="width: 794px; height: 1123px; background: %s; position: relative; overflow: hidden; display: flex; flex-direction: column;">
  <div style="height: 520px; position: relative; overflow: hidden;">
    <img src="cover.jpg" style="width: 100%%; height: 100%%; object-fit: cover; display: block;">
    <div style="position: absolute; inset: 0; background: %s; opacity: 0.55;"></div>
    <div style="position: absolute; left: 56px; top: 48px; font-family: %s; font-size: 11.5px; letter-spacing: 0.12em; color: #FFFFFF;">SYDNEY YOGURT LAB · BRAND &amp; MARKETING EXECUTION PLAN</div>
  </div>
  <div style="flex: 1; padding: 56px 56px 48px 56px; display: flex; flex-direction: column; justify-content: space-between;">
    <div>
      <div style="font-size: 44px; font-weight: 700; line-height: 1.2; letter-spacing: -0.02em; color: #FFFFFF;">시드니요거랩<br>브랜드·마케팅 실행안</div>
      <div style="margin-top: 18px; font-size: 18px; line-height: 1.6; color: #C9CCF0;">광안리의 시드니를 목적지 브랜드로 만드는 12개월<br>진단 · 전략 · 로드맵 · 실행 플레이북 · 검색/AI 노출 · 측정</div>
    </div>
    <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; border-top: 1px solid rgba(255,255,255,0.25); padding-top: 22px;">
      <div><div style="font-family: %s; font-size: 10.5px; letter-spacing: 0.1em; color: #9EA3E0;">VERSION</div><div style="margin-top: 6px; font-size: 14px; color: #FFFFFF;">v1.0 · 2026. 09. 07</div></div>
      <div><div style="font-family: %s; font-size: 10.5px; letter-spacing: 0.1em; color: #9EA3E0;">PREPARED FOR</div><div style="margin-top: 6px; font-size: 14px; color: #FFFFFF;">시드니요거랩 대표</div></div>
      <div><div style="font-family: %s; font-size: 10.5px; letter-spacing: 0.1em; color: #9EA3E0;">PREPARED BY</div><div style="margin-top: 6px; font-size: 14px; color: #FFFFFF;">[대행사명]</div></div>
    </div>
  </div>
</div>
''' % (NAVY, DEEP, MONO, MONO, MONO, MONO) + TAIL
open('Cover.dc.html','w',encoding='utf-8').write(cover)

# ---------- MAIN ----------
S=[]
# 00 문서 안내
S.append(section("00","HOW TO READ","이 문서를 읽는 법",
 lead("이 문서는 제안서가 아니라 실행 문서입니다. 진단에서 측정까지 12개월 동안 무엇을, 누가, 언제 하는지를 담았고, 매주 대시보드와 함께 갱신됩니다.")
 + table(["구분","내용"],[
   ["범위","브랜드 전략, SNS·광고 실행, 배달 분리 원칙, 검색·AI 노출, 예산, 측정 체계"],
   ["기준 시점","2026년 9월 6일 스크린샷 수치. 정식 오픈(5월 29일) 후 100일차"],
   ["표기","확정 = 사실 확인 완료 또는 합의됨. 가정 = 대표 확인 또는 데이터 확보 후 교체"],
   ["갱신","격주 재측정마다 v1.1, v1.2로 개정. 변경 내역은 마지막 장에 기록"],
   ["함께 제공되는 것","랜딩 페이지 시안(sydneyyogurtlab.com), llms.txt·robots.txt·sitemap.xml, 제안 덱(14장), 광고 카피 20안, 12주 드롭 계획"],
 ],["22%",None])
 + '<div style="display: flex; gap: 18px; margin-top: 18px; font-size: 13px; color: %s; align-items: center;"><span>%s 사실 확인 완료</span><span>%s 확인 후 교체</span></div>' % (GRAY, tag_fix().replace('margin-left: 6px;','margin-left: 0;'), tag_asm().replace('margin-left: 6px;','margin-left: 0;'))
))
# 01 요약
S.append(section("01","EXECUTIVE SUMMARY","한 장 요약",
 lead("네이버 안은 이미 잘 되고 있습니다. 비어 있는 곳은 네이버 밖입니다. 12개월 동안 광고를 사는 대신 브랜드 자산을 쌓고, 겨울 전에 배달과 재방문층으로 매출 바닥을 만듭니다.")
 + '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; margin: 22px 0 26px 0;">'
 + '<div style="border-top: 2px solid %s; padding-top: 12px;"><div style="font-family: %s; font-size: 11px; color: %s; letter-spacing: 0.08em; margin-bottom: 8px;">목표</div><div style="font-size: 14.5px; line-height: 1.6;">런던베이글뮤지엄형 목적지 브랜드. 소수 직영, 굿즈, 팝업, 줄 서는 매장.</div></div>' % (NAVY, MONO, YEL)
 + '<div style="border-top: 2px solid %s; padding-top: 12px;"><div style="font-family: %s; font-size: 11px; color: %s; letter-spacing: 0.08em; margin-bottom: 8px;">출발점</div><div style="font-size: 14.5px; line-height: 1.6;">플레이스 리뷰 184, 구글 5.0. 세계관·굿즈·원본 페이지·배달은 아직 없음.</div></div>' % (NAVY, MONO, YEL)
 + '<div style="border-top: 2px solid %s; padding-top: 12px;"><div style="font-family: %s; font-size: 11px; color: %s; letter-spacing: 0.08em; margin-bottom: 8px;">방법</div><div style="font-size: 14.5px; line-height: 1.6;">세계관 → 의식 → 콘텐츠 엔진 → 확장 검증 → 측정. 매장은 체험, 배달은 완성형으로 분리.</div></div>' % (NAVY, MONO, YEL)
 + '</div>'
 + table(["단계","시기","목표","핵심"],[
   ["0 기반","9~10월","세계관·측정 체계","브랜드북 v1, 굿즈 1차, 랜딩, 카카오채널, 주간 드롭, 릴스 체계, 플레이스 광고, 불꽃축제"],
   ["1 겨울","11~2월","매출 바닥 + 세계관 확산","배달 런칭, 시드니의 여름 캠페인, 1월 저당 캠페인, 부산 백화점 팝업"],
   ["2 1주년","3~5월","브랜드 자산 정점","한정 굿즈·레시피, 2호점 입지 리포트, 서울 팝업 검토, 토핑 키트 온라인"],
   ["3 성수기","6~8월","객수 극대화 + 2호점 결정","외국인 라인, 대기 관리, 크리에이터 집중, 2호점 결정"],
 ],["12%","12%","24%",None])
 + h3("예산", "asm") + p("초기 일회성 1,000만 원 + 월 운영 400만 원(광고·콘텐츠). 대행 수수료 별도. 가정은 일 100컵, 객단가 약 1.2만 원, 마케팅비 매출의 10~12%. POS 4주치 확보 후 재산정.")
))
# 02 현황
S.append(section("02","BASELINE","현황 진단",
 '<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 20px; margin: 4px 0 26px 0;">'
 + stat("587","인스타 팔로워","하루 약 6명 순증") + stat("184","플레이스 방문자 리뷰","하루 약 1.8건") + stat("30","플레이스 블로그 리뷰","제목에 광안리 디저트") + stat("5.0","구글 평점","리뷰 23 · 영문 표기 등록")
 + '</div>'
 + callout("브랜드 자산으로 남는 것 0. 세계관 문서 없음, 굿즈 없음, 매장 소유 웹페이지 없음, 배달 없음. 팔로워와 리뷰는 매장 실력으로 쌓였지만 아직 브랜드로 축적되지 않았습니다.")
 + h3("매장 사실", "fix")
 + table(["항목","내용"],[
   ["주소","부산 수영구 수영로540번길 24-4 1층. 광안역 5번 출구 457m, 해변 안쪽 골목"],
   ["영업","월·화·목·금 12:00~20:00, 토 12:00~22:00, 일 14:00~20:00, 라스트오더 마감 30분 전, 수요일 정기휴무"],
   ["상품","요거트 아이스크림 6종(플레인·초콜릿·저당 스트로베리·저당 애플망고·솔티드캬라멜·피스타치오), 토핑 30종 이상"],
   ["가격","컵 1종, 무게 계산 100g 4,500원"],
   ["규모","약 20석. 포장 가능, 배달 없음, 무선 인터넷, 휠체어 출입 가능"],
   ["대표","2023~2025 시드니에서 CJ 마케터 근무. 2026년 5월 23~25일 가오픈, 5월 29일 정식 오픈"],
 ],["14%",None])
 + h3("손님이 찾아오는 네 가지 길")
 + table(["경로","상태","근거"],[
   ["네이버 검색·지도","작동 중","플레이스·블로그·리뷰 184, 쿠폰, AI 요약 노출"],
   ["구글 지도","작동 중","5.0 · 리뷰 23 · 시드니요거랩 광안리 (Sydney Yogurt Lab in Gwangalli)"],
   ["인스타그램","작동 중","팔로워 587, 하이라이트 5개, 콘텐츠 축 정리됨"],
   ["열린 웹 · AI 답변","없음","매장 소유 페이지 없음. 블로그가 대신 답함. Yogurt Lab 검색 시 미국 프랜차이즈가 나옴"],
 ],["24%","14%",None])
 + h3("검색·AI 다섯 레인")
 + table(["레인","상태","근거"],[
   ["SEO (구글·빙)","없음","자체 페이지 없음"],["AEO (AI 오버뷰·Copilot)","없음","인용할 페이지 없음"],["GEO (ChatGPT·Perplexity)","없음","인스타·플레이스는 크롤러가 못 읽음"],["LLMO (모델 지식)","없음","동명 브랜드 충돌"],["NEO (네이버)","양호","플레이스·블로그·리뷰 작동. 순위 측정만 남음"],
 ],["30%","12%",None])
))
# 03 시장·경쟁
S.append(section("03","MARKET","시장과 경쟁",
 lead("성공한 디저트 브랜드는 전부 손님이 올릴 이유를 상품·공간·주기 안에 설계했고, 광고비는 매출의 1~2%였습니다. 실패한 브랜드는 맛이 복제되자 가격 경쟁으로 밀렸습니다.")
 + table(["브랜드","무엇을 했나","통한 이유","가져올 것"],[
   ["Yo-Chi (호주, 셀프서브)","2020년 4개점 → 2026년 70호점. 매장별 토핑 로테이션, 호주 로컬 토핑, 굿즈 상시, 틱톡·인스타로 Gen Z","직접 만드는 즐거움이 중심. 술 대신 가는 저녁 아지트","로컬 토핑, 굿즈, 저녁 포지션"],
   ["요아정 (점원 제조)","2022년 40억 → 2024년 471억, 680개점, 배달앱 디저트 1위. 꿀조합 월 검색 17만","커스텀이 꿀조합 공유 놀이가 됨. 야식 배달","꿀조합 UGC, 야식 배달"],
   ["요거트월드 (무게 셀프)","230여 개점, 일본 26개점. 100g 가격, 저당 라인, 영수증 문구 인증","요아정 대안 + 저당 선점","직접 경쟁자. 영수증 인증 차용"],
   ["런던베이글뮤지엄","일 수량 한정, 웨이팅이 마케팅, 광고비 매출의 1.4%, 2,000억 매각","희소성 + 공간 + 자발적 인증","수량 공개, 경험 투자"],
   ["Crumbl (미국 쿠키)","매주 일요일 신메뉴 4종, 크리에이터가 매주 리뷰","로테이션을 미디어 전략으로","정해진 요일의 주간 드롭"],
   ["16 Handles (미국 셀프서브)","트렌드 맛 즉시 출시, 신규점 첫해 100만 달러","Gen Z 아지트 + 속도","트렌드 토핑 2주 룰"],
   ["실패: 레드망고·핑크베리","160개점 → 10개 미만. 미투 난립, 건강 마케팅 신뢰 붕괴","상품 외 브랜드 자산 없음","복제 불가 자산부터"],
 ],["18%","32%","28%",None])
 + callout("무게 셀프서브는 요거트월드가 이미 230개점입니다. 시드니요거랩의 차별점은 형식이 아니라 세계관, 공간, 로컬 토핑, 저녁 아지트, 굿즈여야 합니다.")
 + h3("공통 성공 공식")
 + numlist(["손님이 올릴 이유를 상품 안에 설계한다: 커스텀, 한정, 캐릭터","주기를 만든다: 매주 같은 요일에 새것이 나오면 크리에이터가 캘린더를 짠다","공간이 촬영 세트다: 오픈키친, 색, 유니폼","희소성은 숫자로 공개한다: 오늘 30개","광고비는 작게, 경험과 굿즈에 투자한다","트렌드 토핑을 2주 안에 올린다","저녁 시간대 술 대신 가는 곳 포지션. 토요일 22시 영업은 이미 이 방향"])
))
# 04 전략
S.append(section("04","STRATEGY","전략",
 lead("광고를 사는 게 아니라 브랜드 자산을 쌓는 12개월입니다. 기둥은 다섯 개입니다.")
 + table(["기둥","내용"],[
   ["세계관","광안리의 시드니. 네이비·크림·서프 비주얼. 레시피 이름은 시드니 해변(Bondi·Manly·Coogee·Bronte). 대표의 시드니 2023~2025가 오리진. 애칭 시요랩 공식화"],
   ["의식","주간 드롭(목요일 12시, 조합 1 + 한정 토핑 1, 수량 공개), #시요랩꿀조합 리그램, 영수증 문구 인증, 무게 맞히기, 겨울 캠페인 시드니의 여름"],
   ["콘텐츠 엔진","손님 컵 UGC → 브랜드 채널(릴스 주 3회) → 크리에이터 월 3~5명 → 검색·지도·원본 페이지가 받아냄"],
   ["확장 검증","배달·팝업·굿즈 채널의 주문·방문 지역 데이터가 2호점 근거. 부산 백화점 팝업 → 서울 팝업 → 2호점"],
   ["측정","브랜드 검색량, 웨이팅 일수, 굿즈 매출 비중, 타지역 방문 비율, 배달 재주문율"],
 ],["16%",None])
 + h3("런던베이글뮤지엄에서 가져올 것과 버릴 것")
 + table(["그들의 방식","시드니요거랩 적용"],[
   ["공간 자체가 콘텐츠","서프보드·캥거루는 이미 있음. 포토스팟 3곳 지정, 바닥 발자국 표시"],
   ["희소성과 의식","주간 드롭 수량 공개, 주말 한정 레시피, 1주년 한정 굿즈"],
   ["굿즈 = 자산 + 매출","스티커·에코백·리유저블 컵부터. 굿즈 매출 비중 관리"],
   ["직영 소수 확장","2호점은 데이터로 결정"],
   ["버릴 것","20석에서 인위적 웨이팅, 가맹 대량 확장, 가격 경쟁"],
 ],["30%",None])
 + h3("배달 원칙: 매장은 체험, 배달은 완성형", "asm")
 + p("배달로 셀프서브를 복제하면 매장의 희소성이 사라집니다. 배달은 야식 시간대 완성형 5종만 팝니다. 요아정이 증명한 겨울 야식 수요를 가져오되 브랜드는 매장에 남깁니다.")
 + table(["항목","내용"],[
   ["운영","18:00~22:00 · 반경 3km · 배민 단독 시작 · 11월 런칭"],
   ["메뉴 5종","Bondi 플레인+그래놀라+꿀 / Manly 초콜릿+누텔라 / Coogee 저당 딸기+베리잼 / Bronte 저당 망고+코코넛 / Dubai 피스타치오+카다이프"],
   ["패키지","네이비 실링 컵, 시요랩 스티커, 드롭 안내 카드 동봉으로 매장 방문 유도"],
   ["지표","주문 수, 재주문율, 주문 지역 분포(2호점 근거)"],
 ],["16%",None])
))
# 05 로드맵
S.append(section("05","ROADMAP","12개월 로드맵과 월별 액션",
 table(["시기","사장","대행"],[
   ["9월","POS 4주치 공유, 카카오톡 채널 개설, 플레이스·구글 권한 공유, 도메인 구매","기준선 리포트, 브랜드북 v1, 랜딩 게시·서치콘솔·빙 등록, 릴스 12편 촬영, 플레이스 광고 시작, 주간 드롭 시작, 굿즈 1차 디자인, 불꽃축제 날짜 확인"],
   ["10월","가을 토핑 3종, 축제 연장 영업·포장 사전 주문 준비, 배달 메뉴 시식","토핑 드롭 운영, 크리에이터 3~5명 방문, 축제 콘텐츠, 배달 패키지 디자인, 배민 입점 준비"],
   ["11월","배달 런칭(18~22시, 3km), 수능 이벤트","시드니의 여름 소재 제작, 배달 런칭 광고, 겨울 메뉴 콘텐츠, 백화점 팝업 제안서"],
   ["12월","연말 대관 운영","시드니의 여름 집행, 크리스마스 레시피, 대관 상품, 트립닷컴 입점 문의(180일 경과)"],
   ["1~2월","저당 메뉴 강화","저당 캠페인, 배달 재주문 쿠폰, 부산 백화점 팝업 집행, 발렌타인 커플 레시피, 봄 토핑 예고"],
   ["3~5월","1주년 한정 레시피·굿즈 확정","1주년 캠페인, 2호점 입지 리포트, 서울 팝업 협의, 토핑 키트 스마트스토어"],
   ["6~8월","성수기 인력·대기 운영","영·일 콘텐츠, 호텔 제휴, 카카오 대기 알림, 성수기 크리에이터, 2호점 결정 보고"],
 ],["10%","36%",None])
 + h3("첫 30일 실행 목록")
 + numlist(["POS 4주치 확보, 기준선 표 작성","카카오톡 채널 개설, 토핑 무료 쿠폰 연결","주간 드롭 시작, 태그 보상 카드 비치","고정 앵글 3개로 릴스 12편 일괄 촬영","플레이스 광고 시작, 소식 주 1회","도메인 구매, 랜딩 게시, 서치콘솔·빙·서치어드바이저 등록","구글 영어 소개, 트립어드바이저 등록, 호텔 카드 3곳","크리에이터 3명 섭외, 10월 방문 확정","불꽃축제 날짜 확인, 운영안 초안"])
))
# 06 플레이북
S.append(section("06","PLAYBOOK","실행 플레이북",
 h3("주간 콘텐츠 캘린더 (수요일 휴무 기준)")
 + table(["요일","포맷","예시"],[
   ["월","스토리 예고","목요일 드롭 예고. 한정 토핑 힌트: 부산 무화과 + 투표 몇 g 담을래?"],
   ["화","릴스 토핑 붓기","초콜릿 소스 3초 → 컵 클로즈업 → 100g 4,500원, 담는 건 네 마음"],
   ["수","스레드 (휴무)","대표 글: 시드니 본다이에서 매일 먹던 요거트, 왜 광안리였는지"],
   ["목","드롭 공개 릴스 + 피드","시요랩 픽 #7 Bondi: 플레인+그래놀라+꿀+무화과. 무화과 40인분"],
   ["금","캐러셀 리그램","이번 주 #시요랩꿀조합 손님 컵 5장, 각 장에 조합 텍스트"],
   ["토","저녁 아지트 릴스","20시 이후 조명 낮춘 매장, 술 대신 시요랩, 22시 영업 표기"],
   ["일","무게 맞히기 결과 / 청결 루틴","이번 주 정답 312g, 3명 무료 또는 토핑 바 교체 타임랩스"],
 ],["8%","22%",None])
 + h3("릴스 스크립트 5개")
 + numlist(["담는 과정 15초: 기계에서 요거트 1초 → 토핑 4종 4초 → 저울 숫자 3초 → 첫 스푼 4초 → 로고 + 광안역 5번 출구 7분. 캡션 첫 줄 광안리 요거트 아이스크림, 직접 담는 셀프 토핑","광안역에서 오는 길 20초: 5번 출구 → 골목 3컷 → 간판. 도보 시간 자막. 고정 게시물","드롭 공개 12초: 카운트 3,2,1 → 조합 클로즈업 → 40인분 한정. 매주 목요일 12시","두 컵 비교 15초: 같은 무게 다른 조합, 둘 다 4,500원대, 뭐 고를래? 댓글 유도","대표 이야기 30초: 시드니에서 2년 동안 매일 이렇게 먹었어요. 한국엔 없길래 광안리에 열었습니다"])
 + p("해시태그 고정 세트: #시요랩 #시드니요거랩 #광안리디저트 #광안리카페 #광안리아이스크림 #요거트아이스크림 #셀프토핑 #부산디저트 #gwangalli #busanfood", muted=True, size=13.5)
 + h3("시요랩 픽 주간 드롭 12주", "asm")
 + table(["주","조합명","구성","한정 토핑","수량"],[
   ["1","Bondi","플레인 + 그래놀라 + 꿀","부산 무화과","40"],["2","Manly","초콜릿 + 누텔라 + 초코칩","비스코프 크럼블","40"],["3","Coogee","저당 딸기 + 베리잼 + 연유","생딸기","30"],["4","Bronte","저당 망고 + 코코넛 + 피치잼","패션프루트","30"],["5","Dubai","피스타치오 + 카다이프 + 초콜릿","카다이프 추가","40"],["6","Tamarama","솔티드캬라멜 + 비스코프 + 아몬드","프레첼","40"],["7","밤 Bondi","플레인 + 밤 + 꿀","구운 밤","30"],["8","불꽃축제 스페셜","초콜릿 + 팝핑캔디 + 스프링클","팝핑캔디","100"],["9","고구마 Manly","초콜릿 + 고구마 + 아몬드","군고구마","30"],["10","유자 Coogee","저당 딸기 + 유자청","유자청","30"],["11","수능 응원","플레인 + 초코 + 엿","엿","50"],["12","시드니의 여름 #1","저당 망고 + 코코넛 + 파인애플","파인애플","40"],
 ],["6%","20%",None,"20%","8%"])
 + p("공개 형식: 목요일 12시 릴스 + 피드 + 스토리 카운트다운. 매장 A보드에 오늘 남은 수량 손글씨.", muted=True, size=13.5)
 + h3("인스타 광고 세팅", "asm")
 + table(["캠페인","목표","타깃","일 예산","소재","판단 기준"],[
   ["A 지역 도달","프로필 방문","반경 3km, 18~34세","2만 원","릴스 1·4","프로필 방문당 150원 이하"],
   ["B 여행객","프로필 방문","부산 여행 관심 + 현재 부산 위치","2만 원","릴스 2","길찾기 클릭 발생"],
   ["C 리타겟","길찾기·메시지","30일 프로필 방문·릴스 75% 시청","1만 원","드롭 릴스","클릭당 300원 이하"],
   ["D 파트너십","도달","크리에이터 릴스 중 저장률 상위 1편","2만 원","원본","저장률 유지"],
 ],["14%","12%",None,"10%","12%","20%"])
 + p("한 광고 세트에 3안씩, 7일 후 프로필 방문당 비용 하위 2안 교체. 월 합계 약 200만 원.", muted=True, size=13.5)
 + h3("광고 카피 A: 로컬 2030 (반경 3km, 재방문)")
 + table(["#","헤드라인","본문","CTA"],[
   ["A1","담는 만큼만 낸다","요거트 6종, 토핑 30종. 100g에 4,500원. 오늘은 얼마나 담을 건데","길찾기"],["A2","같은 컵이 두 번 안 나오는 집","어제 조합 오늘 또 못 만든다. 광안리 셀프 토핑 시요랩","프로필 보기"],["A3","목요일 12시, 이번 주 드롭","이번 주 조합 하나, 한정 토핑 하나, 40인분. 없어지면 다음 주","알림 켜기"],["A4","술 대신 요거트","금·토 밤 10시까지. 광안리에서 술 안 마시고 앉아 있을 곳","길찾기"],["A5","저당인데 딸기 맛이 난다","저당 스트로베리·애플망고. 다이어트 중이면 이 둘","메뉴 보기"],["A6","광안역 5번 출구, 7분","해변 말고 골목. 457m 걸어오면 시드니","길찾기"],["A7","토핑 30종 앞에서 3분 고민","결정 장애면 이번 주 시요랩 픽으로. 이미 정해 놨음","드롭 보기"],["A8","오늘 몇 g?","무게 맞히면 무료. 매주 정답자 3명","참여하기"],["A9","수요일은 쉽니다","대신 목요일 드롭이 있다. 수요일 헛걸음 방지용 광고","영업시간"],["A10","카톡 친구면 토핑 하나","채널 추가하고 보여주면 토핑 1종 무료. 목요일마다 드롭 소식","채널 추가"],
 ],["6%","28%",None,"12%"])
 + h3("광고 카피 B: 여행객 (부산 여행 중, 첫 방문)")
 + table(["#","헤드라인","본문","CTA"],[
   ["B1","광안리에서 시드니","호주에서 매일 먹던 셀프 요거트, 부산에 한 곳","길찾기"],["B2","광안리 디저트 정했어?","요거트 6종에 토핑 30종, 내가 담아서 무게로 계산. 광안역 5번 출구","프로필 보기"],["B3","광안대교 보고 7분","해변에서 골목으로. 걷다 보면 서프보드 벽","길찾기"],["B4","부산 여행 사진 한 장 더","서프보드 벽 앞, 컵 들고. 찍는 자리 바닥에 표시해 뒀음","사진 보기"],["B5","밤 10시까지 여는 디저트","토요일 광안리, 저녁 먹고 한 컵. 술 아님","영업시간"],["B6","100g 4,500원, 담는 건 네 마음","정해진 메뉴 없음. 컵 하나 들고 시작","이용 방법"],["B7","저당 요거트도 있음","여행 중 죄책감 없는 디저트. 스트로베리·애플망고 저당","메뉴 보기"],["B8","이번 주만 있는 토핑","목요일마다 바뀌는 한정 토핑. 이번 주는 부산 무화과","드롭 보기"],["B9","Self-serve froyo, Gwangalli","6 flavors, 30+ toppings, pay by weight. 7 min from Gwangan Stn Exit 5","Directions"],["B10","부산 오면 여기","리뷰 184개가 찾아온 골목. 광안리 시드니요거랩","길찾기"],
 ],["6%","28%",None,"12%"])
 + h3("크리에이터 브리프 (마이크로 1~5만 팔로워)", "asm")
 + table(["항목","내용"],[
   ["조건","방문 체험 + 제작비 10~30만 원(가정). 협찬 표기 필수"],["필수","릴스 1편(15~30초), 스토리 2개, 위치 태그, #시요랩, 공동 게시 수락"],["요청 장면","담는 과정, 저울 숫자, 첫 스푼. 금지: 가격 오기, 요아정 비교 발언"],["사용권","원본 제공, 매장 계정·광고 6개월 사용"],["성과 확인","OO 보고 왔어요 카운트 또는 쿠폰 코드"],["구성","월 3~5명: 부산 맛집 2, 여행 2, 외국인 1"],
 ],["16%",None])
 + h3("매장 내 문구")
 + table(["위치","문구"],[
   ["영수증 하단","이 영수증 사진 + #시요랩 올리면 다음 방문 토핑 1종 무료"],["카운터 카드(한/영)","태그하고 토핑 받기 @sydney.yogurt.lab · Tag us, get a topping"],["바닥 스티커","서프보드 벽 앞 발자국 두 개 + 여기서 찍으면 예뻐요"],["컵 슬리브(시즌)","BUILD YOUR OWN RECIPE · 광안리의 시드니"],["A보드","오늘의 드롭 Bondi · 남은 수량 12"],
 ],["22%",None])
 + h3("카카오톡 채널 메시지")
 + table(["트리거","메시지"],[
   ["친구 추가 자동","시요랩 친구 환영. 이 메시지 보여주면 토핑 1종 무료(1회). 매주 목요일 드롭 소식 보내드려요."],["목요일 11시","이번 주 시요랩 픽 Coogee. 생딸기 30인분 한정. 오늘 12시 오픈."],["21일 미방문","3주 만이네요. 이번 주 드롭 + 100g 무료 쿠폰."],["배달 런칭","11월부터 18~22시 배달 시작. 완성형 5종. 첫 주문 토핑 1종 추가."],
 ],["20%",None])
 + h3("저녁 아지트 · 불꽃축제 · 트렌드 룰")
 + table(["항목","운영"],[
   ["저녁 아지트 (금·토 20시 이후)","조명 60%, 서프 록·로파이 플레이리스트, 컵 슬리브 NIGHT 스탬프, 메뉴판 상단 밤 요거트: 저당 2종 + 디카페인 토핑. 지표는 20시 이후 객수 비중"],
   ["부산불꽃축제 (11월 초, 날짜 확정 후)","2주 전 스페셜 드롭 예고와 포장 사전 주문 폼. 당일 12~23시 연장, 포장 전용 라인, 완성형 100개 사전 제조, 좌석 대기 없이 포장 유도. 불꽃 배경 컵 사진 태그 시 다음 방문 100g 무료"],
   ["트렌드 토핑 2주 룰","틱톡 #dessert, 인스타 탐색, 요아정·요거트월드 신메뉴, 편의점 신상 감시. 감지 → 수급 3일 → 테스트 2일 → 드롭 출시. 부산에서 처음은 사실 확인 후에만"],
 ],["28%",None])
))
# 07 검색·AI
S.append(section("07","SEARCH & AI","검색·AI 노출",
 lead("ChatGPT에서 검색되려면 세 조건이 동시에 필요합니다. 열린 웹에 매장 소유 페이지가 있어야 하고, 그 페이지가 Bing에 색인되어야 하며, 질문에 바로 답하는 문단이 있어야 합니다. 지금은 셋 다 없습니다.")
 + h3("ChatGPT가 답을 만드는 과정")
 + numlist(["Bing 색인과 자체 크롤러(OAI-SearchBot) 색인에서 후보 페이지를 고른다","후보 페이지를 ChatGPT-User 에이전트가 실시간으로 열어 읽는다","답이 되는 문장을 문단 단위로 뽑아 출처 링크와 함께 답한다"])
 + p("인스타는 로그인 벽 뒤라 1단계 후보에 못 들어갑니다. 네이버 플레이스는 네이버 밖 크롤러가 읽기 어렵습니다. 지금 이 매장 관련 질문의 출처는 블로거 글입니다.")
 + h3("실행 5단계")
 + table(["단계","내용","시점"],[
   ["1 원본 색인","랜딩을 sydneyyogurtlab.com에 게시. 구글 서치콘솔 → Bing Webmaster Tools 가져오기. robots.txt에 학습·색인·실시간 열람 크롤러 전부 허용(완료). site: 검색으로 확인","1~2주"],
   ["2 질문 하나 = 페이지 하나","/gwangalli-yogurt, /gwangalli-dessert, /self-topping-busan, /low-sugar, /delivery, /en/gwangalli-frozen-yogurt. 각 페이지 직답 문단 + 표 + FAQ 3~5 + FAQ JSON-LD","2~4주"],
   ["3 남이 못 가진 숫자","월간 최다 판매 조합, 토핑 30종 목록과 교체 기록, 드롭 결과를 /data/monthly에 누적. 유일한 원출처가 됨","매월"],
   ["4 모델 지식 (LLMO)","표기 통일 시드니요거랩 (Sydney Yogurt Lab, 부산 광안리). 지역 언론 창업 스토리 보도, 트립어드바이저·구글·다이닝코드·식신 등록. 분기마다 브라우징 끄고 시드니요거랩이 뭐야? 질의 기록","분기"],
   ["5 측정","질문 8개를 ChatGPT 검색·Perplexity·구글 AI 오버뷰·네이버 AI 브리핑에 14일마다 던져 출처 O/X 기록. 선행 지표는 AI 크롤러 방문 수(Cloudflare 봇 분류)","14일"],
 ],["18%",None,"10%"])
 + h3("기대 시점")
 + table(["단계","반영"],[["Bing·구글 색인","1~2주"],["ChatGPT 검색·Perplexity 인용","4~8주"],["브라우징 없는 모델 지식","분기 단위, 학습 주기 의존"]],["40%",None])
 + p("인용을 보장하는 방법은 없습니다. 위 조건을 갖춘 페이지가 블로거 글보다 원출처로서 우선순위가 높아지는 것이고, 실제 인용 여부는 14일마다 측정으로만 확인됩니다.", muted=True, size=13.5)
 + h3("함께 제공된 파일", "fix")
 + table(["파일","내용"],[["index.html","랜딩 한 장. 한국어 본문 + 영어 요약, IceCreamShop·FAQPage JSON-LD, 확정 사실만 기재"],["llms.txt","AI 크롤러용 사실 요약. 미국·멜버른 동명 브랜드와 무관함 명시"],["robots.txt","GPTBot·OAI-SearchBot·ChatGPT-User·ClaudeBot·Claude-SearchBot·Claude-User·PerplexityBot·Perplexity-User·Google-Extended·Applebot-Extended·Yeti 허용"],["sitemap.xml","사이트맵. 도메인 연결 후 제출"]],["18%",None])
))
# 08 예산
S.append(section("08","BUDGET","예산",
 lead("초기 일회성 1,000만 원 + 월 운영 400만 원. 대행 수수료 별도.") + '<div style="margin: -6px 0 14px 0;">%s</div>' % tag_asm().replace('margin-left: 6px;','margin-left: 0;')
 + p("가정: 일 100컵 × 객단가 약 1.2만 원 = 월 매출 약 3,600만 원, 마케팅비 매출의 10~12%. POS 4주치 확보 후 재산정. 단위 만 원.", muted=True, size=13.5)
 + '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 40px; margin-top: 10px;">'
 + '<div>' + h3("초기 일회성") + table(["항목","금액"],[["굿즈 1차 (스티커 300·에코백 200·리유저블 컵 150)","300"],["포토스팟 · 사이니지","300"],["브랜드 촬영","200"],["배달 패키지 디자인","100"],["예비","100"],["합계","1,000"]],[None,"18%"]) + '</div>'
 + '<div>' + h3("월 운영") + table(["항목","금액"],[["인스타 · 릴스 광고","120"],["크리에이터","130"],["콘텐츠 제작","70"],["플레이스 광고","50"],["인쇄 · 툴","30"],["합계","400 / 월"]],[None,"22%"]) + '</div>'
 + '</div>'
 + p("첫 2개월은 이대로 운영하고 채널 성과에 따라 재배분합니다. 팝업과 1주년은 별도 편성. 대행 수수료는 월 고정 + 성과 연동(브랜드 검색량·객수 기준)을 권장합니다.", muted=True, size=13.5)
))
# 09 측정
S.append(section("09","MEASUREMENT","측정 체계",
 lead("고쳤다로 끝내지 않습니다. 같은 자로 매주 잽니다. 목표 수치는 1차 재측정(게시 14일 후) 결과를 보고 대표와 함께 정합니다.")
 + table(["지표","출처","의미","주기"],[
   ["브랜드 검색량 시드니요거랩 · 시요랩","네이버 데이터랩 · 키워드도구","인지도의 가장 정직한 지표","매주"],["일 객수 · 객단가 · 포장 비율 · 시간대","POS","최종 성과","매주"],["웨이팅 발생 일수","매장 기록","목적지 브랜드 여부","매주"],["굿즈 매출 비중","POS","브랜드 자산 화폐화","매월"],["배달 주문 · 재주문율 · 지역 분포","배민 통계","겨울 바닥 + 2호점 근거","매주"],["타지역 방문 비율","리뷰 · 채널 설문","확장 가능성","매월"],["플레이스 순위 · 저장 · 길찾기 · 리뷰","스마트플레이스 · 구글","탐색 전환","격주"],["릴스 저장률 · 프로필 방문 · 링크 클릭","인스타 인사이트","콘텐츠 효율","매주"],["위치태그 · #시요랩 게시물 수","수동 집계","확산","격주"],["AI 답변 인용 여부","ChatGPT · Perplexity · 네이버 AI 브리핑 질문 8개","원본 페이지 효과","14일"],
 ],["32%","26%",None,"9%"])
 + h3("주간 시트 컬럼")
 + p("주차 / 릴스 편수 / 평균 저장률 / 프로필 방문 / 링크 클릭 / 길찾기 / 위치태그 게시물 수 / #시요랩 게시물 수 / 카카오 친구 순증 / 플레이스 저장 / 리뷰 순증 / 광고비 / 프로필 방문당 비용 / 객수 / 20시 이후 객수 / 드롭 소진 시각", size=14)
 + h3("보고 주기")
 + table(["주기","내용"],[["매주 월요일","주간 시트 갱신, 광고 세트 교체 결정"],["격주","플레이스·구글·AI 인용 재측정, 이 문서 개정"],["매월","굿즈 비중, 타지역 방문 비율, 채널 예산 재배분, 월간 리포트"],["3개월","파일럿 종료 보고. 기준선 대비 전후 비교로 연장 결정"]],["18%",None])
))
# 10 가정·확인·약속
S.append(section("10","ASSUMPTIONS & COMMITMENTS","가정, 확인 사항, 약속",
 h3("이렇게 가정하고 시작합니다", "asm")
 + numlist(["배달: 18~22시, 반경 3km, 완성형 5종, 11월 배민 런칭","굿즈 1차: 스티커 300 · 에코백 200 · 리유저블 컵 150","2호점: 부산 팝업 → 서울 팝업 순으로 검증 후 결정","시요랩 애칭 공식 사용","계정 권한 공유, 도메인 매장 명의 구매"])
 + h3("대표 확인이 필요한 것")
 + numlist(["POS 4주치(일별 객수·매출·포장 비율·시간대)","월 광고비 상한과 대행 수수료 구조","시드니 근무 이력(2023~2025)의 브랜드 스토리 공개 범위","저당 2종의 당 함량 수치(광고에 쓰려면 실제 값 필요)","불꽃축제 당일 운영 인력"])
 + '<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 40px; margin-top: 10px;">'
 + '<div>' + h3("약속하는 것") + ul(["측정 없이 완료라고 말하지 않습니다","14일마다 같은 지표를 전후 비교로 보고합니다","페이지와 구조화 데이터에는 화면에 보이는 사실만 씁니다","대표 계정은 권한 공유 방식으로만 다룹니다"]) + '</div>'
 + '<div>' + h3("하지 않는 것") + ul(["리뷰 구매, 블로그 대량 체험단, 백링크 구매","순위 보장, 인용 보장 문구","화면과 다른 메타·구조화 데이터, 숨긴 텍스트","요아정 직접 비교 광고, 건강 효능 주장"]) + '</div>'
 + '</div>'
 + h3("개정 이력")
 + table(["버전","날짜","내용"],[["v1.0","2026-09-07","최초 발행. 진단·전략·로드맵·플레이북·검색/AI·예산·측정"]],["10%","16%",None])
))

main = HEAD + '<div style="width: 794px; background: #FFFFFF;">' \
 + '<div style="background: %s; padding: 28px 56px; display: flex; justify-content: space-between; align-items: center;"><div style="font-family: %s; font-size: 11px; letter-spacing: 0.12em; color: #FFFFFF;">SYDNEY YOGURT LAB · EXECUTION PLAN v1.0</div><div style="font-family: %s; font-size: 11px; letter-spacing: 0.08em; color: #B7BCE8;">2026. 09. 07</div></div>' % (NAVY, MONO, MONO) \
 + ''.join(S) \
 + '<div style="background: %s; padding: 22px 56px; display: flex; justify-content: space-between; font-family: %s; font-size: 10.5px; letter-spacing: 0.08em; color: #B7BCE8;"><span>시드니요거랩 · 부산 수영구 수영로540번길 24-4 1층 · 0507-1365-1715</span><span>[대행사명] · 격주 개정</span></div>' % (DEEP, MONO) \
 + '</div>\n' + TAIL
open('Main.dc.html','w',encoding='utf-8').write(main)
import json
json.dump({"artboards":[{"file":"Cover.dc.html","x":0,"y":0,"w":794,"h":1123,"print":"fixed","title":"표지"},{"file":"Main.dc.html","x":900,"y":0,"w":794,"h":14800,"print":"flow","expand":"fill","title":"실행안 본문"}],"launch":{"view":"canvas"}}, open('canvas.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print("ok", len(main)//1024, "KB")
