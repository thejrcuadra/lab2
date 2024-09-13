import random

def main():
    trials = 5
    success = 0
    probability = 0
    file = open('birthdayOverlapProbability.txt', 'w')
    file.write('Birthday Overlap Probability Experiment \n--\n')
    file.close()
        
    while trials < 51:
        for x in range(trials):
            result = experiment()
            success += result
            
        probability = success / trials
        text = f'In {trials} trials the probability of same birthday attained was {round(probability * 100, 2)}%'
        print(text)
        f = open('birthdayOverlapProbability.txt', 'a')
        f.write(f'{text}\n')
        f.close()
        trials += 5
        success = 0

def experiment():
    birthdayOverlap = 0

    #Capping the number of people at 60
    numberOfPeople = random.randint(23, 60)
    birthdayList = []
    birthdayChecker = []

    for x in range(numberOfPeople):
        birthday = random.randint(1, 365)
        birthdayList.append(birthday)

    for x in birthdayList:
        if x in birthdayChecker:
            birthdayOverlap += 1
        else:
            birthdayChecker.append(x)

    if birthdayOverlap > 0:
        return 1
    else:
        return 0

main()