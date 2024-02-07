def seq_read_fasta(filename):
    from pathlib import Path

    # -- Constant with the new of the file to open


    # -- Open and read the file
    file_contents = Path(filename).read_text()
    list_contents = file_contents.split('\n')
    for i in range(1, len(list_contents)):
        print(list_contents[i])
seq_read_fasta( "../sequences/U5.fa")