#creating a parent class called band
class band:
    #attributes of the class company,member_number and password 
    company = ''
    member_number = 9
    password = '242DqN!'
class exo(band): #our child class exo inheriting band class attributes
    #on top of the band class attributes we have attributes for just class exo
    #pay_rate, hours_work and group_type
    pay_rate = 44.00
    hours_work = 6
    group_type = 'boy'
class twice(band):#our child class twice inheriting band class attributes
    #on top of band class atrributes we have attributes for just class twice
    #number_of_auditions, donations_for_group and main_dancer_name
    number_of_auditions = 16
    donations_for_group = 56
    main_dancer_name = 'Momo'
    
    
    
    
