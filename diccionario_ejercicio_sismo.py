class Lista1():
    def crearList1(self):
        self.lista=[]
        self.dic={}

        temblores=open("test.txt","r")
        for linea in temblores:
            linea1=linea.replace(",",".")
            linea2=linea1.replace(";",",").strip()
            year=linea2.split(',')[0] # 2015
            month=linea2.split(',')[1] # 1
            magnitud=linea2.split(',')[2] # 4.0
            if year in self.dic:
                self.dic[year].append(float(magnitud))
            else:
                self.dic[year]=[float(magnitud)]
        #print(self.dic)
        generar1.resultado1()

    def resultado1(self):

        for i in self.dic:
            cantidad=(len(self.dic.get(i)))
            promedio=sum(self.dic.get(i))/cantidad
            print("año: " + i + "  Magnitud: " , self.dic.get(i) , "cantidad de sismos por año: ", cantidad , " promedio por año  " ,"%.2f"% promedio)

        
print(" primer paso")
generar1=Lista1()
generar1.crearList1()



class Lista():
    def crearList(self):

        self.dic={}
        self.dic2={}

        temblores=open("test.txt","r")
        for linea in temblores:
            linea1=linea.replace(",",".")
            linea2=linea1.replace(";",",").strip()
            year=linea2.split(',')[0] # 2015
            month=linea2.split(',')[1] # 1
            magnitud=linea2.split(',')[2] # 4.0b

            if year in self.dic:
                self.dic[year].append(str(month))
            else:
                self.dic[year]=[str(month)]

            if year in self.dic:
                self.dic[year].append(float(magnitud))
            else:
                self.dic[year]=[float(magnitud)]


        for key, value in self.dic.items():

            for element in value:


                    mes=(self.dic2.get(key))
                    anio="año: " + key

     
        for key, value in self.dic.items():

            for element in value:

                if type(element) is str:
                    print("añ0",key,"mes",element)


                if type(element) is float:
                    print("magnitud del mes: ", element)

                    print("")






        

print("")
print(" segundo paso")
generar=Lista()
generar.crearList()
