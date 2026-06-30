import json

database = {

    "Tomato___Late_blight": {

        "plant": "Pomidor",

        "disease": "Kech kuyish",

        "latin_name": "Phytophthora infestans",

        "severity": "Yuqori",

        "description": "Kech kuyish pomidorning barglari, poyalari va mevalariga tez zarar yetkazadigan xavfli zamburug'simon kasallikdir.",

        "symptoms": "Barglarda to'q jigarrang dog'lar paydo bo'ladi, pastki qismida oq mog'or hosil bo'ladi, mevalar chiriydi.",

        "causes": "Kasallik Phytophthora infestans qo'zg'atuvchisi sababli yuzaga keladi. Nam va salqin ob-havo uning rivojlanishini tezlashtiradi.",

        "treatment": "Kasallangan barglarni olib tashlang, tavsiya etilgan fungitsidlarni qo'llang va ekin orasida shamollatishni yaxshilang.",

        "prevention": "Sog'lom ko'chat eking, almashlab ekishni qo'llang va barglarga yuqoridan suv sepishdan saqlaning."
    },

    "Tomato___Early_blight": {

        "plant": "Pomidor",

        "disease": "Erta kuyish",

        "latin_name": "Alternaria solani",

        "severity": "O'rta",

        "description": "Erta kuyish asosan eski barglarda boshlanadigan zamburug' kasalligidir.",

        "symptoms": "Barglarda halqasimon jigarrang dog'lar paydo bo'ladi, barglar sarg'ayadi va quriydi.",

        "causes": "Alternaria solani qo'zg'atuvchisi tuproq va o'simlik qoldiqlarida saqlanib qoladi.",

        "treatment": "Kasallangan barglarni olib tashlang va tavsiya etilgan fungitsidlarni qo'llang.",

        "prevention": "Almashlab ekish, dala tozaligini saqlash va chidamli navlardan foydalanish tavsiya etiladi."
    },

    "Tomato___healthy": {

        "plant": "Pomidor",

        "disease": "Sog'lom",

        "latin_name": "Healthy Plant",

        "severity": "Yo'q",

        "description": "O'simlikda kasallik belgilari aniqlanmadi.",

        "symptoms": "Barglari yashil, poyasi sog'lom va mevalari normal rivojlanmoqda.",

        "causes": "Kasallik aniqlanmadi.",

        "treatment": "Davolash talab etilmaydi.",

        "prevention": "Muntazam kuzatish, to'g'ri sug'orish va o'g'itlashni davom ettiring."
    },
    "Tomato___Leaf_Mold": {

    "plant": "Pomidor",

    "disease": "Barg mog'ori",

    "latin_name": "Passalora fulva",

    "severity": "O'rta",

    "description": "Barg mog'ori issiqxona va nam muhitda tez rivojlanadigan zamburug' kasalligi bo'lib, fotosintez jarayonini pasaytiradi.",

    "symptoms": "Bargning yuqori qismida och yashil yoki sarg'ish dog'lar, pastki qismida esa zaytun rangli mog'or qatlami hosil bo'ladi.",

    "causes": "Kasallik Passalora fulva zamburug'i sababli yuzaga keladi. Yuqori namlik va havo almashinuvining yomonligi rivojlanishni tezlashtiradi.",

    "treatment": "Kasallangan barglarni olib tashlash, issiqxonani shamollatish va tavsiya etilgan fungitsidlardan foydalanish tavsiya etiladi.",

    "prevention": "Namlikni nazorat qilish, o'simliklarni siyrak ekish va kasallikka chidamli navlardan foydalanish tavsiya etiladi."

},

"Tomato___Septoria_leaf_spot": {

    "plant": "Pomidor",

    "disease": "Septorioz barg dog'lanishi",

    "latin_name": "Septoria lycopersici",

    "severity": "O'rta",

    "description": "Septorioz pomidor barglarida ko'plab mayda dog'lar hosil qilib, barglarning erta qurishiga olib keladigan zamburug' kasalligidir.",

    "symptoms": "Barglarda kulrang markazli va to'q jigarrang chegarali mayda dumaloq dog'lar paydo bo'ladi. Zararlangan barglar sarg'ayib to'kiladi.",

    "causes": "Kasallik Septoria lycopersici zamburug'i sababli rivojlanadi. Nam ob-havo va yomg'ir tomchilari orqali tez tarqaladi.",

    "treatment": "Kasallangan barglarni olib tashlash, fungitsid qo'llash va dalada havo aylanishini yaxshilash tavsiya etiladi.",

    "prevention": "Almashlab ekish, dala gigiyenasini saqlash va barglarni ortiqcha namlamaslik tavsiya etiladi."

},

"Tomato___Target_Spot": {

    "plant": "Pomidor",

    "disease": "Nishon dog'lanishi",

    "latin_name": "Corynespora cassiicola",

    "severity": "O'rta",

    "description": "Nishon dog'lanishi barg, poya va mevalarda konsentrik halqali dog'lar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barglarda halqasimon jigarrang dog'lar, poyalarda cho'zinchoq zararlanish va mevalarda qoramtir botiq dog'lar kuzatiladi.",

    "causes": "Kasallik Corynespora cassiicola zamburug'i tomonidan qo'zg'atiladi. Issiq va nam sharoit uning rivojlanishini tezlashtiradi.",

    "treatment": "Kasallangan qismlarni olib tashlash, tavsiya etilgan fungitsidlardan foydalanish va ekinlarni shamollatish tavsiya etiladi.",

    "prevention": "Sog'lom ko'chatlardan foydalanish, almashlab ekish va ortiqcha namlikni kamaytirish tavsiya etiladi."

},
"Tomato___Bacterial_spot": {

    "plant": "Pomidor",

    "disease": "Bakterial dog'lanish",

    "latin_name": "Xanthomonas euvesicatoria",

    "severity": "Yuqori",

    "description": "Pomidorning bakterial dog'lanishi barg, poya va mevalarda mayda suvli dog'lar hosil qiladigan bakterial kasallikdir. Kuchli zararlanish hosildorlik va meva sifatini sezilarli pasaytiradi.",

    "symptoms": "Barglarda mayda qora-jigarrang dog'lar paydo bo'ladi. Mevalarda qobiqsimon, qo'pol va biroz botiq dog'lar kuzatiladi. Barglar sarg'ayib to'kilishi mumkin.",

    "causes": "Kasallik Xanthomonas euvesicatoria bakteriyasi sababli yuzaga keladi. U zararlangan urug', o'simlik qoldiqlari, yomg'ir tomchilari va sug'orish suvi orqali tarqaladi.",

    "treatment": "Kasallangan o'simlik qismlarini olib tashlash, mis tarkibli bakteritsidlar va tavsiya etilgan himoya vositalaridan foydalanish tavsiya etiladi.",

    "prevention": "Sertifikatlangan sog'lom urug'lardan foydalanish, almashlab ekish, ortiqcha namlikni kamaytirish va dala gigiyenasiga rioya qilish tavsiya etiladi."
},
"Apple___Apple_scab": {

    "plant": "Olma",
    "disease": "Qo'tir",
    "latin_name": "Venturia inaequalis",
    "severity": "O'rta",

    "description": "Olma qo'tiri barg, meva va yosh novdalarda qora-yashil dog'lar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barglarda zaytun rangli dog'lar paydo bo'ladi. Mevalarda qora, qo'pol dog'lar hosil bo'ladi va sifati pasayadi.",

    "causes": "Kasallik Venturia inaequalis zamburug'i sababli yuzaga keladi. Nam va salqin ob-havo uning rivojlanishiga qulay sharoit yaratadi.",

    "treatment": "Kasallangan barg va mevalarni yig'ishtirish hamda tavsiya etilgan fungitsidlardan foydalanish tavsiya etiladi.",

    "prevention": "Bog'ni shamollatish, barg qoldiqlarini yo'qotish va chidamli navlarni ekish tavsiya etiladi."
},

"Apple___Black_rot": {

    "plant": "Olma",
    "disease": "Qora chirish",
    "latin_name": "Botryosphaeria obtusa",
    "severity": "Yuqori",

    "description": "Qora chirish olma daraxtining barglari, shoxlari va mevalariga zarar yetkazadigan xavfli zamburug' kasalligidir.",

    "symptoms": "Mevalarda qora chirigan halqalar hosil bo'ladi. Barglarda binafsha-jigarrang dog'lar kuzatiladi.",

    "causes": "Kasallik Botryosphaeria obtusa zamburug'i tufayli yuzaga keladi.",

    "treatment": "Kasallangan meva va shoxlarni kesib tashlash hamda fungitsid qo'llash tavsiya etiladi.",

    "prevention": "Bog'ni toza saqlash va zararlangan qismlarni vaqtida olib tashlash tavsiya etiladi."
},

"Apple___Cedar_apple_rust": {

    "plant": "Olma",
    "disease": "Sidr-olma zangi",
    "latin_name": "Gymnosporangium juniperi-virginianae",
    "severity": "O'rta",

    "description": "Olma barglarida sariq-to'q sariq dog'lar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barglarda yorqin sariq dog'lar va keyinchalik shoxsimon o'simtalar paydo bo'ladi.",

    "causes": "Kasallik archa va olma o'rtasida almashib rivojlanadigan Gymnosporangium zamburug'i sababli yuzaga keladi.",

    "treatment": "Fungitsid qo'llash va zararlangan barglarni olib tashlash tavsiya etiladi.",

    "prevention": "Olma bog'larini archa daraxtlaridan uzoqroq joylashtirish tavsiya etiladi."
},

"Apple___healthy": {

    "plant": "Olma",
    "disease": "Sog'lom",
    "latin_name": "Healthy Plant",
    "severity": "Yo'q",

    "description": "O'simlikda kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil, mevalari sog'lom va normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam parvarish, sug'orish va o'g'itlashni davom ettiring."
},

"Blueberry___healthy": {

    "plant": "Ko'k mersini",
    "disease": "Sog'lom",
    "latin_name": "Healthy Plant",
    "severity": "Yo'q",

    "description": "Ko'k mersini o'simligida kasallik aniqlanmadi.",

    "symptoms": "Barglari yashil va mevalari sog'lom rivojlanmoqda.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "To'g'ri sug'orish va muntazam agrotexnik tadbirlarni davom ettiring."
},

"Cherry_(including_sour)___Powdery_mildew": {

    "plant": "Gilos",
    "disease": "Unshudring",
    "latin_name": "Podosphaera clandestina",
    "severity": "O'rta",

    "description": "Gilos barglari va yosh novdalarida oq kukunsimon qoplama hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barglar oq qoplama bilan qoplanadi, buraladi va o'sishi sustlashadi.",

    "causes": "Kasallik Podosphaera clandestina zamburug'i sababli yuzaga keladi.",

    "treatment": "Fungitsid qo'llash va zararlangan barglarni olib tashlash tavsiya etiladi.",

    "prevention": "Bog'ni shamollatish va ortiqcha namlikni kamaytirish tavsiya etiladi."
},

"Cherry_(including_sour)___healthy": {

    "plant": "Gilos",
    "disease": "Sog'lom",
    "latin_name": "Healthy Plant",
    "severity": "Yo'q",

    "description": "Gilos o'simligida kasallik aniqlanmadi.",

    "symptoms": "Barglari yashil va mevalari normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam parvarish va agrotexnik tadbirlarni davom ettiring."
},

"Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {

    "plant": "Makkajo'xori",

    "disease": "Serkospora barg dog'lanishi (Kulrang barg dog'i)",

    "latin_name": "Cercospora zeae-maydis",

    "severity": "O'rta",

    "description": "Makkajo'xori barglarida uzun kulrang-jigarrang dog'lar hosil qiladigan zamburug' kasalligidir. Kuchli zararlanish fotosintezni kamaytirib, hosildorlikni pasaytiradi.",

    "symptoms": "Barglarda uzunchoq kulrang yoki jigarrang dog'lar paydo bo'ladi. Dog'lar vaqt o'tishi bilan birlashib katta zararlangan maydon hosil qiladi.",

    "causes": "Kasallik Cercospora zeae-maydis zamburug'i sababli yuzaga keladi. Nam va iliq ob-havo uning rivojlanishini tezlashtiradi.",

    "treatment": "Kasallangan maydonlarda tavsiya etilgan fungitsidlardan foydalanish va zararlangan qoldiqlarni yo'qotish tavsiya etiladi.",

    "prevention": "Almashlab ekish, chidamli navlardan foydalanish va dala qoldiqlarini tozalash tavsiya etiladi."
},

