# #Dictionaries
# #{key:value}

# ex = {
# "bug":"An error in program that prevents program from running as execpted", 
# "Function":"A piece of code that u can call over again and again",
# "Loop":"The action of doing something again and again"
# }
# # print(ex["bug"])
# # ex["bug"]="Nothing"
# # print(ex)

# # empty_dict={}
# # ex={}
# # print(ex)
# for _ in ex:
#     print(_) #keys will be printed 
#     print(ex[_]) #values will be printed

#nesting
# {
#     key:[] #list
#     key:{} #dict
# }
 
travel_vlog={
    "Andhra":{
        "cities_visited":["Vijayawada","Visakhapatnam","Guntur"],
        "total_visits":3
    },
    "Tamilnadu":{
        "cities_visited":["Chennai","Kanchipuram","Mahabalipuram"],
        "total_visits":3
    }
}
print(travel_vlog["Andhra"]["cities_visited"][0])

