# -*- coding: utf-8 -*-
import os,sys
import string

cnt = 0

pdf_path = '/home/luozhiyi/projects/healthcareSys/data/knownetPdf/'
raw_path = '/home/luozhiyi/projects/healthcareSys/data/knownetTxt/'
processedTxt_path = '/home/luozhiyi/projects/healthcareSys/data/knownetProcessedTxt/'
p1_path = '/home/luozhiyi/projects/healthcareSys/data/Txt1/'
p2_path = '/home/luozhiyi/projects/healthcareSys/data/Txt2/'

def pdf2txt(pdf_path):

    fns = os.listdir(pdf_path)

    for fn in fns:
        txtname = os.path.splitext(fn)[0]
        cmd =  ' '.join(["pdf2txt.py",pdf_path+fn,">",txtname+".txt"])
        os.system(cmd)

def processRawTxt(raw_path,processed_path, processor):
    fns = os.listdir(raw_path)
        
    for fn in fns:
        txtfn = raw_path+fn
        processedfn = processed_path+fn
        processor(txtfn, processedfn)

def txtToOnePara(txtfn,processedfn):
    with open(txtfn) as f, open(processedfn,'w') as outf:
        text = f.read()
        text = text.translate(None,string.whitespace)
        text = text.translate(None,string.uppercase)
        text = text.translate(None,string.lowercase)
        text = text.translate(None,string.punctuation)
        outf.write(text)

def segSentence(txtfn,processedfn):
    cnt = 0
    chiEndPunc = '．：'
    chiEndPunc_list = ['．',' *',' **','·','。']
    with open(txtfn) as f, open(processedfn,'w') as outf:
        text = f.read()
        text = text.replace('\n\n','\n')
        for line in text.split('\n'):
            correctEnd = False
            for ep in chiEndPunc_list:
                if line.endswith(ep):
                    correctEnd = True
                    break
            parts = line.split('．')
            if not parts[-1]: parts = parts[:-1]            
            for i in range(len(parts)):
                sen = parts[i]
                if i==len(parts)-1 and not correctEnd:
                    outf.write(sen)
                else: outf.write(sen + '．\n')

def trimer(txtfn,processedfn):
    with open(txtfn) as f, open(processedfn,'w') as outf:
        for line in f:
            re = ''
            for c in line:
                if not c==' ': re += c
            outf.write(re)


#processRawTxt(raw_path,p1_path,segSentence)
processRawTxt(p1_path,p2_path,trimer)


"""
# Run with python3
errf = open('error.txt','w')
curfilenames = [name for name in os.listdir('.')]
#print(curfilenames)

for fn in fns:
    txtname = os.path.splitext(fn)[0]
    if txtname+".txt" not in curfilenames:
        errf.write(txtname+".pdf\n")
"""


