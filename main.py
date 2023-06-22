# ism = input('ism kiriting')

# ismlar = {
#     'ism1': ism
# }

# print(ism)
# Mashina ={
#     'lamborgini':{

#         'narxi':1800 ,
#         'yili':2023,
#         'comfort':'free'
#         },

#     'Mersamg':{
#     'narxi':2000 ,
#     'yili':2022,
#     'comfort':""
#     }
# }
# f_Mashina =input("nomini kiriting")
# if f_Mashina in Mashina:
#      print(Mashina[f_Mashina]['narxi'],Mashina[f_Mashina]['yili'])


# kitob = {
#     'karl dernegi': {
#         'narxi': 1800000,
#         'yili': 2020,
#         'mualifi': 'karl dernegi'
#     },
#     'biznes kitob': {
#         'narxi': 2500000,
#         'yili': 2005,
#         'mualifi': 'muhamadaliy'
#     }
# }
# f_kitob = input("nomini kiriting")
# if f_kitob in kitob:
#     print(kitob[f_kitob]['narxi'], kitob[f_kitob]
#           ['yili'], kitob[f_kitob]['mualifi'])

# else:
#     tasdiq = input('yangi kiriting ha/yoq'),
# if tasdiq == 'ha':
#     mualifi = input('muallif kiriting')
#     narxi = input('narxini kiriting')
#     yili = input('yilini kiriting')

# print(kitob(f_kitob))
# print('rahmat')

davlatlar = {
    'uzbekiston': {
        'aholisi':1000,
        'pul birligi':'sum',
        'yer maydoni':'ming km',
        'poytaxti':'toshkent',
        'avtomobili':'gm avto'
        
    },
     'uzbekiston2':{
        'aholisi':2000,
        'pul birligi':'euro',
        'yer maydoni':'ming km',
        'poytaxti':'toshkent',
        'avtomobili':'gm2 avto'
        
    },
    'uzbekiston3':{
        'aholisi':2000,
        'pul birligi':'dollars',
        'yer maydoni':'ming km',
        'poytaxti':'quqon',
        'avtomobili':'mers avto'
        
},
'uzbekiston4':{
        'aholisi':2000,
        'pul birligi':'dollars',
        'yer maydoni':'ming km',
        'poytaxti':'andijon',
        'avtomobili':'mustang avto'
},
'uzbekiston5':{
        'aholisi':2000,
        'pul birligi':'dollars',
        'yer maydoni':'ming km',
        'poytaxti':'samarqand',
        'avtomobili':'lambo avto'
},
}
f_davlatni =input('davlat nomini kiriting')
if f_davlatni in davlatlar:
    print(davlatlar['f_davlatni']['aholisi'],davlatlar['f_davlatni']['pul birligi'],davlatlar['f_davlatni']['yer maydonni'],davlatlar['f_davlatni']['poytaxti'],davlatlar['f_davlatlar']['avtomobili'])
else:
    tasdiq = input('yangi kiriting ha/yoq')
if tasdiq == 'ha':
    aholisi= input('yangisini kiriting')
    pulbirligi = input('yangi pul birligi')
    yermaydoni = input('yangi yer maydoni')
    
    print(davlatlar(f_davlatni))
    print('rahmat')