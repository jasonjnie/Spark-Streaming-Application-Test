import sys

if __name__ == "__main__":
    with open(sys.argv[1], "r") as f1:
        with open(sys.argv[2], "w") as f2:
            lines = f1.readlines()
            for line in lines:
                if line.split(' ')[0] == "review/summary:":
                    line_out = line.strip("review/summary: ")
                    print(line_out)
                    f2.write(line_out)
