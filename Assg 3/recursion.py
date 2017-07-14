def list_sum(num_list):

    if len(num_list) == 1:

        return num_list[0]

    else:

#How is it possible that all the numbers are added up?

#So, the number in the num_list[0] just gets keep

#added up?

#Taking a consideration that, eventually, the

#original if block will be triggered and

#it will return num_list.

#Then, how can I THINK like that?

#To be able to think the situations, instead of

#syntaxes.

#But, is there a special reason why num_list[0] is being stored with a desired value?
        return num_list[0] + list_sum(num_list[1: ])

print(list_sum([1,3,5,7,9]))

