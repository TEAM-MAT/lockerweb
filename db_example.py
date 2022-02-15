DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '', #RDS 인스턴스내에서 생성한 Database이름. mysql들어가서 create database ssulocker;과 같이 쿼리문을 통해서 생성.
        'USER':'', #RDS인스턴스 내에서 서비스 용으로 사용할 이용자 이름(관리자와 별도로 생성하는 것을 권장.)
        'PASSWORD':'', # 계정 비밀번호(서비스용 계정 비밀번호)
        'HOST':'', #RDS 인스턴스의 엔드포인트 ( ~.com으로 끝나는 것), ex) db.ckazeqsmvezn.ap-northeast-2.rds.amazonaws.com
        'PORT':'3306'
    }
}