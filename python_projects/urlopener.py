import webbrowser
from tkinter import *


class makera():


    
    
    def windowa(self):
        
        root = Tk()

        root.geometry('400x200')

        self.entry1 = Entry(root, width=20)

        self.entry1.pack()

        label1 = Label(root,text="Enter what you would like your page to say!").pack()

        
        b1 = Button(root,text="Start", command=self.htmlb)
        
        b1.pack()

        root.mainloop()


        


        




    def htmlb(self):

        custom_text = self.entry1.get()

        print(custom_text)
        
        opener = open("autohtml.html","w")

                       
        html_1 = """</h1></body>
            </html>"""

        html_2 = ("""<!DOCTYPE>
        <html>
        <head></head>
        <body><h1>"""+custom_text+html_1)
                        

        opener.write(html_2)

        url = 'file:///Users/slims/Documents/python_projects/' + 'autohtml.html'
                        
                        
        webbrowser.open_new_tab(url)
        
        





if __name__ == '__main__':

    a = makera()
    a.windowa()
    

   
      
        
    



