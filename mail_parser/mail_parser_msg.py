import extract_msg
import colors

f = r'./sencillo.msg' 
# open message
msg = extract_msg.Message(f)

print(colors.bcolors.OKBLUE + 'CABECERAS' + colors.bcolors.ENDC)
for k, v in msg.header.items():
    print("{}: {}".format(k, v))

print(colors.bcolors.OKBLUE + 'ATTACHMENTS' + colors.bcolors.ENDC)
i=1
attachments = msg.attachments
for attachment in attachments:
    print(attachment.getFilename())
    #print(attachment.type())
    # ok attachment.save(custom_path, custom_filename))

print(colors.bcolors.OKBLUE + 'RTFBODY' + colors.bcolors.ENDC)
print(msg.rtfBody)
print(colors.bcolors.OKBLUE + 'SENDER' + colors.bcolors.ENDC)
print(msg.sender)
print(colors.bcolors.OKBLUE + 'CLASSTYPE' + colors.bcolors.ENDC)
print(msg.classType)
print(colors.bcolors.OKBLUE + 'HEADERDICT' + colors.bcolors.ENDC)
print(msg.headerDict)
print(colors.bcolors.OKBLUE + 'HEADER_FORMAT_PROPERTIES' + colors.bcolors.ENDC)
print(msg.headerFormatProperties)
print(colors.bcolors.OKBLUE + 'header_keys' + colors.bcolors.ENDC)
print(msg.header.keys())
print(colors.bcolors.OKBLUE + 'header_values' + colors.bcolors.ENDC)
print(msg.header.values())
print(colors.bcolors.OKBLUE + 'header_items' + colors.bcolors.ENDC)
print(msg.header.items())
