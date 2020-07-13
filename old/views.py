from django.shortcuts import render
import pymysql
#from datetime import datetime
from datetime import datetime
import matplotlib.pyplot as plt
import base64
from django.shortcuts import HttpResponse
from test4 import imgg,imgg1,imgg2
con = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='70582829',
    db='oldweb',
    cursorclass=pymysql.cursors.DictCursor,
    charset='utf8'
)
# Create your views here.
def login(request):
    return render(request, 'login1.html')


def logins(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(password)
    cur=con.cursor()
    sql='select * from sys_user where UserName=%s'
    cur.execute(sql,[username])
    result = cur.fetchall()
    if password == result[0]['Password']:
        return render(request, 'index.html')
    else:
        return render(request, 'login1.html')


def register(request):
    return render(request, 'register.html')


def regist(request):
    name=request.POST.get('name')
    sex=request.POST.get('sex')
    phone= request.POST.get('phone')
    mail=request.POST.get('mail')
    password = request.POST.get('password')
    cpassword = request.POST.get('cpassword')
    if password != cpassword:
        return render(request, 'register.html')
    else:
        cur=con.cursor()
        sql='insert into sys_user(UserName,Password,SEX,EMAIL,PHONE) values({},{},{},{},{})'.format(name,password,sex,mail,phone)
        cur.execute(sql)
        con.commit()
        return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def oldmanzhuce(request):
    return render(request, 'oldmanzhuce.html')


def oldmanzhuce1(request):
    oldmanname = request.GET.get('oldmanname')
    oldmansex = request.GET.get('oldmansex')
    oldmanphone = request.GET.get('oldmanphone')
    oldmancard = request.GET.get('oldmancard')
    oldmanbirth = request.GET.get('oldmanbirth')
    oldmanhealth = request.GET.get('oldmanhealth')
    print(oldmansex)
    print(oldmanphone)
    print(oldmancard)
    print(oldmanbirth)
    print(oldmanhealth)
    cur = con.cursor()
    sql1 = 'select count(*) from oldperson_info'
    cur.execute(sql1)
    result = cur.fetchall()
    oldmanid = result[0]['count(*)']
    oldmanid = int(oldmanid) + 1
    sql = 'replace into oldperson_info(ID,username,gender,phone,id_card,birthday,health_state) values({},{},{},{},{},{},{})'.format(
        oldmanid, "'" + oldmanname + "'", "'" + oldmansex + "'", "'" + oldmanphone + "'"
        , "'" + oldmancard + "'", "'" + oldmanbirth + "'", "'" + oldmanhealth + "'")
    cur.execute(sql)
    con.commit()
    return render(request, 'index.html')


def oldmanruzhu(request):
    cur = con.cursor()
    sql = 'select * from oldperson_info'
    cur.execute(sql)
    result = cur.fetchall()
    return render(request, 'oldmanruzhu.html', {'var': result})


def oldmanruzhu1(request):
    renming = request.POST.get('selec')
    ruzhutime = request.POST.get('ruzhutime')
    likaitime = request.POST.get('likaitime')
    tuxiang = request.POST.get('tuxiang')
    touxiang = request.POST.get('touxiang')
    roomnum = request.POST.get('roomnum')
    print(type(renming))
    cur = con.cursor()
    sql = 'replace into oldperson_info(checkin_date,checkout_date,imgset_dir,profile_photo,room_number) values(%s,%s,%s,%s,%s) where username=%s'.format(
        ruzhutime, likaitime, tuxiang, touxiang, roomnum)
    cur.execute(
        'update oldperson_info set checkin_date=%s ,checkout_date=%s,imgset_dir=%s,profile_photo=%s,room_number=%s where username=%s',
        (ruzhutime, likaitime, tuxiang, touxiang, roomnum, renming))
    con.commit()
    return render(request, 'index.html')


def oldmanernv1(request):
    cur = con.cursor()
    sql = 'select * from oldperson_info'
    cur.execute(sql)
    result = cur.fetchall()
    return render(request, 'oldmanernv1.html', {'var': result})


def oldmanernv11(request):
    ernv1name = request.POST.get('ernv1name')
    relation1 = request.POST.get('relation1')
    phone1 = request.POST.get('phone1')
    weixin1 = request.POST.get('weixin1')
    renming = request.POST.get('selec')
    cur = con.cursor()
    cur.execute(
        'update oldperson_info set firstguardian_name=%s,firstguardian_relationship=%s,firstguardian_phone=%s,firstguardian_wechat=%s where username=%s',
        (ernv1name, relation1, phone1, weixin1, renming))
    con.commit()
    return render(request, 'index.html')


def oldmanernv2(request):
    cur = con.cursor()
    sql = 'select * from oldperson_info'
    cur.execute(sql)
    result = cur.fetchall()
    return render(request, 'oldmanernv2.html', {'var': result})


def oldmanernv22(request):
    ernv2name = request.POST.get('ernv2name')
    relation2 = request.POST.get('relation2')
    phone2 = request.POST.get('phone2')
    weixin2 = request.POST.get('weixin2')
    renming = request.POST.get('selec')
    cur = con.cursor()
    cur.execute(
        'update oldperson_info set secondguardian_name=%s,secondguardian_relationship=%s,secondguardian_phone=%s,secondguardian_wechat=%s where username=%s',
        (ernv2name, relation2, phone2, weixin2, renming))
    con.commit()
    return render(request, 'index.html')


def oldmanchuangjian(request):
    cur = con.cursor()
    sql = 'select * from volunteer_info'
    cur.execute(sql)
    result = cur.fetchall()
    return render(request, 'oldmanchuangjian.html', {'var': result})


def oldmanchuangjian1(request):
    chuangjianname = request.POST.get('chuangjianname')
    chuangjiantime = request.POST.get('chuangjiantime')
    descrip = request.POST.get('descrip')
    gengxintime = request.POST.get('gengxintime')
    gengxinname = request.POST.get('gengxinname')
    cur = con.cursor()
    cur.execute('update oldperson_info set CREATED=$s,CREATEBY=%s,UPDATED=%s,UPDATEBY=%s,DESCRIPTION=%s',
                (chuangjiantime, chuangjianname, gengxintime, gengxinname, descrip))
    con.commit()
    return render(request, 'index.html')


def workmanzhuce(request):
    return render(request, 'workmanzhuce.html')


def workmanzhuce1(request):
    workmanname = request.POST.get('workmanname')
    workmansex = request.POST.get('workmansex')
    workmanphone = request.POST.get('workmanphone')
    workmancard = request.POST.get('workmancard')
    workmanbirth = request.POST.get('workmanbirth')
    cur = con.cursor()
    sql = 'replace into employee_info(username,gender,phone,id_card,birthday) values({},{},{},{},{})'.format(
        "'" + workmanname + "'", "'" + workmansex + "'", "'" + workmanphone + "'", "'" + workmancard + "'",
        "'" + workmanbirth + "'")
    cur.execute(sql)
    con.commit()
    return render(request, 'index.html')


def workmanruzhi(request):
    cur = con.cursor()
    sql = 'select * from employee_info'
    cur.execute(sql)
    result = cur.fetchall()
    return render(request, 'workmanruzhi.html', {'var': result})


def workmanruzhi1(request):
    ruzhitime = request.POST.get('ruzhutime')
    lizhitime = request.POST.get('lizhitime')
    wtouxiang = request.POST.get('wtouxiang')
    wtuxiang = request.POST.get('wtuxiang')
    renming = request.POST.get('selec')
    cur = con.cursor()
    cur.execute('update employee_info set hire_date=%s,resign_date=%s,imgset_dir=%s,profile_photo=%s where username=%s',
                (ruzhitime, lizhitime, wtouxiang, wtuxiang, renming))
    con.commit()
    return render(request, 'index.html')


def workmanchuangjian(request):
    cur = con.cursor()
    sql = 'select * from employee_info'
    cur.execute(sql)
    result = cur.fetchall()
    return render(request, 'workmanchuangjian.html', {'var': result})


def workmanchuangjian1(request):
    chuangjianname = request.POST.get('chuangjianname')
    chuangjiantime = request.POST.get('chuangjiantime')
    descrip = request.POST.get('descrip')
    gengxintime = request.POST.get('gengxintime')
    gengxinname = request.POST.get('gengxinname')
    renming = request.POST.get('selec')
    cur = con.cursor()
    cur.execute(
        'update employee_info set CREATED=%s,CREATEBY=%s,UPDATED=%s,UPDATEBY=%s,DESCRIPTION=%s where username=%s',
        (chuangjiantime, chuangjianname, gengxintime, gengxinname, descrip, renming))
    con.commit()
    return render(request, 'index.html')


def yigongzhuce(request):
    return render(request, 'yigongzhuce.html')


def yigongzhuce1(request):
    vname = request.POST.get('vname')
    vsex = request.POST.get('vsex')
    vphone = request.POST.get('vphone')
    vcard = request.POST.get('vcard')
    vbirth = request.POST.get('vbirth')
    cur = con.cursor()
    sql = 'replace into volunteer_info(name,gender,phone,id_card,birthday) values({},{},{},{},{})'.format(
        "'" + vname + "'", "'" + vsex + "'", "'" + vphone + "'", "'" + vcard + "'", "'" + vbirth + "'")
    cur.execute(sql)
    con.commit()
    return render(request, 'index.html')


def yigonggongzuo(request):
    cur = con.cursor()
    sql = 'select * from volunteer_info'
    cur.execute(sql)
    result = cur.fetchall()
    return render(request, 'yigonggongzuo.html', {'var': result})


def yigonggongzuo1(request):
    renming = request.POST.get('selec')
    time1 = request.POST.get('time1')
    time2 = request.POST.get('time2')
    ytouxiang = request.POST.get('ytouxiang')
    ytuxiang = request.POST.get('ytuxiang')
    cur = con.cursor()
    cur.execute(
        'update volunteer_info set checkin_date=%s,checkout_date=%s,imgset_dir=%s,profile_photo=%s where name=%s',
        (time1, time2, ytuxiang, ytouxiang, renming))
    con.commit()
    return render(request, 'index.html')


def yigongchuangjian(request):
    cur = con.cursor()
    sql = 'select * from volunteer_info'
    cur.execute(sql)
    result = cur.fetchall()
    return render(request, 'yigongchuangjian.html', {'var': result})


def yigongchuangjian1(request):
    chuangjianname = request.POST.get('chuangjianname')
    chuangjiantime = request.POST.get('chuangjiantime')
    descrip = request.POST.get('descrip')
    gengxintime = request.POST.get('gengxintime')
    gengxinname = request.POST.get('gengxinname')
    renming = request.POST.get('selec')
    cur = con.cursor()
    cur.execute('update volunteer_info set CREATED=$s,CREATEBY=%s,UPDATED=%s,UPDATEBY=%s,DESCRIPTION=%s where name=%s',
                (chuangjiantime, chuangjianname, gengxintime, gengxinname, descrip, renming))
    con.commit()
    return render(request, 'index.html')


def chart(request):
    cur = con.cursor()
    sql = 'select birthday from oldperson_info'
    cur.execute(sql)
    result = cur.fetchall()
    a = 0
    b = 0
    time = datetime.now()
    for one in result:
        d = datetime.strptime(str(one['birthday']), '%Y-%m-%d %H:%M:%S')
        c = int((time - d).days / 365)
        if c >= 50:
            a = a + 1
        else:
            b = b + 1
    years = ("50岁以上", "50岁以下")
    li = []
    li.append(a)
    li.append(b)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(years, li)
    plt.title('老年人年龄统计图')
    plt.savefig("D:/web1/static/images/oldman.jpg")
    plt.clf()
    sql1='select birthday from volunteer_info'
    cur.execute(sql1)
    result1=cur.fetchall()
    a1 = 0
    b1 = 0
    time = datetime.now()
    for one in result1:
        d = datetime.strptime(str(one['birthday']), '%Y-%m-%d %H:%M:%S')
        c = int((time - d).days / 365)
        if c >= 50:
            a1 = a1 + 1
        else:
            b1 = b1 + 1
    years = ("50岁以上", "50岁以下")
    li1 = []
    li1.append(a1)
    li1.append(b1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(years, li1)
    plt.title('义工年龄统计图')
    plt.savefig("D:/web1/static/images/yigong.jpg")
    plt.clf()
    sql2 = 'select birthday from employee_info'
    cur.execute(sql2)
    result2 = cur.fetchall()
    a2 = 0
    b2 = 0
    time = datetime.now()
    for one in result1:
        d = datetime.strptime(str(one['birthday']), '%Y-%m-%d %H:%M:%S')
        c = int((time - d).days / 365)
        if c >= 50:
            a2 = a2 + 1
        else:
            b2 = b2 + 1
    years = ("50岁以上", "50岁以下")
    li1 = []
    li1.append(a1)
    li1.append(b1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.bar(years, li1)
    plt.title('义工年龄统计图')
    plt.savefig("D:/web1/static/images/employee.jpg")
    return render(request, 'chart.html')


def camera(request):
    return render(request, 'cameralist.html')


def jiankong(request):
    return render(request, 'charts.html')


def getface(request):
    if request.POST:
        time = datetime.now().strftime('%Y%m%d&%H%M%S')
        time1 = datetime.now()
        strs = request.POST['message']
        imgdata = base64.b64decode(strs)
        print(imgdata)
        file = open(u'static/facedata/' + time + '.jpg', 'wb')
        file.write(imgdata)
        file.close()
        imgg('static/facedata/' + time + '.jpg')
        imgg1(time)
            #imgg(time, time1, 'static/facedata/' + time + '.jpg')
        imgg2(time,time1)
        return HttpResponse('no')
    else:
        return HttpResponse('no')


def caiji(request):
    return render(request, 'caiji.html')


def getface1(request):
    if request.POST:
        time = datetime.now().strftime('%Y%m%d&%H%M%S')
        time1 = datetime.now()
        strs = request.POST['message']
        imgdata = base64.b64decode(strs)
        print(imgdata)
        try:
            file = open(u'D:/web1/imag/faces/old_people/106/' + time + '.jpg', 'wb')
            file.write(imgdata)
            file.close()

        except:
            print('as')

        return HttpResponse('no')
    else:
        return HttpResponse('no')