"Corn_(maize)___Common_rust_": {

    "plant": "Makkajo'xori",

    "disease": "Oddiy zang",

    "latin_name": "Puccinia sorghi",

    "severity": "O'rta",

    "description": "Makkajo'xori barglarida zang rangli pustulalar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barglarning ikkala tomonida mayda jigarrang-to'q sariq pustulalar paydo bo'ladi.",

    "causes": "Kasallik Puccinia sorghi zamburug'i sababli rivojlanadi.",

    "treatment": "Kuchli zararlanishda fungitsid qo'llash tavsiya etiladi.",

    "prevention": "Chidamli navlardan foydalanish va dalani muntazam kuzatish tavsiya etiladi."
},

"Corn_(maize)___Northern_Leaf_Blight": {

    "plant": "Makkajo'xori",

    "disease": "Shimoliy barg kuyishi",

    "latin_name": "Exserohilum turcicum",

    "severity": "Yuqori",

    "description": "Barglarda uzun ellips shaklidagi kulrang dog'lar hosil qiladigan xavfli zamburug' kasalligidir.",

    "symptoms": "Uzun kulrang-jigarrang dog'lar barg bo'ylab kengayadi va barglarning qurishiga olib keladi.",

    "causes": "Kasallik Exserohilum turcicum zamburug'i sababli yuzaga keladi.",

    "treatment": "Fungitsid qo'llash va kasallangan o'simlik qoldiqlarini yo'qotish tavsiya etiladi.",

    "prevention": "Almashlab ekish va chidamli navlardan foydalanish tavsiya etiladi."
},

