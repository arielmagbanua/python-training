from time import sleep

path = 'D:\\Training\\python-training\\CS101\\'

def merge(input_filenames, output_filename):
    '''
    Loop through each file using their filenames then read the content
    and add them to a list of contents and finally write them to the
    output file.
    '''
    contents = []

    for input_filename in input_filenames:
        try:
            # open the current file
            input_file = open(path + input_filename)
            
            # read the content of the file
            content = input_file.read()
            
            # add the content to the contents list
            contents.append(content)

            # close the file after reading
            input_file.close()
        except:
            # file not found therefore continue
            continue
    
    # write the contents to the output file
    output_file = open(path + output_filename, 'w+')
    for content in contents:
        output_file.write(content)
    
    # close the file
    output_file.close()

merge(['file1.txt', 'file2.txt', 'file3.txt'], 'output.txt')
