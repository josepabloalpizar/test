class Lista():
    def crearList(self):
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
        generar.resultado()

    def resultado(self):

        for i in self.dic:
            cantidad=(len(self.dic.get(i)))
            promedio=sum(self.dic.get(i))/cantidad
            print("año: " + i + "  Magnitud: " , self.dic.get(i) , "cantidad de sismos por año: ", cantidad , " promedio por año  " ,"%.2f"% promedio)

        

generar=Lista()
generar.crearList()
