def rectangle(width, height):

    print('|'+ '-' * width + '|')
    for i in range(1,height):
        print('|' + ' ' *width + '|')
        # for x in range(1,width):
    print('|'+ '-' * width + '|')
    
width = input('Veuillez saisir la largeur?')
height = input('Veuillez saisir la hauteur?')