"Corn_(maize)___healthy": {

    "plant": "Makkajo'xori",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "O'simlikda kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil, poyasi mustahkam va normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam parvarish, sug'orish va o'g'itlashni davom ettiring."
},

"Grape___Black_rot": {

    "plant": "Uzum",

    "disease": "Qora chirish",

    "latin_name": "Guignardia bidwellii",

    "severity": "Yuqori",

    "description": "Uzum barglari va mevalariga kuchli zarar yetkazadigan zamburug' kasalligidir.",

    "symptoms": "Barglarda jigarrang dog'lar, mevalarda esa qora burishgan chirish kuzatiladi.",

    "causes": "Kasallik Guignardia bidwellii zamburug'i sababli rivojlanadi.",

    "treatment": "Kasallangan qismlarni olib tashlash va fungitsid qo'llash tavsiya etiladi.",

    "prevention": "Bog'ni toza saqlash va muntazam profilaktik ishlov berish tavsiya etiladi."
},

"Grape___Esca_(Black_Measles)": {

    "plant": "Uzum",

    "disease": "Eska (Qora qizamiq)",

    "latin_name": "Phaeomoniella chlamydospora",

    "severity": "Yuqori",

    "description": "Uzum tanasi va barglariga zarar yetkazadigan surunkali zamburug' kasalligidir.",

    "symptoms": "Barglarda yo'lbars terisiga o'xshash sarg'ish-jigarrang naqshlar hosil bo'ladi.",

    "causes": "Kasallik bir nechta zamburug'lar majmuasi sababli yuzaga keladi.",

    "treatment": "Kasallangan novdalarni kesib tashlash va bog' gigiyenasiga rioya qilish tavsiya etiladi.",

    "prevention": "Kesish asboblarini dezinfeksiya qilish va sog'lom ko'chatlardan foydalanish tavsiya etiladi."
},

"Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {

    "plant": "Uzum",

    "disease": "Barg kuyishi",

    "latin_name": "Pseudocercospora vitis",

    "severity": "O'rta",

    "description": "Uzum barglarida qo'ng'ir dog'lar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barglarda notekis jigarrang dog'lar paydo bo'ladi va barglar quriydi.",

    "causes": "Kasallik Pseudocercospora vitis zamburug'i sababli yuzaga keladi.",

    "treatment": "Fungitsid qo'llash va zararlangan barglarni olib tashlash tavsiya etiladi.",

    "prevention": "Bog'ni shamollatish va ortiqcha namlikni kamaytirish tavsiya etiladi."
},

"Grape___healthy": {

    "plant": "Uzum",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "O'simlikda kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil, novdalari sog'lom va mevalari normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam parvarish va profilaktik kuzatuvni davom ettiring."
},

"Orange___Haunglongbing_(Citrus_greening)": {

    "plant": "Apelsin",

    "disease": "Sitrus ko'karish kasalligi (Huanglongbing)",

    "latin_name": "Candidatus Liberibacter asiaticus",

    "severity": "Juda yuqori",

    "description": "Sitrus o'simliklari uchun eng xavfli bakterial kasalliklardan biri bo'lib, daraxtning sekin qurishiga va hosildorlikning keskin kamayishiga olib keladi.",

    "symptoms": "Barglarda notekis sarg'ayish, mayda va deformatsiyalangan mevalar, mevalarning achchiqlashishi va daraxtning umumiy zaiflashuvi kuzatiladi.",

    "causes": "Kasallik Candidatus Liberibacter asiaticus bakteriyasi sababli yuzaga keladi va asosan sitrus psillidi hasharoti orqali tarqaladi.",

    "treatment": "Kasallikni to'liq davolash usuli mavjud emas. Zararlangan daraxtlarni yo'q qilish va tashuvchi hasharotlarga qarshi kurashish tavsiya etiladi.",

    "prevention": "Sertifikatlangan sog'lom ko'chatlardan foydalanish, psillid hasharotlarini nazorat qilish va muntazam monitoring o'tkazish tavsiya etiladi."
},

