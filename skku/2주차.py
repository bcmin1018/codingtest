
def exchg(money, contry):
    if contry not in ['미국', '중국', '유럽']:
        print('%s에 대한 환율 정보가 없습니다.' % contry)

    if str(contry) == '미국':
        exchange = int(money) / 1362.00
        print('%s 원은 %s 돈으로 %.2f 달러 입니다.' % (money, contry, exchange))

    if str(contry) == '유럽':
        exchange = int(money) / 1358.46
        print('%s 원은 %s 돈으로 %.2f 유로 입니다.' % (money, contry, exchange))

    if str(contry) == '유럽':
        exchange = int(money) / 197.15
        print('%s 원은 %s 돈으로 %.2f 위안 입니다.' % (money, contry, exchange))

exchg(12000, '유럽') # 유럽일 경우 함수 실행
exchg(30000, '미국') # 미국일 경우 함수 실행
exchg(15000, '중국') # 중국일 경우 함수 실행
exchg(10000, '일본') # 일본일 경우 함수 실행