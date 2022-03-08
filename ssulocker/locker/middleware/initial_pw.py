def init_pw(users):
    initresult={"result":"","num":0}
    for u in users:
        if u.is_admin!=True:
            pn=u.phone#전화번호는 010떼고 입력받아야함.
            u.set_password(pn)
            u.save()
            number_process+=1
    if number_process>0:
        initresult["result"]="성공"
    else:
        initresult["result"]="실패 혹은 초기화할 유저가 없습니다."
        initresult["num"]=number_process
    return initresult