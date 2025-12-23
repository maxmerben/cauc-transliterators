from pyscript import document
from pyscript.web import page
def transliterator_avar(word):
  consonant_letters={'цӀцӀ':"cːʼ","чӀчӀ":"čːʼ","лълъ":"ɬː","лъ":"ɬ","лI":"ƛ","м":"m","н":"n","п":"pʰ","пӀ":"p’","р":"r","с":"s","т":"tʰ","тӀ":"t’","ф":"f","х":"χ","хх":"χː","хӀ":"ħ","хъ":"q","хь":"x","ц":"cʰ",
           "цц":"cʰː","цӀ":"cʼ","ч":"čʰ","чч":"čʰː","чӀ":"čʼ","ш":"š","щ":"šː","ъ":"ʔ","б":"b","г":"g","гъ":"ʁ","гь":"h","гӀ":"ʕ","д":"d","ж":"ž","з":"z","й":"j","к":"kʰ","кк":"kː",
                     "къ":"q’","кь":"ƛ’","кӀ":"k’","кӀкӀ":"k’ː","л":"l"}
  vowels={"а":"a","и":"i","о":"o","у":"u","э":"e","е":"je","ю":"ju","я":"ja"}
  i=0
  answ=[]
  word=word.replace("І", "Ӏ")
  word=word.replace("I", "Ӏ")
  word=word.replace("1", "Ӏ")
  while i<len(word):
    if i<=len(word)-4:
      if word[i:i+4] in consonant_letters:
        answ.append(consonant_letters[word[i:i+4]])
        i=i+4
      else:
        answ.append(word[i])
        i=i+1
    else:
      answ.append(word[i])
      i=i+1
  answ2=[]
  i=0
  while i<len(answ):
    if i<len(answ)-1:
      if answ[i]+answ[i+1] in consonant_letters:
        answ2.append(consonant_letters[answ[i]+answ[i+1]])
        i=i+2
      elif answ[i]+answ[i+1] in vowels:
        answ2.append(vowels[answ[i]+answ[i+1]])
        i=i+2
      else:
        answ2.append(answ[i])
        i=i+1
    else:
      answ2.append(answ[i])
      i=i+1
  answ_fin=[]
  i=0
  while i<len(answ2):
    if answ2[i]=='в' and i>0:
      if answ2[i-1] in consonant_letters.values():
        answ_fin.append("ʷ")
      else:
        answ_fin.append("w")
    elif answ2[i]=='в' and i==0:
      answ_fin.append("w")
    else:
      if answ2[i] in consonant_letters.keys():
        answ_fin.append(consonant_letters[answ2[i]])
      elif answ2[i] in vowels.keys():
        answ_fin.append(vowels[answ2[i]])
      else:
        answ_fin.append(answ2[i])
    i=i+1
  return ('').join(answ_fin)