"Peach___Bacterial_spot": {

    "plant": "Shaftoli",

    "disease": "Bakterial dog'lanish",

    "latin_name": "Xanthomonas arboricola pv. pruni",

    "severity": "Yuqori",

    "description": "Shaftoli barglari va mevalarida qora dog'lar hosil qiladigan bakterial kasallikdir.",

    "symptoms": "Barglarda mayda qora dog'lar, mevalarda esa cho'kkan qo'pol dog'lar paydo bo'ladi.",

    "causes": "Kasallik Xanthomonas arboricola pv. pruni bakteriyasi sababli yuzaga keladi.",

    "treatment": "Mis tarkibli preparatlar va tavsiya etilgan bakteritsidlarni qo'llash tavsiya etiladi.",

    "prevention": "Sog'lom ko'chatlardan foydalanish, bog' gigiyenasiga rioya qilish va zararlangan shoxlarni olib tashlash tavsiya etiladi."
},

"Peach___healthy": {

    "plant": "Shaftoli",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "O'simlikda kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil, mevalari normal rivojlangan va daraxt sog'lom.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam sug'orish, o'g'itlash va profilaktik kuzatuvni davom ettiring."
},

"Pepper,_bell___Bacterial_spot": {

    "plant": "Bulg'or qalampiri",

    "disease": "Bakterial dog'lanish",

    "latin_name": "Xanthomonas euvesicatoria",

    "severity": "Yuqori",

    "description": "Barglar, poya va mevalarda qora dog'lar hosil qiladigan bakterial kasallikdir.",

    "symptoms": "Barglarda suvli mayda dog'lar paydo bo'lib, keyinchalik jigarrang tusga kiradi. Mevalarda qo'pol qora dog'lar hosil bo'ladi.",

    "causes": "Kasallik Xanthomonas euvesicatoria bakteriyasi sababli yuzaga keladi.",

    "treatment": "Kasallangan barglarni olib tashlash va tavsiya etilgan bakteritsidlarni qo'llash tavsiya etiladi.",

    "prevention": "Sertifikatlangan urug'lardan foydalanish, almashlab ekish va dala gigiyenasiga rioya qilish tavsiya etiladi."
},

"Pepper,_bell___healthy": {

    "plant": "Bulg'or qalampiri",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "O'simlikda kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil, poyasi sog'lom va mevalari normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam parvarish va agrotexnik tadbirlarni davom ettiring."
},

"Potato___Early_blight": {

    "plant": "Kartoshka",

    "disease": "Erta kuyish",

    "latin_name": "Alternaria solani",

    "severity": "O'rta",

    "description": "Kartoshkaning barglarida halqasimon jigarrang dog'lar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Eski barglarda konsentrik halqali jigarrang dog'lar paydo bo'ladi. Barglar sarg'ayib quriydi.",

    "causes": "Kasallik Alternaria solani zamburug'i sababli rivojlanadi.",

    "treatment": "Kasallangan barglarni olib tashlash va tavsiya etilgan fungitsidlarni qo'llash tavsiya etiladi.",

    "prevention": "Almashlab ekish, sog'lom urug'lik tuganaklardan foydalanish va dala gigiyenasiga rioya qilish tavsiya etiladi."
},

