# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:05:07 2019

@author: Sinead
"""

from nltk import*
#from nltk.corpus import stopwords
from nltk.corpus import udhr
from docx import Document

def langToWord_ratio(text):
    
    tokens=wordpunct_tokenize(text)        //把文档里面的内容分成单个词                     #tokenize the document text
    
    docWords=[]                       //创建一个新的数组                          #create empty list data sturucture called docWords
    for tokenToWord in tokens:                                  #for each token put into variable called tokenToWord
        docWords.append(tokenToWord.lower())       //将所有的词变成小写并写进那个数组                 #make all words put into tokenToWord lowercase and then append to the list docWords(puts it in at the end)
 
#    print("tokens is of variable type: ", type(tokens))        #"type" tells you the class of the variable given
#    print("words is of variable type: ", type(docWords))  
#    print("tokens: ",tokens)                                   #print out all the tokens in document 
#    print("Available languages: ", udhr.fileids())             #A udhr method called file ids brings back the list of languages available
#    print("\n")
    
    langRatios={}                                               #create empty dictionary data structure -> key:value of key
    
    if len(udhr.fileids()) >0:
        for language in udhr.fileids():         //nltk还包含多国语言语料库。比如udhr，包含有超过300种语言的世界人权宣言。fileids:语料库中的文件,每一个语言都有自己的独立文件，language就是遍历这个语料库的各个不同语言的文档#for each language file, put into variable called language
            udhr_set=set(udhr.words(language))  //  words(fileids=[f1,f2,f3])     获得指定文件中的词汇，  language是参数，获得这个language的词汇，然后通过set建立集合。例如此时language代表日文，获得udhr中的日文的词汇， 然后建立集合              #set of most used words in each language

#            print("language: ", language)
#            print(set(udhr.words(language)))
#            print("\n")
        
            docWords_set=set(docWords)       //将文档中的词创建集合，                   #set of words from our document
        
            common_elements=docWords_set.intersection(udhr_set)。//寻找两个集合的交集，也就是相同的词。 #set of words that appear in both docWords_set and udhr_set
        
            if len(common_elements)>0:   //如果存在相同的词汇
                langRatios[language]=len(common_elements)      //在languageration的数组里存入这个语言的词汇在文档中出现的频率    #for each language with atleast one common word = language:number of common words
        
    else:
        print("No Language available")
        return                                                  #will stop here and wont process anymore if true
        
    return langRatios          //返回数组头地址                                  #coming out of method langToWord_ratio with langRatios dictionary



def lang_mostCommonWords(text):                                 #string variable called text-allText now in this
    ratios=langToWord_ratio(text)                               #put langRatios dictionary (from langToWord_Ratio method) in ratios

#    print("ratios: ",ratios)                                   #print the language to word ratio for each language
#    print("\n")   
#    print("ratios is of variable type: ", type(ratios))
    
    langWithMostWords=max(ratios,key=ratios.get)     //找到langratios中最大的值，就是找到出现次数最多的语言           #find max ratio number and bring back key(language) for that
    
#    print("mostlang: ", langWithMostWords)                     #print full name of language from list with highest ratio
    
    return langWithMostWords                                    #comes out of method lang_mostCommonWords with the language that has most common words



def main():                                                     #define a method called main
    doc=Document('C:/Users/Dell/.spyder-py3/Identify_TextLang.docx')
    allText=""                                                  #create empty string called allText(Document text will go into this so that it is readable)
#    print("allText: ", type(allText))
    
    for docpara in doc.paragraphs:                              #for each document paragraph put into docpara
        allText = allText + docpara.text                        #allText has all paragraphs now

#    print("\n")
#    print("Text in my Word document: ", allText)
#    print("\n")
   
    textLanguage=lang_mostCommonWords(allText)                  #result from method lang_mostCommonWords
    docLanguage="-".join(textLanguage.split('-')[0:1])       #removes any text after the first -
    
    print("Text Language is: ", docLanguage)
    
main() #run from main method
