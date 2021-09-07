class getText:

    def startPlay(self, lst):
        cut=0
        for i in range(len(lst)):
            if lst[i] == 'Play By Play':
                cut=i

        return lst[i:]

def main():
    tester = getText()


if __name__ == "__main__":
    main()