"Potato___Late_blight": {

    "plant": "Kartoshka",

    "disease": "Kech kuyish",

    "latin_name": "Phytophthora infestans",

    "severity": "Juda yuqori",

    "description": "Kartoshkaning eng xavfli kasalliklaridan biri bo'lib, qisqa vaqt ichida barg va tuganaklarga kuchli zarar yetkazadi.",

    "symptoms": "Barglarda nam jigarrang dog'lar, pastki qismida oq mog'or va tuganaklarda chirish kuzatiladi.",

    "causes": "Kasallik Phytophthora infestans qo'zg'atuvchisi sababli yuzaga keladi.",

    "treatment": "Kasallangan o'simliklarni yo'qotish va tavsiya etilgan fungitsidlarni qo'llash tavsiya etiladi.",

    "prevention": "Sog'lom urug'lik tuganaklardan foydalanish, almashlab ekish va namlikni nazorat qilish tavsiya etiladi."
},

"Potato___healthy": {

    "plant": "Kartoshka",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "O'simlikda kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil, poyasi sog'lom va normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam sug'orish, o'g'itlash va profilaktik kuzatuvni davom ettiring."
},

"Raspberry___healthy": {

    "plant": "Malina",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "Malina o'simligida kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil va sog'lom, mevalari normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam parvarish va kuzatuvni davom ettiring."
},

"Soybean___healthy": {

    "plant": "Soya",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "Soya o'simligida kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil va sog'lom, o'sishi normal.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "To'g'ri agrotexnik tadbirlarni davom ettirish tavsiya etiladi."
},

"Squash___Powdery_mildew": {

    "plant": "Qovoq",

    "disease": "Un shudring",

    "latin_name": "Podosphaera xanthii",

    "severity": "O'rta",

    "description": "Qovoq barglari yuzasida oq un ko'rinishidagi qoplama hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barglarda oq kukunsimon qoplama paydo bo'ladi, keyinchalik barglar sarg'ayadi va quriydi.",

    "causes": "Kasallik Podosphaera xanthii zamburug'i sababli rivojlanadi.",

    "treatment": "Fungitsidlar qo'llash va zararlangan barglarni olib tashlash tavsiya etiladi.",

    "prevention": "Ekish zichligini kamaytirish va shamollatishni yaxshilash tavsiya etiladi."
},

"Strawberry___Leaf_scorch": {

    "plant": "Qulupnay",

    "disease": "Barg kuyishi",

    "latin_name": "Diplocarpon earlianum",

    "severity": "O'rta",

    "description": "Qulupnay barglarida to'q qizg'ish-jigarrang dog'lar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barg chetlari quriydi, mayda binafsha-jigarrang dog'lar paydo bo'ladi.",

    "causes": "Kasallik Diplocarpon earlianum zamburug'i sababli yuzaga keladi.",

    "treatment": "Kasallangan barglarni olib tashlash va fungitsid qo'llash tavsiya etiladi.",

    "prevention": "Ekish maydonini toza saqlash va ortiqcha namlikni kamaytirish tavsiya etiladi."
},

"Strawberry___healthy": {

    "plant": "Qulupnay",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "Qulupnay o'simligida kasallik belgilari aniqlanmadi.",

    "symptoms": "Barglari yashil, mevalari normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam parvarish va agrotexnik tadbirlarni davom ettiring."
},

"Tomato___Bacterial_spot": {

    "plant": "Pomidor",

    "disease": "Bakterial dog'lanish",

    "latin_name": "Xanthomonas euvesicatoria",

    "severity": "Yuqori",

    "description": "Pomidor barglari, poyalari va mevalarida mayda qora-jigarrang dog'lar hosil qiladigan bakterial kasallikdir. Kuchli zararlanish hosildorlikni sezilarli kamaytiradi.",

    "symptoms": "Barglarda mayda suvli dog'lar paydo bo'ladi, keyinchalik ular qora-jigarrang tusga kiradi. Mevalarda qo'pol va biroz botiq dog'lar hosil bo'ladi.",

    "causes": "Kasallik Xanthomonas euvesicatoria bakteriyasi sababli yuzaga keladi. Zararlangan urug', yomg'ir tomchilari va sug'orish suvi orqali tarqaladi.",

    "treatment": "Kasallangan barglarni olib tashlash, mis tarkibli preparatlar va tavsiya etilgan bakteritsidlardan foydalanish tavsiya etiladi.",

    "prevention": "Sog'lom urug'lardan foydalanish, almashlab ekish va dala gigiyenasiga rioya qilish tavsiya etiladi."
},

