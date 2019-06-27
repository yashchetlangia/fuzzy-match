import fuzzy
import csv
import Levenshtein

def remove_prefix(names):
    for ch in [
        'MR.',
        'MRS.',
        'SMT.',
        '.',
        'mr.',
        'mrs.',
        'smt.'   
    ]:
        try:
            names.remove(ch)
        except:
            pass


    return names


def file1():

    correct=0
    incorrect=0
    f=open("/home/loksuvidha/Desktop/data.csv" ,"r")
                
    data=csv.reader(f)
    total_rows=0            
    for row in data:
        print (row)
        
        total_rows=total_rows+1
        
        proposal_name=remove_prefix(row[0].split(' '))  
        proposal_name=remove_prefix(row[0].split(' '))  
        rto_name=remove_prefix(row[1].split(' '))
      
        min_length=min(len(proposal_name),len(rto_name))

        print(proposal_name,rto_name)

        dmetaphone = fuzzy.DMetaphone(4)
        sum_of_counter=0        

        for i in range (len(proposal_name)):
            
            counter=0
            j=0
            while j<(len(rto_name)):

                word_of_proposal_name=proposal_name[i].upper()
                word_of_rto_name=rto_name[j].upper()
                
                if(word_of_proposal_name in word_of_rto_name or word_of_rto_name in word_of_proposal_name):
                    counter=counter+1

                elif(dmetaphone(word_of_proposal_name)==dmetaphone(word_of_rto_name)) :
                    counter=counter+1

                else:
                    if(Levenshtein.distance(word_of_proposal_name,word_of_rto_name)<=2):                    
                        counter=counter+1
                j=j+1
        

            sum_of_counter=sum_of_counter+counter        
      #  print("Counter=",sum_of_counter)
        if(sum_of_counter>=2 or sum_of_counter>=min_length):
      #      print("Correct name:")
            correct=correct+1
        else:
            
            print("Incorrect name:")
            incorrect=incorrect+1
  
    print("Total rows=",total_rows)
    print("Correct name=",correct)
    print("Incorrect name=",incorrect)
            
    f.close()

if __name__=="__main__":
    file1()
