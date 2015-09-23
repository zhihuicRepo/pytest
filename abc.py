def name_to_number(name):
    game_list = ['rock','Spock','paper','lizard','scissors']
    for i in range(len(game_list)):
        if game_list[i] == name:
            print i
            break
    else:
        print False
    
name_to_number('paper')  
name_to_number('per')  
