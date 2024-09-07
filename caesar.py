alpa=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input(" encode or decode : ")
text = input("Type messege : ")
shift = int(input("Type the number : "))

def encoding(text,shift) :
  encode_text =""

  for letter in text :

    shift_index = (alpa.index(letter) + shift) % 26
    encode_text += alpa[shift_index]

  print("Result : "+encode_text)

def decoding(text,shift) :
  encode_text =""

  for letter in text :

    shift_index = (alpa.index(letter) - shift) % 26
    encode_text += alpa[shift_index]

  print("Result : "+encode_text)

if(direction=="encode") :
  encoding(text,shift) 



else : 
  decoding(text,shift)

  
  








