# FILE NAME - phishing_email_detector.py

# NAME: Isiah Osborn
# DATE: 2025-10-05
# BRIEF DESCRIPTION:
#   Read an email subject line and print a basic phishing risk assessment
#   based on common keywords/phrases. Outputs match the provided samples.

########## ENTER YER CODE BELOW THIS LINE ##########

subject = input("Enter the email subject line: ")

print()

print("SECURITY ASSESSMENT:")

s = subject.lower()
if ("urgent" in s) or ("immediate action required" in s):
    print("HIGH RISK: Possible phishing attempt.")
elif ("win" in s) or ("free" in s):
    print("MEDIUM RISK: Suspicious offer detected.")
elif "password reset" in s:
    print("LOW RISK: Verify legitimacy with sender.")
else:
    print("No phishing indicators detected.")

print("------------------------")
print(f'Analyzed subject: "{subject}"')


########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Enter the email subject line: Meeting on Friday

SECURITY ASSESSMENT:
No phishing indicators detected.
------------------------
Analyzed subject: "Meeting on Friday"
'''

'''
Enter the email subject line: URGENT REQUEST FOR BANK TRANSFER

SECURITY ASSESSMENT:
HIGH RISK: Possible phishing attempt.
------------------------
Analyzed subject: "URGENT REQUEST FOR BANK TRANSFER"
'''

'''
Enter the email subject line: All I do is win win win no matter what

SECURITY ASSESSMENT:
MEDIUM RISK: Suspicious offer detected.
------------------------
Analyzed subject: "All I do is win win win no matter what"
'''

'''
Enter the email subject line: Did you request a password reset?

SECURITY ASSESSMENT:
LOW RISK: Verify legitimacy with sender.
------------------------
Analyzed subject: "Did you request a password reset?"
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. Was using `in` difficult or was it natural?
It felt natural. Python’s in reads like plain English, works on substrings, and pairs well with s.lower() and any() over a tuple of keywords






'''



########################################
#            ATTESTATION
########################################

'''

Please gauge your utilization of AI on the following spectrum. Place an "X" in front
of the appropriate response. Only choose one of the following:

[ ] I did not use AI at all for this lab.
[x ] I wrote the initial draft of the software but had AI help me make it better.
[ ] I fed the lab description to AI and had it generate a response but I modified it.
[ ] AI created the entire program for me.



It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 

[ ] I understand very little about this lab.
[x ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.

'''
