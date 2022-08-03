def seq_fib():
    n = int(input("Which number are o looking for? "))
    last=1
    penultimate=0

    if (n==1) or (n==2):
        print(f'{n} belong to the sequence')
    else:
        value = 0
        while value < n:
            value = last + penultimate
            penultimate = last
            last = value
            if value==n:
                return print(f'{n} belong to the sequence')
        return print(f"{n} don't belong to the sequence")



if __name__=="__main__":
    seq_fib()