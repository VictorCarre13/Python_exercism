action_list=['wink','double blink','close your eyes','jump']
def commands(binary_str):
    final_list=[]
    if binary_str[0]=='0':
        index=0
        binary_str=binary_str[1:]
        for item in reversed(binary_str):
            if item == '1':
                final_list.append(action_list[index])
            index+=1
    else:
        index=3
        binary_str=binary_str[1:]
        for item in binary_str:
            if item == '1':
                final_list.append(action_list[index])
            index-=1
    return final_list