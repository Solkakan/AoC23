




def main():
    with open('input.txt') as f:
        content = f.readlines()

    data = []

    for line in content:
        out = []
        for element in line:
            match element:
                case'1':
                    out.append(1)
                case'2':
                    out.append(2)
                case'3':
                    out.append(3)
                case'4':
                    out.append(4)
                case'5':
                    out.append(5)
                case'6':
                    out.append(6)
                case'7':
                    out.append(7)
                case'8':
                    out.append(8)
                case'9':
                    out.append(9)
                case'0':
                    out.append(0)

        data.append(out)

    tot = 0

    for element in data:
        concat = [element[0], element[-1]]
        print(''.join(str(item) for item in concat))

           



if __name__ == '__main__':
    main()