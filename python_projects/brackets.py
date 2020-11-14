
class bracket:

    def closer():

        brackets = input("Enter in your brackets:")

        left = 0

        right = 0

        answer = 0

        for i in range(len(brackets)):

            if brackets[i] == "(":
                left += 1

            elif brackets[i] == ")":
                right += 1
        if right < left:

            answer = (left - right)

        elif right > left:

            answer = (right - left)
        
        
            
        print("You need {}.".format(answer))

c = bracket
c.closer()


