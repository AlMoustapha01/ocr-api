import cv2
import numpy as np
import os
import imutils
import pytesseract
from pytesseract import Output
import pandas as pd
from .utils import *
import json
from .extraction import *


class invoiceTreatment():

    def invoiceContour(self,pathImg):
        heightImg = 640
        widthImg  = 480
        img = cv2.imread(pathImg)
        img2=cv2.imread(pathImg,0)
        img = cv2.resize(img, (widthImg, heightImg)) # RESIZE IMAGE
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE
        imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) # ADD GAUSSIAN BLUR
        thres=valTrackbars() # GET TRACK BAR VALUES FOR THRESHOLDS
        imgThreshold = cv2.Canny(imgBlur,thres[0],thres[1]) # APPLY CANNY BLUR
        kernel = np.ones((5, 5))
        imgDial = cv2.dilate(imgThreshold, kernel, iterations=2) # APPLY DILATION
        imgThreshold = cv2.erode(imgDial, kernel, iterations=1)  # APPLY EROSION

        ## FIND ALL COUNTOURS
        imgContours = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
        imgBigContour = img.copy() # COPY IMAGE FOR DISPLAY PURPOSES
        contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # FIND ALL CONTOURS
        cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 10) # DRAW ALL DETECTED CONTOURS

        # FIND THE BIGGEST COUNTOUR
        biggest, maxArea = biggestContour(contours) # FIND THE BIGGEST CONTOUR
        if biggest.size != 0:
            biggest=reorder(biggest)
            cv2.drawContours(imgBigContour, biggest, -1, (0, 255, 0), 20) # DRAW THE BIGGEST CONTOUR
            imgBigContour = drawRectangle(imgBigContour,biggest,2)
            pts1 = np.float32(biggest) # PREPARE POINTS FOR WARP
            pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) # PREPARE POINTS FOR WARP
            matrix = cv2.getPerspectiveTransform(pts1, pts2)
            imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

            #REMOVE 20 PIXELS FORM EACH SIDE
            imgWarpColored=imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
            imgWarpColored = cv2.resize(imgWarpColored,(widthImg,heightImg))

            # APPLY ADAPTIVE THRESHOLD
            imgWarpGray = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)

            return imgWarpGray
        else:
            print("l'image n'a pas un fond adapté ou le traitement n'est pas necessaire")
            return img2


    def dataformation(self,img):
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
        test2=cv2.imread(img,0)
        elt=pytesseract.image_to_data(test2, output_type=Output.DATAFRAME,lang='eng+fra')
        Nan= elt[elt.word_num==0]
        space= elt[elt.text==" "]
        df=elt.drop(space.index)
        df=df.drop(Nan.index)
        df['right']=df['left']+df['width']
        df['bottom']=df['top']+df['height']
        lastDf=pd.DataFrame()
        lastDf['xmin']=df.left
        lastDf['xmax']=df.right
        lastDf['ymax']=df.top
        lastDf['ymin']=df.bottom
        lastDf['blockNumber']=df.block_num
        lastDf['Object']=df.text
        return lastDf



    def Separate(self,x,lastDf):
        
        result=lastDf[(lastDf.ymax==x)|(lastDf.ymax==x-1)|(lastDf.ymax==x-2)|(lastDf.ymax==x-3)|(lastDf.ymax==x-4)|(lastDf.ymax==x-5)|(lastDf.ymax==x-6)|(lastDf.ymax==x-7)|(lastDf.ymax==x-8)|(lastDf.ymax==x+1)|(lastDf.ymax==x+2)|(lastDf.ymax==x+3)|(lastDf.ymax==x+4)|(lastDf.ymax==x+5)|(lastDf.ymax==x+6)|(lastDf.ymax==x+7)]
        nb=len(result)
        i=0
        k=0
        tab=pd.DataFrame(columns = ['xmin', 'xmax', 'ymin','ymax','Object'])
        lastDf.drop(index=result.index,inplace=True)
        while i<nb:
            try:
                etat=abs(result.xmin.iloc[i+1]-result.xmax.iloc[i])
                if(etat>30):
                    result1=result[:i+1]
                    result2=result[i+1:]
                    liste=[]
                    for j in result1.index:
                        liste.append(result1.Object[j])
                    line=" ".join(liste)
                    tab.loc[result1.index[0]]={'xmin':result1.xmin.min(), 'xmax':result1.xmax.max(), 'ymin':result1.ymin.max(),'ymax':result1.ymax.min(),'Object':line}
                    result=result[i+1:]
                    i=-1    
            except:
                pass
            nb=len(result)

            i=i+1
            k=k+1
        liste1=[]
        if len(result)>1:
            for j in result.index:
                liste1.append(result.Object[j])
            line1=" ".join(liste1)
            tab.loc[result.index[0]]={'xmin':result.xmin.min(), 'xmax':result.xmax.max(), 'ymin':result.ymin.max(),'ymax':result.ymax.min(),'Object':line1}
            return tab
        final=pd.concat([tab,result],sort=False)
        final.drop(columns=['blockNumber'],inplace=True)
        
        return final

    def listePosition(self,df):
        listymax=df.groupby(df.ymax).count().index
        listymin=df.groupby(df.ymin).count().index
        listxmax=df.groupby(df.xmax).count().index
        listxmin=df.groupby(df.xmin).count().index

        return (listymax,listymin,listxmax,listxmin)

    def groupWord(self,ymax,data):
        nbline=len(data)
        i=0
        tab=pd.DataFrame(columns = ['xmin', 'xmax', 'ymin','ymax','Object'])
        tab.loc[0]={'xmin':0, 'xmax':0, 'ymin':1,'ymax':1,'Object':'test'}
        for x in ymax:
            elt=self.Separate(x,data)
            if not elt.index.empty:
                tab =pd.concat([tab,elt],sort=False)
        return tab
    
    def to_json(self,df):
        df.Object.to_json('df.json', force_ascii=False)
        with open('media/df.json', 'w', encoding='utf-8') as file:
            df.Object.to_json(file, force_ascii=False)
        with open('media/df.json', 'r', encoding='utf-8') as file:
            js=json.load(file)
        return js

def pyocr(img):
    elt=invoiceTreatment()
    df=elt.dataformation(img)
    ymax=elt.listePosition(df)[0]
    tab= elt.groupWord(ymax,df)
    extract= Extraction(tab)
    json = elt.to_json(tab)
    js={
        'total':extract.total(),
        'pourcentage':extract.pourcentage(),
        'tva':extract.tva(),
        'date':extract.date(),
        'ligneFacture':extract.ligneFacture()}
    return js