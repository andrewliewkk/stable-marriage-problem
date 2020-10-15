def is_stable(n, pref, solution):
  rank_dict = {}
  solution_dict = {}
  for element in pref:
    for i in range(1, n + 1):
      if element[0] not in rank_dict:
        if element[0][0] == "m":
          rank_dict[element[0]] = ["f" + str(element.index(i))]
        else:
          rank_dict[element[0]] = ["m" + str(element.index(i))]
      else:
        if element[0][0] == "m":
          rank_dict[element[0]] += ["f" + str(element.index(i))]
        else:
          rank_dict[element[0]] += ["m" + str(element.index(i))]
  for element in solution:
    solution_dict[element[0]] = element[1]
    solution_dict[element[1]] = element[0]
  for couple in solution:
    male = couple[0]
    female = couple[1]
    maleIndex = int(male[1:])
    femaleIndex = int(female[1:])

    # female check
    if rank_dict[female][0] != male:
      for n in range(rank_dict[female].index(male) - 1, -1, -1): #n is index of preferable male parners
        currentMaleChoice = rank_dict[female][n]
        if rank_dict[currentMaleChoice].index(female) < rank_dict[currentMaleChoice].index(solution_dict[currentMaleChoice]):
          return False


    #male check
    if rank_dict[male][0] != female:
      for n in range(rank_dict[male].index(female) - 1, -1, -1): #n is index of preferable female parners
        currentFemaleChoice = rank_dict[male][n]
        if rank_dict[currentFemaleChoice].index(male) < rank_dict[currentFemaleChoice].index(solution_dict[currentFemaleChoice]):
          return False
  return True