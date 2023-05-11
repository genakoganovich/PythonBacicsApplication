with open("input.txt") as f_in, open("output.txt", "w") as f_out:
    lines = [str(x).strip() + '\n' for x in f_in.readlines()]
    lines.reverse()
    f_out.writelines(lines)
