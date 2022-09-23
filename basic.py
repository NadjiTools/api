from flask import Flask , request
api = Flask(__name__)
@api.route("/")
def HomePage():
	return "Convert Binary Code to Intelligible Speech .. @FFF8FFFF"
@api.route("/BinaryToWords")
def getText():
	code = request.args.get("code")
	return {"code":code.replace("01110001","q").replace("01110111","w").replace("01100101","e").replace("01110010","r").replace("01110100","t").replace("01111001","y").replace("01110101","u").replace("01101001","i").replace("01101111","o").replace("01110000","p").replace("01100001","a").replace("01110011","s").replace("01100100","d").replace("01100110","f").replace("01100111","g").replace("01101000","h").replace("01101010","j").replace("01101011","k").replace("01101100","l").replace("01111010","z").replace("01111000","x").replace("01100011","c").replace("01110110","v").replace("01100010","b").replace("01101110","n").replace("01101101","m").replace("01110001","Q").replace("01110111","W").replace("01100101","E").replace("01110010","R").replace("01110100","T").replace("01111001","Y").replace("01110101","U").replace("01101001","I").replace("01101111","O").replace("01110000","P").replace("01100001","A").replace("01110011","S").replace("01100100","D").replace("01100110","F").replace("01100111","G").replace("01101000","H").replace("01101010","J").replace("01101011","K").replace("01101100","L").replace("01111010","Z").replace("01111000","C").replace("01100011","V").replace("01110110","V").replace("01100010","B").replace("01101110","N").replace("01101101","M")}
@api.route("/WordsToBinary")
def getCode():
	code = request.args.get("code")
	return {"code":code.replace("q","01110001").replace("w","01110111").replace("e","01100101").replace("r","01110010").replace("t","01110100").replace("y","01111001").replace("u","01110101").replace("i","01101001").replace("o","01101111").replace("p","01110000").replace("a","01100001").replace("s","01110011").replace("d","01100100").replace("f","01100110").replace("g","01100111").replace("h","01101000").replace("j","01101010").replace("k","01101011").replace("l","01101100").replace("z","01111010").replace("x","01111000").replace("c","01100011").replace("v","01110110").replace("b","01100010").replace("n","01101110").replace("m","01101101")}
@api.route("/formats")
def formats():
    return "Text to Binary Code , Example : http://127.0.0.1:5000/WordsToBinary?code=karar .. .. .. Binary Code to Text , Example : http://127.0.0.1:5000/BinaryToWords?code=0111011101110001"
if __name__ =="__main__":
	api.run()