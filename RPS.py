
def player(prev_play, opponent_history=[],bot_h = [''],state = [''], cont3 = []):
  opponent_history.append(prev_play)
  cont1 = 0
  cont2 = 0
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
  if (len(opponent_history) == 0): state.clear();cont3.clear()
  cont3.append('')
  if (len(cont3) > 22):
    for x in range(-21,0):
      if (opponent_history[x] == ideal_response[bot_h[x]]):
        cont2 = cont2 + 1
      elif(opponent_history[x] != bot_h[x]):
        cont1 = cont1 + 1
  if (cont1 == 0): cont1 = 1
  if (cont1/(cont1 + cont2) < 0.49 and len(cont3) > 22):
    state.append('')
    cont3.clear()    
  if (len(state)%3 == 0):
    last_ten = opponent_history[-6:]
    most_frequent = max(set(last_ten), key=last_ten.count)
    if most_frequent == '':
      most_frequent = "S"
  elif(len(state)%3 == 1):
    last_ten = opponent_history[-3:]
    most_frequent = max(set(last_ten), key=last_ten.count)
    if most_frequent == '':
      most_frequent = "P"
    else:
      most_frequent = ideal_response[most_frequent]
  else:
    most_frequent = ideal_response[bot_h[-2:][1]]
  bot_h.append(ideal_response[most_frequent])
  return ideal_response[most_frequent]

