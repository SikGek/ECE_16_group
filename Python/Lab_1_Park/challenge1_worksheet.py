#0.3 Excercise
def list_shift(base_list, new_data):
    x = len(base_list)
    base_list = base_list + new_data
    print(x)
    base_list = base_list[-x:]
    return base_list

list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0]
list_1[0:3] = ['one', 'two', 'three']
tup = ('eleven','twelve','thirteen')
list_2[0:3] = tup
print('Q3:')
print(list_1)
print('Q4:')
print(list_2)
joint_1 = list_1[:]
joint_1.extend(list_2)
joint_2 = list_1 + list_2
print('Q5:')
print(joint_1)
print('Q5:')
print(joint_2)

fixed_length_list = [1,2,3,4]
new_data = [5,6,7]
new_list = list_shift(fixed_length_list, new_data)
print('Q6:')
print(new_list)
print('\n\n\n')
#I think my function is perfect and there are no edge cases :) 

#1.4 Excercise
st = 'STATUS'
ad = 'ADD'
com = 'COMMIT'
pus = 'PUSH'

'''
for x in st:
    print(x)
for x in ad:
    print(x)
for x in com:
    print(x)
for x in pus:
    print(x)
'''
q3 = ["PUSH FAILED", "BANANAS", "PUSH SUCCESS", "APPLES"]
text = "SUCCESS"

if "SUCCESS" in "SUCCESS":
    print('Q5 i success')
if "SUCCESS" in "ijoisafjoijiojSUCCESS":
    print('Q5 ii success')
if "SUCCESS" == "ijoisafjoijiojSUCCESS":
    print('Q5 iii success')
if "SUCCESS" == text:
    print('Q5 iv success')

#The last 2 are comparing the whole string while first 2 are comparing character by character
x = 0
print('Q6:')
while x < len(q3):
    if text in q3[x]:
        print("This worked!")
        break
    print(q3[x])
    x += 1
print('\n\n\n')
#2.2 Excercise
name = "leo"
byte_name = name.encode('utf-8')
byte_name_bad = byte_name + b'\xef'
#I get the error "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xef in position 3: unexpected end of data" T^T
try:
    byte_name = byte_name.decode()
except:
    byte_name = ""
try:
    byte_name_bad = byte_name_bad.decode()
except:
    byte_name_bad = ""
print("Q6 i: " + byte_name)
print('Q6 ii: '+ byte_name_bad)