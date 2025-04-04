class winConditions:
    def CheckBoard(board):
        #chck line by line not whole board
        # i=0
        allWinOptions = {
            0: [1, 1, 1,
                0, 0, 0,
                0, 0, 0],

            1: [0, 0, 0,
                1, 1, 1,
                0, 0, 0],

            2: [0, 0, 0,
                0, 0, 0,
                1, 1, 1],
                
            2: [0, 0, 0,
                0, 0, 0,
                1, 1, 1],
                
            3: [1, 0, 0,
                1, 0, 0,
                1, 0, 0],
                
            4: [0, 1, 0,
                0, 1, 0,
                0, 1, 0],
                
            5: [0, 0, 1,
                0, 0, 1,
                0, 0, 1],
                
            6: [1, 0, 0,
                0, 1, 0,
                0, 0, 1],
                
            7: [0, 0, 1,
                0, 1, 0,
                1, 0, 0],
        }

        for key in allWinOptions:
            
            currentBorad = allWinOptions[key]
            # print(allWinOptions[key])
            # print(allWinOptions[key][0])
            # print("----------")
            
            matchesFound = 0
            for i in range(9):
                # print(i)
                
                if((board[i] + currentBorad[i]) == 2):
                    # print(allWinOptions[key][i])
                    matchesFound += 1

                i += 1
            
            # print(matchesFound)
            if(matchesFound == 3):
                return True
        return False
    
    print(CheckBoard([1, 1, 1, 0,0,0,0,0,0]))
    print(CheckBoard([0, 1, 1, 0,1,1,0,1,0]))
    print(CheckBoard([1,1,1, 0,1,0, 0,0,1]))
    print(CheckBoard([0,1,0, 0,0,1, 0,0,1]))
