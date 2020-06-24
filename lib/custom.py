class Custom():
    def split_to_array(string, length):
        chunks, chunk_size = len(string), length
        array = [ string[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
        return array