"Tomato___Early_blight": {

    "plant": "Pomidor",

    "disease": "Erta kuyish",

    "latin_name": "Alternaria solani",

    "severity": "O'rta",

    "description": "Pomidorning asosan eski barglarida boshlanadigan keng tarqalgan zamburug' kasalligidir.",

    "symptoms": "Barglarda halqasimon jigarrang dog'lar hosil bo'ladi. Barglar sarg'ayadi va asta-sekin quriydi.",

    "causes": "Kasallik Alternaria solani zamburug'i sababli yuzaga keladi.",

    "treatment": "Kasallangan barglarni olib tashlash va tavsiya etilgan fungitsidlarni qo'llash tavsiya etiladi.",

    "prevention": "Almashlab ekish, dala tozaligini saqlash va chidamli navlardan foydalanish tavsiya etiladi."
},

"Tomato___Late_blight": {

    "plant": "Pomidor",

    "disease": "Kech kuyish",

    "latin_name": "Phytophthora infestans",

    "severity": "Juda yuqori",

    "description": "Pomidorning eng xavfli kasalliklaridan biri bo'lib, qisqa vaqt ichida barg, poya va mevalarni zararlaydi.",

    "symptoms": "Barglarda yirik jigarrang dog'lar hosil bo'ladi, pastki qismida oq mog'or paydo bo'ladi, mevalar chiriydi.",

    "causes": "Kasallik Phytophthora infestans qo'zg'atuvchisi sababli yuzaga keladi. Nam va salqin ob-havo uning rivojlanishini tezlashtiradi.",

    "treatment": "Kasallangan qismlarni olib tashlash va tavsiya etilgan fungitsidlarni qo'llash tavsiya etiladi.",

    "prevention": "Sog'lom ko'chatlardan foydalanish, almashlab ekish va barglarni ortiqcha namlamaslik tavsiya etiladi."
},

"Tomato___Leaf_Mold": {

    "plant": "Pomidor",

    "disease": "Barg mog'ori",

    "latin_name": "Passalora fulva",

    "severity": "O'rta",

    "description": "Issiqxonalarda ko'p uchraydigan zamburug' kasalligi bo'lib, barglarning fotosintez qobiliyatini kamaytiradi.",

    "symptoms": "Barglarning yuqori qismida sarg'ish dog'lar, pastki tomonida esa zaytun-yashil mog'or qatlami hosil bo'ladi.",

    "causes": "Kasallik Passalora fulva zamburug'i sababli rivojlanadi. Yuqori namlik kasallikning tarqalishini kuchaytiradi.",

    "treatment": "Issiqxonani shamollatish, zararlangan barglarni olib tashlash va fungitsid qo'llash tavsiya etiladi.",

    "prevention": "Namlikni nazorat qilish va o'simliklar orasida havo almashinuvini yaxshilash tavsiya etiladi."
},

"Tomato___Septoria_leaf_spot": {

    "plant": "Pomidor",

    "disease": "Septorioz barg dog'lanishi",

    "latin_name": "Septoria lycopersici",

    "severity": "O'rta",

    "description": "Pomidor barglarida ko'plab mayda kulrang-jigarrang dog'lar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Pastki barglarda ko'plab mayda yumaloq dog'lar paydo bo'ladi. Dog'larning markazi kulrang, chetlari to'q jigarrang bo'ladi.",

    "causes": "Kasallik Septoria lycopersici zamburug'i sababli yuzaga keladi. Nam va iliq ob-havo uning rivojlanishiga qulay sharoit yaratadi.",

    "treatment": "Kasallangan barglarni olib tashlash va tavsiya etilgan fungitsidlarni qo'llash tavsiya etiladi.",

    "prevention": "Almashlab ekish, barglarni yuqoridan sug'ormaslik va dala gigiyenasiga rioya qilish tavsiya etiladi."
},

