import json
import time
applied_students=[] 
schools={
    'prempeh college':{
        'science':8,
        'general arts':10,
        'business':9,
        'stem':10
    },
    'legon presec':{
        'science':10,
        'business':12,
        'robotics':14,
        'general arts':15
    },
    'opoku ware school':{
        'science':12,
        'business':15,
        'general arts':15,
        'visual arts':15
    },
    'mfatsipim school':{
        'science':10,
        'business':12,
        'stem':14,
        'general arts':15
    },
    'st. augustine college':{
        'science':12,
        'business':14,
        'general arts':15,
        'visual arts':17,
    },
    'owerriman shts':{
        'science':15,
        'general arts':20,
        'visual arts':20,
        'home science':24,
    },
    'amaniampong shs':{
        'science':16,
        'home economics':18,
        'general arts':20,
        'visual arts':20
    }
            
}
def list_schools():
          print('\navailable schools are')
          for school, programs in schools.items():
                    
                       
                  
                       print(f'{school.title()}')
                       print('Programs offered:', ', '.join(programs.keys()))
                           
def select_school():
    try:
        selected=input("enter the school's name: ").lower().strip()
        name=input('enter your name: ')
        course=input('enter your preferred course: ').lower().strip()
        grade=int(input('enter your bece grade: ')) 
        if selected in schools:
           if course in schools[selected]:
               print('\nplease wait for some seconds...')
               time.sleep(2)
               print('Request submitted...')
       
               time.sleep(1) 
               print('your admission request is under processing...')
               time.sleep(2) 
               cutoff=schools[selected][course]
               if grade<=cutoff:
                   print(f'Your admission request to {selected.title()} has been confirmed, 🎉')
                   applied_students.append({
                   'name': name,
                   'school': selected,
                    'course': course,
                     'bece grade': grade
                     })
               else:
                   print(f'Your admission request to {selected.title()} has been denied due to your grade value')
           else:
                print('course not offered in this school')
        else:
            print('school not available') 
    except ValueError:
        print('please enter valid info...')
        
        
        
def save_file():
        with open('applied_students.json', 'w') as file:
            json.dump(applied_students, file, indent=4)
def load_students_applied():
         try:
             with open('applied_students.json', 'r') as file:
                 stored_data=json.load(file)   
                 applied_students.extend(stored_data)   
         except FileNotFoundError:
              pass    
             

                                  
                                                     
load_students_applied() 


print('WELCOME TO THE SHS ADMISSION PORTAL') 
print('Please select an option to proceed')
print('1.List all schools available')
print('2. Apply admission')
print('3. Exit')
while True:
        choice=input('enter option value: ')
        if choice=='1':
            list_schools()
 
        elif choice=='2':
            select_school()
            save_file() 
        elif choice=='3':
            print('Thanks for using HiveTech')
            break
   


         

     
              
              
            
            
            

