sorted_languages ={
'jen':'python',
'sarah':'c',
'edward':'rust',
'phill':'python',
}
print("The following language has been mentioned")
for language in set (sorted_languages.values()):
    print (language.title())