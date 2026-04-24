def rgb_hex():
  invalid_msg = "some error occured"
  red = int(input("Enter red (R) value: "))
  if (0 > red or 255 < red):
    print(invalid_msg)
    return
  green = int(input("Enter green (G) value: ")) 
  if (0 > green or 255 < green):
    print(invalid_msg)
    return
  blue = int(input("Enter blue (B) value: "))
  if (0 > blue or 255 < blue):
    print(invalid_msg)
    return
  val = (red << 16) + (green << 8) + blue
  print("%s" % (hex(val)[2:]).upper())  
  return

def hex_rgb():
  hex_val = input("Enter a hexadecimal value(colour):")
  if len(hex_val) != 6:
    print("Invalid value has been entered")
    return
  else:
     hex_val = int(hex_val, 16)
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  
  print("Red: %s Green: %s Blue:%s" % (red, green, blue))

def convert():
  while True:
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == '1':
      print("RGB to Hex....")
      rgb_hex()
    elif option == '2':
      print("HEX to RBG ...")
      hex_rgb()
    elif option == 'X' or option == 'x':
      break
    else:
      print("ERROR 404")

convert()