#Which of the following examples will correctly output formatted strings?

#If a code snippet raises SyntaxError or formatting doesn't actually take place in a string, 
#consider such an option incorrect.
"%.4f".format(3.14159265358979)
"{1} {1} {1}".format(1, 2, 3)
#"{1} is a {kind}".format(kind="fruit", "grapefruit") - wrong answer
"{city} is the capital of {country}".format(country="Portugal",
                                            city="Lisbon")