def transliterator_dargwa(word):
  consonant_letters={"м":"m","н":"n","п":"p","пӀ":"p’","р":"r","с":"s","т":"t","тӀ":"t’","ф":"f","х":"χ","хӀ":"ħ","хъ":"q","хь":"x","ц":"c",
           "цӀ":"cʼ","ч":"č","чӀ":"čʼ","ш":"š","щ":"š","ъ":"ʔ","б":"b","в":"w","г":"g","гъ":"ʁ","гь":"h","гӀ":"ʡ","д":"d","ж":"ž","з":"z","й":"j","к":"k",
                     "къ":"ɢ","кь":"q’","кӀ":"k’","л":"l","ь":""}
  vowels={"а":"a","и":"i","о":"o","у":"u","э":"ʔe","е":"je","ю":"ju","я":"ja","ё":'jo'}
  i=0
  answ=[]
  word=word.replace("І", "Ӏ")
  word=word.replace("I", "Ӏ")
  word=word.replace("1", "Ӏ")
  while i<len(word):
    if i<=len(word)-2:
      if word[i:i+2] in consonant_letters.keys():
        answ.append(consonant_letters[word[i:i+2]])
        i=i+2
      else:
        answ.append(word[i])
        i=i+1
    else:
      answ.append(word[i])
      i=i+1
  answ_fin=[]
  i=0
  while i<len(answ):
    if answ[i]=='е' and i>0:
      if answ[i-1] in consonant_letters.values():
        answ_fin.append("e")
      else:
        answ_fin.append("je")
    elif answ[i]=='е' and i==0:
      answ_fin.append("je")
    elif answ[i]=='ё' and i>0:
      if answ[i-1] in consonant_letters.values():
        answ_fin.append("o")
      else:
        answ_fin.append("jo")
    elif answ[i]=='ё' and i==0:
      answ_fin.append("jo")
    elif answ[i]=='я' and i>0:
      if answ[i-1] in consonant_letters.values() and answ[i-1]!='ʔ'and answ[i-1]!='':
        answ_fin.append("æˁ")
      else:
        answ_fin.append("ja")
    elif answ[i]=='я' and i==0:
      answ_fin.append("ja")
    else:
      if answ[i] in consonant_letters:
        answ_fin.append(consonant_letters[answ[i]])
      elif answ[i] in vowels:
        answ_fin.append(vowels[answ[i]])
      else:
        answ_fin.append(answ[i])
    i=i+1
  return ('').join(answ_fin)
def transliterator_lezgian(word):
  consonant_letters={"б":"b","в":"w","г":"g","гъ":"ʁ","гь":"h","д":"d","ж":"ž","з":"z","й":"j","к":"k",
                     "къ":"q","кь":"q’","кӀ":"k’","л":"l","м":"m","н":"n","п":"p","пӀ":"p’","р":"r","с":"s","т":"t","тӀ":"t’","ф":"f","х":"χ","хӀ":"ħ","хъ":"qʰ","хь":"x","ц":"cʰ",
                     "цӀ":"cʼ","ч":"čʰ","чӀ":"čʼ","ш":"š","ъ":"ʡ'"}
  vowels={"а":"a","и":"i","о":"o","у":"u","э":"ʔe","е":"je","ю":"ju","я":"ja","ё":'jo', 'уь':'y'}
  i=0
  answ=[]
  word=word.replace("І", "Ӏ")
  word=word.replace("I", "Ӏ")
  word=word.replace("1", "Ӏ")
  while i<len(word):
    if i<=len(word)-2:
      if word[i:i+2] in consonant_letters:
        answ.append(consonant_letters[word[i:i+2]])
        i=i+2
      elif word[i:i+2] in vowels:
        answ.append(vowels[word[i:i+2]])
        i=i+2
      else:
        answ.append(word[i])
        i=i+1
    else:
      answ.append(word[i])
      i=i+1
  answ_fin=[]
  i=0
  while i<len(answ):
    if answ[i]=='е' and i>0:
      if answ[i-1] in consonant_letters.values() or answ[i-1]=='ʷ':
        answ_fin.append("e")
      else:
        answ_fin.append("je")
    elif answ[i]=='е' and i==0:
      answ_fin.append("je")
    elif answ[i]=='э' and i>0:
      if answ[i-1] in consonant_letters.values() or answ[i-1]=='ʷ':
        answ_fin.append("e")
      else:
        answ_fin.append("ʔe")
    elif answ[i]=='э' and i==0:
      answ_fin.append("ʔe")
    elif answ[i]=='я' and i>0:
      if answ[i-1] in consonant_letters.values() or answ[i-1]=='ʷ':
        answ_fin.append("æ")
      else:
        answ_fin.append("ja")
    elif answ[i]=='я' and i==0:
      answ_fin.append("ja")
    elif answ[i]=='в' and i>0:
      if answ[i-1] in consonant_letters.values() or answ[i-1]=='ʷ':
        answ_fin.append("ʷ")
      else:
        answ_fin.append("w")
    elif answ[i]=='в' and i==0:
      answ_fin.append("w")
    else:
      if answ[i] in consonant_letters:
        answ_fin.append(consonant_letters[answ[i]])
      elif answ[i] in vowels:
        answ_fin.append(vowels[answ[i]])
      else:
        answ_fin.append(answ[i])
    i=i+1
  return ('').join(answ_fin)
