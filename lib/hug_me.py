from transformers import pipeline




def nlp(input_selection,txt):
    global answer
    
    '''try:
        input_selection=int(input('ENTER OPTION>>'))
    except ValueError:
            print('CHECK YOUR VALUE \n ENTER AN INTEGER')

    try :            
        txt=str(input('ENTER TEXT>>'))
    except ValueError:
            print('CHECK VALUES')'''    
    
    
    match input_selection:
        case 1:
            generator=pipeline('zero-shot-classification')
            answer=generator(txt)
            return answer
        case 2:
            generator=pipeline('sentiment-analysis')
            answer=generator(txt)
            return answer
        case 3:
            generator=pipeline('fill-mask')
            answer=generator(txt)
            return answer
        case 4:
            generator=pipeline('text-generation')
            answer=generator(txt)
            return answer
        case 5:
            generator=pipeline('ner')
            answer=generator(txt)
            return answer
        case 6:
            generator=pipeline('summarization')
            answer=generator(txt)
            return answer
        case 7:
            generator=pipeline('translation')
            answer=generator(txt)
            return answer
        case 8:
            generator=pipeline('feature_extraction')
            answer=generator(txt)
            return answer
        case 9:
            generator=pipeline('question_answering')
            answer=generator(txt)
            return answer