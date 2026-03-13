def NULL_not_found(object: any) -> int:
	objType = type(object)
	if (object == None) : print("Nothing:", object, objType)
	elif (objType == float) : print("Cheese:", object, objType)
	elif (objType == int) : print("Zero:", object, objType)
	elif (object == "") : print("Empty:", object, objType)
	elif (objType == bool) : print("Fake:", object, objType)
	else : 
		print("Type not Found:") 
		return 1
	return 0