def transliterator_lak(word):
  consonant_letters={"б":"b","в":"w","г":"g","гъ":"ʁ","гь":"h","гI":"ʕ","д":"d","ж":"ž","з":"z","й":"j","к":"kʰ", "кк":"k:",
                     "къ":"q","кь":"q’","кӀ":"k’","л":"l","м":"m","н":"n","п":"pʰ", "пп":"p:", "пӀ":"p’","р":"r","с":"s", "сс":"s:", "т":"tʰ","тт":"t:","тӀ":"t’","ф":"f","х":"χ","хх":"χ:","хӀ":"ħ","хъ":"qʰ","хь":"x",
                     "хьхь":"x:","ц":"cʰ", "цц":"cʰ:",
           "цӀ":"cʼ","ч":"čʰ","чч":"čʰ:","чӀ":"čʼ","ш":"š","щ":"š:","ъ":"ʡ'"}
  vowels={"а":"a","аь":"æˁ","е":"jeˤ","ё":'jo',"и":"i","о":"o","оь":"øˤ","у":"u","э":"eˤ","ю":"ju","я":"ja"}
  i=0
  answ=[]
  word=word.replace("І", "Ӏ")
  word=word.replace("I", "Ӏ")
  word=word.replace("1", "Ӏ")
  while i<len(word):
    if i<=len(word)-4:
      if word[i:i+4] in consonant_letters.keys():
        answ.append(consonant_letters[word[i:i+4]])
        i=i+4
      else:
        answ.append(word[i])
        i=i+1
    else:
      answ.append(word[i])
      i=i+1
  answ2=[]
  i=0
  while i<len(answ):
    if i<=len(answ)-2:
      if answ[i]+answ[i+1] in consonant_letters.keys():
        answ2.append(consonant_letters[answ[i]+answ[i+1]])
        i=i+2
      elif answ[i]+answ[i+1] in vowels.keys():
        answ2.append(vowels[answ[i]+answ[i+1]])
        i=i+2
      else:
        answ2.append(answ[i])
        i=i+1
    else:
      answ2.append(answ[i])
      i=i+1
  answ_fin=[] #остановился тут
  i=0
  while i<len(answ2):
    if answ2[i]=='е' and i>0:
      if answ2[i-1] in consonant_letters.values():
        answ_fin.append("eˤ")
      else:
        answ_fin.append("jeˤ")
    elif answ2[i]=='е' and i==0:
      answ_fin.append("jeˤ")
    elif answ2[i]=='ю' and i>0:
      if answ2[i-1] in consonant_letters.values() or answ2[i-1]=='ʷ':
        answ_fin.append("øˤ")
      else:
        answ_fin.append("ju")
    elif answ2[i]=='э' and i==0:
      answ_fin.append("ju")
    elif answ2[i]=='я' and i>0:
      if answ2[i-1] in consonant_letters.values() or answ2[i-1]=='ʷ':
        answ_fin.append("æˁ")
      else:
        answ_fin.append("ja")
    elif answ2[i]=='я' and i==0:
      answ_fin.append("ja")
    elif answ2[i]=='в' and i>0:
      if answ2[i-1] in consonant_letters.values() or answ2[i-1]=='ʷ':
        answ_fin.append("ʷ")
      else:
        answ_fin.append("w")
    elif answ2[i]=='в' and i==0:
      answ_fin.append("w")
    else:
      if answ2[i] in consonant_letters.keys():
        answ_fin.append(consonant_letters[answ2[i]])
      elif answ2[i] in vowels.keys():
        answ_fin.append(vowels[answ2[i]])
      else:
        answ_fin.append(answ2[i])
    i=i+1
  return ('').join(answ_fin)
