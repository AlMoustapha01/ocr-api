import re 
import nltk
from geotext import GeoText
from textblob import TextBlob
from googletrans import Translator
translator = Translator() 

class features:
    """ This class is used to classify the different
        words extracted from the image according to their nature.
    """
    def isDate(self,content):
        """ to know if a string is a date """
        date_pattern1 = '(0[1-9]|[12][0-9]|3[01])(-|/|.)(0[1-9]|1[012])(-|/|.)(19|20)\d\d$' #pattern of date in french format 
        date_pattern2 = "(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$" #pattern of date in english format
        date_pattern3 = '([0-3][0-9]?)\s[a-zA-Z-]+\s(19|20)\d{1,2}'
        if(re.findall(date_pattern1, content)):
            return True
        elif(re.findall(date_pattern2, content)):
            return True
        elif(re.findall(date_pattern3, content)):
            return True
        else:
            return False
    
    def isPercentage(self,content):
        pattern="(\d{1,2})(\.\d{1,2})?(%)"
        if(re.findall(pattern, content)):
            return re.findall(pattern, content)
        else:
            return False
        
    def isMonth(self,content):
        month_pattern1="(Jan|Fev|Mar|Avr|Mai|Jun|Jul|Aou|Sep|Oct|Nov|Dec)"
        month_pattern2="(Janvier|Février|Fevrier|Mars|Avril|Juin|Juillet|Août|Aout|Septembre|Octobre|Novembre|Decembre)"
        if(re.match(month_pattern1, content)):
            return True
        elif(re.match(month_pattern2, content)):
            return True
        else:
            return False
        
    def isEmail(self,content):
        """ to know if a string is a email"""
        email_pattern='^[a-zA-Z-]+@[a-zA-Z-]+\.[a-zA-Z]{2,6}$'
        if(re.match(email_pattern, content)):
            return True
        else:
            return False
    def isAlpha(self,content):
        pattern='^[a-zA-Z-]+'
        if(re.findall(pattern, content)):
            return True
        else:
            return False
    def isPrice(self,content):
        """ to know if a string is a price"""
        french="^\d+(\.\d{3}|\s\d{3})?(,\d{1,2})?$"
        price_euro="^(€\d+)(\.\d{3}|\s\d{3})?(,\d{1,2})?$"
        price_eng="^(\$\d+|£\d+)(,\d{3}|\s\d{3})?(\.\d{1,2})?$"
        eng="^\d+(,\d{3}|\s\d{3})?(\.\d{1,2})?$"
        if(re.match(french,content)):
            return True
        elif(re.match(eng,content)):
            return True
        elif(re.match(price_euro,content)):
            return True
        elif(re.match(price_eng,content)):
            return True
        else:
            return False
    def isDevise(self,content):
        """ to know if a string is a device"""
        device="(\$|€|£|¥|franc\sCFA|Franc\sCFA|FRANC\sCFA)"
        if(re.findall(device,content)):
            return True
        else:
            return False
    def isCity(self,content):
        content=content.lower()
        content=content.capitalize()
        city=GeoText(content)
        if not(city.cities):
            return False
        else:
            return True
    def isCountry(self,content):
        trans=translator.translate(content, src='fr').text
        country=GeoText(trans)
        if not(country.countries):
            return False
        else:
            return True
    def nature(self,content):
        text = nltk.word_tokenize(content)
        nltk.pos_tag(text)