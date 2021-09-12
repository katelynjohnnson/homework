def main():
    encrypt_dict = { "A":')', 'a':'(', 'B':'*', 'b':'&', 'C':'^', 'c':'%', 'D':'$', 'd':'#', 
    'E':'@', 'e':'!', 'F':'0', 'f':'1', 'G':'9', 'g':'2', 'H':'8', 
    'h':'3', 'I':'7', 'i':'4', 'J':'6', 'j':'5', 'K':'`', 'k':'=', 
    'L':'~', 'l':'+', 'M':'-', 'm':'_', 'N':'/', 'n':'.', 'O':',',
    'o':';', 'P':']', 'p':'[', 'Q':'?', 'q':'>', 'R':'<', 'r':'"',
    'S':'}', 's':'{', 'T':'j', 't':'A', 'U':'N', 'u':'g', 'V':'o', 
    'v':'f', 'W':'E', 'w':'t', 'X':'T', 'x':'K', 'Y':'w', 'y':'Q',
    'Z':'d', 'z':'S', '.':'R', ':':'p'}

    outfile = open('info_security.txt','r')
    encrypt = open('encrypt_doc.txt','w')

    file_contents = outfile.read()

    for x in file_contents:
        encrypt_dict[x]

        encrypt.write(encrypt_dict[x])
    encrypt.close()
main()