def transliterator_khwarshi(word):
  consonant_letters={"б":"b","в":"w","г":"g","гъ":"ʁ","гь":"h","гӀ":"ʕ","д":"d","ж":"ʒ","з":"z","й":"j","к":"kʰ",
                     "къ":"qχ’","кь":"tɬ’","кӀ":"k’","л":"l","л'":"lʲ","лъ":"ɬ","лӀ":"tɬ","м":"m","н":"n","п":"pʰ","пӀ":"p’","р":"r","с":"s","т":"tʰ",
                     "тӀ":"t’","х":"χ","хъ":"qχ","хь":"x","хӀ":"ħ","ц":"tsʰ",
           "цӀ":"tsʼ","ч":"tʃʰ","чӀ":"c","ш":"ʃ","ъ":"ʔ","Ӏ":""}
  vowels={"а":"a","аᵸ":"ã","ā":"aː","āᵸ":"ãː","е":"e","еᵸ":"ẽ","ē":"eː","ēᵸ":"ẽː","и":"i","иᵸ":"ĩ","ӣ":"iː","о":"o","оᵸ":"õ","ō":"oː","ōᵸ":"õː","у":"u","уᵸ":"ũ","ӯ":"uː","ӯᵸ":"ũː",
          "ы":"ɨ","ыᵸ":"ɨ̃","ы̄":"ɨː","э":"ʔe","эᵸ":"ʔẽ","э̄":"ʔeː","э̄н":"ʔẽː","ё":'jo'}
  i=0
  answ=[]
  word=word.replace("І", "Ӏ")
  word=word.replace("I", "Ӏ")
  word=word.replace("1", "Ӏ")
  while i<len(word):
    if i<=len(word)-2:
      if word[i:i+2] in consonant_letters.keys():
        answ.append(consonant_letters[word[i:i+2]])
        i=i+2
      elif word[i:i+2] in vowels.keys():
        answ.append(vowels[word[i:i+2]])
        i=i+2
      else:
        answ.append(word[i])
        i=i+1
    else:
      answ.append(word[i])
      i=i+1
  answ_fin=[]
  i=0
  while i<len(answ):
    if answ[i]=='ё' and i>0:
      if answ[i-1] in consonant_letters.values() or answ[i-1]=='ʷ':
        answ_fin.append("o")
      else:
        answ_fin.append("jo")
    elif answ[i]=='ё' and i==0:
      answ_fin.append("jo")
    elif answ[i]=='в' and i>0:
      if answ[i-1] in consonant_letters.values() or answ[i-1]=='ʷ':
        answ_fin.append("ʷ")
      else:
        answ_fin.append("w")
    elif answ[i]=='в' and i==0:
      answ_fin.append("w")
    else:
      if answ[i] in consonant_letters:
        answ_fin.append(consonant_letters[answ[i]])
      elif answ[i] in vowels:
        answ_fin.append(vowels[answ[i]])
      else:
        answ_fin.append(answ[i])
    i=i+1
  return ('').join(answ_fin)
