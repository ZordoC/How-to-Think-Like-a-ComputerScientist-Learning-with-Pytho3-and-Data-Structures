


web_site = "https://buildmedia.readthedocs.org/<media>/pdf/howtothink/latest/howtothink.pdf "


#init = st.find("/")

#end = st.find(" ")


#website_name = string[init:end]

result = web_site.find("<")

result_end = web_site.find(">")

print(result)

print(result_end)

print(web_site[result + 1:result_end])