"Tomato___Spider_mites Two-spotted_spider_mite": {

    "plant": "Pomidor",

    "disease": "Ikki nuqtali o'rgimchakkana",

    "latin_name": "Tetranychus urticae",

    "severity": "O'rta",

    "description": "Pomidor barglarining shirasini so'rib oziqlanadigan zararkunanda bo'lib, barglarning sarg'ayishi va qurishiga olib keladi.",

    "symptoms": "Barglarda mayda sariq nuqtalar paydo bo'ladi, keyinchalik barglar bronza tusga kiradi. Barg ostida ingichka o'rgimchak to'ri hosil bo'ladi.",

    "causes": "Issiq va quruq ob-havo o'rgimchakkananing tez ko'payishiga yordam beradi.",

    "treatment": "Akaritsid preparatlarini qo'llash va zararlangan barglarni olib tashlash tavsiya etiladi.",

    "prevention": "Namlikni me'yorida saqlash, o'simliklarni muntazam kuzatish va zararkunandalar ko'payishining oldini olish tavsiya etiladi."
},

"Tomato___Target_Spot": {

    "plant": "Pomidor",

    "disease": "Nishon dog' kasalligi",

    "latin_name": "Corynespora cassiicola",

    "severity": "O'rta",

    "description": "Pomidor barglari va mevalarida konsentrik halqali dog'lar hosil qiladigan zamburug' kasalligidir.",

    "symptoms": "Barglarda dumaloq jigarrang dog'lar va ularning ichida halqasimon naqshlar paydo bo'ladi.",

    "causes": "Kasallik Corynespora cassiicola zamburug'i sababli yuzaga keladi.",

    "treatment": "Kasallangan barglarni olib tashlash va fungitsid qo'llash tavsiya etiladi.",

    "prevention": "Almashlab ekish, dala gigiyenasi va ortiqcha namlikni kamaytirish tavsiya etiladi."
},

"Tomato___Tomato_Yellow_Leaf_Curl_Virus": {

    "plant": "Pomidor",

    "disease": "Pomidor sariq barg buralish virusi",

    "latin_name": "Tomato Yellow Leaf Curl Virus (TYLCV)",

    "severity": "Juda yuqori",

    "description": "Pomidorning eng xavfli virusli kasalliklaridan biri bo'lib, hosildorlikni keskin kamaytiradi.",

    "symptoms": "Yosh barglar sarg'ayadi, yuqoriga buraladi, o'simlikning o'sishi sustlashadi va mevalanish kamayadi.",

    "causes": "Kasallik oqkanot (Bemisia tabaci) orqali tarqaladigan virus sababli yuzaga keladi.",

    "treatment": "Virusni davolash usuli mavjud emas. Zararlangan o'simliklarni yo'q qilish tavsiya etiladi.",

    "prevention": "Oqkanotlarga qarshi kurashish, sog'lom ko'chatlardan foydalanish va dala monitoringini olib borish tavsiya etiladi."
},

"Tomato___Tomato_mosaic_virus": {

    "plant": "Pomidor",

    "disease": "Pomidor mozaika virusi",

    "latin_name": "Tomato Mosaic Virus (ToMV)",

    "severity": "Yuqori",

    "description": "Pomidor barglarida mozaikasimon rang o'zgarishlarini hosil qiladigan virusli kasallikdir.",

    "symptoms": "Barglarda och va to'q yashil mozaikasimon naqshlar, deformatsiya va o'sishning sustlashuvi kuzatiladi.",

    "causes": "Kasallik zararlangan urug', o'simlik qoldiqlari va bog'dorchilik asboblari orqali tarqaladi.",

    "treatment": "Virusli kasallikni davolashning samarali usuli yo'q. Zararlangan o'simliklarni olib tashlash tavsiya etiladi.",

    "prevention": "Sog'lom urug'lardan foydalanish, asboblarni dezinfeksiya qilish va dala gigiyenasiga rioya qilish tavsiya etiladi."
},

"Tomato___healthy": {

    "plant": "Pomidor",

    "disease": "Sog'lom",

    "latin_name": "Healthy Plant",

    "severity": "Yo'q",

    "description": "Pomidor o'simligida kasallik yoki zararkunanda belgilari aniqlanmadi.",

    "symptoms": "Barglari to'liq yashil, poyasi mustahkam va mevalari normal rivojlangan.",

    "causes": "Kasallik aniqlanmadi.",

    "treatment": "Davolash talab qilinmaydi.",

    "prevention": "Muntazam sug'orish, muvozanatli o'g'itlash va o'simlikni kuzatib borish tavsiya etiladi."
}

}

with open("disease_info.json", "w", encoding="utf-8") as file:

    json.dump(database, file, ensure_ascii=False, indent=4)

print("✅ disease_info.json muvaffaqiyatli yaratildi.")