def transliterator_tsakhur(word):
  consonant_letters={"б":"b", "бъ":"b’","в":"w","г":"g","гъ":"ʁ","гь":"h","гӀ":"ɣ","д":"d","дъ":"t’","дж":"dʒ","ж":"ʒ","з":"z","й":"j","к":"kʰ","кк":"k:",
                     "къ":"ɢ","кь":"q’","кӀ":"k’","л":"l","м":"m","н":"n","п":"pʰ","пп":"p:","пӀ":"p’","р":"r","с":"s","сс":"s:","т":"tʰ",
                     "тт":"t:","тӀ":"t’","ф":"f","х":"χ","хх":"χ:","хъ":"qʰ","ххъ":"q:","хь":"x","ххь":"x:","ц":"tsʰ","цц":"ts:",
           "цӀ":"tsʼ","ч":"tʃʰ","чч":"tʃ:","чӀ":"tʃʼ","ш":"ʃ","щ":"ʃ:","ъ":"ʔ","'":"ʲ"}
  vowels={"а":"a","aa":"aː","е":"ʲe","еэ":"ʲeː","и":"ʲi","ии":"ʲiː","о":"o","оо":"oː","у":"u","уу":"uː",
          "ы":"ɘ","э":"e","ю":"ju","юу":"juː","я":"ja","яа":'jaː'}
  i=0
  answ=[]
  word=word.replace("І", "Ӏ")
  word=word.replace("I", "Ӏ")
  word=word.replace("1", "Ӏ")
  while i<len(word):
    if i<=len(word)-3:
      if word[i:i+3] in consonant_letters.keys():
        answ.append(consonant_letters[word[i:i+3]])
        i=i+3
      else:
        answ.append(word[i])
        i=i+1
    else:
      answ.append(word[i])
      i=i+1
  answ2=[]
  i=0
  while i<len(answ):
    if i<len(answ)-1:
      if answ[i]+answ[i+1] in consonant_letters:
        answ2.append(consonant_letters[answ[i]+answ[i+1]])
        i=i+2
      elif answ[i]+answ[i+1] in vowels:
        if answ[i]+answ[i+1]=='юу' and i>0:
          if answ[i-1] in consonant_letters.keys() or answ[i-1] in consonant_letters.values():
            answ2.append('ʲuː')
          else:
            answ2.append('juː')
        elif answ[i]+answ[i+1]=='юу' and i==0:
          answ2.append('juː')
        elif answ[i]+answ[i+1]=='ая' and i>0:
          if answ[i-1] in consonant_letters.keys() or answ[i-1] in consonant_letters.values():
            answ2.append('ʲaː')
          else:
            answ2.append('jaː')
        elif answ[i]+answ[i+1]=='ая' and i==0:
          answ2.append('jaː')
        else:
          answ2.append(vowels[answ[i]+answ[i+1]])
        i=i+2
      else:
        answ2.append(answ[i])
        i=i+1
    else:
      answ2.append(answ[i])
      i=i+1
  answ_fin=[]
  i=0
  while i<len(answ2):
    if answ2[i]=='ё' and i>0:
      if answ2[i-1] in consonant_letters.values() or answ2[i-1]=='ʷ':
        answ_fin.append("ʲo")
      else:
        answ_fin.append("jo")
    elif answ2[i]=='ё' and i==0:
      answ_fin.append("jo")
    elif answ2[i]=='в' and i>0:
      if answ2[i-1] in consonant_letters.values() or answ2[i-1]=='ʷ':
        answ_fin.append("ʷ")
      else:
        answ_fin.append("w")
    elif answ2[i]=='в' and i==0:
      answ_fin.append("w")
    elif answ2[i]=='ю' and i>0:
      if answ2[i-1] in consonant_letters.values() or answ2[i-1]=='ʷ':
        answ_fin.append("ʲu")
      else:
        answ_fin.append("ju")
    elif answ2[i]=='ю' and i==0:
      answ_fin.append("ju")
    elif answ2[i]=='я' and i>0:
      if answ2[i-1] in consonant_letters.values() or answ2[i-1]=='ʷ':
        answ_fin.append("ʲa")
      else:
        answ_fin.append("ja")
    elif answ2[i]=='я' and i==0:
      answ_fin.append("ja")
    elif answ2[i]=='и' and i>0:
      if answ[i-1] in ['d', 't’', 'n', 'l', 'tsʰ','ts:', 'tsʼ', 'z', 's', 's:', 'g', 'kʰ','k:' 'k’', 'x','x:' ]:
        answ_fin.append("ʲi")
      else:
        answ_fin.append("i")
    elif answ2[i]=='и' and i==0:
      answ_fin.append("i")
    elif answ2[i]=='е' and i>0:
      if answ[i-1] in ['d', 't’', 'n', 'l', 'tsʰ','ts:', 'tsʼ', 'z', 's', 's:', 'g', 'kʰ','k:' 'k’', 'x','x:' ]:
        answ_fin.append("ʲe")
      elif answ2[i-1] in consonant_letters.values() or answ2[i-1]=='ʷ':
        answ_fin.append("e")
      else:
        answ_fin.append("je")
    elif answ2[i]=='е' and i==0:
      answ_fin.append("je")
    else:
      if answ2[i] in consonant_letters:
        answ_fin.append(consonant_letters[answ2[i]])
      elif answ2[i] in vowels:
        answ_fin.append(vowels[answ2[i]])
      else:
        answ_fin.append(answ2[i])
    i=i+1
  return ('').join(answ_fin)
