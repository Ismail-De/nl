import streamlit as st
import spacy

nlp = spacy.load('en_core_web_sm')

string1 = st.write("Your text here")

def trsf(f):
  l =[]
  doc = nlp(f)


  for sent in doc.sents:
      print(sent)
      l+=[sent]

  m = string1.index(l[0])
  mm = string1.index(l[-1])
  string1 = string1[m+len(l[0]) : mm] 
  return string1


st.write(trsf(string1))
