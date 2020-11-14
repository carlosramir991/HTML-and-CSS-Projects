class training:

    def __init__(self,name,bodypart):
        self.name = name
        self.bodypart = bodypart

        

    def m_greeting(self):
        print("Good Morning {}! Today you will be training {}.".format(self.name,self.bodypart))

        
if __name__ == "__main__":
    x = training("Carlos Ramirez","Back")
    x.m_greeting()


    
        