def transliterator_botlikh(word):
  consonant_letters={"б":"b","в":"w","г":"g","гъ":"ʁ","гь":"h","гӀ":"ʕ","д":"d","дж":"dʒ","ж":"ʒ","з":"z","й":"j","к":"kʰ","кк":"kxː",
                     "къ":"qχ’ː","кь":"tɬ’ː","кӀ":"k’","кӀкӀ":"kx’ː","л":"l","лл":"lː","лъ":"ɬ","лълъ":"ɬː","лӀ":"tɬ","м":"m","н":"n","п":"pʰ","р":"r","с":"s","сс":"s:",
                     "сс":"sː","т":"tʰ",
                     "тӀ":"t’","ф":"f","х":"χ","хх":"χ:","хъ":"qχː","хь":"xː","хӀ":"ħ","ц":"tsʰ","цц":"cː",
           "цӀ":"tsʼ","цӀцӀ":"c’ː","ч":"tʃʰ","чч":"čː","чӀ":"tʃʼ","чӀчӀ":"č’ː","ш":"ʃ","щ":"ʃ:","ъ":"ʔ"}
  vowels={"а":"a","аᵸ":"ã","ā":"aː","е":"e","еᵸ":"ẽ","ē":"eː","и":"i","иᵸ":"ĩ","ӣ":"iː","о":"o","ō":"oː","у":"u","уᵸ":"ũ","ӯ":"uː",
          "э":"ʔe","эᵸ":"ʔẽ"}
  i=0
  answ=[]
  word=word.replace("І", "Ӏ")
  word=word.replace("I", "Ӏ")
  word=word.replace("1", "Ӏ")
  while i<len(word):
    if i<=len(word)-4:
      if word[i:i+4] in consonant_letters:
        answ.append(consonant_letters[word[i:i+4]])
        i=i+4
      else:
        answ.append(word[i])
        i=i+1
    else:
      answ.append(word[i])
      i=i+1
  answ2=[]
  i=0
  while i<len(answ):
    if i<len(answ)-1:
      if answ[i]+answ[i+1] in consonant_letters:
        answ2.append(consonant_letters[answ[i]+answ[i+1]])
        i=i+2
      elif answ[i]+answ[i+1] in vowels:
        answ2.append(vowels[answ[i]+answ[i+1]])
        i=i+2
      else:
        answ2.append(answ[i])
        i=i+1
    else:
      answ2.append(answ[i])
      i=i+1
  answ_fin=[]
  i=0
  while i<len(answ2):
    if answ2[i]=='в' and i>0:
      if answ2[i-1] in consonant_letters.values():
        answ_fin.append("ʷ")
      else:
        answ_fin.append("w")
    elif answ2[i]=='в' and i==0:
      answ_fin.append("w")
    else:
      if answ2[i] in consonant_letters.keys():
        answ_fin.append(consonant_letters[answ2[i]])
      elif answ2[i] in vowels.keys():
        answ_fin.append(vowels[answ2[i]])
      else:
        answ_fin.append(answ2[i])
    i=i+1
  return ('').join(answ_fin)
