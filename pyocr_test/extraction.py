import re
import pandas as pd
from .features import *

class Extraction:
    def __init__(self,data):
        self.data= data
        self.feature= features()
    def ligne(self,i):
        ligne=self.data[(self.data.ymax==self.data.loc[i].ymax)|(self.data.ymax==self.data.loc[i].ymax-1)|(self.data.ymax==self.data.loc[i].ymax-2)|(self.data.ymax==self.data.loc[i].ymax-3)|(self.data.ymax==self.data.loc[i].ymax-4)|(self.data.ymax==self.data.loc[i].ymax-5)|(self.data.ymax==self.data.loc[i].ymax-6)|(self.data.ymax==self.data.loc[i].ymax-7)|(self.data.ymax==self.data.loc[i].ymax-8)|(self.data.ymax==self.data.loc[i].ymax+8)|(self.data.ymax==self.data.loc[i].ymax+7)|(self.data.ymax==self.data.loc[i].ymax+6)|(self.data.ymax==self.data.loc[i].ymax+5)|(self.data.ymax==self.data.loc[i].ymax+4)|(self.data.ymax==self.data.loc[i].ymax+3)|(self.data.ymax==self.data.loc[i].ymax+2)|(self.data.ymax==self.data.loc[i].ymax+1)]
        return ligne
        
    def colonne(self,i):
        colonne=self.data[(self.data.xmax==self.data.loc[i].xmax)|(self.data.xmax==self.data.loc[i].xmax-1)|(self.data.xmax==self.data.loc[i].xmax-2)|(self.data.xmax==self.data.loc[i].xmax-3)|(self.data.xmax==self.data.loc[i].xmax-4)|(self.data.xmax==self.data.loc[i].xmax-5)|(self.data.xmax==self.data.loc[i].xmax-6)|(self.data.xmax==self.data.loc[i].xmax-7)|(self.data.xmax==self.data.loc[i].xmax+7)|(self.data.xmax==self.data.loc[i].xmax+6)|(self.data.xmax==self.data.loc[i].xmax+5)|(self.data.xmax==self.data.loc[i].xmax+4)|(self.data.xmax==self.data.loc[i].xmax+3)|(self.data.xmax==self.data.loc[i].xmax+2)|(self.data.xmax==self.data.loc[i].xmax+1)|(self.data.xmin==self.data.loc[i].xmin)|(self.data.xmin==self.data.loc[i].xmin-1)|(self.data.xmin==self.data.loc[i].xmin-2)|(self.data.xmin==self.data.loc[i].xmin-3)|(self.data.xmin==self.data.loc[i].xmin-4)|(self.data.xmin==self.data.loc[i].xmin-5)|(self.data.xmin==self.data.loc[i].xmin-6)|(self.data.xmin==self.data.loc[i].xmin-7)|(self.data.xmin==self.data.loc[i].xmin+7)|(self.data.xmin==self.data.loc[i].xmin+6)|(self.data.xmin==self.data.loc[i].xmin+5)|(self.data.xmin==self.data.loc[i].xmin+4)|(self.data.xmin==self.data.loc[i].xmin+3)|(self.data.xmin==self.data.loc[i].xmin+2)|(self.data.xmin==self.data.loc[i].xmin+1)]
        return colonne
        
    def total(self):
        liste=self.data.Object.index.tolist() #liste des index des mots
        total=[]
        totaux=[]
        tot=pd.DataFrame()
        for i in liste:
            if self.data.Object.str.contains('(tota|TTC)',flags=re.IGNORECASE, regex=True)[i]:
                total.append(i)
        if len(total)>=1:
            for j in total:
                tot = self.data.loc[j]
                ligne=self.ligne(j)
                colonne=self.colonne(j)
                haut=None
                bas=None
                gauche=None
                droit=None
                ColIndex=colonne.index.tolist()
                LinIndex=ligne.index.tolist()
                if not int(ColIndex[0])==int(tot.name):
                    indice=ColIndex.index(tot.name)
                    haut=ColIndex[indice-1]
                if not int(ColIndex[-1])==int(tot.name):
                    indice=ColIndex.index(tot.name)
                    bas=ColIndex[indice+1]
                if not int(LinIndex[0])== int(tot.name):
                    indice=LinIndex.index(tot.name)
                    gauche=LinIndex[indice-1]
                if not int(LinIndex[-1])==int(tot.name):
                    indice=LinIndex.index(tot.name)
                    droit=LinIndex[indice+1]
                datadict={"haut":haut,"bas":bas,"gauche":gauche,"droit":droit}
                print(datadict)
                if haut:
                    if self.feature.isDevise(self.data.loc[haut].Object) or self.feature.isPrice(self.data.loc[haut].Object):
                        if not self.feature.isAlpha(self.data.loc[haut].Object):
                            TOTAL=haut
                            print(self.data.loc[TOTAL].Object)
                            totaux.append(self.data.loc[TOTAL].Object)
                if gauche:
                    if self.feature.isDevise(self.data.loc[gauche].Object) or self.feature.isPrice(self.data.loc[gauche].Object):
                        if not self.feature.isAlpha(self.data.loc[gauche].Object):
                            TOTAL=gauche
                            print(self.data.loc[TOTAL].Object)
                            totaux.append(self.data.loc[TOTAL].Object)
                if bas:
                    if self.feature.isDevise(self.data.loc[bas].Object) or self.feature.isPrice(self.data.loc[bas].Object):
                        if not self.feature.isAlpha(self.data.loc[bas].Object):
                            TOTAL=bas
                            print(self.data.loc[TOTAL].Object)
                            totaux.append(self.data.loc[TOTAL].Object)
                if droit:
                    if self.feature.isDevise(self.data.loc[droit].Object) or self.feature.isPrice(self.data.loc[droit].Object):
                        if not self.feature.isAlpha(self.data.loc[droit].Object):
                            TOTAL=droit
                            print(self.data.loc[TOTAL].Object)
                            totaux.append(self.data.loc[TOTAL].Object)
            try:
                
                return (totaux[-1],totaux)
            except:
                return totaux
        
    def pourcentage(self):
        listPer=[]
        listIndex=self.data.Object.index.tolist()
        for i in listIndex:
            if self.data.Object.str.contains('(\d{1,2})(\.\d{1,3})?(%)',flags=re.IGNORECASE, regex=True)[i]:
                listPer.append(i)
        pp=[]      
        if len(listPer)==1:
            if self.data.Object.str.contains('(tva|tax|tps|tvq)',flags=re.IGNORECASE, regex=True)[listPer[0]]:
                elt=self.data.loc[listPer[0]].Object
                per1=re.findall('(\d{1,2}\.\d{1,3}?%)',elt)
                per2=re.findall('(\d{1,2}%)',elt)
                per3=re.findall('(\d{1,2}\s{1,3}%)',elt)
                if per1:
                    pp.append(per1[0])
                if per2:
                    pp.append(per2[0])
                if per3:
                     pp.append(per3[0])
                return pp
            line=self.ligne(listPer[0]).index.tolist()
            row=self.colonne(listPer[0]).index.tolist()
            for i,j in zip(line,row):
                if self.data.Object.str.contains('(tva|tax|tps|tvq)',flags=re.IGNORECASE, regex=True)[i] or self.data.Object.str.contains('(tva|tax|tps|tvq)',flags=re.IGNORECASE, regex=True)[j]:
                    elt=self.data.loc[listPer[0]].Object
                    per1=re.findall('(\d{1,2}\.\d{1,3}?%)',elt)
                    per2=re.findall('(\d{1,2}%)',elt)
                    per3=re.findall('(\d{1,2}\s{1,3}%)',elt)
                    if per1:
                        pp.append(per1[0])
                    if per2:
                        pp.append(per2[0])
                    if per3:
                        pp.append(per3[0])
                    return pp
        
        else:
            for j in listPer:
                if self.data.Object.str.contains('(tva|tax|tps|tvq)',flags=re.IGNORECASE, regex=True)[j]:
                    elt=self.data.loc[j].Object
                    per1=re.findall('(\d{1,2}\.\d{1,3}?%)',elt)
                    per2=re.findall('(\d{1,2}%)',elt)
                    per3=re.findall('(\d{1,2}\s{1,3}%)',elt)
                    if per1:
                        pp.append(per1[0])
                    if per2:
                        pp.append(per2[0])
                    if per3:
                         pp.append(per3[0])
                line=self.ligne(j).index.tolist()
                row=self.colonne(j).index.tolist()
                for i,k in zip(line,row):
                    if self.data.Object.str.contains('(tva|tax|tps|tvq)',flags=re.IGNORECASE, regex=True)[i] or self.data.Object.str.contains('(tva|tax|tps|tvq)',flags=re.IGNORECASE, regex=True)[k]:
                        elt=self.data.loc[j].Object
                        per1=re.findall('(\d{1,2}\.\d{1,3}?%)',elt)
                        per2=re.findall('(\d{1,2}%)',elt)
                        per3=re.findall('(\d{1,2}\s{1,3}%)',elt)
                        if per1:
                            pp.append(per1[0])
                        if per2:
                            pp.append(per2[0])
                        if per3:
                            pp.append(per3[0])
                
            return pp
            
        return listPer
            
        
    
    def tva(self):
        listIndex=self.data.Object.index.tolist()
        tot=pd.DataFrame()
        listTva=[]
        per=None
        for i in listIndex:
            if self.data.Object.str.contains('(tva|tax|tps|tvq)',flags=re.IGNORECASE, regex=True)[i]:
                listTva.append(i)
        if len(listTva)==1:
                i=listTva[0]
                tot = self.data.loc[i]
                ligne=self.ligne(i)
                colonne=self.colonne(i)
                haut=None
                bas=None
                gauche=None
                droit=None
                ColIndex=colonne.index.tolist()
                LinIndex=ligne.index.tolist()
                if not int(ColIndex[0])==int(tot.name):
                    indice=ColIndex.index(tot.name)
                    haut=ColIndex[indice-1]
                if not int(ColIndex[-1])==int(tot.name):
                    indice=ColIndex.index(tot.name)
                    bas=ColIndex[indice+1]
                if not int(LinIndex[0])== int(tot.name):
                    indice=LinIndex.index(tot.name)
                    gauche=LinIndex[indice-1]
                if not int(LinIndex[-1])==int(tot.name):
                    indice=LinIndex.index(tot.name)
                    droit=LinIndex[indice+1]
                datadict={"haut":haut,"bas":bas,"gauche":gauche,"droit":droit}

                if haut:
                    if self.feature.isDevise(self.data.loc[haut].Object) or self.feature.isPrice(self.data.loc[haut].Object):
                        if not self.feature.isAlpha(self.data.loc[haut].Object):
                            TOTAL=haut
                if gauche:
                    if self.feature.isDevise(self.data.loc[gauche].Object) or self.feature.isPrice(self.data.loc[gauche].Object):
                        if not self.feature.isAlpha(self.data.loc[gauche].Object):
                            TOTAL=gauche
                if bas:
                    if self.feature.isDevise(self.data.loc[bas].Object) or self.feature.isPrice(self.data.loc[bas].Object):
                        if not self.feature.isAlpha(self.data.loc[bas].Object):
                            TOTAL=bas
                if droit:
                    if self.feature.isDevise(self.data.loc[droit].Object) or self.feature.isPrice(self.data.loc[droit].Object):
                        if not self.feature.isAlpha(self.data.loc[droit].Object):
                            TOTAL=droit
                colonne=self.colonne(TOTAL).Object.tolist()
                for elt in colonne:
                    if self.feature.isPrice(elt)  or self.feature.isDevise(elt):
                        pass
                    else:
                        del colonne[colonne.index(elt)]
                tva=self.data.loc[TOTAL].Object
        elif len(listTva)>1:
            Ttva=[]
            tva=None
            for i in listTva:
                tot = self.data.loc[i]
                ligne=self.ligne(i)
                print(ligne)
                colonne=self.colonne(i)
                haut=None
                bas=None
                gauche=None
                droit=None
                ColIndex=colonne.index.tolist()
                LinIndex=ligne.index.tolist()
                if not int(ColIndex[0])==int(tot.name):
                    indice=ColIndex.index(tot.name)
                    haut=ColIndex[indice-1]
                if not int(ColIndex[-1])==int(tot.name):
                    indice=ColIndex.index(tot.name)
                    bas=ColIndex[indice+1]
                if not int(LinIndex[0])== int(tot.name):
                    indice=LinIndex.index(tot.name)
                    gauche=LinIndex[indice-1]
                if not int(LinIndex[-1])==int(tot.name):
                    indice=LinIndex.index(tot.name)
                    droit=LinIndex[indice+1]
                datadict={"haut":haut,"bas":bas,"gauche":gauche,"droit":droit}
                print(datadict)
                if bas:
                    if self.feature.isDevise(self.data.loc[bas].Object) or self.feature.isPrice(self.data.loc[bas].Object):
                        TVA=bas
                        Ttva.append(self.data.loc[TVA].Object)
                if droit:
                    if self.feature.isDevise(self.data.loc[droit].Object) or self.feature.isPrice(self.data.loc[droit].Object):
                        TVA=droit
                        Ttva.append(self.data.loc[TVA].Object)
            return Ttva
        return (tva,colonne)
    
    def date(self):
        obj=self.data.Object
        index=obj.index
        date=[]
        allDate=[]
        for i in index:
            if self.feature.isDate(obj[i]):
                date.append(i)
                
        for i in date:
            dat = self.data.loc[i]
            dates=None
            ligne=self.ligne(i)
            colonne=self.colonne(i)
            haut=None
            gauche=None
            ColIndex=colonne.index.tolist()
            LinIndex=ligne.index.tolist()
            if not int(ColIndex[0])==int(dat.name):
                indice=ColIndex.index(dat.name)
                haut=ColIndex[indice-1]
            if not int(LinIndex[0])== int(dat.name):
                indice=LinIndex.index(dat.name)
                gauche=LinIndex[indice-1]

            if haut:
                dateH=self.data.loc[haut].Object
            else:
                dateH=None
            if gauche:
                dateG=self.data.loc[gauche].Object
            else:
                dateG=None
            if re.findall('(:)',dat.Object):
                elt=dat.Object.split(':')
                allDate.append({'haut':None,'gauche':elt[0],'date':elt[1]})
            else:
                allDate.append({'haut':dateH,'gauche':dateG,'date':dat.Object})
            
        if not allDate:
            listDate=[]
            listIndex=self.data.Object.index.tolist()
            for i in listIndex:
                if self.data.Object.str.contains('(DATE)',flags=re.IGNORECASE, regex=True)[i]:
                    listDate.append(i)
            for j in listDate:
                tot = self.data.loc[j]
                ligne=self.ligne(j)
                colonne=self.colonne(j)
                haut=None
                bas=None
                gauche=None
                droit=None
                ColIndex=colonne.index.tolist()
                LinIndex=ligne.index.tolist()
                if not int(ColIndex[0])==int(tot.name):
                    indice=ColIndex.index(tot.name)
                    haut=ColIndex[indice-1]
                if not int(ColIndex[-1])==int(tot.name):
                    indice=ColIndex.index(tot.name)
                    bas=ColIndex[indice+1]
                if not int(LinIndex[0])== int(tot.name):
                    indice=LinIndex.index(tot.name)
                    gauche=LinIndex[indice-1]
                if not int(LinIndex[-1])==int(tot.name):
                    indice=LinIndex.index(tot.name)
                    droit=LinIndex[indice+1]
                datadict={"haut":haut,"bas":bas,"gauche":gauche,"droit":droit}

                
                if droit:
                    allDate.append(self.data.loc[droit].Object)
            return allDate
                
                
                
        

        
        return allDate
    
    def ligneFacture(self):
        index=self.data.index
        objects= self.data.Object
        listePrice=[]
        line=[]
        actu=0
        for i in index :
            if self.feature.isPrice(self.data.loc[i].Object) or self.feature.isDevise(self.data.loc[i].Object):
                listePrice.append(i)
        for j in listePrice:
            ligne=self.ligne(j)
            
            if len(ligne.index)>=4:
                if actu == ligne.index.tolist():
                    pass
                else:
                    line.append(ligne)
                
            actu=ligne.index.tolist()
        last=[]
        for tab in line:
            ob= tab.Object
            count=0
            for elt in ob:
                if self.feature.isPrice(elt) or self.feature.isDevise(elt):
                    count+=1
            
            if count>=2:
                last.append(tab)
            else:
                pass
        test=[]
        for li in last:
            colonne=self.colonne(li.iloc[0].name)
            ind=colonne.index.tolist()
            i=ind.index(li.iloc[0].name)
            try:
                
                l=[ind[i],ind[i+1]]
                lignesecond=self.ligne(ind[i+1])
                etat=colonne.loc[ind[i+1]].ymax-colonne.loc[ind[i]].ymin
                if len(lignesecond)<4:
                    if etat<=15:
                        text=colonne.loc[ind[i]].Object + ' ' + colonne.loc[ind[i+1]].Object
                        li.loc[ind[i]].Object=text
                    else:
                        pass
                else:
                    pass
            except IndexError:
                pass
        t=[]
        final=[]
        nb=0
        for elt in last:
            nb=nb+1
            t.append({'ligne {}'.format(nb) : elt.Object.tolist()})
        return t
    
               
