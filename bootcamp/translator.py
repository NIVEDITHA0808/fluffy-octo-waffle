def translation(phrase):
    
    #translate = ""
    
    #translate_1 = ""
    translate_2 = ""
    translate_3 = ""
    '''
    for i in phrase:
         if i in "aeiou":
            break
         else:  
            translate_1 = translate_1 + i
     '''          
    
    for letter in phrase:
        if letter in "aeiou":
           translate_2 = translate_2 + letter 
           break 
    
   
    for letter_1 in phrase:
        
        if letter_1 == translate_2:
           translate_3 = translate_3
        else:
           translate_3 = translate_3 + letter_1
        
    #translate = translate + "ay"
          
    return(translate_3)
    

print ("**************TRANSLATOR OF PIG LATIN**************")
phrase = input("Enter the phrase: ")
print("translation = ")
print(translation(phrase))