def transliterator_chamalal(word):
  consonant_letters={"б":"b","в":"w","г":"g","гъ":"ʁ","гь":"h","гӀ":"ʕ","д":"d","дж":"dʒ","ж":"ʒ","з":"z","й":"j","к":"kʰ",
                     "къ":"qχ’ː","кь":"tɬ’ː","кӀ":"k’","к̅Ӏ":"x’ː","л":"l","лъ":"ɬ","л̅ъ":"ɬː","лӀ":"tɬ","м":"m","н":"n","п":"pʰ","р":"r","с":"s",
                     "с̄ ":"sː","с̅Ӏ":"s’ː","т":"tʰ",
                     "тӀ":"t’","ф":"f","х":"χ","х̄ ":"χ:","хъ":"qχ","хь":"x","хӀ":"ħ","ц":"tsʰ",
           "цӀ":"tsʼ","ц̅Ӏ ":"c’ː","ч":"tʃʰ","чӀ":"tʃʼ","ч̅Ӏ ":"š’ː","ш":"ʃ","щ":"ʃ:","ъ":"ʔ"}
  vowels={"а":"a","аᵸ":"ã","ā":"aː","āᵸ":"ãː","е":"e","еᵸ":"ẽ","ē":"eː","и":"i","иᵸ":"ĩ","ӣ":"iː","ӣᵸ":"ĩː","о":"o","ō":"oː","у":"u","уᵸ":"ũ","ӯ":"uː","ӯᵸ":"ũː",
          "э":"ʔe","э̄":"ʔeː"}
  i=0
  answ=[]
  word=word.replace("І", "Ӏ")
  word=word.replace("I", "Ӏ")
  word=word.replace("1", "Ӏ")
  while i<len(word):
    if i<=len(word)-2:
      if word[i:i+2] in consonant_letters.keys():
        answ.append(consonant_letters[word[i:i+2]])
        i=i+2
      elif word[i:i+2] in vowels.keys():
        answ.append(vowels[word[i:i+2]])
        i=i+2
      else:
        answ.append(word[i])
        i=i+1
    else:
      answ.append(word[i])
      i=i+1
  answ_fin=[]
  i=0
  while i<len(answ):
    if answ[i]=='в' and i>0:
      if answ[i-1] in consonant_letters.values():
        answ_fin.append("ʷ")
      else:
        answ_fin.append("w")
    elif answ[i]=='в' and i==0:
      answ_fin.append("w")
    else:
      if answ[i] in consonant_letters.keys():
        answ_fin.append(consonant_letters[answ[i]])
      elif answ[i] in vowels.keys():
        answ_fin.append(vowels[answ[i]])
      else:
        answ_fin.append(answ[i])
    i=i+1
  return ('').join(answ_fin)
def transliterating(event):
    input_text = document.querySelector("#lang")
    language = input_text.value
    input_text = document.querySelector("#word")
    word = input_text.value
    if language=='avar':
        output_div = document.querySelector("#output")
        output_div.innerText = transliterator_avar(word)
    elif language=='lezgian':
        output_div = document.querySelector("#output")
        output_div.innerText = transliterator_lezgian(word)
    elif language=='lak':
        output_div = document.querySelector("#output")
        output_div.innerText = transliterator_lak(word)
    elif language=='dargwa':
        output_div = document.querySelector("#output")
        output_div.innerText = transliterator_dargwa(word)
    elif language=='chamalal':
        output_div = document.querySelector("#output")
        output_div.innerText = transliterator_chamalal(word)
    elif language=='botlikh':
        output_div = document.querySelector("#output")
        output_div.innerText = transliterator_botlikh(word)
    elif language=='khwarshi':
        output_div = document.querySelector("#output")
        output_div.innerText = transliterator_khwarshi(word)
    elif language=='tsakhur':
        output_div = document.querySelector("#output")
        output_div.innerText = transliterator_tsakhur(word)
