#根据身高与体重计算BMI
def main() :
    come = "Y"
    while come == "Y" or come == "y" :
      height = eval(input("please input the height(m) is "))
      weight = eval(input("\nplease input the weight(kg) is "))
      BMI = weight / (height**2)
      print("\nThe BMI is ", BMI)
      if BMI < 18.5 :
          print("\n国际与国内BMI标准均偏瘦")
      elif BMI >=18.5 and BMI <= 24 :
          print("\n国际与国内BMI标准均为正常")
      elif BMI > 24 and BMI <=25 :
          print("\n国际BMI标准为偏胖，国内BMI标准为正常")
      elif BMI > 25 and BMI <=28 :
          print("\n国际与国内标准均为偏胖")
      elif BMI > 28 and BMI <=30 :
          print("\n国际BMI标准为肥胖，国内BMI标准为偏胖")
      else :
         print("\n国际与国内BMI标准均为肥胖")
      come = input("\nDO you want to test again(y or n)?")

main()