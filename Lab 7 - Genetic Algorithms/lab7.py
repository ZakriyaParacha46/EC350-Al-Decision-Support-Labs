import pprint
class slider():
    def __init__(self,moves):
        self.blankcord= (1,1)
        self.board = [[1,2,3],[8,'B',4],[7,6,5]] 
        self.moves = moves
        self.first_error =-1
        self.fit= 0

    def fitness(self):
        temp_board= self.board
        blankcordtemp = self.blankcord
        score= 0
        ind= 0
        firsterror =-1
        for m in self.moves:
            if (m=="U" and blankcordtemp[0]>0):
                score+=1 
                temp = temp_board[blankcordtemp[0]-1][blankcordtemp[1]] 
                temp_board[blankcordtemp[0]-1][blankcordtemp[1]] = 'B'
                temp_board[blankcordtemp[0]][blankcordtemp[1]] = temp
                blankcordtemp=(blankcordtemp[0]-1,blankcordtemp[1])
            
            elif(m=="D" and blankcordtemp[0]<2):
                score+=1
                temp = temp_board[blankcordtemp[0]+1][blankcordtemp[1]] 
                temp_board[blankcordtemp[0]+1][blankcordtemp[1]] = 'B'
                temp_board[blankcordtemp[0]][blankcordtemp[1]] = temp
                blankcordtemp=(blankcordtemp[0]+1,blankcordtemp[1]) 
            
            elif(m=="L" and blankcordtemp[1]>0):
                score+=1
                temp = temp_board[blankcordtemp[0]][blankcordtemp[1]-1] 
                temp_board[blankcordtemp[0]][blankcordtemp[1]-1] = 'B'
                temp_board[blankcordtemp[0]][blankcordtemp[1]] = temp
                blankcordtemp=(blankcordtemp[0],blankcordtemp[1]-1) 
            
            elif(m=="R"  and blankcordtemp[1]<2):
                score+=1
                temp = temp_board[blankcordtemp[0]][blankcordtemp[1]+1] 
                temp_board[blankcordtemp[0]][blankcordtemp[1]+1] = 'B'
                temp_board[blankcordtemp[0]][blankcordtemp[1]] = temp
                blankcordtemp=(blankcordtemp[0],blankcordtemp[1]+1) 

            else:
                if(firsterror==-1):
                    firsterror=ind
            ind+=1
        
        self.fit=score
        self.first_error=firsterror
        return temp_board,score,firsterror

class genetic:
    def __init__(self):
        self.moves = [['U','R','U','D','D','R','L','D'],
                    ['U','L','D','U','D','U','R','R'],
                    ['U','U','R','U','R','U','R','R'],
                    ['R','U','L','U','L','D','R','D']]

    def calcfit(self):
        fit_array, chorom_array, error_array = [], [], []
        # Populate the arrays
        for ch in self.choromosome:
            ch.fitness()
            fit_array.append(ch.fit)
            chorom_array.append(ch.moves)
            error_array.append(ch.first_error)

        # Combine the arrays into a list of tuples and sort based on fit_array
        zipped = list(zip(fit_array, chorom_array, error_array))
        zipped.sort(key=lambda x: x[0])  # Sort based on the first element of each tuple (fit_array)
        fit_array, chorom_array, error_array = zip(*zipped)
        
        fit_array=list(fit_array)
        error_array=list(error_array)
        chorom_array=list(chorom_array)
        
        # Now you can return the sorted arrays
        return fit_array, chorom_array, error_array

    def crossover(self,chorom1,chorom2,split):
        chorom1,_= chorom1[:split] + chorom2[split:], chorom2[:8-split] + chorom1[:split]
        return chorom1
   
    def mutate(self, chorom, index):
        if(index!=-1):
            if(chorom[index]=='L'): chorom[index] ='R'
            elif(chorom[index]=='R'): chorom[index] ='L'
            elif(chorom[index]=='U'): chorom[index] ='D'
            elif(chorom[index]=='D'): chorom[index] ='U'
        return chorom
    
    
    def nextgen(self):
        sorted_chorome = self.moves
        c= 0
        while(c<20):
            self.choromosome = [slider(m) for m in sorted_chorome] 
            sorted_fit,sorted_chorome,firsterror= self.calcfit()
           
            for i in range(4):
                print(sorted_fit[i],sorted_chorome[i],firsterror[i])
            print("--------------")
            if sorted_fit[0] != 8:
                sorted_chorome[0]=self.crossover(sorted_chorome[0],sorted_chorome[1],sorted_fit[0])
                #crossover ch1 with ch2  ch1[0:f1] + ch2[f1:8]
            
            elif sorted_fit[1] != 8:
                sorted_chorome[1]=self.crossover(sorted_chorome[1],sorted_chorome[0],sorted_fit[1])
                #crossover ch2 with ch1
            
            elif sorted_fit[2] != 8:
                #crossover ch3 with ch4
                sorted_chorome[2]=self.crossover(sorted_chorome[2],sorted_chorome[3],sorted_fit[2])
            elif sorted_fit[3] != 8:
                #crossover ch4 with ch3
                sorted_chorome[3]=self.crossover(sorted_chorome[3],sorted_chorome[2],sorted_fit[3])

            else:
                break
            
            sorted_chorome[0]= self.mutate(sorted_chorome[0],firsterror[0])
            c+=1

ga = genetic()
ga.nextgen()