if __name__ == '__main__':
    k={}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        k[score]=name
    k1=dict(set(sorted(k.items())))

    print(k1)
    print(min(k1.keys()))

