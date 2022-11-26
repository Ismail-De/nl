import streamlit as st
import spacy

string1 = st.text_input("Your text here")

def trsf(f):
  
  l =[]
  import en_core_web_sm
  nlp = en_core_web_sm.load()
  doc = nlp(f)
  for sent in doc.sents:
      l+=[sent]

  m = f.index(str(l[0]))
  mm = f.index(str(l[-1]))
  f = f[m + len(str(l[0])) : mm] 
  return f

butt = st.button('Transform')
if butt:
  st.write(trsf(string1))
