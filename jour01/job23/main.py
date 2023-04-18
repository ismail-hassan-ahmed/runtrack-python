def draw_triangle(width, height): # 3 / 4
    innerWidth = 0 
    for x in range(1,height):
            
        for i in range(width,1,-1):
            if i == 2:
                string = '-'
                for y in range(1,innerWidth): 
                    string += '-'

                print(' '* width + '/' + string + '\\')
            else:
                print(' '* width + '/' + innerWidth* ' ' + '\\')
            width = width - 1
            innerWidth += 2
            # print('|' + ' ' *width + '|')
            # for x in range(1,width):
            # print('|'+ '-' * width + '|')
    
    
# width = input('Quelle largeur?')
height = int(input('Quelle hauteur?'))
width = int(input("Quelle largeur"))
draw_triangle(width,height)