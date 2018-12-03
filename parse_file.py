import sys

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f1:
        with open(sys.argv[2], "w") as f2:
            lines = f1.readlines()
            if sys.argv[3] == "1":
                for line in lines:
                    if line.split(' ')[0] == "review/summary:":
                        line_out = line.strip("review/summary: ")
                        print(line_out)
                        f2.write(line_out)
            elif sys.argv[3] == "2":
                skip_line = False
                for line in lines:
                    line = line.rstrip("\n")
                    if line.split(' ')[0] == "review/helpfulness:":
                        if float(line.split(' ')[-1].split('/')[1]) == 0:
                            skip_line = True
                            continue
                        else:
                            helpfulness = float(line.split(' ')[1].split('/')[0]) / float(line.split(' ')[1].split('/')[1])
                            print("helpfulness =",helpfulness)
                            f2.write(str(helpfulness))
                            f2.write(" ")
                    elif line.split(' ')[0] == "review/score:":
                        if skip_line:
                            skip_line = False
                            continue
                        else:
                            score = float(line.split(' ')[1])
                            print(("score =", score))
                            f2.write(str(score))
                            f2.write("\n")
