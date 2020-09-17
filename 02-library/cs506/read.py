def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    matrix = []
    with open(csv_file_path, 'r') as f:
        data = f.readlines()
        for line in data:
            line = line.split(",")
            line[1] = line[1].rstrip("\n")
            int_list = []
            for text in line:
                try:
                    int_list.append(int(text))
                except ValueError:
                    int_list.append(text.strip('\"'))
                    
            matrix.append(int_list)
            
    return matrix 
